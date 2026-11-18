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
