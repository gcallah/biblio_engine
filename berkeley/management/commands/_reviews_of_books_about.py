"""Data for load_reviews_of_books_about_oakeshott: reviews of books about
Oakeshott, stored as "Book Reviews of Books About Oakeshott" (RVAB).

Sources:
- MOA: section 3 ("Books on Oakeshott and their Reviews") of the Michael
  Oakeshott Association bibliography,
  michaeloakeshottassociation.org/bibliography/, parsed on 2026-11-07
  and checked by hand. MOA stops at about 2008.
- WEB: later reviews found on the publishers' and journals' sites on
  2026-11-07. Each of these has a URL or DOI.

Each entry's "book" is the Books About Oakeshott entry it reviews (by
its title in the database). A review of several books is one entry
here; "also" names the other books. The database links a review to
one book (pub_reviewed), but the authors (or, for edited volumes, the
editors) of every book it reviews are its reviewees, so a "Reviewed
author" search finds it under each of them.

Left out:
- M. Rushton, 'Michael Oakeshott: A Review Essay' (Review of Politics,
  1992), and P. Coleman, 'Escaping Plato's Cave' (Quadrant, 2006):
  both are already Book Reviews of Books by Oakeshott entries. (Rushton
  also reviews Franco 1990 and Grant; Coleman also reviews Soininen and
  Worthington.)
- Letters, not reviews: P. Franco, TLS (10 August 1990), p. 847, and
  T. Fuller, TLS (27 July 1990), p. 799, both answering J. Waldron's
  review of Franco 1990.
- R. Orr, LSE Magazine, p. 32 (on Grant): MOA gives no date.
- Leads not confirmed (no page, URL or DOI seen), 2026-11-07: a Political
  Studies Review notice of Candreva (quoted on Amazon); a Spanish review
  of Botwinick (Universidad de Navarra repository, by "Alonso"?); C. F.
  Murphy, Philosophical Quarterly 45 (1995), and P. Franco, Review of
  Politics 57 (1995), pp. 346-8, on Covell; P. Coby, Choice 32 (1994), on
  Devigne; W. J. Coats, Choice 54 (May 2017), on Orsi.
- J. L. Auspitz, 'A New Look at Michael Oakeshott' (Claremont Review of
  Books, Spring 2014): it reviews Experience and Its Modes, so it is a
  Book Reviews of Books by Oakeshott entry, though it also discusses
  Callahan, the two Companions and others.
- The Cosmos + Taxis 10(1+2) (2022) symposium on McIlwain's book: its
  essays are Short Works About Oakeshott entries.
- RealClearBooks' 'Michael Oakeshott's Life of Reflection' (26 June
  2024) reposts E. Corey's Law & Liberty review of the day before.
- D. Orsi, 'Review Article: Philosophy and Politics: Recent Studies of
  Oakeshott' (CBIS, 2013) is already a Short Works About Oakeshott entry.

Corrections to MOA: 'Oaekshott' in L. Armour's title; G. Feaver's
'Out of the Rough' lacks its closing quote in one listing. Farr's book
is listed as 'Understanding Sartre's Radicalism ...'; the database
title has no 'Understanding'. A year range such as '1966-7' is stored
as its first year.

Kept as MOA gives them, though doubtful: C. B. Macpherson, Political
Science Quarterly 36 (1971) (PSQ's 1971 volume is 86).

MOA's 'K. Reschauer' (Canadian Journal of Political Science, 1970) is
Ken Reshaur, as Cambridge Core lists him.
"""

# Books About Oakeshott, by their titles in the database
LEGACY = "The Intellectual Legacy of Michael Oakeshott"
ASTROV = ("On World Politics: R. G. Collingwood, Michael Oakeshott and "
          "Neotraditionalism in International Relations")
COATS = "Oakeshott and His Contemporaries: Montaigne, St. Augustine, Hegel, et al."
COREY = "Michael Oakeshott on Religion, Aesthetics, and Politics"
FARR = "Sartre's Radicalism and Oakeshott's Conservatism: The Duplicity of Freedom"
FRANCO90 = "The Political Philosophy of Michael Oakeshott"
FRANCO04 = "Michael Oakeshott: An Introduction"
GERENCSER = "The Skeptic's Oakeshott"
GRANT = "Oakeshott"
GREENLEAF = "Oakeshott's Philosophical Politics"
ISAACS = "The Politics and Philosophy of Michael Oakeshott"
KING_PAREKH = ("Politics and Experience: Essays Presented to Professor "
               "Michael Oakeshott on the Occasion of His Retirement")
