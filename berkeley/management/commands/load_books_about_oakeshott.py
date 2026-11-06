"""Load the "Books About Oakeshott" entries into the database.

A book counts as being about Oakeshott if his name is in its title, even
when other names are there too (e.g. Tradition v. Rationalism:
Voegelin, Oakeshott, Hayek, and Others). First editions only.

Sources: the bibliographies of the Michael Oakeshott Association
(michaeloakeshottassociation.org/bibliography/), the Stanford
Encyclopedia of Philosophy entry, and contemporarythinkers.org, checked
against publisher and library records.

Safe to re-run: people and publishers are matched on their names,
and books on title and year, so running it twice does not create
duplicates. Subjects (SUBJECTS) are applied to every book, new or
existing, so re-running picks up edits to them.

    python manage.py load_books_about_oakeshott
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import Authorship, Publication, Subject, UNKNOWN_ID

from ._loaders import get_person, get_publisher

# (first, middle, last). Person has no suffix field, so "Jr." is dropped.
ABEL = ("Corey", "", "Abel")
ASTROV = ("Alexander", "", "Astrov")
BAKHURST = ("David", "", "Bakhurst")
BOTWINICK = ("Aryeh", "", "Botwinick")
CALLAHAN = ("Gene", "", "Callahan")
CANDREVA = ("Debra", "", "Candreva")
COATS = ("Wendell", "John", "Coats")
COREY = ("Elizabeth", "Campbell", "Corey")
DEVIGNE = ("Robert", "", "Devigne")
FAIRFIELD = ("Paul", "", "Fairfield")
FARR = ("Anthony", "", "Farr")
FRANCO = ("Paul", "", "Franco")
FULLER = ("Timothy", "", "Fuller")
GERENCSER = ("Steven", "Anthony", "Gerencser")
GRANT = ("Robert", "", "Grant")
GREENLEAF = ("W.", "H.", "Greenleaf")
ISAACS = ("Stuart", "", "Isaacs")
KING = ("Preston", "", "King")
KINZEL = ("Till", "", "Kinzel")
KOS = ("Eric", "S.", "Kos")
MARSH = ("Leslie", "", "Marsh")
MCILWAIN = ("David", "", "McIlwain")
MCINTYRE = ("Kenneth", "B.", "McIntyre")
NARDIN = ("Terry", "", "Nardin")
NORMAN = ("Jesse", "", "Norman")
ORSI = ("Davide", "", "Orsi")
OSULLIVAN_L = ("Luke", "", "O'Sullivan")
OSULLIVAN_N = ("Noël", "", "O'Sullivan")
PAREKH = ("B.", "C.", "Parekh")
PERRET = ("Quentin", "", "Perret")
PODOKSIK = ("Efraim", "", "Podoksik")
SINGH = ("Randhir", "", "Singh")
SOININEN = ("Suvi", "", "Soininen")
SULLIVAN = ("Andrew", "", "Sullivan")
THOMPSON = ("Martyn", "P.", "Thompson")
TREGENZA = ("Ian", "", "Tregenza")
TREPANIER = ("Lee", "", "Trepanier")
TSENG = ("Roy", "", "Tseng")
WILLIAMS = ("Kevin", "", "Williams")
WORTHINGTON = ("Glenn", "", "Worthington")

# name: (usual city, province). A book can override the city with "city".
PUBLISHERS = {
    "Antaios": ("Schnellroda", "Germany"),
    "Bloomsbury Academic": ("London", "England"),
    "Cambridge University Press": ("Cambridge", "England"),
    "The Claridge Press": ("London", "England"),
    "Continuum": ("New York", "NY"),
    "Duckworth": ("London", "England"),
    "Faber & Faber": ("London", "England"),
    "Imprint Academic": ("Exeter", "England"),
    "Lexington Books": ("Lanham", "MD"),
    "Liberty Fund": ("Carmel", "IN"),
    "Longmans": ("London", "England"),
    "Macmillan": ("London", "England"),
    "Michael Oakeshott Association": ("London", "England"),
    "Michalon": ("Paris", "France"),
    "Palgrave Macmillan": ("Cham", "Switzerland"),
    "Pennsylvania State University Press": ("University Park", "PA"),
    "People's Publishing House": ("New Delhi", "India"),
    "Princeton University Press": ("Princeton", "NJ"),
    "Routledge": ("London", "England"),
    "St. Martin's Press": ("New York", "NY"),
    "Susquehanna University Press": ("Selinsgrove", "PA"),
    "University of Missouri Press": ("Columbia", "MO"),
    "Vita e Pensiero": ("Milan", "Italy"),
    "Yale University Press": ("New Haven", "CT"),
}

BOOKS = [
    dict(title="Oakeshott's Philosophical Politics", year=1966,
         publisher="Longmans", authors=[GREENLEAF]),
    dict(title="Reason, Revolution and Political Theory: Notes on "
               "Oakeshott's 'Rationalism in Politics'",
         year=1967, publisher="People's Publishing House", authors=[SINGH]),
    dict(title="Politics and Experience: Essays Presented to Professor "
               "Michael Oakeshott on the Occasion of His Retirement",
         year=1968, publisher="Cambridge University Press",
         editors=[KING, PAREKH]),
    dict(title="The Politics of Imperfection: The Religious and Secular "
               "Traditions of Conservative Thought in England from Hooker to "
               "Oakeshott",
         year=1978, publisher="Faber & Faber",
         authors=[("Anthony", "", "Quinton")]),
    dict(title="The Political Philosophy of Michael Oakeshott", year=1990,
         publisher="Yale University Press", authors=[FRANCO]),
    dict(title="Oakeshott", year=1990, publisher="The Claridge Press",
         authors=[GRANT]),
    dict(title="The Achievement of Michael Oakeshott", year=1993,
         publisher="Duckworth", editors=[NORMAN]),
    dict(title="The Defence of Natural Law: A Study of the Ideas of Law and "
               "Justice in the Writings of Lon L. Fuller, Michael Oakeshott, "
               "F. A. Hayek, Ronald Dworkin and John Finnis",
         year=1992, publisher="Macmillan", city="Basingstoke",
         authors=[("Charles", "", "Covell")]),
    dict(title="Recasting Conservatism: Oakeshott, Strauss, and the "
               "Response to Postmodernism",
         year=1994, publisher="Yale University Press", authors=[DEVIGNE]),
    dict(title="Sartre's Radicalism and Oakeshott's Conservatism: "
               "The Duplicity of Freedom",
         year=1998, publisher="Macmillan", authors=[FARR]),
    dict(title="Il ragionevole disaccordo: Hayek, Oakeshott e le regole "
               "immotivate della società",
         year=1999, publisher="Vita e Pensiero",
         authors=[("S.", "", "Cotellessa")]),
    dict(title="The Skeptic's Oakeshott", year=2000,
         publisher="St. Martin's Press", authors=[GERENCSER]),
    dict(title="Oakeshott and His Contemporaries: Montaigne, St. Augustine, "
               "Hegel, et al.",
         year=2000, publisher="Susquehanna University Press",
         authors=[COATS]),
    dict(title="The Philosophy of Michael Oakeshott", year=2001,
         publisher="Pennsylvania State University Press", authors=[NARDIN]),
    dict(title="Michael Oakeshott, Philosopher: A Commemoration of the "
               "Centenary of Oakeshott's Birth",
         year=2001, publisher="Michael Oakeshott Association",
         editors=[MARSH]),
    dict(title="Oakeshott on History", year=2003,
         publisher="Imprint Academic", authors=[OSULLIVAN_L]),
    dict(title="In Defence of Modernity: Vision and Philosophy in "
               "Michael Oakeshott",
         year=2003, publisher="Imprint Academic", authors=[PODOKSIK]),
    dict(title="The Sceptical Idealist: Michael Oakeshott as a Critic of "
               "the Enlightenment",
         year=2003, publisher="Imprint Academic", authors=[TSENG]),
    dict(title="Michael Oakeshott on Hobbes: A Study in the Renewal of "
               "Philosophical Ideas",
         year=2003, publisher="Imprint Academic", authors=[TREGENZA]),
    dict(title="Michael Oakeshott: An Introduction", year=2004,
         publisher="Yale University Press", authors=[FRANCO]),
    dict(title="The Limits of Political Theory: Oakeshott's Philosophy of "
               "Civil Association",
         year=2004, publisher="Imprint Academic", authors=[MCINTYRE]),
    dict(title="Oakeshott: le scepticisme en politique", year=2004,
         publisher="Michalon", authors=[PERRET]),
    dict(title="The Enemies of Perfection: Oakeshott, Plato, and the "
               "Critique of Rationalism",
         year=2005, publisher="Lexington Books", authors=[CANDREVA]),
    dict(title="On World Politics: R. G. Collingwood, Michael Oakeshott "
               "and Neotraditionalism in International Relations",
         year=2005, publisher="Palgrave Macmillan", city="New York",
         authors=[ASTROV]),
    dict(title="The Intellectual Legacy of Michael Oakeshott", year=2005,
         publisher="Imprint Academic", editors=[ABEL, FULLER]),
    dict(title="Religious and Poetic Experience in the Thought of "
               "Michael Oakeshott",
         year=2005, publisher="Imprint Academic", authors=[WORTHINGTON]),
    dict(title="From a 'Necessary Evil' to an Art of Contingency: Michael "
               "Oakeshott's Conception of Political Activity",
         year=2005, publisher="Imprint Academic", authors=[SOININEN]),
    dict(title="Michael Oakeshott on Religion, Aesthetics, and Politics",
         year=2006, publisher="University of Missouri Press",
         authors=[COREY]),
    dict(title="The Politics and Philosophy of Michael Oakeshott",
         year=2006, publisher="Routledge", authors=[ISAACS]),
    dict(title="Michael Oakeshott: Philosoph der Politik", year=2007,
         publisher="Antaios", authors=[KINZEL]),
    dict(title="Michael Oakeshott, the Ancient Greeks, and the "
               "Philosophical Study of Politics",
         year=2007, publisher="Imprint Academic", authors=[KOS]),
    dict(title="Intimations Pursued: The Voice of Practice in the "
               "Conversation of Michael Oakeshott",
         year=2007, publisher="Imprint Academic", authors=[SULLIVAN]),
    dict(title="Education and the Voice of Michael Oakeshott", year=2007,
         publisher="Imprint Academic", authors=[WILLIAMS]),
    dict(title="Michael Oakeshott", year=2010, publisher="Continuum",
         authors=[("Edmund", "", "Neill")]),
    dict(title="The Meanings of Michael Oakeshott's Conservatism",
         year=2010, publisher="Imprint Academic", editors=[ABEL]),
    dict(title="Michael Oakeshott's Skepticism", year=2011,
         publisher="Princeton University Press", authors=[BOTWINICK]),
    dict(title="Oakeshott on Rome and America", year=2012,
         publisher="Imprint Academic", authors=[CALLAHAN]),
    dict(title="The Cambridge Companion to Oakeshott", year=2012,
         publisher="Cambridge University Press", editors=[PODOKSIK]),
    dict(title="A Companion to Michael Oakeshott", year=2012,
         publisher="Pennsylvania State University Press",
         editors=[FRANCO, MARSH]),
    dict(title="Michael Oakeshott's Cold War Liberalism", year=2015,
         publisher="Palgrave Macmillan", city="New York", editors=[NARDIN]),
    dict(title="Education and Conversation: Exploring Oakeshott's Legacy",
         year=2016, publisher="Bloomsbury Academic",
         editors=[BAKHURST, FAIRFIELD]),
    dict(title="Michael Oakeshott's Political Philosophy of International "
               "Relations: Civil Association and International Society",
         year=2016, publisher="Palgrave Macmillan", authors=[ORSI]),
    dict(title="The Place of Michael Oakeshott in Contemporary Western and "
               "Non-Western Thought",
         year=2017, publisher="Imprint Academic", editors=[OSULLIVAN_N]),
    dict(title="Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, "
               "and Others",
         year=2018, publisher="Lexington Books",
         editors=[TREPANIER, CALLAHAN]),
    dict(title="Michael Oakeshott on Authority, Governance, and the State",
         year=2019, publisher="Palgrave Macmillan", editors=[KOS]),
    dict(title="Michael Oakeshott and Leo Strauss: The Politics of "
               "Renaissance and Enlightenment",
         year=2019, publisher="Palgrave Macmillan", authors=[MCILWAIN]),
    dict(title="Michael Oakeshott and the Cambridge School on the History "
               "of Political Thought",
         year=2019, publisher="Routledge", authors=[THOMPSON]),
    dict(title="Michael Oakeshott as a Philosopher of the \"Creative\" "
               "and Other Essays",
         year=2019, publisher="Imprint Academic", authors=[COATS]),
    dict(title="Oakeshott's Skepticism, Politics, and Aesthetics", year=2022,
         publisher="Palgrave Macmillan", editors=[KOS]),
    dict(title="Michael Oakeshott on the Human Condition: Essays", year=2024,
         publisher="Liberty Fund", authors=[FULLER]),
    dict(title="Michael Oakeshott and Liberalism Revisited", year=2025,
         publisher="Palgrave Macmillan", editors=[KOS]),
]


# Subject for each book, keyed by title.
PHIL, POL, HIST, EDUC, IR = ("Philosophy", "Politics", "History",
                             "Education", "International Relations")
SUBJECTS = {
    "The Politics of Imperfection: The Religious and Secular Traditions of "
    "Conservative Thought in England from Hooker to Oakeshott": POL,
    "The Defence of Natural Law: A Study of the Ideas of Law and Justice in "
    "the Writings of Lon L. Fuller, Michael Oakeshott, F. A. Hayek, Ronald "
    "Dworkin and John Finnis": POL,
    "Il ragionevole disaccordo: Hayek, Oakeshott e le regole immotivate "
    "della società": POL,
    "Oakeshott's Philosophical Politics": POL,
    "Reason, Revolution and Political Theory: Notes on "
    "Oakeshott's 'Rationalism in Politics'": POL,
    "Politics and Experience: Essays Presented to Professor "
    "Michael Oakeshott on the Occasion of His Retirement": POL,
    "The Political Philosophy of Michael Oakeshott": POL,
    "Oakeshott": PHIL,
    "The Achievement of Michael Oakeshott": PHIL,
    "Recasting Conservatism: Oakeshott, Strauss, and the "
    "Response to Postmodernism": POL,
    "Sartre's Radicalism and Oakeshott's Conservatism: "
    "The Duplicity of Freedom": POL,
    "The Skeptic's Oakeshott": POL,
    "Oakeshott and His Contemporaries: Montaigne, St. Augustine, "
    "Hegel, et al.": PHIL,
    "The Philosophy of Michael Oakeshott": PHIL,
    "Michael Oakeshott, Philosopher: A Commemoration of the "
    "Centenary of Oakeshott's Birth": PHIL,
    "Oakeshott on History": HIST,
    "In Defence of Modernity: Vision and Philosophy in "
    "Michael Oakeshott": PHIL,
    "The Sceptical Idealist: Michael Oakeshott as a Critic of "
    "the Enlightenment": PHIL,
    "Michael Oakeshott on Hobbes: A Study in the Renewal of "
    "Philosophical Ideas": PHIL,
    "Michael Oakeshott: An Introduction": PHIL,
    "The Limits of Political Theory: Oakeshott's Philosophy of "
    "Civil Association": POL,
    "Oakeshott: le scepticisme en politique": POL,
    "The Enemies of Perfection: Oakeshott, Plato, and the "
    "Critique of Rationalism": POL,
    "On World Politics: R. G. Collingwood, Michael Oakeshott "
    "and Neotraditionalism in International Relations": IR,
    "The Intellectual Legacy of Michael Oakeshott": PHIL,
    "Religious and Poetic Experience in the Thought of "
    "Michael Oakeshott": PHIL,
    "From a 'Necessary Evil' to an Art of Contingency: Michael "
    "Oakeshott's Conception of Political Activity": POL,
    "Michael Oakeshott on Religion, Aesthetics, and Politics": PHIL,
    "The Politics and Philosophy of Michael Oakeshott": POL,
    "Michael Oakeshott: Philosoph der Politik": POL,
    "Michael Oakeshott, the Ancient Greeks, and the "
    "Philosophical Study of Politics": POL,
    "Intimations Pursued: The Voice of Practice in the "
    "Conversation of Michael Oakeshott": PHIL,
    "Education and the Voice of Michael Oakeshott": EDUC,
    "Michael Oakeshott": POL,
    "The Meanings of Michael Oakeshott's Conservatism": POL,
    "Michael Oakeshott's Skepticism": PHIL,
    "Oakeshott on Rome and America": POL,
    "The Cambridge Companion to Oakeshott": PHIL,
    "A Companion to Michael Oakeshott": PHIL,
    "Michael Oakeshott's Cold War Liberalism": POL,
    "Education and Conversation: Exploring Oakeshott's Legacy": EDUC,
    "Michael Oakeshott's Political Philosophy of International "
    "Relations: Civil Association and International Society": IR,
    "The Place of Michael Oakeshott in Contemporary Western and "
    "Non-Western Thought": PHIL,
    "Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, "
    "and Others": PHIL,
    "Michael Oakeshott on Authority, Governance, and the State": POL,
    "Michael Oakeshott and Leo Strauss: The Politics of "
    "Renaissance and Enlightenment": POL,
    "Michael Oakeshott and the Cambridge School on the History "
    "of Political Thought": HIST,
    "Michael Oakeshott as a Philosopher of the \"Creative\" "
    "and Other Essays": PHIL,
    "Oakeshott's Skepticism, Politics, and Aesthetics": PHIL,
    "Michael Oakeshott on the Human Condition: Essays": PHIL,
    "Michael Oakeshott and Liberalism Revisited": POL,
}


class Command(BaseCommand):
    help = "Load the Books About Oakeshott entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        created = updated = 0
        for book in BOOKS:
            pub, is_new = Publication.objects.get_or_create(
                title=book["title"], year=book["year"], pub_type="BKAB",
                defaults={"publisher": get_publisher(
                    book["publisher"], PUBLISHERS, book.get("city"))})
            subject, _ = Subject.objects.get_or_create(
                name=SUBJECTS[book["title"]])
            if pub.subject_id != subject.id:
                pub.subject = subject
                pub.save(update_fields=["subject"])
                updated += 1
            if not is_new:
                continue
            created += 1
            for pos, name in enumerate(book.get("authors", []), 1):
                Authorship.objects.create(publication=pub,
                                          person=get_person(name),
                                          position=pos)
            for name in book.get("editors", []):
                pub.editors.add(get_person(name))
        self.stdout.write(f"Added {created} books "
                          f"({len(BOOKS) - created} already present); "
                          f"set subject on {updated}.")
