"""The editors' to-do page and its menu links, with a few open questions
and possible entries made here (each site loads its own)."""
from berkeley.models import Candidate, OpenQuestion

from .helpers import ROOT
from .test_login import LoginTestCase

TODO_URL = f"{ROOT}todo/"
QUESTION = "Are these two reviews one piece?"


class TodoTestCase(LoginTestCase):
    def setUp(self):
        super().setUp()
        self.reviews = [self.pub("A review", 1963, pub_type="RVOB",
                                 authors=[self.person("A.", name)])
                        for name in ("Reviewer", "Critic")]
        self.question = OpenQuestion.objects.create(
            title=QUESTION, details="They share a page.")
        self.question.entries.set(self.reviews)
        self.undecided = Candidate.objects.create(
            author="Undecided Author", citation="A Hard Case (1970)",
            status=Candidate.UNDECIDED, reason="It may not mention him.",
            evidence="https://example.com/hard-case")
        self.unchecked = Candidate.objects.create(
            author="Unchecked Author", citation="Not Looked At (1980)")
        Candidate.objects.create(citation="Already In (1990)",
                                 status=Candidate.ADDED, entry=self.book)
        Candidate.objects.create(citation="Left Out (1995)",
                                 status=Candidate.LEFT_OUT)


class AnonymousTodoTest(TodoTestCase):
    def test_no_editor_links_in_menu(self):
        html = self.client.get(ROOT).content.decode()
        self.assertNotIn("Add entry", html)
        self.assertNotIn("To do", html)

    def test_todo_page_needs_a_login(self):
        resp = self.client.get(TODO_URL)
        self.assertRedirects(resp, f"{ROOT}login/?next={TODO_URL}",
                             fetch_redirect_response=False)


class EditorTodoTest(TodoTestCase):
    def setUp(self):
        super().setUp()
        self.login()

    def test_menu_links(self):
        html = self.client.get(ROOT).content.decode()
        self.assertIn('href="/admin/berkeley/publication/add/">Add entry</a>',
                      html)
        self.assertIn(f'href="{TODO_URL}">To do</a>', html)

    def test_add_entry_page(self):
        resp = self.client.get("/admin/berkeley/publication/add/")
        self.assertEqual(resp.status_code, 200)

    def test_open_question_with_its_entries(self):
        html = self.client.get(TODO_URL).content.decode()
        self.assertIn(QUESTION, html)
        self.assertIn("They share a page.", html)
        for review in self.reviews:
            self.assertIn(f'href="{ROOT}pub_detail/{review.id}/"', html)
        self.assertIn("(Reviewer)", html)
        self.assertIn("(Critic)", html)
        self.assertIn('href="/admin/berkeley/openquestion/'
                      f'{self.question.id}/change/"', html)

    def test_undecided_and_unchecked_candidates_are_listed(self):
        html = self.client.get(TODO_URL).content.decode()
        self.assertIn("Undecided: researched, but we could not tell (1)",
                      html)
        self.assertIn("Not checked yet (1)", html)
        self.assertIn("Undecided Author, A Hard Case (1970)", html)
        self.assertIn("It may not mention him.", html)
        self.assertIn('<a href="https://example.com/hard-case">Source</a>',
                      html)
        self.assertIn("Unchecked Author, Not Looked At (1980)", html)
        for candidate in (self.undecided, self.unchecked):
            self.assertIn('href="/admin/berkeley/candidate/'
                          f'{candidate.id}/change/"', html)

    def test_decided_candidates_are_only_counted(self):
        html = self.client.get(TODO_URL).content.decode()
        self.assertIn("2 have been decided already.", html)
        self.assertNotIn("Already In", html)
        self.assertNotIn("Left Out (1995)", html)

    def test_deciding_a_candidate_takes_it_off_the_page(self):
        self.undecided.status = Candidate.LEFT_OUT
        self.undecided.save()
        html = self.client.get(TODO_URL).content.decode()
        self.assertNotIn("A Hard Case", html)
        self.assertIn("Undecided: researched, but we could not tell (0)",
                      html)
        self.assertIn("3 have been decided already.", html)

    def test_settled_questions_leave_the_page(self):
        OpenQuestion.objects.update(settled=True)
        html = self.client.get(TODO_URL).content.decode()
        self.assertNotIn(QUESTION, html)

    def test_admin_lists(self):
        for url in ("/admin/berkeley/openquestion/",
                    "/admin/berkeley/candidate/",
                    "/admin/berkeley/openquestion/add/",
                    "/admin/berkeley/candidate/add/",
                    f"/admin/berkeley/openquestion/{self.question.id}/"
                    "change/",
                    f"/admin/berkeley/candidate/{self.undecided.id}/"
                    "change/"):
            self.assertEqual(self.client.get(url).status_code, 200, url)