MCINTYRE = "The Limits of Political Theory: Oakeshott's Philosophy of Civil Association"
MARSH = ("Michael Oakeshott, Philosopher: A Commemoration of the Centenary "
         "of Oakeshott's Birth")
NARDIN = "The Philosophy of Michael Oakeshott"
NORMAN = "The Achievement of Michael Oakeshott"
OSULLIVAN = "Oakeshott on History"
PERRET = "Oakeshott: le scepticisme en politique"
PODOKSIK = "In Defence of Modernity: Vision and Philosophy in Michael Oakeshott"
SINGH = ("Reason, Revolution and Political Theory: Notes on Oakeshott's "
         "'Rationalism in Politics'")
TREGENZA = "Michael Oakeshott on Hobbes: A Study in the Renewal of Philosophical Ideas"
TSENG = "The Sceptical Idealist: Michael Oakeshott as a Critic of the Enlightenment"
WILLIAMS = "Education and the Voice of Michael Oakeshott"
ROME_AMERICA = "Oakeshott on Rome and America"
CAMBRIDGE_SCHOOL = ("Michael Oakeshott and the Cambridge School on the "
                    "History of Political Thought")
PLOTICA = ("Michael Oakeshott and the Conversation of Modern Political "
           "Thought")
HUMAN_CONDITION = "Michael Oakeshott on the Human Condition: Essays"
KINZEL = "Michael Oakeshott: Philosoph der Politik"
COLD_WAR = "Michael Oakeshott's Cold War Liberalism"
EDUCATION_CONVERSATION = "Education and Conversation: Exploring Oakeshott's Legacy"
ORSI = ("Michael Oakeshott's Political Philosophy of International "
        "Relations: Civil Association and International Society")
PLACE = ("The Place of Michael Oakeshott in Contemporary Western and "
         "Non-Western Thought")
TRADITION = "Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, and Others"
MCILWAIN = ("Michael Oakeshott and Leo Strauss: The Politics of Renaissance "
            "and Enlightenment")
COATS19 = 'Michael Oakeshott as a Philosopher of the "Creative" and Other Essays'
KOS22 = "Oakeshott's Skepticism, Politics, and Aesthetics"
SULLIVAN = ("Intimations Pursued: The Voice of Practice in the Conversation "
            "of Michael Oakeshott")
ABEL = "The Meanings of Michael Oakeshott's Conservatism"
BOTWINICK = "Michael Oakeshott's Skepticism"
CAMBRIDGE_COMPANION = "The Cambridge Companion to Oakeshott"
COMPANION = "A Companion to Michael Oakeshott"
DEVIGNE = ("Recasting Conservatism: Oakeshott, Strauss, and the Response to "
           "Postmodernism")
COVELL = ("The Defence of Natural Law: A Study of the Ideas of Law and "
          "Justice in the Writings of Lon L. Fuller, Michael Oakeshott, F. A. "
          "Hayek, Ronald Dworkin and John Finnis")

ARMOUR_TITLE = "Michael Oakeshott – A Fish Too Big or Too Slippery?"
CT = "Cosmos + Taxis"
CT_PDF = "https://cosmosandtaxis.org/wp-content/uploads/"
TLS = "Times Literary Supplement"

