"""Data for load_works_mentioning_oakeshott: works on other subjects that
have something of substance to say about Oakeshott.

Source: section 4 ("Other Published Works") of the Michael Oakeshott
Association bibliography, michaeloakeshottassociation.org/bibliography/
(parsed 2026-11-07), which lists anything that mentions him. Its items
whose titles do not name him were sorted on 2026-11-09/10, and only
conservatively:

- a work is here only if a source we could open (the full text, a
  search inside the book, the index, a publisher's or journal's
  abstract, or, for one essay, a contemporary review describing its
  argument) shows that it discusses Oakeshott at some length: a
  chapter, a section, several pages, or an argument built on or
  against his views. A passing reference or quotation is not enough.
- items that are about Oakeshott himself (chapters in books about him,
  introductions to his books, obituaries) are Short Works About
  Oakeshott entries instead (see _short_works_about.py).
- everything else, with the reason it was left out, is in
  docs/works_mentioning_triage.csv. Its "edge" rows are works that may
  well have something to say about Oakeshott but where we could not
  tell.

Each entry's abstract, in _abstracts.py, says how the work deals with
Oakeshott rather than what the work as a whole is about.

BOOKS are whole books. ARTICLES are in journals. CHAPTERS are parts of
books: "book" is the title of a book already in the database (Books
About, Books by, or Works Mentioning) or a key into HOSTS. A book's year
is the edition MOA cites.
"""

PHIL, POL, HIST, EDUC, IR = ("Philosophy", "Politics", "History",
                             "Education", "International Relations")

# name: (usual city, province)
PUBLISHERS = {
    "Clarendon Press": ("Oxford", "England"),
    "Oxford University Press": ("Oxford", "England"),
    "Prentice-Hall": ("Englewood Cliffs", "NJ"),
    "Random House": ("New York", "NY"),
    "Hutchinson": ("London", "England"),
    "Martinus Nijhoff": ("The Hague", "Netherlands"),
    "Ashgate": ("Aldershot", "England"),
    "Weidenfeld and Nicolson": ("London", "England"),
    "Martin Robertson": ("Oxford", "England"),
    "Macmillan": ("Basingstoke", "England"),
    "Methuen": ("London", "England"),
    "Penguin": ("Harmondsworth", "England"),
    "Cambridge University Press": ("Cambridge", "England"),
    "Princeton University Press": ("Princeton", "NJ"),
    "Cornell University Press": ("Ithaca", "NY"),
    "Polity Press": ("Cambridge", "England"),
    "Harper and Row": ("New York", "NY"),
    "Routledge and Kegan Paul": ("London", "England"),
    "Edinburgh University Press": ("Edinburgh", "Scotland"),
    "Susquehanna University Press": ("Selinsgrove", "PA"),
    "Palgrave Macmillan": ("Cham", "Switzerland"),
    "Verso": ("London", "England"),
    "Basil Blackwell": ("Oxford", "England"),
}

# Books holding a chapter that discusses Oakeshott. Stored as Works
# Mentioning entries; the chapter carries the abstract.
HOSTS = {
    "radical_democracy": dict(
        subject=POL,
        title="Dimensions of Radical Democracy: Pluralism, Citizenship, "
              "Community",
        year=1992, publisher="Verso", editors=[("Chantal", "", "Mouffe")]),
    "wittgenstein_times": dict(
        subject=PHIL, title="Wittgenstein and His Times", year=1982,
        publisher="Basil Blackwell", editors=[("B.", "", "McGuinness")]),
}