class DraftEntryTest(TodoTestCase):
    """A possible entry's citation, in MOA's style, read as a draft
    entry."""

    def draft(self, citation, author=""):
        return Candidate(author=author, citation=citation).draft_entry()

    def test_article_in_a_known_journal(self):
        draft = self.draft("‘Trollope’s Politics’,\xa0Political Studies, "
                           "29 (1981), pp. 232-44.")
        self.assertEqual(draft, {
            "pub_type": "MENT", "title": "Trollope’s Politics",
            "journal": self.journal.id, "volume": "29", "pages": "232-44",
            "year": "1981"})

    def test_chapter_in_a_known_book_by_its_short_title(self):
        draft = self.draft("‘A Chapter’, in A. Editor (ed.),\xa0Rationalism"
                           "\xa0in Politics\xa0(London: Methuen, 1962), "
                           "pp. 1-10.")
        self.assertEqual(draft["title"], "A Chapter")
        self.assertEqual(draft["collection"], self.book.id)
        self.assertEqual(draft["year"], "1962")

    def test_book(self):
        draft = self.draft("The Devil in Modern Philosophy\xa0(Boston: "
                           "Routledge, 1974).")
        self.assertEqual(draft, {"pub_type": "MENT", "year": "1974",
                                 "title": "The Devil in Modern Philosophy"})

    def test_author_names(self):
        self.assertEqual(Candidate(author="Minogue, K.R.").author_name(),
                         ("K.", "R.", "Minogue"))
        self.assertEqual(Candidate(author="Mayhew.").author_name(),
                         ("", "", "Mayhew"))
        self.assertIsNone(Candidate(author="Anon.").author_name())
        self.assertIsNone(Candidate(author="").author_name())


class AddItTest(TodoTestCase):
    """"Add it" opens the new-entry form filled in from a possible entry;
    saving it marks the possible entry added and links the two."""

    def setUp(self):
        super().setUp()
        self.login()
        self.candidate = Candidate.objects.create(
            author="Minogue, K.R.",
            citation="‘Parts and Wholes’,\xa0Political Studies, 14 (1974), "
                     "pp. 77-108.")
        self.url = ("/admin/berkeley/publication/add/"
                    f"?candidate={self.candidate.id}")

    def test_todo_page_has_add_it(self):
        html = self.client.get(TODO_URL).content.decode()
        self.assertIn(f'href="/admin/berkeley/publication/add/?candidate='
                      f'{self.unchecked.id}"', html)

    def test_form_is_filled_in(self):
        resp = self.client.get(self.url)
        initial = resp.context["adminform"].form.initial
        self.assertEqual(initial["title"], "Parts and Wholes")
        self.assertEqual(initial["journal"], self.journal.id)
        self.assertEqual(initial["year"], "1974")
        self.assertContains(resp, "Adding the possible entry")

    def save(self, **fields):
        data = {"title": "Parts and Wholes", "year": 1974,
                "pub_type": "MENT", "subject": self.unknown.id,
                "journal": self.journal.id, "volume": "14",
                "pages": "77-108",
                "authorship_set-TOTAL_FORMS": 0,
                "authorship_set-INITIAL_FORMS": 0,
                "editorship_set-TOTAL_FORMS": 0,
                "editorship_set-INITIAL_FORMS": 0, **fields}
        resp = self.client.post(self.url, data)
        self.assertEqual(resp.status_code, 302)
        self.candidate.refresh_from_db()
        return self.candidate.entry

    def test_saving_marks_it_added_with_its_author(self):
        entry = self.save()
        self.assertEqual(self.candidate.status, Candidate.ADDED)
        self.assertEqual(entry.title, "Parts and Wholes")
        self.assertEqual([(p.fname, p.mname, p.lname)
                          for p in entry.ordered_authors()],
                         [("K.", "R.", "Minogue")])

    def test_an_author_given_in_the_form_is_kept(self):
        entry = self.save(**{"authorship_set-TOTAL_FORMS": 1,
                             "authorship_set-0-person": self.mo.id,
                             "authorship_set-0-position": 1})
        self.assertEqual(entry.ordered_authors(), [self.mo])

    def test_candidate_admin_has_add_it(self):
        resp = self.client.get(
            f"/admin/berkeley/candidate/{self.candidate.id}/change/")
        self.assertContains(resp, f"?candidate={self.candidate.id}")