REVIEWS = [
    # ---- MOA ----
    dict(book=LEGACY, authors=[('A.', '', 'Van de Putte')],
         journal='Tijdschrift voor Filosofie', volume='68', year=2006,
         pages='668'),
    dict(book=ASTROV, authors=[('L.', 'G.', 'Montoya')],
         journal='Journal of International Relations and Development',
         volume='11', year=2008, pages='314-6'),
    # Coats
    dict(book=COATS, authors=[('L.', '', 'Armour')], title=ARMOUR_TITLE,
         journal='British Journal for the History of Philosophy',
         volume='13', year=2005, pages='779-93',
         also=[FARR, FRANCO90, FRANCO04, GERENCSER, MCINTYRE, MARSH, NARDIN,
               OSULLIVAN, PODOKSIK, TSENG]),
    dict(book=COATS, authors=[('D.', '', 'Boucher')],
         journal='English Historical Review', volume='117', year=2002,
         pages='225-6'),
    dict(book=COATS, authors=[('M.', '', 'Britnell')],
         journal='Political Studies', volume='49', year=2001,
         pages='567-8', also=[GERENCSER]),
    dict(book=COATS, authors=[('T.', '', 'Fuller')],
         journal='American Political Science Review', volume='95',
         year=2001, pages='461-3', also=[FARR, GERENCSER]),
    dict(book=COATS, authors=[('S.', '', 'Roggeveen')],
         journal='Australian Journal of Political Science', volume='36',
         year=2001, pages='205-6'),
    # Corey
    dict(book=COREY, authors=[('E.', '', 'Podoksik')],
         title="Commentary on Elizabeth Corey's Interpretation of Michael "
               "Oakeshott",
         journal='Zygon: Journal of Religion & Science', volume='44',
         year=2009, pages='223-6'),
    dict(book=COREY, authors=[('B.', '', 'Swaim')], title='The Right Stuff',
         journal='Weekly Standard', day='21', month='April', year=2008),
    # Farr
    dict(book=FARR, authors=[('C.', '', 'Abel')], journal='Political Theory',
         volume='28', year=2000, pages='875-9'),
    dict(book=FARR, authors=[('D.', '', 'Detmer')],
         journal='Sartre Studies International', volume='6', year=2000,
         pages='70-2'),
    dict(book=FARR, authors=[('G.', '', 'Feaver')], title='Freedom for Our Kind',
         journal=TLS, day='16', month='October', year=1998, pages='28'),
    dict(book=FARR, authors=[('R.', '', 'Huelson')], journal='Choice',
         volume='36', month='October', year=1998, pages='332'),
    dict(book=FARR, authors=[('S.', '', 'Soininen')],
         title='The Three Faces of Oakeshott',
         journal='European Journal of Political Theory', volume='4',
         year=2005, pages='109-18', also=[GERENCSER, NARDIN]),
    dict(book=FARR, authors=[('S.', '', 'Soininen'), ('L.', '', 'Subra')],
         title='Anthony Farr on Oakeshott and Sartre',
         journal='Finnish Yearbook of Political Thought', volume='3',
         year=1999, pages='229-38'),
    # Franco 1990
    dict(book=FRANCO90, authors=[('W.', 'J.', 'Coats')],
         journal='Review of Politics', volume='53', year=1991,
         pages='414-16'),
    dict(book=FRANCO90, authors=[('E.', 'J.', 'Eisenach')], journal='Choice',
         volume='28', year=1991, pages='1001'),
    dict(book=FRANCO90, authors=[('T.', '', 'Fuller')], journal='Ethics',
         volume='105', year=1995, pages='444-445'),
    dict(book=FRANCO90, authors=[('W.', 'H.', 'Greenleaf')],
         title='A Liberal Learning',
         journal='Times Higher Education Supplement', day='6', month='July',
         year=1990, pages='18'),
    dict(book=FRANCO90, authors=[('P.', '', 'Johnson')], journal='Utilitas',
         volume='4', year=1992, pages='178-81'),
    dict(book=FRANCO90, authors=[('C.', '', 'Kukathas')],
         journal='Political Theory', volume='21', year=1993, pages='339-43'),
    dict(book=FRANCO90, authors=[('C.', '', 'Lawn')],
         title='Against the Illusion of Technique',
         journal='Radical Philosophy', volume='58', year=1991, pages='40-4'),
    dict(book=FRANCO90, authors=[('P.', '', 'Nelson')],
         journal='Journal of Politics', volume='53', year=1991,
         pages='1195-9'),
    dict(book=FRANCO90, authors=[('A.', '', "O'Hear")],
         title='A World of Meanings', journal='Salisbury Review',
         month='September', year=1991, pages='41', also=[GRANT]),
    dict(book=FRANCO90, authors=[('B.', 'C.', 'Parekh')],
         journal='Political Studies', volume='38', year=1990,
         pages='723-4'),
    dict(book=FRANCO90, authors=[('D.', 'H.', 'Rice')],
         journal='Perspectives on Political Science', volume='20',
         year=1991, pages='23'),
    dict(book=FRANCO90, authors=[('P.', '', 'Riley')],
         journal='American Political Science Review', volume='86',
         year=1992, pages='509-10'),
    dict(book=FRANCO90, authors=[('J.', '', 'Shubow')],
         journal='Common Review', volume='4', issue='2', year=2005,
         pages='32-7'),
    dict(book=FRANCO90, authors=[('J.', '', 'Waldron')],
         title='Politics Without Purpose?', journal=TLS, issue='4553',
         day='6-12', month='July', year=1990, pages='715-6'),
    # Franco 2004
    dict(book=FRANCO04, authors=[], journal='Economist', day='2',
         month='December', year=2004),
    dict(book=FRANCO04, authors=[('G.', '', 'Callahan')],
         journal='Independent Review', volume='10', year=2005,
         pages='295-9'),
    dict(book=FRANCO04, authors=[('T.', '', 'Congdon')], journal=TLS,
         day='8', month='April', year=2005, pages='3-4'),
    dict(book=FRANCO04, authors=[('N.', '', 'Malcolm')],
         title='Modern Philosopher of Tradition', journal='Daily Telegraph',
         day='29', month='August', year=2004),
    dict(book=FRANCO04, authors=[('T.', 'W.', 'Merrill')], journal='Society',
         volume='43', year=2005, pages='98-100'),
    dict(book=FRANCO04, authors=[('R.', '', 'Mullender')],
         journal='History of Political Thought', volume='26', year=2005,
         pages='724-6'),
    dict(book=FRANCO04, authors=[('V.', '', 'Nemoianu')],
         journal='Review of Metaphysics', volume='59', year=2005,
         pages='421-3'),
    # Gerencser
    dict(book=GERENCSER, authors=[('P.', '', 'Digeser')],
         journal='Political Theory', volume='29', year=2001, pages='896-8'),
    dict(book=GERENCSER, authors=[('P.', '', 'Franco')],
         journal='Journal of Politics', volume='63', year=2001,
         pages='984-7'),
    dict(book=GERENCSER, authors=[('H.', 'M.', 'Hopfl')],
         journal='History of Political Thought', volume='23', year=2002,
         pages='691-3'),
    dict(book=GERENCSER, authors=[('P.', '', 'Riley')],
         journal='Annals of the American Academy of Political and Social '
                 'Science',
         volume='576', year=2001, pages='133-4'),
    # Grant
    dict(book=GRANT, authors=[('J.', '', 'Casey')],
         title='Mankind in Conversation: The Philosophy of Michael Oakeshott '
               'and Its Misunderstandings',
         journal=TLS, day='29', month='March', year=1991, pages='3-4'),
    dict(book=GRANT, authors=[('C.', 'A. J.', 'Coady')],
         journal='Philosophical Quarterly', volume='45', year=1995,
         pages='273-5'),
    # Greenleaf
    dict(book=GREENLEAF, authors=[('B.', '', 'Crick')], journal='New Society',
         volume='8', year=1966, pages='622'),
    dict(book=GREENLEAF, authors=[('A.', '', 'Flew')], journal='Spectator',
         volume='218', year=1967, pages='108-9'),
    dict(book=GREENLEAF, authors=[('J.', '', 'Hamburger')],
         journal='American Political Science Review', volume='61',
         year=1967, pages='782-3'),
    dict(book=GREENLEAF, authors=[('F.', 'S.', 'McNeilly')],
         journal='Philosophical Books', volume='8', year=1967, pages='4-6'),
    dict(book=GREENLEAF, authors=[('T.', '', 'McPherson')],
         journal='Political Studies', volume='15', year=1967, pages='373'),
    dict(book=GREENLEAF, authors=[('J.', 'B.', 'Sanderson')],
         journal='Durham University Journal', volume='59', year=1966,
         pages='120-1'),
    # Isaacs
    dict(book=ISAACS, authors=[('A.', '', 'Botwinick')],
         journal='Political Theory', volume='36', year=2008, pages='479-85'),
    # King and Parekh
    dict(book=KING_PAREKH, authors=[], journal=TLS, day='13',
         month='February', year=1969, pages='150'),
    dict(book=KING_PAREKH, authors=[('G.', '', 'Barraclough')],
         journal='Spectator', volume='222', year=1969, pages='144-6'),
    dict(book=KING_PAREKH, authors=[('M.', '', 'Beloff')],
         journal='Cambridge Review', volume='90', year=1969, pages='239-40'),
    dict(book=KING_PAREKH, authors=[('C.', 'B.', 'Macpherson')],
         journal='Political Science Quarterly', volume='36', year=1971,
         pages='310-11'),
    dict(book=KING_PAREKH, authors=[('Ken', '', 'Reshaur')],
         journal='Canadian Journal of Political Science', volume='3',
         year=1970, pages='167-8',
         url='https://cambridge.org/core/journals/canadian-journal-of-'
             'political-science-revue-canadienne-de-science-politique/'
             'article/preston-king-and-b-c-parekh-eds-politics-and-'
             'experience-essays-presented-to-michael-oakeshott-cambridge-'
             'university-press-1968-pp-424/ED96D0D7BF7E1A38C169B740A6A0621A'),
    dict(book=KING_PAREKH, authors=[('J.', 'B.', 'Sanderson')],
         journal='Durham University Journal', volume='62', year=1969,
         pages='130-2'),
    dict(book=KING_PAREKH, authors=[('T.', 'L.', 'Thorsen')],
         journal='American Political Science Review', volume='63',
         year=1969, pages='934-5'),
    # Nardin
    dict(book=NARDIN, authors=[], journal='History and Theory', volume='41',
         year=2002, pages='412'),
    dict(book=NARDIN, authors=[('M.', '', 'Bacon')],
         journal='Political Studies Review', volume='1', year=2003),
    dict(book=NARDIN, authors=[('L.', 'H.', 'Brody')],
         journal='Library Journal', volume='127', year=2002, pages='148'),
    dict(book=NARDIN, authors=[('W.', 'J.', 'Coats')],
         journal='Journal of Politics', volume='65', year=2003,
         pages='584-5'),
    dict(book=NARDIN, authors=[('T.', '', 'Fuller')], journal='Ethics',
         volume='113', year=2003, pages='711-3'),
    dict(book=NARDIN, authors=[('S.', 'A.', 'Gerencser')],
         journal='Perspectives on Politics', volume='1', year=2003,
         pages='175-6'),
    dict(book=NARDIN, authors=[('C.', '', 'Kukathas')],
         journal='Notre Dame Philosophical Reviews', month='December',
         year=2002),
    dict(book=NARDIN, authors=[('P.', '', 'Madigan')],
         journal='Heythrop Journal', volume='47', year=2006, pages='140-1'),
    dict(book=NARDIN, authors=[('L.', '', "O'Sullivan")],
         journal='History of Political Thought', volume='24', year=2003,
         pages='339-41'),
    dict(book=NARDIN, authors=[('N.', '', "O'Sullivan")],
         journal='Collingwood and British Idealism Studies', volume='9',
         year=2003, pages='165-71'),
    dict(book=NARDIN, authors=[('J.', 'D.', 'Rayner')],
         journal='Canadian Journal of Political Science', volume='36',
         year=2003, pages='228-30'),
    dict(book=NARDIN, authors=[('D.', '', 'Richter')],
         journal='Philosophy in Review', volume='22', year=2002,
         pages='429-31'),
    dict(book=NARDIN, authors=[('S.', '', 'Turner')],
         title='The English Heidegger',
         journal='Philosophy of the Social Sciences', volume='35',
         year=2005, pages='353-68'),
    dict(book=NARDIN, authors=[('G.', '', 'Worthington')],
         journal='Review of Politics', volume='64', year=2002,
         pages='758-61'),
    # Norman
    dict(book=NORMAN, authors=[('A.', '', 'Cocks')],
         journal='Policy: A Journal of Public Policy and Ideas', volume='10',
         year=1994, pages='55-6'),
    # O'Sullivan
    dict(book=OSULLIVAN, authors=[('A.', '', 'Astrov')],
         journal='Contemporary Political Theory', volume='4', year=2005,
         pages='211-7', also=[PODOKSIK, TSENG]),
    dict(book=OSULLIVAN, authors=[('M.', '', 'Bentley')],
         journal='English Historical Review', volume='118', year=2003,
         pages='1345-6'),
    dict(book=OSULLIVAN, authors=[('M.', '', 'Garnett')],
         journal='Conservative History Journal', volume='1', issue='3',
         year=2004, pages='29-30', also=[PODOKSIK, TREGENZA, TSENG]),
    dict(book=OSULLIVAN, authors=[('N.', '', 'Johnson')],
         journal='History of Political Thought', volume='25', year=2004,
         pages='152-4'),
    dict(book=OSULLIVAN, authors=[('R.', '', 'Martin')],
         journal='History and Theory', volume='44', year=2005,
         pages='138-48'),
    dict(book=OSULLIVAN, authors=[('K.', '', 'Minogue')],
         title='No Blood or Dagger', journal=TLS, day='12',
         month='December', year=2003, pages='11'),
    # Perret
    dict(book=PERRET, authors=[], journal='Esprit', volume='5', year=2005,
         pages='232-3'),
    # Podoksik
    dict(book=PODOKSIK, authors=[('R.', '', 'Bourke')],
         journal='European Legacy', volume='10', year=2005, pages='252-3'),
    dict(book=PODOKSIK, authors=[('J.', '', 'Charvet')],
         journal='History of Political Thought', volume='25', year=2004,
         pages='729-30'),
    dict(book=PODOKSIK, authors=[('E.', '', 'Corey')], journal='Society',
         volume='42', year=2005, pages='83-6'),
    dict(book=PODOKSIK, authors=[('G.', '', 'Feaver')],
         title='Out of the Rough', journal=TLS, day='7', month='May',
         year=2004, pages='8-9', also=[TREGENZA, TSENG]),
    dict(book=PODOKSIK, authors=[('L.', '', 'Marsh')],
         journal='Political Studies Review', volume='2', year=2004,
         pages='337-8'),
    # Singh
    dict(book=SINGH, authors=[('W.', 'H.', 'Greenleaf')],
         journal='Political Studies', volume='16', year=1968, pages='456-7'),
    dict(book=SINGH, authors=[('J.', 'B.', 'Sanderson')],
         journal='Durham University Journal', volume='60', year=1967,
         pages='47-8'),
    # Tregenza
    dict(book=TREGENZA, authors=[('S.', 'A.', 'Gerencser')],
         journal='History of Political Thought', volume='26', year=2005,
         pages='147-8'),
    dict(book=TREGENZA, authors=[('M.', '', 'Payne')], journal='Network',
         volume='83', year=2003, pages='53'),
    # Tseng
    dict(book=TSENG, authors=[('E.', '', 'Neill')],
         journal='English Historical Review', volume='119', year=2004,
         pages='1010-2'),
    dict(book=TSENG, authors=[('I.', '', 'Tregenza')],
         journal='History of Political Thought', volume='24', year=2003,
         pages='706-8'),
    # Williams
    dict(book=WILLIAMS, authors=[('D.', '', 'Carr')],
         journal='Journal of Philosophy of Education', volume='42',
         year=2008, pages='345-7'),

    # ---- WEB ----
    # These three were first loaded with the short works
    # (_short_works_about.REVIEWS).
    dict(book=CAMBRIDGE_SCHOOL, authors=[("James", "", "Alexander")],
         title="Oakeshott and the Cambridge School", journal=CT,
         volume="8", issue="2+3", year=2020, pages="66-83",
         url=CT_PDF + "2020/04/review_alexander_ct_vol8_iss_2_3.pdf"),
    dict(book=PLOTICA, authors=[("P.", "", "Digeser")], journal=CT,
         volume="8", issue="10+11", year=2020, pages="83-87",
         url=CT_PDF + "2020/10/digeser_ct_vol8_iss10_11.pdf"),
    dict(book=ROME_AMERICA, authors=[("Kenneth", "B.", "McIntyre")],
         title="Oakeshott vs. America", journal="The American Conservative",
         year=2013, month="Jan./Feb.",
         url="https://www.theamericanconservative.com/oakeshott-vs-america-112/"),
    dict(book=ROME_AMERICA, authors=[("Elizabeth", "", "Corey")],
         title="Oakeshott and the American Founding",
         journal="Law & Liberty", day="21", month="October", year=2013,
         url="https://lawliberty.org/book-review/"
             "oakeshott-and-the-american-founding/"),
    dict(book=ROME_AMERICA, authors=[("Corey", "", "Abel")],
         title="Can Rationalism Make it in the Long Run?",
         journal="The University Bookman", day="8", month="December",
         year=2013,
         url="https://kirkcenter.org/reviews/"
             "can-rationalism-make-it-in-the-long-run/"),
    dict(book=ROME_AMERICA, authors=[("Corey", "", "Abel")],
         title="Oakeshott on Rome and America", journal="VoegelinView",
         day="22", month="September", year=2013,
         url="https://voegelinview.com/oakeshott-on-rome-and-america-review/"),
    dict(book=HUMAN_CONDITION, authors=[("Gene", "", "Callahan")],
         title="Getting to Know Oakeshott", journal="Modern Age",
         month="Summer", year=2024,
         url="https://modernagejournal.com/getting-to-know-oakeshott/243896/"),

    dict(book=COVELL, authors=[("Neil", "", "Duxbury")],
         journal="Cambridge Law Journal", volume="52", issue="1",
         month="March", year=1993, pages="155",
         doi="10.1017/S000819730001730X"),
    dict(book=DEVIGNE, authors=[("Steven", "B.", "Smith")],
         journal="American Political Science Review", volume="88",
         issue="4", month="December", year=1994, pages="971-972",
         doi="10.2307/2082721"),
    dict(book=DEVIGNE, authors=[("Kenneth", "", "Minogue")],
         title="True Blue Response to a Red Threat",
         journal="Times Higher Education Supplement", day="24",
         month="March", year=1995,
         url="https://www.timeshighereducation.com/books/"
             "true-blue-response-to-a-red-threat/161859.article"),
    dict(book=DEVIGNE, authors=[("Gregory", "R.", "Johnson")],
         journal="Review of Metaphysics", volume="50", issue="4", year=1997,
         pages="876-878", url="https://philpapers.org/rec/JOHRC-2",
         exact=True),  # not "G. Johnson" of Poetry Review (1960)
    dict(book=KINZEL, authors=[("Daniel", "", "Bigalke")],
         journal="Buchtips.net", day="14", month="December", year=2007,
         url="https://www.buchtips.net/"
             "rez2874-michael-oakeshott-philosoph-der-politik.htm"),
    dict(book=SULLIVAN, authors=[("Ian", "", "Tregenza")],
         title="The Philosophy and Poetry of Practice",
         journal="Review of Politics", volume="71", issue="2", year=2009,
         pages="347-351", doi="10.1017/S0034670509000473"),
    dict(book=ABEL, authors=[("Elizabeth", "", "Corey")],
         title="Accepting the World's Imperfections: Michael Oakeshott's "
               "Conservatism",
         journal="VoegelinView", day="4", month="October", year=2011,
         url="https://voegelinview.com/meanings-of-oakeshotts-conservatism-"
             "review/"),
    dict(book=BOTWINICK, authors=[("Paul", "", "Franco")],
         title="Antifoundationalist in Spite of Himself?",
         journal="Review of Politics", volume="74", issue="1", year=2012,
         pages="153-155", doi="10.1017/S0034670512000149"),
    dict(book=CAMBRIDGE_COMPANION, authors=[("Martin", "", "Beckstein")],
         journal="Political Studies Review", volume="12", issue="2",
         year=2014, pages="262-263", url="https://philpapers.org/rec/BECROT-4"),
    dict(book=CAMBRIDGE_COMPANION, authors=[("Luke", "Philip", "Plotica")],
         journal="Law, Culture and the Humanities", volume="9", issue="3",
         year=2013, pages="494-496", doi="10.1177/1743872113494301b",
         also=[COMPANION]),
    dict(book=COMPANION, authors=[("John", "", "Kekes")],
         journal="Notre Dame Philosophical Reviews", volume="2013.02.03",
         year=2013,
         url="https://ndpr.nd.edu/reviews/a-companion-to-michael-oakeshott/"),
    dict(book=COMPANION, authors=[("Martin", "", "Beckstein")],
         journal="Political Studies Review", volume="12", issue="1",
         year=2014, pages="96-97", url="https://philpapers.org/rec/BECROA"),
    dict(book=COMPANION, authors=[("Terry", "", "Nardin")],
         journal="Philosophy of the Social Sciences", volume="44",
         issue="6", year=2014, pages="839-843",
         url="https://www.academia.edu/3608600/"
             "Review_of_Franco_and_Marsh_A_Companion_to_Michael_Oakeshott"),
    dict(book=COMPANION, authors=[("Suvi", "", "Soininen")],
         title="Conversations with Michael Oakeshott – An Interlude to "
               "Oakeshott Scholarship",
         journal="Redescriptions", volume="16", year=2013, pages="172-187",
         url="https://jyx.jyu.fi/dspace/handle/123456789/42047"),

    dict(book=COLD_WAR, authors=[("Steven", "A.", "Gerencser")],
         journal="Perspectives on Politics", volume="14", issue="1",
         month="March", year=2016, pages="219-220",
         doi="10.1017/S1537592715003680"),
    dict(book=PLOTICA, authors=[], journal="Choice", volume="53",
         issue="2", month="October", year=2015,
         doi="10.5860/choice.191957"),
    dict(book=PLOTICA, authors=[("Luke", "", "O'Sullivan")],
         journal="Contemporary Political Theory", volume="15", issue="3",
         year=2016, pages="e37-e40", doi="10.1057/cpt.2015.46"),
    dict(book=PLOTICA, authors=[("Elizabeth", "", "Corey")],
         journal="Review of Politics", volume="79", issue="1", year=2017,
         pages="151-154", doi="10.1017/S003467051600084X"),
    dict(book=EDUCATION_CONVERSATION, authors=[("Eric", "", "Wearne")],
         title="Review of Education and Conversation: Exploring "
               "Oakeshott's Legacy",
         journal="Education Review", volume="24", day="14", month="June",
         year=2017, doi="10.14507/er.v24.2182"),
    dict(book=ORSI, authors=[("J.", "E.", "Spence")],
         journal="International Affairs", volume="95", issue="1",
         month="January", year=2019, pages="208-209",
         doi="10.1093/ia/iiy273"),
    dict(book=PLACE, authors=[("W.", "J.", "Morgan")],
         title="The Place of Michael Oakeshott in Contemporary Western and "
               "Non-Western Thought",
         journal="Collingwood and British Idealism Studies", volume="23",
         issue="2", year=2017, pages="259-269",
         url="https://orca.cardiff.ac.uk/143905"),
    dict(book=TRADITION, authors=[("Thomas", "", "Cloud")],
         title="Review of Tradition v. Rationalism: Voegelin, Oakeshott, "
               "Hayek, and Others",
         journal="VoegelinView", day="22", month="June", year=2019,
         url="https://voegelinview.com/review-of-tradition-v-rationalism-"
             "voegelin-oakeshott-hayek-and-others/"),
    dict(book=TRADITION, authors=[("C.", "P.", "Goodman")],
         journal="Tradition and Discovery",
         volume="46", issue="3", year=2020, pages="31-37",
         doi="10.5840/traddisc202046325"),
    dict(book=MCILWAIN, authors=[("Wendell", "John", "Coats")],
         journal="Review of Politics", volume="82", issue="2", year=2020,
         pages="363-366", doi="10.1017/S0034670520000066"),
    dict(book=COATS19, authors=[("Luke", "Philip", "Plotica")],
         journal="Review of Politics", volume="82", issue="2", year=2020,
         pages="361-363", doi="10.1017/S003467052000008X"),
    dict(book=KOS22, authors=[("Elizabeth", "", "Corey")],
         journal="History of European Ideas", volume="50", issue="6",
         year=2024, pages="1152-1153",
         doi="10.1080/01916599.2024.2326880"),
    dict(book=HUMAN_CONDITION, authors=[("Elizabeth", "", "Corey")],
         title="Michael Oakeshott's Life of Reflection",
         journal="Law & Liberty", day="25", month="June", year=2024,
         url="https://lawliberty.org/classic/"
             "michael-oakeshotts-life-of-reflection/"),
]
