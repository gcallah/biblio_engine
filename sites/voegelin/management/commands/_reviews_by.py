"""Book reviews by Eric Voegelin: his reviews of other people's books,
each in its first publication (1923-1955), for a reviews load like
load_reviews_by_oakeshott. Compiled 2026-11-19.

Sources:
- The Collected Works of Eric Voegelin, vol. 13, Selected Book Reviews,
  ed. and trans. Jodi Cockerill and Barry Cooper (University of Missouri
  Press, 2001): its 65 numbered reviews (cited "CW13 §n") and the
  editors' note at the head of each, which gives the first publication.
  CW13's introduction says the reviews run from 1923 to 1955 ("His last
  reviews appeared in 1955"); Crossref and the Hoover register show
  none later either.
- CW27, The Nature of the Law and Related Legal Writings (1991), which
  reprints three review pieces of 1941-42 (contents as listed at
  https://openlibrary.org/isbn/0807116734).
- Crossref (DOIs for the English journals: issue, month, pages).
- The Register of the Eric Voegelin Papers, Hoover Institution
  (https://faculty.lsu.edu/voegelin/files/eric-voegelin-papers.pdf),
  "Speeches and Writings", boxes 51-64: dates, and two printed reviews
  that CW13 does not include.
- K10plus (offprint records), the Eric Voegelin Institute's list of
  articles (faculty.lsu.edu/voegelin), and LSU Law's Digital Commons
  for the Louisiana Law Review.
Other Collected Works volumes: the contents of CW8 (Internet Archive
MARC record), CW10 (Google Books) and CW27 (Open Library) were seen;
for CW7, CW9, CW11 and CW12 the reprint links in _short_works_by.py
were relied on. None of them reprints a review here; CW11 reprints the
Arendt and Oxford pieces left out below. No other book in _books_by.py
says it reprints a review.

Left out:
- Already loaded as short works (_short_works_by.py): "The Origins of
  Totalitarianism" (Review of Politics 15, 1953, on Hannah Arendt's book,
  with her reply; key l18), "Zu Sanders 'Allgemeiner Staatslehre'"
  (1947, l09), and "The Oxford Political Philosophers" (Philosophical
  Quarterly 3, 1953, l20), a review-essay on recent Oxford writing.
  "Kelsen's Pure Theory of Law" (1927, e07) and "Die
  Souveränitätstheorie Dickinsons" (1929, e15) are essays, also loaded
  there. The 1931 Carl Schmitt piece is NOT in that file and is here.
- Reviews CW13 prints from typescripts whose publication its editors
  could not trace (so CW13 is their first publication): §9 Muntsch and
  Spalding, §10 Hankins, §11 Gee, §12 Mirkin-Getzewitsch, §13 W.
  Arendt (all c. 1929), §30 Sander (1935), §31 Raschhofer (1936), §33
  Hudal (1937), §44 Engel-Janosi (1944), §54 Curtius (1948); and §61
  Koschaker (1950), a publisher's reader's report, not a review.
- Typescripts in the Hoover register only, never published as far as
  is known: B. K. Sarkar (1922), Rostovtzeff (c. 1926), W. F. Bruck
  (1928), Richard Schmitz and Odo Neustädter-Stürmer (1936). Also left
  out: Karl Herrmann, Die Grundlegung des öffentlichen Rechts (ZöR
  1932) and Franz W. Jerusalem, Gemeinschaft und Staat (ZöR 1933), of
  which the register has only galley proofs (no printing confirmed),
  and a printed review of Mélanges offerts à Ernest Mahaim (c. 1935)
  whose journal the register does not name. CW13's editors say they
  left out a few "notices" that were little more than a table of
  contents; these may be some of them.

A piece covering several books is one entry per book, sharing the
journal and pages; the Frankfurter Zeitung piece of 10 June 1928 on
eight books about America is one entry (see the comment there).

Fields:
  key        r + year + letter
  names      the reviewed book's author(s)/editor(s) as a citation shows
             them
  reviewees  the same people as (first, middle, last)
  book       the reviewed book's title (subtitle after ": ")
  title      the review's own title, when it had one distinct from the
             book's; for a multi-book piece, the shared title
  volume, issue, day, month   strings; month a number; "" if unknown
  language   the language of the review (not of the book)
  reprinted  keys (in _books_by.py) of the Collected Works volumes that
             reprint the review; [] if none
  subject    best fit for the reviewed book
  source     the record(s) used; "CW13 §n" is CW13's note to review n
"""

PHIL, POL, HIST, LAW, REL, LIT, UNCAT = (
    "Philosophy", "Politics", "History", "Law", "Religion", "Literature",
    "Uncategorized")