BOOKS = [
    dict(authors=[("R.", "G.", "Collingwood")],
         title="The Idea of History", year=1946,
         publisher="Clarendon Press", subject=HIST),
    dict(authors=[("W.", "H.", "Dray")],
         title="Laws and Explanation in History", year=1957,
         publisher="Oxford University Press", subject=HIST),
    dict(authors=[("W.", "H.", "Dray")], title="Philosophy of History",
         year=1964, publisher="Prentice-Hall", subject=HIST),
    dict(authors=[("J.", "W.", "Meiland")],
         title="Scepticism and Historical Knowledge", year=1965,
         publisher="Random House", subject=HIST),
    # The third, revised edition (first published 1951).
    dict(authors=[("W.", "H.", "Walsh")],
         title="An Introduction to Philosophy of History", year=1967,
         publisher="Hutchinson", subject=HIST),
    dict(authors=[("N.", "", "Rotenstreich")],
         title="Philosophy, History and Politics: Studies in Contemporary "
               "English Philosophy of History",
         year=1976, publisher="Martinus Nijhoff", subject=HIST),
    dict(authors=[("C.", "", "Parker")],
         title="The English Idea of History from Coleridge to Collingwood",
         year=2000, publisher="Ashgate", subject=HIST),
    # --- politics and conservatism ---
    dict(authors=[("N.", "", "Annan")],
         title="Our Age: Portrait of a Generation", year=1990,
         publisher="Weidenfeld and Nicolson", subject=POL),
    dict(authors=[("B.", "C.", "Parekh")],
         title="Contemporary Political Thinkers", year=1982,
         publisher="Martin Robertson", subject=POL),
    dict(authors=[("Charles", "", "Covell")],
         title="The Redefinition of Conservatism: Politics and Doctrine",
         year=1986, publisher="Macmillan", subject=POL),
    dict(authors=[("I.", "", "Gilmour")],
         title="Inside Right: A Study of Conservatism", year=1977,
         publisher="Hutchinson", subject=POL),
    # The revised Pelican edition (first published 1962).
    dict(authors=[("B.", "", "Crick")], title="In Defence of Politics",
         year=1964, publisher="Penguin", subject=POL),
    # Volume I.
    dict(authors=[("M.", "", "Cowling")],
         title="Religion and Public Doctrine in Modern England", year=1980,
         publisher="Cambridge University Press", subject=HIST),
    dict(authors=[("B.", "R.", "Barber")],
         title="The Conquest of Politics: Liberal Philosophy in Democratic "
               "Times",
         year=1988, publisher="Princeton University Press", subject=POL),
    dict(authors=[("D.", "", "Germino")],
         title="Beyond Ideology: The Revival of Political Theory", year=1967,
         publisher="Harper and Row", subject=POL),
    dict(authors=[("R.", "E.", "Flathman")], title="Toward a Liberalism",
         year=1989, publisher="Cornell University Press",
         subject=POL),
    dict(authors=[("J.", "N.", "Gray")],
         title="Endgames: Questions in Late Modern Political Thought",
         year=1997, publisher="Polity Press", subject=POL),
    dict(authors=[("David", "", "Boucher"),
                  ("A.", "", "Vincent")],
         title="British Idealism and Political Theory", year=2000,
         publisher="Edinburgh University Press", subject=PHIL),
    dict(authors=[("Wendell", "John", "Coats")],
         title="Political Theory and Practice: Eight Essays on a Theme",
         year=2003, publisher="Susquehanna University Press", subject=POL),
    dict(authors=[("N.", "E.", "Nedzel"), ("N.", "", "Capaldi")],
         title="The Anglo-American Conception of the Rule of Law",
         year=2019, publisher="Palgrave Macmillan",
         doi="10.1007/978-3-030-26361-4", subject=POL),
    # --- social science, law and international relations ---
    dict(authors=[("P.", "", "Winch")],
         title="The Idea of a Social Science and Its Relation to "
               "Philosophy",
         year=1958, publisher="Routledge and Kegan Paul", subject=PHIL),
    dict(authors=[("Terry", "", "Nardin")],
         title="Law, Morality, and the Relations of States", year=1983,
         publisher="Princeton University Press", subject=IR),
    dict(authors=[("R.", "", "Jackson")],
         title="The Global Covenant: Human Conduct in a World of States",
         year=2000, publisher="Oxford University Press", subject=IR),
]

