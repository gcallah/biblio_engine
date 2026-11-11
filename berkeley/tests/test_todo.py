"""The editors' to-do page, its menu links, and load_editors_todo."""
from io import StringIO

from django.core.management import call_command

from berkeley.management.commands._short_works_about import OBIT
from berkeley.models import Candidate, Journal, OpenQuestion

from .test_login import LoginTestCase

TODO_URL = "/oakeshott/todo/"
DT_QUESTION = ("Are the three Daily Telegraph obituaries (21 December "
               "1990) one piece?")


class TodoTestCase(LoginTestCase):
    def setUp(self):
        super().setUp()
        telegraph = Journal.objects.create(name="Daily Telegraph")
        self.obits = [
            self.pub(OBIT, 1990, journal=telegraph, month="December",
                     day="21", authors=authors, pub_type="SWAB")
            for authors in ([], [self.person("J.", "Casey")],
                            [self.person("P.", "Worsthorne")])]
        # a different obituary in the same paper is not part of it
        self.pub(OBIT, 1990, journal=telegraph, month="December", day="22",
                 pub_type="SWAB")

    def load(self):
        out = StringIO()
        call_command("load_editors_todo", stdout=out)
        return out.getvalue()


class AnonymousTodoTest(TodoTestCase):
    def test_no_editor_links_in_menu(self):
        html = self.client.get("/oakeshott/").content.decode()
        self.assertNotIn("Add entry", html)
        self.assertNotIn("To do", html)

    def test_todo_page_needs_a_login(self):
        resp = self.client.get(TODO_URL)
        self.assertRedirects(resp, f"/oakeshott/login/?next={TODO_URL}",
                             fetch_redirect_response=False)


class EditorTodoTest(TodoTestCase):
    def setUp(self):
        super().setUp()
        self.login()

    def test_menu_links(self):
        html = self.client.get("/oakeshott/").content.decode()
        self.assertIn('href="/admin/berkeley/publication/add/">Add entry</a>',
                      html)
        self.assertIn(f'href="{TODO_URL}">To do</a>', html)

    def test_add_entry_page(self):
        resp = self.client.get("/admin/berkeley/publication/add/")
        self.assertEqual(resp.status_code, 200)

    def test_loader_is_idempotent(self):
        self.assertIn("Added 351 possible entries and 1 open questions",
                      self.load())
        self.assertIn("Added 0 possible entries and 0 open questions",
                      self.load())
        self.assertEqual(Candidate.objects.count(), 351)

    def test_statuses_from_the_csv(self):
        self.load()
        acton = Candidate.objects.get(moa_line=837)
        self.assertEqual(acton.status, Candidate.UNDECIDED)
        self.assertTrue(acton.reason)
        abbate = Candidate.objects.get(moa_line=831)
        self.assertEqual(abbate.status, Candidate.NOT_CHECKED)
        self.assertEqual(abbate.reason, "")
        mayer = Candidate.objects.get(moa_line=1179)
        self.assertEqual(mayer.status, Candidate.ADDED)
        self.assertTrue(mayer.reason.startswith("Short Works About (loaded)."))

    def test_loader_keeps_editors_decisions(self):
        self.load()
        Candidate.objects.filter(moa_line=837).update(
            status=Candidate.LEFT_OUT)
        self.load()
        self.assertEqual(Candidate.objects.get(moa_line=837).status,
                         Candidate.LEFT_OUT)

    def test_question_links_the_three_obituaries(self):
        self.load()
        question = OpenQuestion.objects.get(title=DT_QUESTION)
        self.assertEqual(set(question.entries.all()), set(self.obits))

    def test_todo_page(self):
        self.load()
        html = self.client.get(TODO_URL).content.decode()
        self.assertIn(DT_QUESTION, html)
        self.assertIn("(Casey)", html)
        self.assertIn("Tradition and Some Other Forms of Order", html)
        self.assertIn("A Preface to the Philosophy of the State", html)
        self.assertIn("Undecided: researched, but we could not tell (86)",
                      html)
        self.assertIn("Not checked yet (146)", html)
        # decided ones are not listed
        self.assertNotIn("Managers, Machiavelli", html)
        acton = Candidate.objects.get(moa_line=837)
        self.assertIn(f'href="/admin/berkeley/candidate/{acton.id}/change/"',
                      html)

    def test_settled_questions_leave_the_page(self):
        self.load()
        OpenQuestion.objects.update(settled=True)
        html = self.client.get(TODO_URL).content.decode()
        self.assertNotIn(DT_QUESTION, html)

    def test_admin_lists(self):
        self.load()
        for url in ("/admin/berkeley/openquestion/",
                    "/admin/berkeley/candidate/",
                    "/admin/berkeley/openquestion/add/",
                    "/admin/berkeley/candidate/add/"):
            self.assertEqual(self.client.get(url).status_code, 200, url)