HOOVER = "https://faculty.lsu.edu/voegelin/files/eric-voegelin-papers.pdf"

REVIEWS = [
    # ---- 1923-1937: German reviews (CW13, translated) ----
    dict(key="r1923a", year=1923, names="Felix Kaufmann",
         reviewees=[("Felix", "", "Kaufmann")],
         book="Logik und Rechtswissenschaft: Grundriss eines Systems der "
              "reinen Rechtslehre",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="3", issue="", day="", month="", pages="707-708",
         language="German", reprinted=["cw13"], subject=LAW,
         source="CW13 §1, editor's note; " + HOOVER + " (box 51, f. 6)"),
    dict(key="r1923b", year=1923, names="Heinrich Konrad",
         reviewees=[("Heinrich", "", "Konrad")],
         book="Das natürliche System der menschlichen Gesellschaft oder "
              "die Entstehung der Arten im periodischen System der "
              "sozialen Elemente",
         title="",
         journal="Zeitschrift für Volkswirtschaft und Sozialpolitik",
         volume="N.F. 3", issue="", day="", month="", pages="177-179",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §2, editor's note; " + HOOVER + " (box 51, f. 7)"),
    dict(key="r1924a", year=1924, names="Phil. al. Phil.",
         reviewees=[("", "", "Phil. al. Phil.")],
         book="The Soul of the State (The Know Thyself), vol. 10",
         title="",
         journal="Archiv für Sozialwissenschaft und Sozialpolitik",
         volume="51", issue="", day="", month="", pages="540",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §3, editor's note; " + HOOVER + " (box 51, f. 8)"),
    dict(key="r1924b", year=1924, names="Peter Trisca",
         reviewees=[("Peter", "", "Trisca")],
         book="Prolégomènes à une mécanique sociale",
         title="",
         journal="Archiv für Sozialwissenschaft und Sozialpolitik",
         volume="51", issue="", day="", month="", pages="540-541",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §4, editor's note; " + HOOVER + " (box 51, f. 8)"),
    dict(key="r1924c", year=1924, names="Felix Kaufmann",
         reviewees=[("Felix", "", "Kaufmann")],
         book="Die Kriterien des Rechts",
         title="",
         journal="Archiv für Sozialwissenschaft und Sozialpolitik",
         volume="53", issue="", day="", month="", pages="261-263",
         language="German", reprinted=["cw13"], subject=LAW,
         source="CW13 §5, editor's note; " + HOOVER + " (box 51, f. 10)"),
    dict(key="r1924d", year=1924, names="Leo Wittmayer",
         reviewees=[("Leo", "", "Wittmayer")],
         book="Österreichisches Verfassungsrecht",
         title="",
         journal="Archiv für Sozialwissenschaft und Sozialpolitik",
         volume="", issue="", day="", month="", pages="",
         language="German", reprinted=[], subject=LAW,
         source=HOOVER + " (box 51, f. 11: printed copy)"),
    dict(key="r1928a", year=1928, names="Walther Böhmer",
         reviewees=[("Walther", "", "Böhmer")],
         # Subtitle (Hoover register): "Pietätlose Schilderung selbsterlebter
         # Tatsachen und zwangsläufiger Konsequenzen aus dem
         # Weltwirtschaftskrieg, 1919-1927" (too long for the field).
         book="Mit Gott für Trust und Dividende",
         title="", journal="Frankfurter Zeitung",
         volume="", issue="", day="29", month="7", pages="",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §6, editor's note; " + HOOVER + " (box 52, f. 5)"),
    # One piece on eight books about America, under the title of the
    # first: also S. Marquis, Henry Ford; Augustin Souchy,
    # Schreckensherrschaft in Amerika; Eugène Lyons, Sacco und Vanzetti;
    # Fritz Tänzler, Aus dem Arbeitsleben Amerikas; Heinz Ludwig,
    # Systematische Wirtschaft; Ernst Jüngst, Die wirtschaftlichen und
    # sozialen Verhältnisse im Kohlenbergbau der Vereinigten Staaten;
    # André Siegfried, Die Vereinigten Staaten von Amerika. Too many
    # for one entry each, so only the first book is entered.
    dict(key="r1928b", year=1928, names="Karl H. Panhorst",
         reviewees=[("Karl", "H.", "Panhorst")],
         book="Deutschland und Amerika",
         title="Deutschland und Amerika", journal="Frankfurter Zeitung",
         volume="", issue="", day="10", month="6", pages="1",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §7, editor's note; " + HOOVER + " (box 52, f. 4)"),
    dict(key="r1928c", year=1928, names="Edgar Ansel Mowrer",
         reviewees=[("Edgar", "Ansel", "Mowrer")],
         book="Amerika: Vorbild und Warnung",
         title="", journal="Frankfurter Zeitung",
         volume="", issue="", day="19", month="8", pages="1",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §8, editor's note; " + HOOVER + " (box 52, f. 6)"),
    dict(key="r1930a", year=1930, names="Charlotte Lütkens",
         reviewees=[("Charlotte", "", "Lütkens")],
         book="Staat und Gesellschaft in Amerika",
         title="",
         journal="Archiv für Sozialwissenschaft und Sozialpolitik",
         volume="63", issue="", day="", month="", pages="649-653",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §14, editor's note"),
    dict(key="r1930b", year=1930, names="E. Jordan",
         reviewees=[("E.", "", "Jordan")],
         book="Theory of Legislation: An Essay on the Dynamics of Public "
              "Mind",
         title="", journal="Nationalwirtschaft",
         volume="3", issue="", day="", month="", pages="590",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §15, editor's note"),
    dict(key="r1931a", year=1931, names="Hellmuth Plessner",
         reviewees=[("Hellmuth", "", "Plessner")],
         book="Macht und menschliche Natur",
         title="", journal="Kölner Vierteljahrshefte für Soziologie",
         volume="9", issue="", day="", month="", pages="255-257",
         language="German", reprinted=["cw13"], subject=PHIL,
         source="CW13 §16, editor's note"),
    # The review-essay CW13 counts as a review (§17).
    dict(key="r1931b", year=1931, names="Carl Schmitt",
         reviewees=[("Carl", "", "Schmitt")],
         book="Verfassungslehre",
         title="Die Verfassungslehre von Carl Schmitt: Versuch einer "
               "konstruktiven Analyse ihrer staatstheoretischen "
               "Prinzipien",
         journal="Zeitschrift für öffentliches Recht",
         volume="11", issue="1", day="", month="", pages="89-109",
         language="German", reprinted=["cw13"], subject=LAW,
         source="CW13 §17, editor's note; "
                "https://opac.k10plus.de/DB=2.1/PPNSET?PPN=1137889993"),
    dict(key="r1932a", year=1932, names="Heinz O. Ziegler",
         reviewees=[("Heinz", "O.", "Ziegler")],
         book="Die moderne Nation",
         title="",
         journal="Zeitschrift für die gesamte Staatswissenschaft",
         volume="95", issue="", day="", month="", pages="507-509",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §18, editor's note; " + HOOVER + " (box 53)"),
    dict(key="r1932b", year=1932, names="Ernst Gerhard Jacob",
         reviewees=[("Ernst", "Gerhard", "Jacob")],
         book="Daniel Defoe, Essay on Projects (1697)",
         title="",
         journal="Archiv für Rechts- und Wirtschaftsphilosophie",
         volume="25", issue="", day="", month="4", pages="397",
         language="German", reprinted=["cw13"], subject=HIST,
         source="CW13 §19, editor's note; " + HOOVER + " (box 53)"),
    dict(key="r1933a", year=1933, names="Hans Steingräber",
         reviewees=[("Hans", "", "Steingräber")],
         # Subtitle shortened to fit the field; in full: "Eine Untersuchung
         # ihrer Grundkategorien und kritische Darstellung ihrer
         # hauptsächlichen metaphysischen Gestaltungen".
         book="Deutsche Gemeinschaftsphilosophie der Gegenwart: Eine "
              "Untersuchung ihrer Grundkategorien",
         title="", journal="Blätter für deutsche Philosophie",
         volume="10", issue="", day="", month="", pages="",
         language="German", reprinted=["cw13"], subject=PHIL,
         source="CW13 §20, editor's note; " + HOOVER + " (box 53, f. 15)"),
    dict(key="r1933b", year=1933, names="Walter Hamel",
         reviewees=[("Walter", "", "Hamel")],
         book="Das Wesen des Staatsgebietes",
         title="", journal="Blätter für deutsche Philosophie",
         volume="10", issue="", day="", month="", pages="",
         language="German", reprinted=["cw13"], subject=LAW,
         source="CW13 §21, editor's note; " + HOOVER + " (box 53, f. 16)"),
    dict(key="r1933c", year=1933,
         names="E. von Hartig and W. Schellberg (eds.)",
         reviewees=[("E.", "", "von Hartig"), ("W.", "", "Schellberg")],
         book="Handbuch der Amerikakunde (Handbücher der Auslandskunde, "
              "vol. 6)",
         title="Amerikakunde", journal="Frankfurter Zeitung",
         volume="66", issue="13", day="26", month="3", pages="5",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §22, editor's note (Literaturblatt, p. 5); "
                + HOOVER + " (box 54, f. 10)"),
    dict(key="r1933d", year=1933, names="Günter Namslau",
         reviewees=[("Günter", "", "Namslau")],
         book="Rechtfertigung des Staates bei Christian Wolff",
         title="", journal="Zentralblatt für die juristische Praxis",
         volume="51", issue="", day="", month="", pages="141-142",
         language="German", reprinted=["cw13"], subject=PHIL,
         source="CW13 §23, editor's note; " + HOOVER + " (box 54, f. 8)"),
    dict(key="r1934a", year=1934, names="Reinhold Horneffer",
         reviewees=[("Reinhold", "", "Horneffer")],
         book="Die Entstehung des Staates: Eine staatstheoretische "
              "Untersuchung",
         title="", journal="Blätter für deutsche Philosophie",
         volume="11", issue="", day="", month="", pages="",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §24, editor's note; " + HOOVER + " (box 54, f. 6)"),
    dict(key="r1934b", year=1934, names="Dietrich Schindler",
         reviewees=[("Dietrich", "", "Schindler")],
         book="Verfassungsrecht und soziale Struktur",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="14", issue="", day="", month="", pages="256-257",
         language="German", reprinted=["cw13"], subject=LAW,
         source="CW13 §25, editor's note; " + HOOVER + " (box 54, f. 14)"),
    dict(key="r1934c", year=1934, names="Max Rumpf",
         reviewees=[("Max", "", "Rumpf")],
         book="Politische und soziologische Staatslehre",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="14", issue="", day="", month="", pages="268-269",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §26, editor's note; " + HOOVER + " (box 54, f. 15)"),
    # One review of two books by Zimmern (CW13 §27): an entry for each.
    dict(key="r1934d", year=1934, names="Alfred E. Zimmern",
         reviewees=[("Alfred", "E.", "Zimmern")],
         book="Nationality and Government, with Other War-Time Essays",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="14", issue="", day="", month="", pages="269",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §27, editor's note; " + HOOVER + " (box 54, f. 13)"),
    dict(key="r1934e", year=1934, names="Alfred E. Zimmern",
         reviewees=[("Alfred", "E.", "Zimmern")],
         book="The Prospects of Democracy, and Other Essays",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="14", issue="", day="", month="", pages="269",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §27, editor's note; " + HOOVER + " (box 54, f. 13)"),
    dict(key="r1934f", year=1934, names="A. E. Hoche",
         reviewees=[("A.", "E.", "Hoche")],
         book="Das Rechtsgefühl in Justiz und Politik",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="14", issue="", day="", month="", pages="270-271",
         language="German", reprinted=["cw13"], subject=LAW,
         source="CW13 §28, editor's note; " + HOOVER + " (box 54, f. 12)"),
    dict(key="r1934g", year=1934, names="Alfred Schütz",
         reviewees=[("Alfred", "", "Schütz")],
         book="Der sinnhafte Aufbau der sozialen Welt",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="14", issue="", day="", month="", pages="668-672",
         language="German", reprinted=["cw13"], subject=PHIL,
         source="CW13 §29, editor's note"),
    dict(key="r1935a", year=1935, names="Godehard Jos. Ebers",
         reviewees=[("Godehard", "Jos.", "Ebers")],
         book="Verfassungsrecht",
         title="", journal="Zentralblatt für die juristische Praxis",
         volume="53", issue="", day="", month="", pages="",
         language="German", reprinted=[], subject=LAW,
         source=HOOVER + " (box 54, f. 28: printed copy)"),
    dict(key="r1936a", year=1936, names="Bernhard Laum",
         reviewees=[("Bernhard", "", "Laum")],
         book="Die geschlossene Wirtschaft: Soziologische Grundlegung des "
              "Autarkieproblems",
         title="", journal="Zeitschrift für Nationalökonomie",
         volume="7", issue="", day="", month="", pages="138-141",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §32, editor's note; " + HOOVER + " (box 53, f. 14)"),
    dict(key="r1937a", year=1937, names="Eduard Baumgarten",
         reviewees=[("Eduard", "", "Baumgarten")],
         book="Benjamin Franklin, der Lehrmeister der amerikanischen "
              "Revolution: Die geistigen Grundlagen des amerikanischen "
              "Gemeinwesens",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="17", issue="", day="", month="", pages="255-257",
         language="German", reprinted=["cw13"], subject=HIST,
         source="CW13 §34, editor's note; " + HOOVER + " (box 55, f. 18)"),
    dict(key="r1937b", year=1937, names="Hans Krupa",
         reviewees=[("Hans", "", "Krupa")],
         book="Carl Schmitts Theorie des \"Politischen\"",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="17", issue="", day="", month="", pages="665",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §35, editor's note; " + HOOVER + " (box 55, f. 19)"),
    dict(key="r1937c", year=1937, names="Barna Horváth",
         reviewees=[("Barna", "", "Horváth")],
         book="Rechtssoziologie: Probleme der Gesellschaftslehre und der "
              "Geschichtslehre des Rechts",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="17", issue="", day="", month="", pages="667-672",
         language="German", reprinted=["cw13"], subject=LAW,
         source="CW13 §36, editor's note"),
    dict(key="r1937d", year=1937, names="Peter Berger",
         reviewees=[("Peter", "", "Berger")],
         book="Faschismus und Nationalsozialismus",
         title="", journal="Zeitschrift für öffentliches Recht",
         volume="17", issue="", day="", month="", pages="671-672",
         language="German", reprinted=["cw13"], subject=POL,
         source="CW13 §37, editor's note"),

    # ---- 1939-1955: English reviews ----
    dict(key="r1939a", year=1939, names="J. Boissonnet",
         reviewees=[("J.", "", "Boissonnet")],
         book="La misère par la surabondance: Karl Marx, père de la crise "
              "mondiale",
         title="", journal="The American Economic Review",
         volume="29", issue="", day="", month="", pages="572",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §38, editor's note; " + HOOVER + " (box 55, f. 30)"),
    dict(key="r1939b", year=1939, names="Gaetano Mosca",
         reviewees=[("Gaetano", "", "Mosca")],
         book="The Ruling Class",
         title="", journal="The Journal of Politics",
         volume="1", issue="4", day="", month="11", pages="434-436",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §39, editor's note; "
                "https://doi.org/10.2307/2125230"),
    dict(key="r1941a", year=1941, names="James Brown Scott",
         reviewees=[("James", "Brown", "Scott")],
         book="Law, the State, and the International Community",
         title="Right and Might", journal="The Review of Politics",
         volume="3", issue="1", day="", month="1", pages="122-123",
         language="English", reprinted=["cw27"], subject=LAW,
         source="https://doi.org/10.1017/s0034670500000796; "
                "https://openlibrary.org/isbn/0807116734 (CW27 contents)"),
    # "Two Recent Contributions to the Science of Law": one piece on two
    # books, an entry for each.
    dict(key="r1941b", year=1941, names="N. S. Timasheff",
         reviewees=[("N.", "S.", "Timasheff")],
         book="An Introduction to the Sociology of Law",
         title="Two Recent Contributions to the Science of Law",
         journal="The Review of Politics",
         volume="3", issue="3", day="", month="7", pages="399-404",
         language="English", reprinted=["cw27"], subject=LAW,
         source="https://doi.org/10.1017/s0034670500001819; "
                "https://openlibrary.org/isbn/0807116734 (CW27 contents)"),
    dict(key="r1941c", year=1941, names="Edgar Bodenheimer",
         reviewees=[("Edgar", "", "Bodenheimer")],
         book="Jurisprudence: The Philosophy and Method of the Law",
         title="Two Recent Contributions to the Science of Law",
         journal="The Review of Politics",
         volume="3", issue="3", day="", month="7", pages="399-404",
         language="English", reprinted=["cw27"], subject=LAW,
         source="https://doi.org/10.1017/s0034670500001819; "
                "https://openlibrary.org/isbn/0807116734 (CW27 contents)"),
    dict(key="r1942a", year=1942, names="Huntington Cairns",
         reviewees=[("Huntington", "", "Cairns")],
         book="The Theory of Legal Science",
         title="The Theory of Legal Science: A Review",
         journal="Louisiana Law Review",
         volume="4", issue="4", day="", month="", pages="554-572",
         language="English", reprinted=["cw27"], subject=LAW,
         source="https://digitalcommons.law.lsu.edu/lalrev/vol4/iss4/4; "
                "https://openlibrary.org/isbn/0807116734 (CW27 contents); "
                + HOOVER + " (box 61, f. 13)"),
    # One review of two books (CW13 §40): an entry for each.
    dict(key="r1942b", year=1942, names="Maxine Y. Sweezy",
         reviewees=[("Maxine", "Y.", "Sweezy")],
         book="The Structure of the Nazi Economy",
         title="", journal="The Journal of Politics",
         volume="4", issue="2", day="", month="5", pages="269-272",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §40, editor's note; "
                "https://doi.org/10.2307/2125775"),
    dict(key="r1942c", year=1942, names="Ernst Fraenkel",
         reviewees=[("Ernst", "", "Fraenkel")],
         book="The Dual State: A Contribution to the Theory of "
              "Dictatorship",
         title="", journal="The Journal of Politics",
         volume="4", issue="2", day="", month="5", pages="269-272",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §40, editor's note; "
                "https://doi.org/10.2307/2125775"),
    dict(key="r1943a", year=1943, names="Alec de Montmorency",
         reviewees=[("Alec", "", "de Montmorency")],
         book="The Enigma of Admiral Darlan",
         title="", journal="The American Political Science Review",
         volume="37", issue="", day="", month="", pages="751-752",
         language="English", reprinted=["cw13"], subject=HIST,
         source="CW13 §41, editor's note; " + HOOVER + " (box 62, f. 2)"),
    dict(key="r1944a", year=1944, names="John H. Hallowell",
         reviewees=[("John", "H.", "Hallowell")],
         book="The Decline of Liberalism as an Ideology: With Particular "
              "Reference to German Politico-Legal Thought",
         title="", journal="The Journal of Politics",
         volume="6", issue="1", day="", month="2", pages="107-109",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §42, editor's note; "
                "https://doi.org/10.2307/2125360"),
    dict(key="r1944b", year=1944, names="Marvin Farber",
         reviewees=[("Marvin", "", "Farber")],
         book="The Foundation of Phenomenology: Edmund Husserl and the "
              "Quest for a Rigorous Science of Philosophy",
         title="", journal="Social Research",
         volume="11", issue="", day="", month="", pages="389-397",
         language="English", reprinted=["cw13"], subject=PHIL,
         source="CW13 §43, editor's note; " + HOOVER + " (box 61, f. 17)"),
    # One review of two books (CW13 §45): an entry for each.
    dict(key="r1945a", year=1945, names="Hans Kelsen",
         reviewees=[("Hans", "", "Kelsen")],
         book="General Theory of Law and State",
         title="", journal="Louisiana Law Review",
         volume="6", issue="3", day="", month="", pages="489-492",
         language="English", reprinted=["cw13"], subject=LAW,
         source="CW13 §45, editor's note; "
                "https://digitalcommons.law.lsu.edu/lalrev/vol6/iss3/17"),
    dict(key="r1945b", year=1945, names="William Ebenstein",
         reviewees=[("William", "", "Ebenstein")],
         book="The Pure Theory of Law",
         title="", journal="Louisiana Law Review",
         volume="6", issue="3", day="", month="", pages="489-492",
         language="English", reprinted=["cw13"], subject=LAW,
         source="CW13 §45, editor's note; "
                "https://digitalcommons.law.lsu.edu/lalrev/vol6/iss3/17"),
    dict(key="r1945c", year=1945, names="Carlo Sforza",
         reviewees=[("Carlo", "", "Sforza")],
         book="Contemporary Italy: Its Intellectual and Moral Origins",
         title="", journal="The Journal of Politics",
         volume="7", issue="1", day="", month="2", pages="94-97",
         language="English", reprinted=["cw13"], subject=HIST,
         source="CW13 §46, editor's note; "
                "https://doi.org/10.2307/2125948"),
    dict(key="r1946a", year=1946, names="Albert R. Chandler",
         reviewees=[("Albert", "R.", "Chandler")],
         book="Rosenberg's Nazi Myth",
         title="", journal="The American Journal of Sociology",
         volume="52", issue="2", day="", month="9", pages="161",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §47, editor's note; "
                "https://doi.org/10.1086/219969"),
    dict(key="r1946b", year=1946, names="Frederick L. Schuman",
         reviewees=[("Frederick", "L.", "Schuman")],
         book="Soviet Politics: At Home and Abroad",
         title="", journal="The Journal of Politics",
         volume="8", issue="2", day="", month="5", pages="212-220",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §48, editor's note; "
                "https://doi.org/10.2307/2125897"),
    dict(key="r1946c", year=1946,
         names="Gerhart Eisler, Albert Norden and Albert Schreiner",
         reviewees=[("Gerhart", "", "Eisler"), ("Albert", "", "Norden"),
                    ("Albert", "", "Schreiner")],
         book="The Lesson of Germany: A Guide to Her History",
         title="", journal="The American Political Science Review",
         volume="40", issue="", day="", month="", pages="385-386",
         language="English", reprinted=["cw13"], subject=HIST,
         source="CW13 §49, editor's note"),
    dict(key="r1947a", year=1947, names="Rudolf Schlesinger",
         reviewees=[("Rudolf", "", "Schlesinger")],
         book="Soviet Legal Theory: Its Social Background and Development",
         title="", journal="The Journal of Politics",
         volume="9", issue="1", day="", month="2", pages="129-131",
         language="English", reprinted=["cw13"], subject=LAW,
         source="CW13 §50, editor's note; "
                "https://doi.org/10.2307/2125871"),
    dict(key="r1947b", year=1947, names="F. S. C. Northrop",
         reviewees=[("F.", "S. C.", "Northrop")],
         book="The Meeting of East and West: An Inquiry Concerning World "
              "Understanding",
         title="", journal="Social Research",
         volume="14", issue="", day="", month="", pages="244-249",
         language="English", reprinted=["cw13"], subject=PHIL,
         source="CW13 §51, editor's note"),
    dict(key="r1947c", year=1947, names="David Fellman (ed.)",
         reviewees=[("David", "", "Fellman")],
         book="Post-War Governments of Europe",
         title="", journal="The American Political Science Review",
         volume="41", issue="", day="", month="", pages="595-596",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §52, editor's note"),
    dict(key="r1947d", year=1947, names="Ernst Cassirer",
         reviewees=[("Ernst", "", "Cassirer")],
         book="The Myth of the State",
         title="", journal="The Journal of Politics",
         volume="9", issue="3", day="", month="8", pages="445-447",
         language="English", reprinted=["cw13"], subject=PHIL,
         source="CW13 §53, editor's note; "
                "https://doi.org/10.2307/2125803"),
    dict(key="r1948a", year=1948, names="Jan Huizinga",
         reviewees=[("Jan", "", "Huizinga")],
         book="Homo Ludens: Versuch einer Bestimmung des Spielelementes "
              "der Kultur",
         title="", journal="The Journal of Politics",
         volume="10", issue="1", day="", month="2", pages="179-187",
         language="English", reprinted=["cw13"], subject=HIST,
         source="CW13 §55, editor's note; "
                "https://doi.org/10.2307/2125824"),
    dict(key="r1949a", year=1949, names="Leo Strauss",
         reviewees=[("Leo", "", "Strauss")],
         book="On Tyranny: An Interpretation of Xenophon's Hiero",
         title="", journal="The Review of Politics",
         volume="11", issue="2", day="", month="4", pages="241-244",
         language="English", reprinted=["cw13"], subject=PHIL,
         source="CW13 §56, editor's note; "
                "https://doi.org/10.1017/s0034670500043187"),
    dict(key="r1949b", year=1949, names="Nathan A. Pelcovits",
         reviewees=[("Nathan", "A.", "Pelcovits")],
         book="Old China Hands and the Foreign Office",
         title="", journal="Social Research",
         volume="16", issue="", day="", month="", pages="102-104",
         language="English", reprinted=["cw13"], subject=HIST,
         source="CW13 §57, editor's note"),
    dict(key="r1949c", year=1949, names="John Bowle",
         reviewees=[("John", "", "Bowle")],
         book="Western Political Thought: An Historical Introduction from "
              "the Origins to Rousseau",
         title="A Simplification of History",
         journal="The Review of Politics",
         volume="11", issue="2", day="", month="4", pages="262-263",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §58, editor's note; "
                "https://doi.org/10.1017/s0034670500043266"),
    dict(key="r1949d", year=1949, names="Alfred Verdross-Drossberg",
         reviewees=[("Alfred", "", "Verdross-Drossberg")],
         book="Grundlinien der antiken Rechts- und Staatsphilosophie",
         title="", journal="The Western Political Quarterly",
         volume="2", issue="3", day="", month="9", pages="437-438",
         language="English", reprinted=["cw13"], subject=LAW,
         source="CW13 §59, editor's note; "
                "https://doi.org/10.1177/106591294900200319"),
    dict(key="r1949e", year=1949,
         names="Thomas G. Bergin and Max A. Fisch (trans.)",
         reviewees=[("Thomas", "G.", "Bergin"), ("Max", "A.", "Fisch")],
         book="The New Science of Giambattista Vico",
         title="", journal="The Catholic Historical Review",
         volume="35", issue="", day="", month="", pages="76-77",
         language="English", reprinted=["cw13"], subject=PHIL,
         source="CW13 §60, editor's note; " + HOOVER + " (box 62, f. 35)"),
    dict(key="r1953a", year=1953, names="Fritz Wagner",
         reviewees=[("Fritz", "", "Wagner")],
         book="Geschichtswissenschaft",
         title="", journal="The American Political Science Review",
         volume="47", issue="1", day="", month="3", pages="261-262",
         language="English", reprinted=["cw13"], subject=HIST,
         source="CW13 §62, editor's note; "
                "https://doi.org/10.2307/1950985"),
    # One review of two books (CW13 §63): an entry for each.
    dict(key="r1954a", year=1954, names="John Wild",
         reviewees=[("John", "", "Wild")],
         book="Plato's Modern Enemies and the Theory of Natural Law",
         title="", journal="The American Political Science Review",
         volume="48", issue="3", day="", month="9", pages="859-862",
         language="English", reprinted=["cw13"], subject=PHIL,
         source="CW13 §63, editor's note; "
                "https://doi.org/10.2307/1951062"),
    dict(key="r1954b", year=1954, names="Ronald B. Levinson",
         reviewees=[("Ronald", "B.", "Levinson")],
         book="In Defense of Plato",
         title="", journal="The American Political Science Review",
         volume="48", issue="3", day="", month="9", pages="859-862",
         language="English", reprinted=["cw13"], subject=PHIL,
         source="CW13 §63, editor's note; "
                "https://doi.org/10.2307/1951062"),
    dict(key="r1955a", year=1955, names="Raymond Polin",
         reviewees=[("Raymond", "", "Polin")],
         book="Politique et philosophie chez Thomas Hobbes",
         title="", journal="The American Political Science Review",
         volume="49", issue="2", day="", month="6", pages="597-598",
         language="English", reprinted=["cw13"], subject=PHIL,
         source="CW13 §64, editor's note; "
                "https://doi.org/10.1017/s0003055400275862"),
    dict(key="r1955b", year=1955, names="Ewart Lewis",
         reviewees=[("Ewart", "", "Lewis")],
         book="Medieval Political Ideas",
         title="", journal="The Yale Review",
         volume="44", issue="", day="", month="", pages="616",
         language="English", reprinted=["cw13"], subject=POL,
         source="CW13 §65, editor's note; " + HOOVER + " (box 64, f. 20)"),
]

QUESTIONS = {
    "Voegelin reviews 1923–1937: volumes and pages to check": (
        "CW13's notes and the other records disagree, or leave gaps:\n"
        "- Kaufmann, Die Kriterien des Rechts: CW13 gives Archiv 53 "
        "(1925); the Hoover register dates it 1924, and Archiv 53 is "
        "1924/25 (Voegelin's 'Die Zeit in der Wirtschaft', same volume, "
        "is dated 1924). Year set to 1924.\n"
        "- The Soul of the State and Trisca: CW13 gives Archiv 51 "
        "(1924); the register dates both 1923, and by the numbering "
        "above Bd. 51 would be about 1923/24.\n"
        "- Wittmayer (1924) and Ebers (1935): not in CW13; the register "
        "has a printed copy of each but gives no volume or pages. "
        "Archiv volume unknown. The Zentralblatt volume 53 is worked out "
        "from its numbering (Bd. 39 = 1921), not seen.\n"
        "- Namslau (1933): CW13 says Zentralblatt '2 (1933)', which "
        "cannot be the volume (the journal was in its 51st year in "
        "1933); volume set to 51, and '2' may be the issue.\n"
        "- Plessner (1931): CW13 says Kölner Vierteljahrshefte '19 "
        "(1931)', which is impossible; Jahrgang 9 was 1930/31 (the "
        "1930 'Max Weber' is in Jg. 9), so 9 is assumed ('19' a stray "
        "digit), though 10 (1931/32) is possible.\n"
        "- Schmitt (1931): CW13 gives pp. 89-109, the K10plus offprint "
        "90-109, the LSU list 80-109.\n"
        "- Steingräber, Hamel, Horneffer: CW13 gives Blätter für "
        "deutsche Philosophie 10 (1933) and 11 (1934) with no pages, "
        "and these may be issue rather than volume numbers (not "
        "checked). "
        "The register dates Horneffer 1933.\n"
        "- Horváth (667-672) and Berger (671-672) overlap in CW13; "
        "Horváth probably ends on 671.",
        ["r1924a", "r1924b", "r1924c", "r1924d", "r1935a", "r1933d",
         "r1931a", "r1931b",
         "r1933a", "r1933b", "r1934a", "r1937c", "r1937d"]),
    "Voegelin reviews 1939–1955: CW13 slips": (
        "- Mosca: CW13 says Journal of Politics 1: 434-446; Crossref "
        "gives 434-436, used here.\n"
        "- Ewart Lewis: CW13 says Yale Review 44 (1955): 616-668, an "
        "evident misprint for a review; only the first page is given.\n"
        "- Eisler, Norden and Schreiner: CW13 says 'The Lessons of "
        "Germany'; other reviews of the book give 'The Lesson of "
        "Germany', used here. The APSR 1943, 1946, 1947 issue numbers "
        "were not confirmed.",
        ["r1939b", "r1955b", "r1946c"]),
}
