"""Data for load_reviews_of_books_by_oakeshott: reviews of Oakeshott's
books, stored as "Book Reviews of Books by Oakeshott" (RVOB).

Source: section 2.1 ("Reviews") of the Michael Oakeshott Association
bibliography, michaeloakeshottassociation.org/bibliography/, parsed on
2026-11-07 and checked by hand. MOA has not been updated much since
about 2006, so later books (2007-2014) have no reviews here.

Each entry's "book" is the Books by Oakeshott entry it reviews (by its
title in the database). A review MOA lists under several books is one
entry here; "also" names the other books it reviews (the database links
a review to one book, so "also" is a record only).

Left out:
- the three reviews of Oakeshott's 1946 edition of Hobbes's Leviathan,
  which is not a Books by Oakeshott entry (TLS 11 January 1947; C. Read,
  William & Mary Quarterly 1948; K. Schilling, Zeitschrift fur
  philosophische Forschung 1947);
- the Magill Book Reviews notice of The Voice of Liberal Learning (MOA
  gives no date);
- MOA's anonymous Publishers Weekly notice of The Voice of Liberal
  Learning, which has the same volume, date and page as G. Stuttaford's;
- K. McIntyre, 'Publication as Polemic' (2005), already a Short Works
  About Oakeshott entry linked to What is History?.

Corrections to MOA: journal typos 'Specator' and 'Journal of the History
of Philsophy'; 'Annals of the American Academy of Social and Political
Science' is the 'Annals of the American Academy of Political and Social
Science'; J.G. Kerwin's 'Commonwealth' 30 (1939) is Commonweal. G. Graham's Philosophical Quarterly 26 is 1976 (MOA: 1967, nine
years before the book). D. McCabe's Commonweal is vol. 121, no. 8 (MOA
gives '21' and '21(8)'). Collingwood's review is untitled; MOA's title
for it, 'Oakeshott and the Modes of Experience', is that of its reprint
in The Cambridge Mind (1970). Benjamin DeMott is MOA's 'Mott, B. de'.

Kept as MOA gives them, though doubtful: M.Q. Sibley, American
Political Science Review 33 (1943) (vol. 33 is 1939); J.L. Auspitz,
National Review pp. '42, 44-88'.

A year range such as '1962-3' is stored as its first year.

One review is not from MOA: J. L. Auspitz, 'A New Look at Michael
Oakeshott' (Claremont Review of Books, 2014), with its URL.
"""

EIM = "Experience and Its Modes"
SPD = "The Social and Political Doctrines of Contemporary Europe"
DERBY = "A New Guide to the Derby: How to Pick the Winner"
PE = "Political Education: An Inaugural Lecture"
VOICE = "The Voice of Poetry in the Conversation of Mankind: An Essay"
RIP = "Rationalism in Politics and Other Essays"
HCA = "Hobbes on Civil Association"
OHC = "On Human Conduct"
OH = "On History and Other Essays"
VLL = "The Voice of Liberal Learning: Michael Oakeshott on Education"
RIP91 = ("Rationalism in Politics and Other Essays: New and Expanded "
         "Edition")
MPME = "Morality and Politics in Modern Europe: The Harvard Lectures"
RPML = "Religion, Politics and the Moral Life"
PFPS = "The Politics of Faith and the Politics of Scepticism"
WIH = "What is History? and Other Essays"
LHPT = "Lectures in the History of Political Thought"

OAKESHOTT = ("Michael", "", "Oakeshott")