ARTICLES = [
    dict(authors=[("W.", "", "Bain")],
         title="Are There Any Lessons of History? The English School and "
               "the Activity of Being an Historian",
         journal="International Politics", volume="44", issue="5",
         year=2007, pages="513-530", doi="10.1057/palgrave.ip.8800204",
         subject=IR),
    dict(authors=[("K.", "R.", "Minogue")],
         title="Parts and Wholes: Twentieth Century Interpretation of "
               "Thomas Hobbes",
         journal="Anales de la Cátedra Francisco Suárez", volume="14",
         year=1974, pages="77-108", doi="10.30827/acfs.v14i.26435",
         subject=POL),
    dict(authors=[("R.", "", "Staal")],
         title="The Irony of Modern Conservatism",
         journal="International Political Science Review", volume="8",
         issue="4", year=1987, pages="343-353",
         doi="10.1177/019251218700800405", subject=POL),
    dict(authors=[("A.", "", "Edgar")],
         title="Enterprise Association or Civil Association? The UK "
               "National Health Service",
         journal="Journal of Medicine and Philosophy", volume="20",
         issue="6", year=1995, pages="669-688", doi="10.1093/jmp/20.6.669",
         subject=POL),
    dict(authors=[("M.", "", "Canovan")],
         title="Trust the People! Populism and the Two Faces of Democracy",
         journal="Political Studies", volume="47", issue="1", year=1999,
         pages="2-16", doi="10.1111/1467-9248.00184", subject=POL),
    dict(authors=[("B.", "", "Arditi")],
         title="Populism as a Spectre of Democracy: A Response to Canovan",
         journal="Political Studies", volume="52", issue="1", year=2004,
         pages="135-143", doi="10.1111/j.1467-9248.2004.00468.x",
         subject=POL),
    dict(authors=[("F.", "", "Dallmayr")],
         title="Conversation Across Boundaries: Political Theory and Global "
               "Diversity",
         journal="Millennium: Journal of International Studies",
         volume="30", issue="2", year=2001, pages="331-347",
         doi="10.1177/03058298010300021101", subject=IR),
    dict(authors=[("N.", "", "Rengger")],
         title="The Boundaries of Conversation: A Response to Dallmayr",
         journal="Millennium: Journal of International Studies",
         volume="30", issue="2", year=2001, pages="357-364",
         doi="10.1177/03058298010300020201", subject=IR),
    dict(authors=[("James", "", "Alexander")],
         title="An Essay on Historical, Philosophical and Theological "
               "Attitudes to Modern Political Thought",
         journal="History of Political Thought", volume="25", issue="1",
         year=2004, pages="116-148", subject=POL),
]

POLITICS_AND_EXPERIENCE = ("Politics and Experience: Essays Presented to "
                           "Professor Michael Oakeshott on the Occasion of "
                           "His Retirement")

CHAPTERS = [
    # An essay in Oakeshott's Festschrift arguing that he does not solve
    # the traditionalist's dilemma. The evidence is G. Barraclough's
    # review of the volume (Spectator, 31 January 1969), which describes
    # that argument; Pocock's essay in the volume, which the same review
    # describes less clearly, is an edge case.
    dict(authors=[("K.", "R.", "Minogue")],
         title="Revolution, Tradition and Political Continuity",
         book=POLITICS_AND_EXPERIENCE, pages="283-308", subject=POL),
    # MOA lists the whole book; the discussion is in Mouffe's chapter.
    dict(authors=[("Chantal", "", "Mouffe")],
         title="Democratic Citizenship and the Political Community",
         book="radical_democracy", subject=POL),
    dict(authors=[("J.", "C.", "Nyiri")],
         title="Wittgenstein's Later Work in Relation to Conservatism",
         book="wittgenstein_times", pages="44-68", subject=PHIL),
]
