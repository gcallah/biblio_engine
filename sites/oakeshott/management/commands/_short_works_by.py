"""Data for load_short_works_by_oakeshott: shorter works by Oakeshott,
chiefly those whose full text can be read free online from a legitimate
source ("url"). A few without a free text are added at the user's
request.

Each entry records the first publication (from the Michael Oakeshott
Association bibliography) and, in "url", where the full text can be
read. Sources used, and why they are legitimate:

- Liberty Fund's Online Library of Liberty, which offers its edition of
  Hobbes on Civil Association (2000) free for educational use;
- the Journal of Educational Thought, which publishes its back issues
  open access;
- First Things, which printed "Work and Play" with the permission of the
  Oakeshott estate and keeps it on its site.

Copies uploaded without permission (course reading lists, file-sharing
uploads of in-copyright books) are deliberately left out.

ARTICLES and CHAPTERS work as in _short_works_about.py; a chapter's
"book" is the title of a Books by Oakeshott entry or a key into HOSTS.
"""

PHIL, POL, EDUC, HIST = ("Philosophy", "Politics", "Education",
                         "History")

OAKESHOTT = ("Michael", "", "Oakeshott")

HOBBES_ON_CIVIL_ASSOCIATION_URL = (
    "https://oll.libertyfund.org/titles/franco-hobbes-on-civil-association")

# Books by Oakeshott already in the database
RATIONALISM = "Rationalism in Politics and Other Essays"

PUBLISHERS = {
    "Basil Blackwell": ("Oxford", "England"),
}

HOSTS = {
    "leviathan": dict(
        subject=POL,
        title="Leviathan, or the Matter, Forme and Power of a Commonwealth "
              "Ecclesiasticall and Civil",
        year=1946, publisher="Basil Blackwell",
        authors=[("Thomas", "", "Hobbes")], editors=[OAKESHOTT]),
}

ARTICLES = [
    dict(authors=[OAKESHOTT], title="Dr. Leo Strauss on Hobbes",
         journal="Politica", volume="2", year=1937, pages="364-379",
         url=HOBBES_ON_CIVIL_ASSOCIATION_URL, subject=POL),
    # broadcast talk; reprinted as "Leviathan: A Myth"
    dict(authors=[OAKESHOTT],
         title='The "Collective Dream of Civilisation"',
         journal="Listener", volume="37", year=1947, pages="966-967",
         url=HOBBES_ON_CIVIL_ASSOCIATION_URL, subject=POL),
    dict(authors=[OAKESHOTT], title="The Definition of a University",
         journal="Journal of Educational Thought", volume="1", issue="3",
         year=1967, pages="129-142",
         url="https://journalhosting.ucalgary.ca/index.php/jet/article/"
             "view/43498",
         doi="10.55016/ojs/jet.v1i3.43498", subject=EDUC),
    # Without a free text online:
    dict(authors=[OAKESHOTT],
         title="The University Programme: Arts Philosophy of History",
         journal="Collingwood and British Idealism Studies", volume="8",
         issue="1", year=2001, pages="1-5", subject=HIST),
    dict(authors=[OAKESHOTT],
         title="The Concept of Government in Modern Europe",
         journal="Collingwood and British Idealism Studies", volume="12",
         issue="2", year=2006, pages="17-35", subject=POL),
    dict(authors=[OAKESHOTT], title="Work and Play", journal="First Things",
         volume="54", month="June/July", year=1995, pages="29-33",
         url="https://firstthings.com/work-and-play/", subject=PHIL),
]

CHAPTERS = [
    dict(authors=[OAKESHOTT], title="Introduction to Leviathan",
         book="leviathan", url=HOBBES_ON_CIVIL_ASSOCIATION_URL,
         subject=POL),
    # from a lecture at the University of Nottingham
    dict(authors=[OAKESHOTT],
         title="The Moral Life in the Writings of Thomas Hobbes",
         book=RATIONALISM, url=HOBBES_ON_CIVIL_ASSOCIATION_URL,
         subject=POL),
]
