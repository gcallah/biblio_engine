"""Doubts about Voegelin entries noticed while searching for abstracts
(November 2026), for load_abstracts_voegelin to put on the editors'
to-do page. Entries are keyed by (title, year, where), as in
_abstracts.py. Nothing in the entries was changed."""

KUNST = ("Die Kunst des Denkens", 1932, "Herder")
NACHWORT = ("Nachwort", 1932, "in: Die Kunst des Denkens")
ZWISCHEN = ("Zwischen Revolution und Restauration: Politisches Denken in "
            "England im 17. Jahrhundert", 1968, "Paul List Verlag")
ZUR_GESCHICHTE = ("Zur Geschichte des politischen Denkens", 1968,
                  "in: " + ZWISCHEN[0])
HELVETIUS = ("Helvétius", 1968, "in: Aufklärung und Materialismus im "
             "Frankreich des 18. Jahrhunderts")
ARENDT = ("The Origins of Totalitarianism", 1953, "The Review of Politics")
INTERVIEW = ("Philosophy of History: An Interview", 1977,
             "New Orleans Review")
RECOLLECTED = ("Voegelin Recollected: Conversations on a Life", 2008,
               "University of Missouri Press")
ANGST = ("Angst und Vernunft", 2018, "Matthes & Seitz")
RELIGIONS = ("Political Religions", 1986, "Edwin Mellen Press")
TEACHING = ("Teaching in an Age of Ideology", 2012, "Lexington Books")
NIETZSCHE = ("Nietzsche, the Crisis and the War", 1944,
             "The Journal of Politics")
EQUIVALENCES = ("Equivalences of Experience and Symbolization in History",
                1970, "in: Eternità e storia: I valori permanenti nel "
                "divenire storico")
TUEBINGEN = ("Psychologie des Gemeinschaftslebens: Bericht über den 14. "
             "Kongreß der Deutschen Gesellschaft für Psychologie in "
             "Tübingen vom 22.-26. Mai 1934", 1935, "Gustav Fischer")
RASSE = ("Rasse und Staat", 1935, "in: " + TUEBINGEN[0])
APSR = ("Political Theory and the Pattern of General History", 1944,
        "The American Political Science Review")
KELSEN = ("Gesellschaft, Staat und Recht: Festschrift gewidmet Hans Kelsen "
          "zum 50. Geburtstage", 1931, "Springer")
RAYMOND = ("Die unternehmerische Verantwortung in unserer "
           "Gesellschaftsordnung (Veröffentlichungen der Walter-Raymond-"
           "Stiftung, Bd. 4)", 1964, "Westdeutscher Verlag")

QUESTIONS = {
    "Voegelin: is Die Kunst des Denkens (Herder, 1932) the right book?": (
        "Library catalogues list Die Kunst des Denkens (Herder, 1932) as "
        "Ernest Dimnet's book, translated by Clotilde Schweiger, and none "
        "of the records found mentions Voegelin. Check that this is the "
        "volume that holds his 'Nachwort'.",
        [KUNST, NACHWORT]),
    "Voegelin: did he edit Zwischen Revolution und Restauration (1968)?": (
        "Catalogues give the book as 'hrsg. von Eric Voegelin', with "
        "essays by Henningsen, Gebhardt and others. If he edited it, it "
        "may belong with his own books rather than among the books that "
        "mention him, and he should be added as its editor.",
        [ZWISCHEN, ZUR_GESCHICHTE]),
    "Voegelin: 'Helvétius' (1968) co-written with Peter Leuschner?": (
        "The catalogue contents of Aufklärung und Materialismus im "
        "Frankreich des 18. Jahrhunderts (ed. Arno Baruzzi) give the "
        "Helvétius chapter as by Eric Voegelin and Peter Leuschner. If "
        "so, add Leuschner as a co-author.",
        [HELVETIUS]),
    "Voegelin: 'The Origins of Totalitarianism' (1953) is a review": (
        "This is Voegelin's review of Hannah Arendt's book, but the "
        "entry's reviewed book is blank. Should it be filled in (Arendt, "
        "The Origins of Totalitarianism), and the entry moved to the "
        "Book Reviews by Voegelin?",
        [ARENDT]),
    "Voegelin: 'Philosophy of History: An Interview' – 1977 or 1973?": (
        "Other sources describe a 1973 interview by Cangelosi and "
        "Corrington in New Orleans Review 2, titled 'Philosophies of "
        "History: An Interview with Eric Voegelin'. The entry's year and "
        "title may be wrong; not verified.",
        [INTERVIEW]),
    "Voegelin: publication years that sources give differently": (
        "- Voegelin Recollected: the publisher gives 5 December 2007; "
        "the entry says 2008.\n"
        "- Angst und Vernunft: the publisher's page says 2019; library "
        "catalogues and the entry say 2018.\n"
        "- Political Religions (Mellen): the publisher's page says 1985; "
        "the entry, HathiTrust and Open Library say 1986.\n"
        "- Teaching in an Age of Ideology: Google Books gives 2013 "
        "(Bloomsbury); the entry and Open Library say 2012.",
        [RECOLLECTED, ANGST, RELIGIONS, TEACHING]),
    "Voegelin: titles that catalogues give more fully": (
        "- 'Political Theory and the Pattern of General History' "
        "appeared in the APSR as part IV of a 1944 symposium.\n"
        "- The Kelsen Festschrift (1931), ed. Alfred Verdross, is "
        "catalogued as 'Gesellschaft, Staat und Recht: Untersuchungen "
        "zur reinen Rechtslehre; Festschrift Hans Kelsen zum 50. "
        "Geburtstage gewidmet'.\n"
        "- The Walter-Raymond-Stiftung volume (1964) has the subtitle "
        "'Tatbestand und Forderung'.\n"
        "- The 1935 Tübingen congress report: no record found confirms "
        "Voegelin's contribution 'Rasse und Staat' in it; unverified, "
        "not shown wrong.",
        [APSR, KELSEN, RAYMOND, TUEBINGEN, RASSE]),
    "Voegelin: two abstracts taken from a reprint or translation": (
        "No abstract of the first publication was found for these, so "
        "each was paraphrased from the same piece as later published: "
        "'Nietzsche, the Crisis and the War' from the abstract of its "
        "2017 Routledge reprint, and 'Equivalences of Experience' from "
        "the abstract of its French translation (Les Études "
        "philosophiques, 2009). Keep them, or clear them?",
        [NIETZSCHE, EQUIVALENCES]),
}