REVIEWS = [
    dict(book=EIM, authors=[], journal='Guardian', day='13', month='April', year=1934),
    dict(book=EIM, authors=[], journal='London Quarterly and Holborn Review', volume='159', year=1934, pages='279-80'),
    dict(book=EIM, authors=[], journal='Nottingham Guardian', day='17', month='January', year=1934),
    dict(book=EIM, authors=[], journal='Psychological Medicine', volume='9', year=1979, pages='602-3'),
    dict(book=EIM, authors=[], journal='Spectator', day='23', month='December', year=1933),
    dict(book=EIM, authors=[('G.', 'O.', 'Wood')], journal='Times Literary Supplement', day='26', month='April', year=1934, pages='294'),
    dict(book=EIM, authors=[('J.', 'R.', 'Balow')], journal='Australian Journal of Politics and History', volume='25', year=1979, pages='289-90'),
    dict(book=EIM, authors=[('W.', 'G.', 'de Burgh')], journal='Hibbert Journal', volume='33', year=1934, pages='144-50'),
    dict(book=EIM, authors=[('R.', 'G.', 'Collingwood')], journal='Cambridge Review', volume='55', year=1933, pages='249-50'),
    dict(book=EIM, authors=[('I.', '', 'Crowther')], journal='Salisbury Review', volume='5', month='April', year=1987, pages='71'),
    dict(book=EIM, authors=[('R.', '', 'Franks')], journal='Congregational Quarterly', year=1935),
    dict(book=EIM, authors=[('J.', 'W.', 'Hunkin')], journal='Church of England Newspaper', day='2', month='March', year=1934),
    dict(book=EIM, authors=[('T.', 'E.', 'Jessop')], journal='Philosophy', volume='9', year=1934, pages='357-9'),
    dict(book=EIM, authors=[('T.', 'E.', 'Jessop')], journal='Jahrbuch für die idealistische Philosophie', year=1934),
    dict(book=EIM, authors=[('T.', 'M.', 'Knox')], journal='Oxford Magazine', volume='52', year=1934, pages='551-2'),
    dict(book=EIM, authors=[('S.', 'P.', 'Lamprecht')], journal='Journal of Philosophy', volume='31', year=1934, pages='163-4'),
    dict(book=EIM, authors=[('J.', '', 'Oman')], journal='Journal of Theological Studies', volume='35', year=1934, pages='314-6'),
    dict(book=EIM, authors=[('L.', 'R.', 'Perry')], journal='British Journal of Educational Studies', volume='16', year=1968, pages='96-7'),
    dict(book=EIM, authors=[('L.', 'S.', 'Stebbing')], journal='Mind', volume='43', year=1934, pages='403-5'),
    dict(book=EIM, authors=[('A.', '', 'Sullivan')], journal='New Republic', volume='195', day='22', month='December', year=1986, pages='28-34, 36'),
    # Not in MOA (found 2026-11-07). A review essay on the Cambridge
    # paperback of EIM that also discusses Callahan, Oakeshott on Rome and
    # America; the Cambridge and Franco/Marsh Companions; Coats and
    # Cheung, The Poetic Character of Human Activity; Henkel and Lembcke,
    # Praxis und Politik; O'Sullivan, Oakeshott on History; and Tregenza,
    # Michael Oakeshott on Hobbes.
    dict(book=EIM, authors=[('Josiah', 'Lee', 'Auspitz')], title='A New Look at Michael Oakeshott', journal='Claremont Review of Books', volume='14', issue='2', month='Spring', year=2014, url='https://claremontreviewofbooks.com/a-new-look-at-michael-oakeshott/'),
    dict(book=SPD, authors=[], journal='Times Literary Supplement', day='1', month='April', year=1939, pages='182'),
    dict(book=SPD, authors=[('W.', 'G.', 'de Burgh')], journal='Mind', volume='49', year=1940, pages='100-2'),
    dict(book=SPD, authors=[('S.', 'J.', 'G.')], journal='Dublin Review', volume='205', year=1939, pages='195-7'),
    dict(book=SPD, authors=[('J.', 'L.', 'Hammond')], journal='Manchester Guardian', day='25', month='April', year=1939, pages='7'),
    dict(book=SPD, authors=[('J.', 'G.', 'Kerwin')], journal='Commonweal', volume='30', year=1939, pages='191'),
    dict(book=SPD, authors=[('J.', 'G.', 'Kerwin')], journal='Journal of Political Economy', volume='51', year=1943, pages='278-9'),
    dict(book=SPD, authors=[('H.', '', 'Kohn')], journal='Nation', volume='149', year=1939, pages='299-300'),
    dict(book=SPD, authors=[('H.', 'D.', 'Lasswell')], journal='Annals of the American Academy of Political and Social Science', volume='229', month='September', year=1943, pages='193'),
    dict(book=SPD, authors=[('E.', 'J.', 'Passant')], journal='Philosophy', volume='14', year=1939, pages='373-4'),
    dict(book=SPD, authors=[('J.', 'S.', 'Roucek')], journal='American Sociological Review', volume='4', year=1939, pages='737-8'),
    dict(book=SPD, authors=[('J.', 'S.', 'Roucek')], journal='Annals of the American Academy of Political and Social Science', volume='204', month='July', year=1939, pages='187-8'),
    dict(book=SPD, authors=[('G.', '', 'de Ruggiero')], journal='Politica', volume='4', year=1939, pages='284-5'),
    dict(book=SPD, authors=[('W.', '', 'Sandelius')], journal='American Political Science Review', volume='33', year=1939, pages='932-3'),
    dict(book=SPD, authors=[('M.', 'Q.', 'Sibley')], journal='American Political Science Review', volume='33', year=1943, pages='183'),
    dict(book=DERBY, authors=[], journal='Times Literary Supplement', day='24', month='May', year=1947, pages='259'),
    dict(book=PE, authors=[], journal='Times Literary Supplement', day='1', month='June', year=1951, pages='341'),
    dict(book=PE, authors=[('R.', 'H. S.', 'Crossman')], journal='New Statesman and Nation', volume='42', year=1951, pages='60-1'),
    dict(book=PE, authors=[('P.', '', 'Laslett')], journal='Cambridge Journal', volume='5', year=1951, pages='765-6, 768'),
    dict(book=PE, authors=[('W.', 'J. M.', 'Mackenzie')], title='Political Theory and Political Education', journal='Universities Quarterly', volume='9', year=1955, pages='351-63'),
    dict(book=PE, authors=[('J.', 'C.', 'Rees')], title='Professor Oakeshott on Political Education', journal='Mind', volume='62', year=1953, pages='68-74'),
    dict(book=VOICE, authors=[], journal='Times Literary Supplement', day='11', month='December', year=1959, pages='725'),
    dict(book=VOICE, authors=[('L.', '', 'Clark')], journal='Time and Tide', volume='41', year=1960, pages='62'),
    dict(book=VOICE, authors=[('A.', 'R.', 'Fell')], journal='Queen’s Quarterly', volume='67', year=1960, pages='698-9'),
    dict(book=VOICE, authors=[('G.', '', 'Johnson')], journal='Poetry Review', volume='51', year=1960, pages='43'),
    dict(book=VOICE, authors=[('R.', '', 'Lawrence')], journal='English', volume='13', year=1960, pages='29-31'),
    dict(book=VOICE, authors=[('C.', '', 'Madge')], journal='Modern Language Review', volume='55', year=1960, pages='622-3'),
    dict(book=VOICE, authors=[('V.', '', 'Minogue')], title='Philosopher Go Home! Poetry and Professor Oakeshott', journal='Twentieth Century', volume='167', year=1960, pages='226-34'),
    dict(book=VOICE, authors=[('B.', 'E.', 'Owen')], journal='Contemporary Review', volume='198', year=1960, pages='519-20'),
    dict(book=VOICE, authors=[('L.', 'R.', 'Perry')], journal='New Era in Home and School', volume='41', year=1960, pages='62-4'),
    dict(book=VOICE, authors=[('R.', '', 'Wollheim')], journal='Spectator', volume='203', year=1959, pages='881'),
    dict(book=RIP, authors=[], journal='Christian Century', volume='79', year=1962, pages='1328'),
    dict(book=RIP, authors=[], journal='Hibbert Journal', volume='61', year=1962, pages='100, 102'),
    dict(book=RIP, authors=[], journal='International Relations', volume='2', month='October', year=1962, pages='405'),
    dict(book=RIP, authors=[], journal='Times', day='13', month='September', year=1962, pages='11'),
    dict(book=RIP, authors=[], journal='Times Literary Supplement', day='28', month='September', year=1962, pages='753-4'),
    dict(book=RIP, authors=[('H.', '', 'Bernard-Maitre')], journal='Erasmus', volume='17', year=1965, pages='406-7'),
    dict(book=RIP, authors=[('W.', '', 'Berns')], journal='American Political Science Review', volume='57', year=1963, pages='670-1'),
    dict(book=RIP, authors=[('J.', '', 'Bowle')], journal='Daily Telegraph', day='2', month='November', year=1962),
    dict(book=RIP, authors=[('G.', 'E. G.', 'Catlin')], journal='Western Political Quarterly', volume='16', year=1963, pages='259-61'),
    dict(book=RIP, authors=[('G.', 'C.', 'Duncan')], journal='Australasian Journal of Philosophy', volume='41', year=1963, pages='112-20'),
    dict(book=RIP, authors=[('D.', '', 'Emmet')], journal='Philosophical Quarterly', volume='13', year=1963, pages='283-4'),
    dict(book=RIP, authors=[('H.', '', 'Fairlie')], journal='Spectator', volume='209', year=1962, pages='644-5'),
    dict(book=RIP, authors=[('C.', '', 'Falck')], title='Romanticism in Politics', journal='New Left Review', volume='18', year=1963, pages='60-71'),
    dict(book=RIP, authors=[('J.', 'H.', 'Franklin')], journal='Journal of Philosophy', volume='60', year=1963, pages='811-20'),
    dict(book=RIP, authors=[('O.', '', 'Gass')], title='Politics of Dead Center', journal='New Republic', volume='2516', issue='6', day='9', month='February', year=1963, pages='21-6'),
    dict(book=RIP, authors=[('C.', 'J.', 'Hughes')], journal='Philosophical Books', volume='4', issue='1', year=1963, pages='25-6'),
    dict(book=RIP, authors=[('H.', 'V.', 'Jaffa')], journal='National Review', day='22', month='October', year=1963, pages='360-2'),
    dict(book=RIP, authors=[('D.', '', 'Kettler')], title='The Cheerful Discourses of Michael Oakeshott', journal='World Politics', volume='16', year=1964, pages='483-9'),
    dict(book=RIP, authors=[('R.', '', 'Kirk')], journal='Annals of the American Academy of Political and Social Science', volume='347', month='May', year=1963, pages='181'),
    dict(book=RIP, authors=[('A.', '', 'Kolnai')], journal='Philosophy', volume='40', year=1965, pages='68-71'),
    dict(book=RIP, authors=[('H.', '', 'Kuhn')], journal='Zeitschrift für Politik', volume='10', year=1963, pages='194-7'),
    dict(book=RIP, authors=[('P.', '', 'Laslett')], journal='Manchester Guardian', day='14', month='September', year=1962, pages='4'),
    dict(book=RIP, authors=[('G.', '', 'Lavau')], journal='Revue Française de Science Politique', volume='14', year=1964, pages='124-6'),
    dict(book=RIP, authors=[('G.', '', 'Lichtheim')], title='A Settled Habit of Behaviour', journal='Commentary', volume='35', year=1963, pages='168-72'),
    dict(book=RIP, authors=[('J.', 'D.', 'Mabbott')], journal='Mind', volume='72', year=1963, pages='609-11'),
    dict(book=RIP, authors=[('W.', 'J. M.', 'Mackenzie')], journal='Universities Quarterly', volume='17', year=1962, pages='81-3'),
    dict(book=RIP, authors=[('D.', '', 'Marquand')], journal='New Statesman and Nation', volume='64', year=1962, pages='574'),
    dict(book=RIP, authors=[('B.', '', 'Miller')], journal='Listener', volume='68', year=1962, pages='424-5'),
    dict(book=RIP, authors=[('B.', '', 'DeMott')], journal='Harper’s Magazine', month='March', year=1963, pages='106, 108, 110'),
    dict(book=RIP, authors=[('P.', 'H.', 'Partridge')], title='The Study of Politics', journal='Australian Journal of Politics and History', volume='9', year=1963, pages='109-13'),
    dict(book=RIP, authors=[('J.', '', 'Plamenatz')], journal='British Journal of Sociology', volume='14', year=1963, pages='284-6'),
    dict(book=RIP, authors=[('D.', 'D.', 'Raphael')], journal='Political Studies', volume='12', year=1964, pages='202-15'),
    dict(book=RIP, authors=[('P.', '', 'Schwartz')], journal='Clare Market Review', volume='57', issue='2', month='Winter', year=1962, pages='60-3'),
    dict(book=RIP, authors=[('V.', '', 'Weiss')], journal='Philosophisches Jahrbuch', volume='85', year=1978, pages='167'),
    dict(book=RIP, authors=[('F.', 'G.', 'Wilson')], title='Oakeshott and Conservatism', journal='Universities Bookman', volume='4', month='Autumn', year=1963, pages='19-23'),
    dict(book=HCA, authors=[('L.', 'H.', 'C.')], journal='Heythrop Journal', volume='23', year=1982, pages='105'),
    dict(book=HCA, authors=[('J.', '', 'Lively')], journal='Times Higher Education Supplement', day='13', month='February', year=1976, pages='20'),
    dict(book=HCA, authors=[('K.', 'R.', 'Minogue')], journal='Political Studies', volume='24', year=1976, pages='212-3'),
    dict(book=HCA, authors=[('D.', 'E. B.', 'Pollard')], journal='Philosophical Studies (Dublin)', volume='24', year=1976, pages='314-5'),
    dict(book=HCA, authors=[('A.', '', 'Seller')], journal='Philosophical Books', volume='17', year=1976, pages='54-7', also=[OHC]),
    dict(book=HCA, authors=[('T.', 'A.', 'Spragens')], journal='American Political Science Review', volume='72', year=1978, pages='652-3'),
    dict(book=HCA, authors=[('L.', 'J.', 'Thro')], journal='Modern Schoolman', volume='56', year=1977, pages='289-92'),
    dict(book=HCA, authors=[('C.', '', 'Walton')], journal='Journal of the History of Philosophy', volume='14', year=1976, pages='499'),
    dict(book=OHC, authors=[('F.', 'J.', 'Abbate')], journal='Metaphilosophy', volume='9', year=1978, pages='175-80'),
    dict(book=OHC, authors=[('J.', 'E. J.', 'Altham')], journal='Cambridge Review', volume='97', day='24', month='October', year=1975, pages='23-5'),
    dict(book=OHC, authors=[], journal='British Book News', month='July', year=1975),
    dict(book=OHC, authors=[], journal='Economist', volume='256', day='26', month='July', year=1975, pages='109, 111'),
    dict(book=OHC, authors=[], title='Booknotes', journal='Philosophy', volume='50', year=1975, pages='373-4'),
    dict(book=OHC, authors=[('G.', '', 'Ardley')], journal='Philosophical Studies (Dublin)', volume='27', year=1980, pages='415-7'),
    dict(book=OHC, authors=[('J.', 'L.', 'Auspitz')], journal='Commentary', volume='61', month='May', year=1976, pages='89-92, 94'),
    dict(book=OHC, authors=[('B.', 'R.', 'Barber')], title='Conserving Politics: Michael Oakeshott and Political Theory', journal='Government and Opposition', volume='10', year=1976, pages='446-63'),
    dict(book=OHC, authors=[('J.', 'A.', 'Bradley')], journal='Heythrop Journal', volume='18', year=1977, pages='202-4'),
    dict(book=OHC, authors=[('S.', '', 'Chauvier')], journal='Revue de Métaphysique et de Morale', issue='2', year=1998, pages='314-6'),
    dict(book=OHC, authors=[('B.', '', 'Crick')], journal='Observer', day='20', month='April', year=1975, pages='30'),
    dict(book=OHC, authors=[('H.', '', 'Davis')], journal='New Behaviour', day='22', month='May', year=1975, pages='231'),
    dict(book=OHC, authors=[('G.', 'R.', 'Dunstan')], journal='Law Quarterly Review', volume='92', year=1976, pages='122-6'),
    dict(book=OHC, authors=[('T.', '', 'Fuller')], journal='Leviathan', day='17', month='October', year=1976, pages='6-8'),
    dict(book=OHC, authors=[('T.', '', 'Fuller')], journal='Journal of Politics', volume='38', year=1976, pages='184-6'),
    dict(book=OHC, authors=[('G.', '', 'Gale')], journal='Spectator', volume='234', year=1975, pages='540'),
    dict(book=OHC, authors=[('G.', '', 'Graham')], journal='Philosophical Quarterly', volume='26', year=1976, pages='201-3'),
    dict(book=OHC, authors=[('W.', '', 'Hennis')], journal='Frankfurter allgemeine Zeitung', day='18', month='March', year=1976),
    dict(book=OHC, authors=[('R.', 'L.', 'Hunt')], journal='Annals of the American Academy of Political and Social Science', volume='430', year=1977, pages='181-2'),
    dict(book=OHC, authors=[('D.', 'A.', 'Lloyd Thomas')], journal='Mind', volume='86', year=1977, pages='453-6'),
    dict(book=OHC, authors=[('D.', '', 'Lopp')], journal='Philosophical Review', volume='86', year=1977, pages='235-8'),
    dict(book=OHC, authors=[('D.', 'G.', 'Macrae')], journal='Sunday Times', day='6', month='April', year=1975, pages='38'),
    dict(book=OHC, authors=[('M.', 'E.', 'Marty')], journal='Christian Century', volume='108', day='10', month='July', year=1991, pages='676'),
    dict(book=OHC, authors=[('S.', '', 'Miller')], journal='Partisan Review', volume='44', year=1977, pages='304-9'),
    dict(book=OHC, authors=[('K.', 'R.', 'Minogue')], title='Oakeshott and the Idea of Freedom', journal='Quadrant', volume='19', month='October', year=1975, pages='77-83'),
    dict(book=OHC, authors=[('F.', '', 'Mount')], title='Oakeshott’s Distinction', journal='National Review', volume='27', year=1975, pages='1301-2, 1304-5'),
    dict(book=OHC, authors=[('G.', '', 'Parry')], journal='Bibliographie de la Philosophie', volume='23', year=1976, pages='143'),
    dict(book=OHC, authors=[('Z.', '', 'Pelczynski')], journal='Times Higher Education Supplement', day='23', month='May', year=1975, pages='25'),
    dict(book=OHC, authors=[('D.', 'D.', 'Raphael')], journal='Political Quarterly', volume='46', year=1975, pages='450, 452, 454'),
    dict(book=OHC, authors=[('R.', '', 'Rorty')], journal='Social Theory and Practice', volume='4', year=1976, pages='107-15'),
    dict(book=OHC, authors=[('L.', '', 'Rubinoff')], title='On Theorizing Human Conduct', journal='Canadian Journal of Political and Social Theory', volume='3', issue='2', year=1979, pages='5-30'),
    dict(book=OHC, authors=[('A.', '', 'Ryan')], journal='Listener', volume='93', year=1975, pages='517-8'),
    dict(book=OHC, authors=[('J.', '', 'Shklar')], title='Purposes and Procedures', journal='Times Literary Supplement', day='12', month='September', year=1975, pages='1018'),
    dict(book=OHC, authors=[('W.', '', 'Vossenkuhl')], journal='Neue Bücher Zeitung', day='27', month='December', year=1976, pages='12'),
    dict(book=OHC, authors=[('W.', '', 'Vossenkuhl')], title='Die Lebensform des Menschen', journal='Zeitschrift für philosophische Forschung', volume='31', year=1977, pages='138-46'),
    dict(book=OHC, authors=[('G.', 'J.', 'Warnock')], title='The Minefields of Moral Philosophy', journal='Encounter', volume='46', month='April', year=1976, pages='84-7'),
    dict(book=OHC, authors=[('M.', '', 'Warnock')], journal='New Society', volume='32', day='1', month='May', year=1975, pages='288'),
    dict(book=OH, authors=[], journal='Choice', month='July', year=1983, pages='1642'),
    dict(book=OH, authors=[], journal='Critical Philosophy', volume='12', year=1983, pages='116'),
    dict(book=OH, authors=[], journal='Osgoode Hall Law Journal', volume='22', month='Winter', year=1984, pages='794'),
    dict(book=OH, authors=[('J.', 'L.', 'Auspitz')], journal='National Review', volume='36', day='10', month='February', year=1984, pages='42, 44-88'),
    dict(book=OH, authors=[('D.', 'W.', 'Bebbington')], journal='British Book News', month='August', year=1983, pages='522'),
    dict(book=OH, authors=[('R.', 'N.', 'Berard')], journal='History Teacher', volume='18', year=1985, pages='449-51'),
    dict(book=OH, authors=[('R.', 'N.', 'Berard')], journal='International History Review', volume='6', year=1984, pages='301-3'),
    dict(book=OH, authors=[('D.', '', 'Boucher')], journal='History of Political Thought', volume='5', year=1984, pages='163-7'),
    dict(book=OH, authors=[('J.', '', 'Bradley')], journal='Heythrop Journal', volume='27', year=1986, pages='360-3'),
    dict(book=OH, authors=[('E.', '', 'Christianson')], journal='Spectator', volume='250', day='9', month='April', year=1983, pages='22-3'),
    dict(book=OH, authors=[('W.', 'H.', 'Dray')], journal='Ethics', volume='96', year=1985, pages='197-8'),
    dict(book=OH, authors=[('J.', '', 'Dunn')], journal='History', volume='70', year=1985, pages='64'),
    dict(book=OH, authors=[('R.', '', 'Eccleshall')], journal='Political Studies', volume='32', year=1984, pages='167'),
    dict(book=OH, authors=[('A.', '', 'Esler')], journal='Social Science Journal', volume='22', year=1985, pages='135-6'),
    dict(book=OH, authors=[('D.', 'M.', 'Fahey')], journal='Clio', volume='14', year=1984, pages='89-91'),
    dict(book=OH, authors=[('R.', 'A. D.', 'Grant')], journal='Salisbury Review', volume='3', month='October', year=1984, pages='46-8'),
    dict(book=OH, authors=[('J.', '', 'Gray')], journal='Political Theory', volume='12', year=1984, pages='449-53'),
    dict(book=OH, authors=[('G.', '', 'Leff')], journal='English Historical Review', volume='100', year=1985, pages='953-4'),
    dict(book=OH, authors=[('K.', 'R.', 'Minogue')], journal='American Spectator', volume='16', month='September', year=1983, pages='36-8'),
    dict(book=OH, authors=[('P.', '', 'Munz')], journal='European History Quarterly', volume='14', year=1984, pages='489-92'),
    dict(book=OH, authors=[('H.', '', 'Palmer')], journal='Philosophical Books', volume='26', year=1985, pages='117-20'),
    dict(book=OH, authors=[('J.', 'G. A.', 'Pocock')], journal='Times Literary Supplement', day='21', month='October', year=1983, pages='1155'),
    dict(book=OH, authors=[('J.', '', 'Sanderson')], journal='Durham University Journal', volume='45', year=1983, pages='315-17'),
    dict(book=OH, authors=[('S.', 'B.', 'Smith')], journal='Review of Politics', volume='47', year=1985, pages='150-4'),
    dict(book=OH, authors=[('W.', 'A.', 'Speck')], journal='Modern Language Review', volume='79', year=1984, pages='384-5'),
    dict(book=OH, authors=[('B.', '', 'Verschaffel')], journal='Tijdschrift voor Filosofie', volume='47', year=1985, pages='534-5'),
    dict(book=OH, authors=[('W.', 'H.', 'Walsh')], journal='Times Higher Education Supplement', day='15', month='April', year=1983, pages='16'),
    dict(book=OH, authors=[('D.', '', 'Weigall')], journal='Ideas and Production', year=1984, pages='93-5'),
    dict(book=VLL, authors=[], journal='Economist', volume='311', month='22-28 April', year=1989, pages='120, 125'),
    dict(book=VLL, authors=[], journal='Kenton, OH Times', day='16', month='February', year=1989),
    dict(book=VLL, authors=[], journal='Methodist Recorder', day='7', month='September', year=1989),
    dict(book=VLL, authors=[('C.', '', 'Bailey')], journal='Cambridge Journal of Education', volume='20', year=1990, pages='83-4'),
    dict(book=VLL, authors=[('D.', '', 'Bromwich')], journal='New Republic', volume='201', day='3', month='July', year=1989, pages='33-6'),
    dict(book=VLL, authors=[('R.', 'F.', 'Dearden')], journal='Journal of Educational Administration and History', volume='2', year=1990),
    dict(book=VLL, authors=[('G.', '', 'Feaver')], journal='Canadian Journal of Political Science', volume='24', year=1991, pages='418-21'),
    dict(book=VLL, authors=[('A.', '', 'Flew')], journal='British Journal of Educational Studies', volume='38', year=1990, pages='386-8'),
    dict(book=VLL, authors=[('I.', '', 'Gilmour')], journal='London Review of Books', volume='12', day='12', month='July', year=1990, pages='8-9'),
    dict(book=VLL, authors=[('W.', 'H.', 'Greenleaf')], journal='Times Higher Education Supplement', day='6', month='July', year=1990, pages='18'),
    dict(book=VLL, authors=[('T.', '', 'Hall')], journal='Review of Metaphysics', volume='43', year=1989, pages='159-61'),
    dict(book=VLL, authors=[('W.', 'E.', 'Hall')], journal='Birmingham Post', day='25', month='May', year=1989),
    dict(book=VLL, authors=[('P.', '', 'Johnson')], journal='Utilitas', volume='4', year=1992, pages='178-81'),
    dict(book=VLL, authors=[('B.', 'A.', 'Kimball')], title='Professions of Language and Reason', journal='American Journal of Education', volume='98', year=1990, pages='251-69'),
    dict(book=VLL, authors=[('C.', '', 'Moore')], journal='Spectator', volume='262', day='17', month='June', year=1989, pages='27-8'),
    dict(book=VLL, authors=[('F.', '', 'Mount')], journal='Sunday Telegraph', day='23', month='April', year=1989),
    dict(book=VLL, authors=[('D.', 'G.', 'Myers')], journal='American Scholar', volume='59', year=1989, pages='626-8'),
    dict(book=VLL, authors=[('A.', '', "O'Hear")], journal='Salisbury Review', volume='8', month='September', year=1989, pages='64-5'),
    dict(book=VLL, authors=[('J.', '', 'Passmore')], journal='Times Literary Supplement', day='26', month='May', year=1989, pages='567-8'),
    dict(book=VLL, authors=[('J.', 'E.', 'Powell')], journal='Independent', day='9', month='March', year=1989, pages='28'),
    dict(book=VLL, authors=[('J.', 'R.', 'Searle')], journal='New York Review of Books', volume='37', day='6', month='December', year=1990, pages='34-42'),
    dict(book=VLL, authors=[('R.', 'R.', 'Sherman')], journal='Change', volume='21', month='July', year=1989, pages='61'),
    dict(book=VLL, authors=[('R.', 'R.', 'Sherman')], journal='Choice', volume='26', month='July', year=1989, pages='1882'),
    dict(book=VLL, authors=[('J.', '', 'Sobran')], journal='National Review', volume='42', day='16', month='April', year=1990, pages='50-1'),
    dict(book=VLL, authors=[('G.', '', 'Stuttaford')], journal='Publishers Weekly', volume='235', day='13', month='January', year=1989, pages='81'),
    dict(book=VLL, authors=[('A.', '', 'Sullivan')], journal='Wall Street Journal', day='31', month='May', year=1989),
    dict(book=VLL, authors=[('S.', '', 'Walsh')], journal='Oxford Times', day='17', month='March', year=1989),
    dict(book=VLL, authors=[('K.', '', 'Williams')], journal='Studies in Education: A Journal of Educational Research', volume='7', year=1990, pages='68-70'),
    dict(book=RIP91, authors=[], journal='First Things', month='March', year=1992, pages='53'),
    dict(book=RIP91, authors=[], journal='Wisconsin Bookwatch', volume='1', month='September', year=1991, pages='1-2'),
    dict(book=RIP91, authors=[('P.', '', 'Gottfried')], journal='Modern Age', volume='35', year=1992, pages='173-8'),
    dict(book=RIP91, authors=[('C.', '', 'Kukathas')], journal='Political Theory', volume='21', year=1993, pages='339-43'),
    dict(book=RIP91, authors=[('D.', 'A.', 'Lloyd Thomas')], journal='Philosophy', volume='67', year=1992, pages='416-8'),
    dict(book=RIP91, authors=[('H.', 'M.', 'MacDonald')], journal='Social Science Quarterly', volume='73', year=1992, pages='475-6'),
    dict(book=RIP91, authors=[('K.', '', 'Minogue')], journal='Society', volume='43', year=2006, pages='81-7'),
    dict(book=RIP91, authors=[('N.', '', 'Pearcey')], journal='American Enterprise', volume='7', month='March', year=1996, pages='80'),
    dict(book=RIP91, authors=[('R.', 'A.', 'Peterson')], journal='Freeman', month='June', year=1992, pages='246-7'),
    dict(book=RIP91, authors=[('J.', 'E.', 'Powell')], journal='Economic Affairs', month='November', year=1991),
    dict(book=RIP91, authors=[('M.', '', 'Rushton')], title='Michael Oakeshott: A Review Essay', journal='Review of Politics', volume='54', year=1992, pages='665-74'),
    dict(book=MPME, authors=[], journal='Virginia Quarterly Review', volume='70', year=1994, pages='SS95-SS96'),
    dict(book=MPME, authors=[('B.', '', 'Charlton')], journal='Psychological Medicine', volume='25', year=1995, pages='427-30'),
    dict(book=MPME, authors=[('W.', '', 'Christian')], journal='Review of Politics', volume='57', year=1995, pages='344-6', also=[RPML]),
    dict(book=MPME, authors=[('R.', '', 'Devigne')], title='The Legacy of Michael Oakeshott', journal='Political Theory', volume='27', year=1999, pages='131-9', also=[RPML, PFPS]),
    dict(book=MPME, authors=[('A.', '', 'Edel')], journal='Society', volume='32', month='March', year=1995, pages='94-6', also=[RPML]),
    dict(book=MPME, authors=[('F.', '', 'Goldsmith')], journal='Library Journal', volume='118', day='1', month='November', year=1993, pages='96', also=[RPML]),
    dict(book=MPME, authors=[('R.', 'A. D.', 'Grant')], journal='Times Literary Supplement', day='15', month='April', year=1994, pages='31-2', also=[RPML]),
    dict(book=MPME, authors=[('I.', '', 'Holliday')], journal='Political Studies', volume='42', year=1994, pages='356-7', also=[RPML]),
    dict(book=MPME, authors=[('R.', 'J. B.', 'Jones')], journal='Times Higher Education Supplement', day='25', month='March', year=1994, pages='26'),
    dict(book=MPME, authors=[('D.', '', 'McCabe')], journal='Commonweal', volume='121', issue='8', day='22', month='April', year=1994, pages='21-2', also=[RPML]),
    dict(book=MPME, authors=[('B.', '', 'Parekh')], journal='Ethics', volume='106', year=1995, pages='158-86', also=[RPML]),
    dict(book=MPME, authors=[('P.', '', 'Riley')], journal='American Political Science Review', volume='88', year=1994, pages='746-8', also=[RPML]),
    dict(book=MPME, authors=[('D.', '', 'Schulz')], journal='Choice', volume='31', month='April', year=1994, pages='1364', also=[RPML]),
    dict(book=RPML, authors=[('A.', '', 'Cocks')], journal='Quadrant', volume='38', month='November', year=1994, pages='84'),
    dict(book=PFPS, authors=[('P.', '', 'Berkowitz')], journal='First Things', volume='72', month='April', year=1997, pages='38-42'),
    dict(book=PFPS, authors=[('D.', '', 'Boucher')], journal='International Studies in Philosophy', volume='33', year=2001, pages='151-2'),
    dict(book=PFPS, authors=[('W.', '', 'Christian')], journal='Perspectives on Political Science', volume='26', year=1997, pages='182'),
    dict(book=PFPS, authors=[('P.', '', 'Franco')], journal='American Political Science Review', volume='91', month='June', year=1997, pages='438-9'),
    dict(book=PFPS, authors=[('G.', '', 'Giorgini')], journal='Political Studies', volume='46', year=1998, pages='210-1'),
    dict(book=PFPS, authors=[('A.', '', 'Hartle')], journal='Review of Metaphysics', volume='50', year=1997, pages='676-8'),
    dict(book=PFPS, authors=[('E.', '', 'Heath')], journal='Independent Review', volume='2', year=1998, pages='443'),
    dict(book=PFPS, authors=[('J.', '', 'Landau')], journal='Wilson Quarterly', volume='20', year=1996, pages='102'),
    dict(book=PFPS, authors=[('N.', 'K.', "O'Sullivan"), ('L.', 'D.', "O'Sullivan")], title='Politics, Faith, and Scepticism', journal='Utilitas', volume='11', year=1999, pages='235-45'),
    dict(book=PFPS, authors=[('J.', '', 'Samples')], journal='Governance', volume='10', year=1997, pages='436'),
    dict(book=PFPS, authors=[('H.', '', 'Zeigler')], journal='Choice', volume='34', month='December', year=1996, pages='689'),
    dict(book=WIH, authors=[('J.', '', 'Alexander')], journal='Times Higher Education Supplement', day='8', month='April', year=2005),
    dict(book=WIH, authors=[('D.', '', 'Boucher')], journal='History of Political Thought', volume='27', year=2006, pages='171-4'),
    dict(book=WIH, authors=[('P.', '', 'Coleman')], title='The Sad and Noble Music of Michael Oakeshott: Politics in an Elgarian Mood', journal='Quadrant', month='June', year=2004, pages='86-8'),
    dict(book=WIH, authors=[('J.', '', 'Sumption')], title='Sworn Enemy of the Gradgrinds', journal='Spectator', day='15', month='May', year=2004, pages='67'),
    dict(book=LHPT, authors=[('P.', '', 'Coleman')], title='Escaping Plato’s Cave: A Parable for Politicians', journal='Quadrant', volume='50', month='April', year=2006, pages='28-30'),
    dict(book=LHPT, authors=[('L.', '', 'Marsh')], title='A History of Political Experience', journal='European Journal of Political Theory', volume='5', year=2006, pages='504-10'),
    dict(book=LHPT, authors=[('K.', '', 'Minogue')], journal='Times Literary Supplement', day='24', month='March', year=2006, pages='32'),
    dict(book=LHPT, authors=[('B.', '', 'Swaim')], title='The Right Stuff', journal='Weekly Standard', day='21', month='April', year=2008),
]
