"""Possible matches for authors we could not confirm. NOT loaded.

CANDIDATES: a likely identity was found, but no source ties that person
to the work in the bibliography. Each entry is in the same format as
_author_info.py, plus "candidate" (who we think it is), "evidence" and
"works". Once a match is confirmed, move the entry (without candidate,
evidence and works) into _author_info.py and run load_author_info.

UNIDENTIFIED: no match found yet; "evidence" records what was tried and
any lead worth following.

Researched 2026-11-06; every UNIDENTIFIED entry got a second search on
2026-11-07, along with the people loaded since.
"""

CANDIDATES = {
    ('Ademi', 'G.', ''): dict(
        candidate='Guri Ademi',
        confidence='low',
        evidence=(
            'The UW Law School repository '
            '(https://repository.law.wisc.edu/s/uwlaw/item/1627) lists the name'
            ' Guri Ademi with this Wisconsin Law Review article, but gives no '
            'biography, role or dates; it may be a student note. Nothing else '
            'was found, so only the first name is filled.'
        ),
        works=[
            'author: Legal Intimations: Michael Oakeshott and the Rule of Law (1993) — Wisconsin Law Journal',
        ],),
    ('Bahners', 'P.', ''): dict(
        candidate='P. Bahners',
        confidence='medium',
        affiliation='Frankfurter Allgemeine Zeitung',
        yob=1967,
        descr=(
            'German journalist and historian who studied history and philosophy'
            ' at Bonn and Oxford and joined the culture (Feuilleton) desk of '
            'the Frankfurter Allgemeine Zeitung in 1989. He headed the FAZ '
            'Feuilleton from 2001 to 2011 and later served as a cultural '
            'correspondent; his books include studies of Helmut Kohl and of '
            'German debates on Islam. He wrote the FAZ obituary of Oakeshott in'
            ' 1990.'
        ),
        evidence=(
            'Identified as Patrick Bahners: he joined the FAZ Feuilleton in '
            '1989 and studied at Oxford, fitting a 1990 FAZ obituary of '
            "Oakeshott signed 'P. Bahners'. No direct source attributing the "
            'obituary was found, but no other P. Bahners at FAZ is known.'
        ),
        sources=dict(
            yob='https://de.wikipedia.org/wiki/Patrick_Bahners',
            affiliation='https://de.wikipedia.org/wiki/Patrick_Bahners',
            descr='https://de.wikipedia.org/wiki/Patrick_Bahners',
        ),
        works=[
            'author: Auf hoher See. Zum Tode des Philosophen Michael Oakeshott (1990) — Frankfurter allgemeine Zeitung',
        ],),
    ('Coleman', 'P.', ''): dict(
        candidate='P. Coleman',
        confidence='medium',
        affiliation='Quadrant',
        yob=1928,
        yod=2019,
        descr=(
            'Australian journalist, editor and politician (William Peter '
            'Coleman), who edited The Bulletin and, for about two decades, the '
            'conservative magazine Quadrant, and served in the New South Wales '
            'and federal parliaments. He wrote widely on conservative and anti-'
            'communist intellectual life.'
        ),
        evidence=(
            'Inferred from Australian conservative outlet (News Weekly, 1991) '
            'and era; not directly confirmed the article is his.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Peter_Coleman',
            yod='https://en.wikipedia.org/wiki/Peter_Coleman',
            affiliation='https://en.wikipedia.org/wiki/Peter_Coleman',
            descr='https://en.wikipedia.org/wiki/Peter_Coleman',
        ),
        works=[
            'author: Michael Oakeshott (1901-1990): Beyond the Shadow Line (1991) — News Weekly',
        ],),
    ('Connelly', 'J.', ''): dict(
        candidate='J. Connelly',
        confidence='medium',
        affiliation='University of Hull',
        descr=(
            'Political theorist, emeritus professor of political theory at the '
            'University of Hull and a leading Collingwood scholar. He wrote '
            "Metaphysics, Method and Politics on Collingwood's political "
            'philosophy and R.G. Collingwood: A Biography (2022), and co-edited'
            " editions of Collingwood's works."
        ),
        evidence=(
            'Identified as James Connelly because he is the principal '
            'Collingwood scholar publishing in Collingwood Studies in the '
            '1990s; the specific 1998 article could not be found in his online '
            "bibliography. A LibraryThing entry gives 'James Connelly (1957-)' "
            'but could not be verified, so yob left blank.'
        ),
        sources=dict(
            affiliation='https://hull.academia.edu/JamesConnelly/Books',
            descr='https://hull.academia.edu/JamesConnelly/Books',
        ),
        works=[
            'author: Art, History and Science: The Contrasting Worlds of Collingwood and Oakeshott (1998) — Collingwood Studies',
        ],),
    ('Costelloe', 'T.', 'M.'): dict(
        candidate='Timothy M. Costelloe',
        confidence='medium',
        affiliation='College of William & Mary',
        yob=1964,
        descr=(
            'Philosopher who holds doctorates in sociology (Boston University) '
            'and philosophy (Emory) and is a professor of philosophy at the '
            'College of William & Mary. He works mainly on aesthetics and the '
            'history of modern philosophy, especially Hume and the sublime; his'
            ' early work related Oakeshott and Wittgenstein to the philosophy '
            'of social science.'
        ),
        evidence=(
            'Identified as Timothy M. Costelloe (b. 14 Dec 1964 per LoC); '
            'sociology PhD 1996 fits a 1998 social-theory article on '
            'Oakeshott/Wittgenstein in J. Theory of Social Behaviour. Not '
            'directly confirmed by a source listing the article.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n2006077297',
            affiliation='https://www.wm.edu/as/philosophy/people/faculty/costelloe_t.php',
            descr='https://www.wm.edu/as/philosophy/people/faculty/costelloe_t.php',
        ),
        works=[
            'author: Oakeshott, Wittgenstein and the Practice of Social Science (1998) — Journal for the Theory of Social Behaviour',
        ],),
    ('Fulop', 'E.', ''): dict(
        candidate='Endre Fülöp',
        confidence='medium',
        affiliation='Eötvös Loránd University',
        descr=(
            'Hungarian political philosopher who writes in Hungarian on modern '
            'conservatism and Michael Oakeshott. He reviewed the Hungarian '
            "edition of Oakeshott's Rationalism in Politics (2001) and has "
            "taught a course on Oakeshott's political philosophy in the "
            'philosophy programme at Eötvös Loránd University (ELTE), Budapest.'
        ),
        evidence=(
            "Input 'E. Fulop'; identified as Fülöp Endre, the Hungarian author "
            'writing on Oakeshott (Hungarian journals Valóság and Világosság '
            'match). The specific Valóság/Világosság articles were not directly'
            ' confirmed online. ELTE affiliation inferred from a 2021 ELTE '
            'course syllabus (course code BBN-FIL) listing him as lecturer; his'
            " rank/department is not stated. Name changed from input 'E. Fulop'"
            " to 'Endre Fülöp' (Hungarian spelling with diacritics)."
        ),
        sources=dict(
            affiliation='https://lps.elte.hu/leszabo/courselist/sillabuszok/2021-1-2-10-12-45/Fnnlnnp_Endre_Oakeshott_2021_tavasz_BBN-FIL-402.58.rtf',
            descr='https://eksearch.ek.szte.hu/Record/bibDOK00021493/Description',
        ),
        works=[
            'author: The Meaning of Traditionalism: Hayek, Cecil and Oakeshott on Conservatism (2000) — Valóság',
            'author: Argument, Disput, and Conversation: Michael Oakeshott and the Possibility of Persuasion in Politics (2004) — Világosság',
        ],),
    ('Gaita', 'R.', ''): dict(
        candidate='Raimond Gaita',
        confidence='medium',
        affiliation='University of Melbourne',
        yob=1946,
        descr=(
            'German-born Australian moral philosopher, emeritus professor of '
            "moral philosophy at King's College London and professorial fellow "
            'at the University of Melbourne, formerly foundation professor of '
            'philosophy at Australian Catholic University. Author of Good and '
            'Evil, A Common Humanity and the memoir Romulus, My Father; a '
            'contributor to Quadrant.'
        ),
        evidence=(
            "Identification inferred: 'R. Gaita' writing a 1991 memorial of "
            'Oakeshott in the Australian magazine Quadrant matches Raimond '
            "Gaita (then at King's College London, a Quadrant contributor), but"
            ' no source directly attributes this piece to him.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Raimond_Gaita',
            affiliation='https://en.wikipedia.org/wiki/Raimond_Gaita',
            descr='https://en.wikipedia.org/wiki/Raimond_Gaita',
        ),
        works=[
            'author: In Memoriam: Michael Oakeshott, 1901 – 1990 (1991) — Quadrant',
        ],),
    ('Harvey', 'A.', 'D.'): dict(
        candidate='Arnold David Harvey',
        confidence='medium',
        yob=1947,
        descr=(
            'English historian, novelist and essayist, educated at Oxford and '
            'Cambridge, who has taught at Cambridge, Salerno, La Reunion and '
            'Leipzig and edited the Salisbury Review (2000-02). He writes '
            'widely in British periodicals on history and politics; books '
            'include Collision of Empires and Body Politic: Political Metaphor '
            'and Political Violence.'
        ),
        evidence=(
            'Medium confidence. No source directly ties the 2004 Contemporary '
            'Review piece to Arnold D. Harvey, but he fits on topic, journal, '
            'country and era: a British historian and essayist and former '
            'editor of the conservative Salisbury Review (2000-02) who writes '
            'widely on politics in British general periodicals. LoC: Arnold '
            'David Harvey, b. 7 Oct 1947. No current institutional post, so '
            'affiliation blank.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n77008507',
            descr='https://en.wikipedia.org/wiki/A._D._Harvey',
        ),
        works=[
            'author: Michael Oakeshott: Rationalism and Self-Serving in Politics (2004) — Contemporary Review',
        ],),
    ('Havard', 'W.', 'C.'): dict(
        candidate='W. C. Havard',
        confidence='medium',
        affiliation='Vanderbilt University',
        yob=1923,
        yod=2002,
        descr=(
            'American political scientist (William C. Havard Jr.) who chaired '
            'the political science department at Vanderbilt University, where '
            'he became Harvey Branscomb Distinguished Professor. He edited The '
            'Journal of Politics, led the Southern Political Science '
            'Association, and wrote on political philosophy, literature and '
            'politics, and Southern politics.'
        ),
        evidence=(
            'Identified as William C. Havard Jr., a political philosopher of '
            'the right era (Voegelin scholar) who wrote on Oakeshott; no direct'
            ' source tying the 1974 Oakeshott essay to him was fetched. Birth '
            'year 1923 from VIAF heading seen via search snippet (VIAF not '
            'directly reachable); death 2002 from Vanderbilt bio.'
        ),
        sources=dict(
            yob='https://viaf.org/viaf/68942084',
            yod='https://as.vanderbilt.edu/political-science/bio/william-havard',
            affiliation='https://as.vanderbilt.edu/political-science/bio/william-havard',
            descr='https://as.vanderbilt.edu/political-science/bio/william-havard',
        ),
        works=[
            'author: Michael Oakeshott (1974)',
        ],),
    ('Holliday', 'I.', ''): dict(
        candidate='Ian Holliday',
        confidence='medium',
        affiliation='University of Hong Kong',
        descr=(
            'British political scientist trained at Cambridge and Oxford who '
            'taught in the Department of Government at the University of '
            'Manchester (1990-99) before moving to Hong Kong, where he became a'
            ' dean and later vice-president at the University of Hong Kong. His'
            ' later research centres on Myanmar, including Burma Redux (2011).'
        ),
        evidence=(
            'Cambridge Core confirms the 1992 Government and Opposition article'
            ' (27:2, pp.131-147) is by Ian Holliday '
            '(https://cambridge.org/core/journals/government-and-'
            'opposition/article/on-michael-'
            'oakeshott1/988E5D94856B908CFF865D12D6506704). Matching him to the '
            'HKU Ian Holliday (then a young lecturer at Manchester) is inferred'
            ' from era and field; affiliation footnote not seen.'
        ),
        sources=dict(
            affiliation='https://en.wikipedia.org/wiki/Ian_Holliday',
            descr='https://en.wikipedia.org/wiki/Ian_Holliday',
        ),
        works=[
            'author: On Michael Oakeshott (1992) — Government and Opposition',
        ],),
    ('Jacobs', 'Michael', 'N.'): dict(
        candidate='Michael N. Jacobs',
        confidence='medium',
        affiliation='Wright State University',
        descr=(
            'American political scientist and deputy director of civics at the '
            'Center for Civics, Culture, and Workforce Development at Wright '
            'State University in Ohio, previously associate professor of '
            'political science at the University of Mary Hardin-Baylor. His '
            'research covers international trade disputes, investment treaties '
            'and Two Kingdoms political theology.'
        ),
        evidence=(
            'Exact name match (with middle initial) and research on Two '
            'Kingdoms political theology fit a 2025 Oakeshottian critique of '
            "Stephen Wolfe's Christian nationalism, but no source directly ties"
            ' him to the Cosmos + Taxis article. UMHB affiliation from European'
            ' Conservative author page '
            '(https://europeanconservative.com/articles/author/michael-n-'
            'jacobs); Providence (2025) gives Wright State, treated as current.'
        ),
        sources=dict(
            affiliation='https://providencemag.com/authors/michael-n-jacobs/',
            descr='https://providencemag.com/authors/michael-n-jacobs/',
        ),
        works=[
            "author: An Oakeshottian Analysis of Stephen Wolfe's Christian Nationalism: Civil Associations vs. The Complete Good (2025) — Cosmos + Taxis",
        ],),
    ('Knepper', 'P.', ''): dict(
        candidate='P. Knepper',
        confidence='medium',
        affiliation='University of Sheffield',
        descr=(
            'Criminologist (Paul Knepper), Professor of Criminology in the '
            'School of Law at the University of Sheffield, who writes on '
            'criminological theory, social policy, crime prevention and the '
            'history of international crime; he draws on Oakeshott in his book '
            'Explaining Criminal Conduct.'
        ),
        evidence=(
            'Identified as Paul Knepper from criminology topic and his use of '
            'Oakeshott in Explaining Criminal Conduct (2001); article itself '
            'not directly linked.'
        ),
        sources=dict(
            affiliation='https://theportobellobookshop.com/contributed-by/paul-knepper',
            descr='https://uk.sagepub.com/en-gb/eur/criminology-and-social-policy/book229363',
        ),
        works=[
            'author: Oakeshott and the New Crime Prevention (2003) — Australian and New Zealand Journal of Criminology',
        ],),
    ('Lawn', 'C.', ''): dict(
        candidate='Chris Lawn',
        confidence='medium',
        descr=(
            'Philosopher working in hermeneutics, author of Wittgenstein and '
            'Gadamer (2004). He wrote a comparison of Gadamer and Oakeshott on '
            'self-understanding and education.'
        ),
        evidence=(
            'Chris Lawn (LoC n2004102881, Wittgenstein and Gadamer). The topic '
            'fits the 1996 Gadamer/Oakeshott article, but no affiliation was '
            'sourced (believed to be Mary Immaculate College, Limerick) because'
            ' the search budget ran out.'
        ),
        sources=dict(
            descr='http://id.loc.gov/authorities/names/n2004102881',
        ),
        works=[
            'author: Adventures of Self-Understanding: Gadamer, Oakeshott and the Question of Education (1996) — Journal of the British Society for Phenomenology',
        ],),
    ('Lopez', 'F.', ''): dict(
        candidate='Francisco Lopez',
        confidence='low',
        evidence=(
            'PhilArchive/PhilPapers lists the author of the 2006 CBIS '
            "introduction (12(2):5-15) as 'Francisco Lopez'. Possibly Francisco"
            " Javier López Atanes, Spanish translator/editor of Oakeshott's "
            'Lectures in the History of Political Thought '
            '(https://www.marcialpons.es/libros/lecciones-de-historia-del-'
            'pensamiento-politico/9788472095670/), but no source links the two,'
            ' and no affiliation or biography found. Left blank.'
        ),
        works=[
            "author: Introduction to Oakeshott's “The Concept of Government in Modern Europe” (2006) — Collingwood and British Idealism Studies",
        ],),
    ('Manning', 'D.', 'J.'): dict(
        candidate='David John Manning',
        confidence='medium',
        affiliation='Durham University',
        descr=(
            'British political theorist who was a lecturer and later senior '
            'lecturer in politics at the University of Durham, and later a '
            'visiting professor at the University of Texas at Austin. His books'
            ' include The Mind of Jeremy Bentham and work on professional '
            "business ethics; he wrote early appraisals of Oakeshott's "
            'contribution to political thought.'
        ),
        evidence=(
            'D. J. (David John) Manning per LoC. The match to the 1965-66 '
            'Oakeshott pieces (Clare Market Review is an LSE student journal) '
            'rests on name and field only. Birth year unknown (LoC 046 gives '
            "only '19')."
        ),
        sources=dict(
            affiliation='http://id.loc.gov/authorities/names/n82268192',
            descr='http://id.loc.gov/authorities/names/n82268192',
        ),
        works=[
            "author: Professor Michael Oakeshott's Contribution to Political Thought (1965) — Clare Market Review",
            "author: Michael Oakeshott's Contribution to Political Thought (1966) — Kolokon",
        ],),
    ('Mewes', 'H.', ''): dict(
        candidate='Horst Mewes',
        confidence='medium',
        descr=(
            "Political theorist who wrote on Kant's theory and practice, Hannah"
            " Arendt's political humanism and the American political system (in"
            ' German), and contributed to a volume on Hannah Arendt and Leo '
            'Strauss.'
        ),
        evidence=(
            'Identified as Horst Mewes from his Arendt/Strauss publications, '
            "which match the 1992 article's subject. Believed to have taught at"
            ' the University of Colorado Boulder, but could not verify this '
            '(web search budget exhausted), so affiliation left blank. No dates'
            ' found.'
        ),
        sources=dict(
            descr='https://openlibrary.org/authors/OL698846A/works.json',
        ),
        works=[
            'author: Individualism in Oakeshott, Arendt and Strauss (1992) — Political Science Reviewer',
        ],),
    ('Oldfield', 'A.', ''): dict(
        candidate='Adrian Oldfield',
        confidence='medium',
        yob=1939,
        descr=(
            'Political theorist whose books include Citizenship and Community, '
            'Hobbes and Sociability, Ordered Cities, Ordered Souls, and a study'
            " of metaphysics and history in Collingwood's thought."
        ),
        evidence=(
            'Identified as Adrian Oldfield (b. 1939 per Open Library) from his '
            'work on Hobbes and Collingwood, which fits a 1983 essay on '
            'Oakeshott; not directly confirmed. Institution (possibly '
            'University of Salford) not verified - web search budget exhausted.'
        ),
        sources=dict(
            yob='https://openlibrary.org/authors/OL889911A',
            descr='https://openlibrary.org/authors/OL889911A/works.json',
        ),
        works=[
            'author: Michael Oakeshott (1983)',
        ],),
    ('Ornaghi', 'L.', ''): dict(
        candidate='Lorenzo Ornaghi',
        confidence='medium',
        affiliation='Università Cattolica del Sacro Cuore',
        yob=1948,
        descr=(
            'Italian political scientist, a pupil of Gianfranco Miglio, who '
            'became full professor of political science at the Università '
            'Cattolica del Sacro Cuore in Milan and served as its rector from '
            "2002 to 2012. He was Italy's Minister for Cultural Heritage and "
            'Activities in the Monti government (2011-13).'
        ),
        evidence=(
            "'L. Ornaghi', a 1979 Italian political-science essay on Oakeshott "
            'and the modern state, fits Lorenzo Ornaghi (Cattolica political '
            'scientist, Miglio school) in era and field, but no source directly'
            ' attributes the article to him.'
        ),
        sources=dict(
            yob='https://ipfs.ssi.eecc.de/ipns/en.wikipedia-on-ipfs.org/wiki/Lorenzo_Ornaghi',
            affiliation='https://ipfs.ssi.eecc.de/ipns/en.wikipedia-on-ipfs.org/wiki/Lorenzo_Ornaghi',
            descr='https://cultura.gov.it/comunicato/lorenzo-ornaghi-nuovo-ministro-per-i-beni-e-le-attivita-culturali',
        ),
        works=[
            "author: Dall' “Ambivalenza” dello Stato Moderno all'Analisi della Condotta Umana: Michael Oakeshott e la Ricerca Politica Contemporanea (1979) — Annali dell'Istituto Storico Italo-Germanico in Trento",
        ],),
    ('Radner', 'Isaac', ''): dict(
        candidate='Isaac Radner',
        confidence='low',
        descr=(
            'Writer on liberal education who guest-edited a 2025 Cosmos + Taxis'
            ' issue on liberal education, contributing an editorial '
            "introduction and the essay 'The Meaning of Plurality in Liberal "
            "Education', which draws on Aristotle and Oakeshott."
        ),
        evidence=(
            'Identity certain only as the author/guest editor in Cosmos + Taxis'
            ' 13:3+4 (2025). Affiliation could not be extracted from the PDF '
            'and the web-search budget was exhausted, so no other biographical '
            'data.'
        ),
        sources=dict(
            descr='https://cosmosandtaxis.org/wp-content/uploads/2025/03/Radner_Intro_CT_Vol13_Iss_3_4.pdf',
        ),
        works=[
            'author: The Meaning of Plurality in Liberal Education (2025) — Cosmos + Taxis',
        ],),
    ('Rueda', 'Beckett', ''): dict(
        candidate='Beckett Rueda',
        confidence='low',
        affiliation='University of Texas at Austin',
        descr=(
            'Author of an essay in Cosmos + Taxis (2022) asking why Oakeshott '
            "praised John Rawls's early theory of justice in 1965 but dismissed"
            " its later form in 1983, and arguing that Oakeshott's view of "
            'ideology was more complex than usually presented.'
        ),
        evidence=(
            'Only source is a self-maintained academia.edu profile under the '
            'utexas subdomain carrying the same article abstract; rank/status '
            '(likely student) and current affiliation unconfirmed.'
        ),
        sources=dict(
            affiliation='https://utexas.academia.edu/BeckettRueda',
            descr='https://utexas.academia.edu/BeckettRueda',
        ),
        works=[
            'author: Rationalism in Ideal Theory: Michael Oakeshott on John Rawls (2022) — Cosmos + Taxis',
        ],),
    ('Varma', 'V.', 'P.'): dict(
        candidate='Vishwanath Prasad Varma',
        confidence='medium',
        yob=1924,
        descr=(
            'Indian political scientist and prolific author on political '
            'philosophy, Hindu and modern Indian political thought, Gandhi, '
            'Aurobindo and Tilak, and Bihar elections, writing in English and '
            'Hindi, including a Hindi history of Western political thought.'
        ),
        evidence=(
            'V. P. Varma writing in the Indian Journal of Political Science '
            '(1975) taken to be Vishwanath Prasad Varma (b. 1924), the prolific'
            ' Indian writer on political thought; not directly confirmed. '
            'Believed to be at Patna University but unverified, so affiliation '
            'blank.'
        ),
        sources=dict(
            yob='https://www.wikidata.org/wiki/Q112663537',
            descr='https://openlibrary.org/authors/OL47A/works.json',
        ),
        works=[
            'author: Michael Oakeshott as a Political Philosopher (1975) — Indian Journal of Political Science',
        ],),
    ('Wood', 'N.', ''): dict(
        candidate='Neal Wood',
        confidence='medium',
        affiliation='York University',
        yob=1922,
        yod=2003,
        descr=(
            'American-born political theorist who taught at Columbia and UCLA '
            'before holding a chair in political science at York University, '
            'Toronto (1966-88). He wrote Communism and British Intellectuals '
            "(1959), The Politics of Locke's Philosophy and other studies in "
            'the social history of political thought.'
        ),
        evidence=(
            'Identification inferred: Neal Wood was a political theorist at '
            'Columbia in 1959 whose first book dealt with British '
            'intellectuals, fitting a 1959 Journal of Politics essay on '
            'Oakeshott; no source directly confirms he wrote it.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Neal_Wood',
            yod='https://en.wikipedia.org/wiki/Neal_Wood',
            affiliation='https://en.wikipedia.org/wiki/Neal_Wood',
            descr='https://en.wikipedia.org/wiki/Neal_Wood',
        ),
        works=[
            'author: A Guide to the Classics: The Skepticism of Professor Oakeshott (1959) — Journal of Politics',
        ],),
    ('Woodings', 'R.', 'B.'): dict(
        candidate='R. B. Woodings',
        confidence='low',
        evidence=(
            'Co-editor with Alan Bullock of The Fontana Biographical Companion '
            'to Modern Thought (1983). Could not find biographical information '
            '(full name, dates, affiliation) before the web search budget ran '
            'out; left blank.'
        ),
        works=[
            'editor: The Fontana Biographical Companion to Modern Thought (1983) — Fontana',
        ],),
    ('Ardley', 'G.', ''): dict(
        candidate='Gavin Ardley',
        confidence='medium',
        affiliation='University of Auckland',
        yob=1915,
        yod=1992,
        descr=(
            'Australian-born philosopher and physicist, author of Aquinas '
            'and Kant (1950), who taught for 25 years in the philosophy '
            'department of the University of Auckland, retiring in 1981.'
        ),
        evidence=(
            'A Catholic/Thomist philosopher with matching initial, active '
            'in 1980, fits a review in the Dublin Philosophical Studies; '
            'dates from a library record '
            '(find.library.upenn.edu/catalog/999574453503681) and an '
            'obituary reproduced at brightmorningstar-amaic.blogspot.com/20'
            '18/04/gavin-ardleys-obituary.html. Nothing directly ties him '
            'to the review.'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1980) [Book Reviews '
                'of Books by Oakeshott] — Philosophical Studies (Dublin)'
            ),
        ],
    ),
    ('Bacon', 'M.', ''): dict(
        candidate='Michael Bacon',
        confidence='medium',
        affiliation='Royal Holloway, University of London',
        descr=(
            'British political theorist, Senior Lecturer at Royal Holloway,'
            ' author of Richard Rorty: Pragmatism and Political Liberalism '
            '(2007) and Pragmatism: An Introduction (2012).'
        ),
        evidence=(
            'Political theorist active in the early 2000s reviewing in '
            'Political Studies Review fits; source '
            'pure.royalholloway.ac.uk/en/persons/michael-bacon. No listing '
            'of this specific review found.'
        ),
        works=[
            (
                'author: A Review of The Philosophy of Michael Oakeshott '
                '(2003) [Book Reviews of Books About Oakeshott] — Political'
                ' Studies Review'
            ),
        ],
    ),
    ('Carr', 'D.', ''): dict(
        candidate='David Carr',
        confidence='medium',
        descr=(
            'British philosopher of education who published regularly in '
            'the Journal of Philosophy of Education.'
        ),
        evidence=(
            'David Carr is a prolific contributor to the Journal of '
            'Philosophy of Education (philarchive.org/rec/CAREPA); the '
            'review was not found in any listing, and Carr is a common '
            'surname.'
        ),
        works=[
            (
                'author: A Review of Education and the Voice of Michael '
                'Oakeshott (2008) [Book Reviews of Books About Oakeshott] —'
                ' Journal of Philosophy of Education'
            ),
        ],
    ),
    ('Bailey', 'C.', ''): dict(
        candidate='Charles Bailey',
        confidence='medium',
        yob=1924,
        descr=(
            'British philosopher of education, author of Beyond the Present'
            ' and the Particular: A Theory of Liberal Education (1984).'
        ),
        evidence=(
            'A liberal-education theorist is a natural reviewer of The '
            'Voice of Liberal Learning; birth year from a catalogue record '
            '(ci.nii.ac.jp/ncid/BA0033184X). The review itself was not '
            'found.'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1990) [Book Reviews of Books by '
                'Oakeshott] — Cambridge Journal of Education'
            ),
        ],
    ),
    ('Christian', 'W.', ''): dict(
        candidate='William Christian',
        confidence='medium',
        affiliation='University of Guelph',
        yob=1945,
        descr=(
            'Canadian political scientist at the University of Guelph '
            '(retired 2008), with a PhD from the London School of '
            'Economics, known for work on Canadian political thought and a '
            'biography of George Grant.'
        ),
        evidence=(
            'LSE-trained political theorist active in the 1990s; source htt'
            'ps://en.wikipedia.org/wiki/William_Christian_(political_scient'
            'ist). The reviews themselves were not located to confirm '
            'authorship.'
        ),
        works=[
            (
                'author: A Review of Morality and Politics in Modern '
                'Europe: The Harvard Lectures (1995) [Book Reviews of Books'
                ' by Oakeshott] — Review of Politics'
            ),
            (
                'author: A Review of The Politics of Faith and the Politics'
                ' of Scepticism (1997) [Book Reviews of Books by Oakeshott]'
                ' — Perspectives on Political Science'
            ),
        ],
    ),
    ('Bloomfield', 'P.', ''): dict(
        candidate='Paul Bloomfield',
        confidence='medium',
        yob=1898,
        descr=(
            'British writer, author of Imaginary Worlds, or the Evolution '
            'of Utopia (1932).'
        ),
        evidence=(
            'A British author Paul Bloomfield (b. 1898; '
            'search.ub.tum.de/vufind/Record/DE-604.BV026250597) was active '
            'in this period, but no source tying him to Uncommon People '
            '(1955) was found.'
        ),
        works=[
            (
                'reviewee: Review of P. Bloomfield, Uncommon People (1955) '
                '[Book Reviews by Oakeshott] — Spectator'
            ),
        ],
    ),
    ('Abbate', 'F.', 'J.'): dict(
        candidate='Fred J. Abbate',
        confidence='low',
        descr=(
            'American philosopher, compiler of the textbook The Philosophic'
            ' Impulse (Wadsworth, 1972).'
        ),
        evidence=(
            'Only a philosopher of matching initials active in the 1970s '
            '(opac.ucu.edu.ua/bib/237221); no link to Metaphilosophy found.'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1978) [Book Reviews '
                'of Books by Oakeshott] — Metaphilosophy'
            ),
        ],
    ),
    ('Clark', 'L.', ''): dict(
        candidate='Leonard Clark',
        confidence='low',
        yob=1905,
        yod=1981,
        descr=(
            'English poet, writer, editor and educator associated with the '
            'Forest of Dean.'
        ),
        evidence=(
            'A poet reviewing The Voice of Poetry in Time and Tide (1960) '
            'is plausible '
            '(https://en.wikipedia.org/wiki/Leonard_Clark_(poet)), but '
            'Clark is a common surname and nothing ties him to the review.'
        ),
        works=[
            (
                'author: A Review of The Voice of Poetry in the '
                'Conversation of Mankind: An Essay (1960) [Book Reviews of '
                'Books by Oakeshott] — Time and Tide'
            ),
        ],
    ),
    ('Bernard-Maitre', 'H.', ''): dict(
        candidate='Henri Bernard-Maître',
        confidence='medium',
        affiliation='Institut catholique de Paris',
        yob=1889,
        yod=1975,
        descr=(
            'French Jesuit missionary, historian and sinologist who taught '
            'in Tianjin and Shanghai and, after returning to France in '
            '1947, founded an institute of religious ethnology at the '
            'Institut catholique de Paris.'
        ),
        evidence=(
            'The rare hyphenated surname with initial H. strongly suggests '
            'him (sources: e-aoi.uzh.ch/apps/china-west/chronologies/5397; '
            'angkordatabase.asia/authors/henri-bernard), but no source '
            'confirms that he reviewed for Erasmus, and political theory '
            'lies outside his field.'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1965) [Book Reviews of Books by Oakeshott] — '
                'Erasmus'
            ),
        ],
    ),
    ('Congdon', 'T.', ''): dict(
        candidate='Tim Congdon',
        confidence='low',
        yob=1951,
        descr='Timothy George Congdon, British economist (b. 1951).',
        evidence=(
            'Tim Congdon is a British economist who writes for '
            'conservative-leaning periodicals, but no source was found '
            "linking him to a 2005 TLS review of Franco's Michael "
            'Oakeshott: An Introduction. Source: '
            'https://en.wikipedia.org/wiki/Tim_Congdon'
        ),
        works=[
            (
                'author: A Review of Michael Oakeshott: An Introduction '
                '(2005) [Book Reviews of Books About Oakeshott] — Times '
                'Literary Supplement'
            ),
        ],
    ),
    ('Dunn', 'J.', ''): dict(
        candidate='John Dunn',
        confidence='medium',
        yob=1940,
        affiliation="King's College, Cambridge",
        descr=(
            'John Montfort Dunn, British political theorist and emeritus '
            "professor of political theory at King's College, Cambridge."
        ),
        evidence=(
            'A 1985 review of On History in the journal History fits the '
            'Cambridge historian of political thought John Dunn, but "J. '
            'Dunn" is common and no citation with full name was found. '
            'Source: '
            'https://en.wikipedia.org/wiki/John_Dunn_(political_theorist)'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1985) '
                '[Book Reviews of Books by Oakeshott] — History'
            ),
        ],
    ),
    ('Duncan', 'G.', 'C.'): dict(
        candidate='Graeme Duncan',
        confidence='medium',
        yob=1936,
        affiliation='University of East Anglia',
        descr=(
            'Australian-born political theorist (b. Bairnsdale 1936, Oxford'
            ' DPhil), Professor of Politics at the University of East '
            'Anglia, author of Marx and Mill (1973).'
        ),
        evidence=(
            'An Australian political theorist reviewing Rationalism in '
            'Politics in the Australasian Journal of Philosophy (1963) fits'
            ' Graeme Duncan, but his middle initial "C." was not confirmed.'
            ' Sources: https://www.wob.com/en-au/books/graeme-duncan-univer'
            'sity-of-ea/marx-and-mill/9780521202572 ; '
            'https://nias.knaw.nl/?p=6291'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1963) [Book Reviews of Books by Oakeshott] — '
                'Australasian Journal of Philosophy'
            ),
        ],
    ),
    ('Gass', 'O.', ''): dict(
        candidate='Oscar Gass',
        confidence='medium',
        descr=(
            'American economist and political commentator who wrote '
            'Washington commentary for Commentary in the 1960s.'
        ),
        evidence=(
            'Oscar Gass was an economist-essayist active in US liberal '
            'periodicals in the 1960s; the 1963 New Republic piece '
            '"Politics of Dead Center" fits him but no source directly '
            'confirms authorship; no dates found. Source: https://econbiz.d'
            'e/Record/the-political-economy-of-the-great-society-a-washingt'
            'on-commentary-gass-oscar/10002415152'
        ),
        works=[
            (
                'author: Politics of Dead Center (1963) [Book Reviews of '
                'Books by Oakeshott] — New Republic'
            ),
        ],
    ),
    ('Goodman', 'C.', 'P.'): dict(
        candidate='Chris Goodman',
        confidence='medium',
        evidence=(
            'The Polanyi Society table of contents for Tradition & '
            'Discovery 46:3 (Oct 2020), pp. 31-37, lists the review as by '
            'Chris Goodman, but no biographical information about him was '
            'found. Source: https://polanyisociety.org/TAD%20WEB%20ARCHIVE/'
            'TAD46-3/TAD46-3-basic-pg.html'
        ),
        works=[
            (
                'author: A Review of Tradition v. Rationalism: Voegelin, '
                'Oakeshott, Hayek, and Others (2020) [Book Reviews of Books'
                ' About Oakeshott] — Tradition and Discovery'
            ),
        ],
    ),
    ('Madge', 'C.', ''): dict(
        candidate='Charles Madge',
        confidence='medium',
        affiliation='University of Birmingham',
        yob=1912,
        yod=1996,
        url='https://en.wikipedia.org/wiki/Charles_Madge',
        descr=(
            'English poet, journalist and sociologist, co-founder of '
            'Mass-Observation and first Professor of Sociology at the '
            'University of Birmingham (1950-1970).'
        ),
        evidence=(
            'A poet with initials C. Madge active in 1960 fits a Modern '
            'Language Review notice of The Voice of Poetry, but no source '
            'attributes the review to him. Source: '
            'https://en.wikipedia.org/wiki/Charles_Madge'
        ),
        works=[
            (
                'author: A Review of The Voice of Poetry in the '
                'Conversation of Mankind: An Essay (1960) [Book Reviews of '
                'Books by Oakeshott] — Modern Language Review'
            ),
        ],
    ),
    ('Marquand', 'D.', ''): dict(
        candidate='David Marquand',
        confidence='medium',
        affiliation='University of Oxford',
        yob=1934,
        yod=2024,
        url='https://en.wikipedia.org/wiki/David_Marquand',
        descr=(
            'British political scientist, journalist and Labour MP, later '
            'professor at Salford and Sheffield and Principal of Mansfield '
            'College, Oxford.'
        ),
        evidence=(
            'Wrote political journalism for left-of-centre papers around '
            '1962, when the New Statesman review of Rationalism in Politics'
            ' appeared; no source found tying him to that review. Source: '
            'https://en.wikipedia.org/wiki/David_Marquand'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1962) [Book Reviews of Books by Oakeshott] — New '
                'Statesman and Nation'
            ),
        ],
    ),
    ('Kuhn', 'H.', ''): dict(
        candidate='Helmut Kuhn',
        confidence='medium',
        yob=1899,
        yod=1991,
        affiliation='University of Munich',
        descr=(
            'German philosopher who taught in the USA (1938-1949), then at '
            'Erlangen and Munich, writing on Greek and political philosophy'
            ' and co-editing the Philosophische Rundschau.'
        ),
        evidence=(
            'Leading German political philosopher in 1963 with matching '
            'initial, plausible reviewer for the Zeitschrift für Politik; '
            'not confirmed. Sources: '
            'https://www.wissen.de/lexikon/kuhn-helmut , '
            'https://relbib.de/Authority/079506577'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1963) [Book Reviews of Books by Oakeshott] — '
                'Zeitschrift für Politik'
            ),
        ],
    ),
    ('McPherson', 'T.', ''): dict(
        candidate='Thomas McPherson',
        confidence='medium',
        descr=(
            'British philosopher, author of Political Obligation '
            '(Routledge, 1967).'
        ),
        evidence=(
            'Author of Political Obligation (1967), same year as the '
            "Political Studies review of Greenleaf's Oakeshott's "
            'Philosophical Politics; also co-reviewed in Philosophical '
            'Quarterly 1968. No source ties him to the review; affiliation '
            '(possibly Cardiff) unconfirmed. Source: '
            'https://cir.nii.ac.jp/crid/1130000794298855296'
        ),
        works=[
            (
                "author: A Review of Oakeshott's Philosophical Politics "
                '(1967) [Book Reviews of Books About Oakeshott] — Political'
                ' Studies'
            ),
        ],
    ),
    ('Merrill', 'T.', 'W.'): dict(
        candidate='Thomas W. Merrill',
        confidence='medium',
        affiliation='American University',
        url='https://wwwprod103.american.edu/spa/faculty/merrill.cfm',
        descr=(
            "American political theorist at American University's School of"
            ' Public Affairs, author of Hume and the Politics of '
            'Enlightenment (2015).'
        ),
        evidence=(
            'Political theorist with exact initials active in the 2000s; '
            "review of Franco's Michael Oakeshott: An Introduction in "
            'Society (2005) not confirmed as his. Source: '
            'https://wwwprod103.american.edu/spa/faculty/merrill.cfm'
        ),
        works=[
            (
                'author: A Review of Michael Oakeshott: An Introduction '
                '(2005) [Book Reviews of Books About Oakeshott] — Society'
            ),
        ],
    ),
    ('Maclure', 'J.', 'S.'): dict(
        candidate='Stuart Maclure (John Stuart Maclure)',
        confidence='medium',
        affiliation='Times Educational Supplement',
        yob=1926,
        yod=2011,
        descr=(
            'British education journalist, editor of the Times Educational '
            'Supplement from 1969 to 1989.'
        ),
        evidence=(
            'Documents of Modern Political Thought (CUP, 1957) was edited '
            'by T. E. Utley and "J. Stuart Maclure" '
            '(https://cmu.marmot.org/Record/.b12910600); the TES editor '
            'Stuart Maclure (1926-2011, '
            'https://www.tes.com/news/obituary-stuart-maclure-1926-2011) is'
            ' very likely the same man, but no source found explicitly '
            'linking him to the anthology.'
        ),
        works=[
            (
                'reviewee: Review of T.E. Utley and J.S. Maclure, Documents'
                ' of Modern Political Thought (1958) [Book Reviews by '
                'Oakeshott] — Crossbow'
            ),
        ],
    ),
    ('Katzoff', 'C.', ''): dict(
        candidate='Charlotte Katzoff',
        confidence='medium',
        affiliation='Bar-Ilan University',
        url='https://philosophy.biu.ac.il/CharlotteKatzoff',
        descr=(
            'Philosopher in the Department of Philosophy at Bar-Ilan '
            'University, with a 1971 Columbia PhD in philosophy.'
        ),
        evidence=(
            'PhilPapers record id KATOAT-2 '
            '(https://api.philpapers.org/rec/KATOAT-2) appears to be '
            '"Oakeshott and the..." by Katzoff, on Oakeshott\'s view of '
            'political knowledge as practical; Charlotte Katzoff is the '
            'only philosopher of that surname found. First name not '
            'confirmed on the article itself.'
        ),
        works=[
            (
                'author: Oakeshott and the Practice of Politics (1992) '
                '[Short Works About Oakeshott] — Journal of Philosophical '
                'Research'
            ),
        ],
    ),
    ('MacDonald', 'H.', 'M.'): dict(
        candidate='H. Malcolm Macdonald',
        confidence='low',
        yob=1914,
        affiliation='University of Texas at Austin',
        descr=(
            'American political scientist in the Department of Government, '
            'University of Texas.'
        ),
        evidence=(
            'Social Science Quarterly is published from Texas; a University'
            ' of Texas government scholar H. Malcolm MacDonald (b. 1914) is'
            ' catalogued '
            '(https://libcat.library.tamu.edu/Record/in00000065565), but he'
            ' would have been about 78 in 1992 and nothing ties him to the '
            'review.'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays: New and Expanded Edition (1992) [Book Reviews of '
                'Books by Oakeshott] — Social Science Quarterly'
            ),
        ],
    ),
    ('Madigan', 'P.', ''): dict(
        candidate='Patrick Madigan SJ',
        confidence='medium',
        affiliation='Heythrop College',
        descr=(
            'Jesuit philosopher, long-time editor and book reviews editor '
            'of The Heythrop Journal.'
        ),
        evidence=(
            'As Heythrop Journal editor he regularly reviewed philosophy '
            'books there, matching the 2006 review of The Philosophy of '
            'Michael Oakeshott; not confirmed. Sources: '
            'https://en.wikipedia.org/wiki/The_Heythrop_Journal , https://w'
            'ww.dcu.ie/theologyphilosophymusic/news/2016/04/seminar-on-theo'
            'logy-and-literature'
        ),
        works=[
            (
                'author: A Review of The Philosophy of Michael Oakeshott '
                '(2006) [Book Reviews of Books About Oakeshott] — Heythrop '
                'Journal'
            ),
        ],
    ),
    ('Johnson', 'P.', ''): dict(
        candidate='Peter Johnson',
        confidence='low',
        evidence=(
            'RePEc lists a Peter Johnson as a Utilitas reviewer in 1994 (ht'
            'tps://econpapers.repec.org/RePEc:cup:utilit:v:6:y:1994:i:01:p:'
            '147-149_00), suggesting the first name; the 1992 Utilitas '
            'review was a joint review of Fuller (ed.) The Voice of Liberal'
            ' Learning and Franco, The Political Philosophy of Michael '
            'Oakeshott. Possibly the British philosopher Peter Johnson who '
            'wrote on Collingwood, but no affiliation or identity '
            'confirmed.'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1992) [Book Reviews of Books by '
                'Oakeshott] — Utilitas'
            ),
            (
                'author: A Review of The Political Philosophy of Michael '
                'Oakeshott (1992) [Book Reviews of Books About Oakeshott] —'
                ' Utilitas'
            ),
        ],
    ),
    ('Parry', 'G.', ''): dict(
        candidate='Geraint Parry',
        confidence='medium',
        affiliation='University of Manchester',
        descr=(
            'Geraint Parry is a British political theorist, W. J. M. '
            'Mackenzie Professor (now emeritus) of Government at the '
            'University of Manchester, who writes on democratic theory, '
            'political participation and the history of political ideas, '
            'including a book on Locke.'
        ),
        evidence=(
            'Most prominent British political theorist "G. Parry" active in'
            ' 1976 and wrote on political thought, but no source ties him '
            'to the Bibliographie de la Philosophie review of On Human '
            'Conduct. Source: https://origin-www.alibris.co.uk/search/books'
            '/author/Geraint-Parry'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1976) [Book Reviews '
                'of Books by Oakeshott] — Bibliographie de la Philosophie'
            ),
        ],
    ),
    ('Rees', 'J.', 'C.'): dict(
        candidate='John C. Rees',
        confidence='medium',
        evidence=(
            'Library records give the author of "Professor Oakeshott on '
            'Political Education" (Mind 62, 1953, 68-74) as "Rees, John C."'
            ' (https://ibl.kb.nl/article/0000000080133/LXIX/245/6, '
            'https://dc2.philarchive.org/rec/REEPOO). Probably the '
            'political theorist J. C. Rees, author of Mill and His Early '
            'Critics (1956) and later at Swansea, but no source found '
            'confirming that identity, dates or affiliation.'
        ),
        works=[
            (
                'author: Professor Oakeshott on Political Education (1953) '
                '[Book Reviews of Books by Oakeshott] — Mind'
            ),
        ],
    ),
    ('Perry', 'L.', 'R.'): dict(
        candidate='Leslie R. Perry',
        confidence='medium',
        descr=(
            'British philosopher of education who published in the British '
            'Journal of Educational Studies and the Journal of Philosophy '
            'of Education in the 1960s-70s.'
        ),
        evidence=(
            'PhilPapers lists L. R. / Leslie R. Perry as an author of '
            'philosophy-of-education articles in the British Journal of '
            'Educational Studies (1965, 1975) - the same journal as the '
            '1968 review. No affiliation or dates found, and nothing '
            'directly ties him to the reviews. '
            'https://philpapers.org/s/L.%20R.%20Perry'
        ),
        works=[
            (
                'author: A Review of Experience and Its Modes (1968) [Book '
                'Reviews of Books by Oakeshott] — British Journal of '
                'Educational Studies'
            ),
            (
                'author: A Review of The Voice of Poetry in the '
                'Conversation of Mankind: An Essay (1960) [Book Reviews of '
                'Books by Oakeshott] — New Era in Home and School'
            ),
        ],
    ),
    ('Pearcey', 'N.', ''): dict(
        candidate='Nancy Pearcey',
        confidence='medium',
        yob=1952,
        descr=(
            'American evangelical author on Christian worldview and '
            'intelligent design, a fellow of the Discovery Institute.'
        ),
        evidence=(
            'Pearcey is an unusual surname and Nancy Pearcey was an active '
            'conservative/Christian writer in the 1990s, but no source '
            'found confirming she wrote the 1996 American Enterprise '
            'review. https://en.wikipedia.org/wiki/Nancy_Pearcey'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays: New and Expanded Edition (1996) [Book Reviews of '
                'Books by Oakeshott] — American Enterprise'
            ),
        ],
    ),
    ('Osbourne', 'J.', 'W.'): dict(
        candidate='John W. Osborne',
        confidence='medium',
        yob=1927,
        yod=2019,
        affiliation='Rutgers University',
        descr=(
            'American historian of Britain and Europe at Rutgers '
            'University, author of William Cobbett: His Thought and His '
            'Times (1966).'
        ),
        evidence=(
            'Name probably misspelled (Osborne). John W. Osborne was a '
            'Rutgers historian of modern Britain who wrote an essay titled '
            '"On Being Conservative" (Journal of the Rutgers University '
            'Library, 1976 - the title of an Oakeshott essay), fitting a '
            'Modern Age article on Powell and Oakeshott, but no source '
            'confirms authorship. '
            'https://en.wikipedia.org/wiki/John_W._Osborne ; https://ejbe.l'
            'ibraries.rutgers.edu/index.php/jrul/issue/view/204'
        ),
        works=[
            (
                'author: Anthony Powell and Michael Oakeshott (1985) [Short'
                ' Works About Oakeshott] — Modern Age'
            ),
        ],
    ),
    ('Price', 'R.', ''): dict(
        candidate='Russell Price',
        confidence='low',
        descr=(
            'Senior lecturer in politics at Lancaster University and '
            'translator of Machiavelli.'
        ),
        evidence=(
            'Previous pass suggested Russell Price; a further web search '
            'found no record linking anyone to "Memories of Michael '
            'Oakeshott" (Cambridge Review, 1991).'
        ),
        works=[
            (
                'author: Memories of Michael Oakeshott (1991) [Short Works '
                'About Oakeshott] — Cambridge Review'
            ),
        ],
    ),
    ('Schwartz', 'P.', ''): dict(
        candidate='Pedro Schwartz',
        confidence='low',
        yob=1935,
        descr=(
            'Spanish liberal economist and former politician who took a '
            "master's and PhD at the London School of Economics."
        ),
        evidence=(
            "Clare Market Review is the LSE students' union journal and "
            'Pedro Schwartz studied at the LSE, but his LSE degrees may '
            'date from later than 1962 and no source ties him to this '
            'review. https://en.wikipedia.org/wiki/Pedro_Schwartz'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1962) [Book Reviews of Books by Oakeshott] — Clare'
                ' Market Review'
            ),
        ],
    ),
    ('Richter', 'D.', ''): dict(
        candidate='Duncan Richter',
        confidence='low',
        evidence=(
            'Plausible match (a philosopher named Duncan Richter); no '
            "source found naming the reviewer of Nardin's The Philosophy of"
            ' Michael Oakeshott in Philosophy in Review (2002).'
        ),
        works=[
            (
                'author: A Review of The Philosophy of Michael Oakeshott '
                '(2002) [Book Reviews of Books About Oakeshott] — '
                'Philosophy in Review'
            ),
        ],
    ),
    ('Roggeveen', 'S.', ''): dict(
        candidate='Sam Roggeveen',
        confidence='low',
        evidence=(
            'Plausible match on an uncommon surname (an Australian writer '
            'on politics named Sam Roggeveen); no source found confirming '
            "the author of the 2001 AJPS review of Coats's Oakeshott and "
            'His Contemporaries.'
        ),
        works=[
            (
                'author: A Review of Oakeshott and His Contemporaries: '
                'Montaigne, St. Augustine, Hegel, et al. (2001) [Book '
                'Reviews of Books About Oakeshott] — Australian Journal of '
                'Political Science'
            ),
        ],
    ),
    ('Samples', 'J.', ''): dict(
        candidate='John Samples',
        confidence='low',
        evidence=(
            'Plausible match (an American political scientist named John '
            'Samples); no source found naming the author of the 1997 '
            'Governance review.'
        ),
        works=[
            (
                'author: A Review of The Politics of Faith and the Politics'
                ' of Scepticism (1997) [Book Reviews of Books by Oakeshott]'
                ' — Governance'
            ),
        ],
    ),
    ('Smellie', 'K.', 'B.'): dict(
        candidate='K. B. Smellie',
        confidence='medium',
        evidence=(
            'Author of Reason in Politics (Duckworth, 1939; NLI catalogue '
            'https://catalogue.nli.ie/Record/vtls000405056) and A Hundred '
            'Years of English Government; believed to be Kingsley Bryce '
            'Speakman Smellie of the LSE politics staff, but no source '
            'found confirming full name, dates or affiliation.'
        ),
        works=[
            (
                'reviewee: Review of K.B. Smellie, Reason in Politics '
                '(1939) [Book Reviews by Oakeshott] — Politica'
            ),
            (
                'reviewee: Review of K.B. Smellie, Why We Read History '
                '(1948) [Book Reviews by Oakeshott] — Cambridge Journal'
            ),
        ],
    ),
    ('Shubow', 'J.', ''): dict(
        candidate='Justin Shubow',
        confidence='medium',
        descr=(
            'Justin Shubow is an American architectural critic, president '
            'of the National Civic Art Society and former chairman of the '
            "U.S. Commission of Fine Arts; he holds a master's in "
            'philosophy from Michigan and taught philosophy there and at '
            'Yale.'
        ),
        url='https://en.wikipedia.org/wiki/Justin_Shubow',
        evidence=(
            'Writer with philosophy training active as a reviewer/editor in'
            ' the mid-2000s; no source found linking him to the 2005 Common'
            ' Review piece.'
        ),
        works=[
            (
                'author: A Review of The Political Philosophy of Michael '
                'Oakeshott (2005) [Book Reviews of Books About Oakeshott] —'
                ' Common Review'
            ),
        ],
    ),
    ('Stuttaford', 'G.', ''): dict(
        candidate='Genevieve Stuttaford',
        confidence='low',
        evidence=(
            'Recalled as a long-time Publishers Weekly nonfiction '
            'reviewer/editor, but a search found no source confirming this.'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1989) [Book Reviews of Books by '
                'Oakeshott] — Publishers Weekly'
            ),
        ],
    ),
    ('Bromwich', 'D.', ''): dict(
        candidate='David Bromwich',
        confidence='medium',
        url='https://en.wikipedia.org/wiki/David_Bromwich',
        affiliation='Yale University',
        descr=(
            'American literary scholar and critic, Sterling Professor of '
            'English at Yale, who writes on Romantic literature, Burke and '
            "politics. He reviewed Oakeshott's The Voice of Liberal "
            'Learning in the New Republic (1989).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/David_Bromwich'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1989) [Book Reviews of Books by '
                'Oakeshott] — New Republic'
            ),
        ],
    ),
    ('Armour', 'L.', ''): dict(
        candidate='Leslie Armour',
        confidence='medium',
        url='https://en.wikipedia.org/wiki/Leslie_Armour',
        affiliation='University of Ottawa',
        yob=1931,
        yod=2014,
        descr=(
            'Canadian philosopher and social economist, Emeritus Professor '
            'at the University of Ottawa and Fellow of the Royal Society of'
            ' Canada, known for histories of Canadian philosophy. He '
            'reviewed a book on Oakeshott in the British Journal for the '
            'History of Philosophy (2005).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/Leslie_Armour'
        ),
        works=[
            (
                'author: Michael Oakeshott – A Fish Too Big or Too '
                'Slippery? (2005) [Book Reviews of Books About Oakeshott] —'
                ' British Journal for the History of Philosophy'
            ),
        ],
    ),
    ('Charlton', 'B.', ''): dict(
        candidate='Bruce Charlton',
        confidence='medium',
        url='https://en.wikipedia.org/wiki/Bruce_Charlton',
        affiliation='Newcastle University',
        descr=(
            'British medical doctor and theoretical-medicine writer, Reader'
            ' in Evolutionary Psychiatry at Newcastle University and editor'
            " of Medical Hypotheses (2003-10). He reviewed Oakeshott's "
            'Morality and Politics in Modern Europe in Psychological '
            'Medicine (1995).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/Bruce_Charlton'
        ),
        works=[
            (
                'author: A Review of Morality and Politics in Modern '
                'Europe: The Harvard Lectures (1995) [Book Reviews of Books'
                ' by Oakeshott] — Psychological Medicine'
            ),
        ],
    ),
    ('Bourke', 'R.', ''): dict(
        candidate='Richard Bourke',
        confidence='medium',
        url='https://en.wikipedia.org/wiki/Richard_Bourke_(academic)',
        affiliation='University of Cambridge',
        yob=1965,
        descr=(
            'Irish historian of political thought, formerly at Queen Mary, '
            'University of London, and since 2018 Professor of the History '
            'of Political Thought at Cambridge; author of Empire and '
            "Revolution on Burke. He reviewed Efraim Podoksik's In Defence "
            'of Modernity in the European Legacy (2005).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/Richard_Bourke_(academic)'
        ),
        works=[
            (
                'author: A Review of In Defence of Modernity: Vision and '
                'Philosophy in Michael Oakeshott (2005) [Book Reviews of '
                'Books About Oakeshott] — European Legacy'
            ),
        ],
    ),
    ('Altham', 'J.', 'E. J.'): dict(
        candidate='J. E. J. Altham',
        confidence='medium',
        url='https://en.wikipedia.org/wiki/Jimmy_Altham',
        affiliation='Gonville and Caius College, Cambridge',
        yob=1944,
        descr=(
            'British philosopher (James Edward John "Jimmy" Altham), '
            'lecturer in the Cambridge philosophy faculty from the early '
            '1970s and Fellow of Gonville and Caius College, writing on '
            'logic, ethics and political philosophy. He reviewed On Human '
            'Conduct in the Cambridge Review (1975).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/Jimmy_Altham'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1975) [Book Reviews '
                'of Books by Oakeshott] — Cambridge Review'
            ),
        ],
    ),
    ('Berard', 'R.', 'N.'): dict(
        candidate='Robert Nicholas Berard',
        confidence='medium',
        affiliation='Mount Saint Vincent University',
        url=(
            'https://www.msvu.ca/academics/faculty-of-education/faculty-pro'
            'files/dr-robert-berard/'
        ),
        descr=(
            'Robert Nicholas Berard, Canadian historian of education with '
            'an MA and PhD in history from McMaster, who taught history at '
            "Dalhousie and King's College, Halifax, and education at Mount "
            'Saint Vincent University. He reviewed On History and Other '
            'Essays in two journals (1984, 1985).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: htt'
            'ps://cchahistory.ca/journal/CCHA1997/List%20of%20Contributors.'
            'htm https://www.msvu.ca/academics/faculty-of-education/faculty'
            '-profiles/dr-robert-berard/'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1985) '
                '[Book Reviews of Books by Oakeshott] — History Teacher'
            ),
            (
                'author: A Review of On History and Other Essays (1984) '
                '[Book Reviews of Books by Oakeshott] — International '
                'History Review'
            ),
        ],
    ),
    ('Edel', 'A.', ''): dict(
        candidate='Abraham Edel',
        confidence='medium',
        url='https://en.wikipedia.org/wiki/Abraham_Edel',
        yob=1908,
        yod=2007,
        affiliation='City College of New York',
        descr=(
            'American philosopher and ethicist, educated at McGill, Oxford '
            'and Columbia, who taught for many years at City College of New'
            ' York. He reviewed Morality and Politics in Modern Europe in '
            'Society (1995).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/Abraham_Edel'
        ),
        works=[
            (
                'author: A Review of Morality and Politics in Modern '
                'Europe: The Harvard Lectures (1995) [Book Reviews of Books'
                ' by Oakeshott] — Society'
            ),
        ],
    ),
    ('Emmet', 'D.', ''): dict(
        candidate='Dorothy Emmet',
        confidence='medium',
        url='https://en.wikipedia.org/wiki/Dorothy_Emmet',
        yob=1904,
        yod=2000,
        affiliation='University of Manchester',
        descr=(
            'British philosopher who headed the philosophy department at '
            'Manchester University for some twenty years and co-founded the'
            ' Epiphany Philosophers. She reviewed Rationalism in Politics '
            'in the Philosophical Quarterly (1963).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/Dorothy_Emmet'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1963) [Book Reviews of Books by Oakeshott] — '
                'Philosophical Quarterly'
            ),
        ],
    ),
    ('Gottfried', 'P.', ''): dict(
        candidate='Paul Gottfried',
        confidence='medium',
        url='https://en.wikipedia.org/wiki/Paul_Gottfried',
        yob=1941,
        affiliation='Elizabethtown College',
        descr=(
            'American paleoconservative political philosopher and '
            'intellectual historian, long a professor of humanities at '
            'Elizabethtown College. He reviewed the expanded edition of '
            'Rationalism in Politics in Modern Age (1992).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/Paul_Gottfried'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays: New and Expanded Edition (1992) [Book Reviews of '
                'Books by Oakeshott] — Modern Age'
            ),
        ],
    ),
    ('Dunstan', 'G.', 'R.'): dict(
        candidate='Gordon Reginald Dunstan',
        confidence='medium',
        affiliation="King's College London",
        yob=1917,
        yod=2004,
        url=(
            'https://history.rcplondon.ac.uk/inspiring-physicians/gordon-re'
            'ginald-dunstan'
        ),
        descr=(
            'Gordon Reginald Dunstan, Anglican priest and theological '
            'ethicist, F. D. Maurice Professor of Moral and Social Theology'
            " at King's College London and a leading figure in British "
            'medical ethics. He reviewed On Human Conduct in the Law '
            'Quarterly Review (1976).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: htt'
            'ps://archiveshub.ac.uk/search/archives/5b207522-775e-343b-abdd'
            '-cc1fdb972cd0 https://history.rcplondon.ac.uk/inspiring-physic'
            'ians/gordon-reginald-dunstan'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1976) [Book Reviews '
                'of Books by Oakeshott] — Law Quarterly Review'
            ),
        ],
    ),
    ('Franklin', 'J.', 'H.'): dict(
        candidate='Julian H. Franklin',
        confidence='medium',
        affiliation='Columbia University',
        yob=1925,
        url='https://prabook.com/web/julian_harold.franklin/1697632',
        descr=(
            'Julian H. Franklin, American historian of political thought '
            'and professor of political science at Columbia University, '
            'known for work on absolutism and constitutionalism in the '
            'sixteenth and seventeenth centuries, notably on Bodin. He '
            'reviewed Rationalism in Politics in the Journal of Philosophy '
            '(1963).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://prabook.com/web/julian_harold.franklin/1697632 '
            'https://www.routledge.com/products/9780754625452'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1963) [Book Reviews of Books by Oakeshott] — '
                'Journal of Philosophy'
            ),
        ],
    ),
    ('Esler', 'A.', ''): dict(
        candidate='Anthony James Esler',
        confidence='medium',
        affiliation='College of William & Mary',
        yob=1934,
        url=(
            'https://www.encyclopedia.com/arts/culture-magazines/esler-anth'
            'ony-james'
        ),
        descr=(
            'Anthony James Esler, American historian and novelist who '
            'taught history at the College of William & Mary (professor '
            '1972-99), author of The Human Venture and Bombs, Beards, and '
            'Barricades. He reviewed On History and Other Essays in the '
            'Social Science Journal (1985).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: htt'
            'ps://www.encyclopedia.com/arts/culture-magazines/esler-anthony'
            '-james'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1985) '
                '[Book Reviews of Books by Oakeshott] — Social Science '
                'Journal'
            ),
        ],
    ),
    ('Fahey', 'D.', 'M.'): dict(
        candidate='David M. Fahey',
        confidence='medium',
        affiliation='Miami University',
        yob=1937,
        url='https://en.wikipedia.org/wiki/David_M._Fahey',
        descr=(
            'David M. Fahey, American historian of modern Britain and of '
            'temperance movements, professor (now emeritus) at Miami '
            'University in Oxford, Ohio. He reviewed On History and Other '
            'Essays in Clio (1984).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/David_M._Fahey https://miamioh.e'
            'du/cas/academics/departments/history/emeriti-faculty/fahey/ind'
            'ex.html'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1984) '
                '[Book Reviews of Books by Oakeshott] — Clio'
            ),
        ],
    ),
    ('Eccleshall', 'R.', ''): dict(
        candidate='Robert Eccleshall',
        confidence='medium',
        affiliation="Queen's University Belfast",
        descr=(
            'Robert Eccleshall, British political theorist in the '
            "Department of Politics at Queen's University Belfast, author "
            'of English Conservatism since the Restoration and writings on '
            'conservative ideology. He reviewed On History and Other Essays'
            ' in Political Studies (1984).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://www.librarything.com/author/eccleshallrobert '
            'https://www.taylorfrancis.com/books/9780203205181'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1984) '
                '[Book Reviews of Books by Oakeshott] — Political Studies'
            ),
        ],
    ),
    ('Hartle', 'A.', ''): dict(
        candidate='Ann Hartle',
        confidence='medium',
        affiliation='Emory University',
        url='https://philosophy.emory.edu/people/bios/hartle-ann.html',
        descr=(
            'Ann Hartle, American philosopher and professor emerita at '
            'Emory University, known for her books on Montaigne. She '
            'reviewed The Politics of Faith and the Politics of Scepticism '
            'in the Review of Metaphysics (1997).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://philosophy.emory.edu/people/bios/hartle-ann.html'
        ),
        works=[
            (
                'author: A Review of The Politics of Faith and the Politics'
                ' of Scepticism (1997) [Book Reviews of Books by Oakeshott]'
                ' — Review of Metaphysics'
            ),
        ],
    ),
    ('Heath', 'E.', ''): dict(
        candidate='Eugene Heath',
        confidence='medium',
        affiliation='State University of New York at New Paltz',
        url='https://press.uchicago.edu/ucp/books/author/H/E/au25581489.html',
        descr=(
            'Eugene Heath, American philosopher at SUNY New Paltz who '
            'writes on Adam Ferguson and the ethics of markets, author or '
            'editor of Morality and the Market. He reviewed The Politics of'
            ' Faith and the Politics of Scepticism in the Independent '
            'Review (1998).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: htt'
            'ps://press.uchicago.edu/ucp/books/author/H/E/au25581489.html'
        ),
        works=[
            (
                'author: A Review of The Politics of Faith and the Politics'
                ' of Scepticism (1998) [Book Reviews of Books by Oakeshott]'
                ' — Independent Review'
            ),
        ],
    ),
    ('Dearden', 'R.', 'F.'): dict(
        candidate='R. F. Dearden',
        confidence='medium',
        yob=1934,
        yod=2005,
        descr=(
            'R. F. Dearden, British philosopher of education and former '
            "primary-school teacher who joined R. S. Peters's circle at the"
            ' London Institute of Education and wrote The Philosophy of '
            'Primary Education (1968). He reviewed The Voice of Liberal '
            'Learning in the Journal of Educational Administration and '
            'History (1990).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://libmast.utm.my/Record/KOHA-OAI-TEST:472069/Description'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1990) [Book Reviews of Books by '
                'Oakeshott] — Journal of Educational Administration and '
                'History'
            ),
        ],
    ),
    ('Graham', 'G.', ''): dict(
        candidate='Gordon Graham',
        confidence='medium',
        affiliation='Princeton Theological Seminary',
        yob=1949,
        url='https://en.wikipedia.org/wiki/L._Gordon_Graham',
        descr=(
            'Gordon Graham, Irish-born philosopher who was Lecturer in '
            'Moral Philosophy at St Andrews (from 1975), later Regius '
            'Professor of Moral Philosophy at Aberdeen and a professor at '
            'Princeton Theological Seminary. He reviewed On Human Conduct '
            'in the St Andrews-based Philosophical Quarterly (1976).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/L._Gordon_Graham '
            'https://www.gordon-graham.net/philosophy.html'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1976) [Book Reviews '
                'of Books by Oakeshott] — Philosophical Quarterly'
            ),
        ],
    ),
    ('Munz', 'P.', ''): dict(
        candidate='Peter Munz',
        confidence='medium',
        yob=1921,
        yod=2006,
        affiliation='Victoria University of Wellington',
        descr=(
            'Peter Munz was a German-born New Zealand historian and '
            'philosopher, a professor at Victoria University of Wellington '
            'and one of the few students of both Popper and Wittgenstein, '
            'who wrote on the philosophy of history. He reviewed '
            "Oakeshott's On History and Other Essays in European History "
            'Quarterly.'
        ),
        url='https://en.wikipedia.org/wiki/Peter_Munz',
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/Peter_Munz'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1984) '
                '[Book Reviews of Books by Oakeshott] — European History '
                'Quarterly'
            ),
        ],
    ),
    ('Searle', 'J.', 'R.'): dict(
        candidate='John Searle',
        confidence='medium',
        yob=1932,
        yod=2025,
        affiliation='University of California, Berkeley',
        descr=(
            'John Searle was an American philosopher of language and mind '
            'at Berkeley, known for speech-act theory and the Chinese room '
            'argument. His 1990 New York Review of Books essay "The Storm '
            'Over the University", on books about the state of higher '
            "education, is listed as a review of Oakeshott's The Voice of "
            'Liberal Learning.'
        ),
        url='https://en.wikipedia.org/wiki/John_Searle',
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/John_Searle'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1990) [Book Reviews of Books by '
                'Oakeshott] — New York Review of Books'
            ),
        ],
    ),
    ('Partridge', 'P.', 'H.'): dict(
        candidate='Percy Herbert Partridge',
        confidence='medium',
        yob=1910,
        yod=1988,
        affiliation='Australian National University',
        url='https://adb.anu.edu.au/biography/partridge-percy-herbert-15021',
        descr=(
            'Percy Herbert Partridge was an Australian social and political'
            ' philosopher and educationist who taught at Sydney and '
            'Melbourne before taking the foundation chair of social '
            'philosophy at the Australian National University in 1952. He '
            'wrote on Oakeshott and the study of politics in the Australian'
            ' Journal of Politics and History (1963).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://adb.anu.edu.au/biography/partridge-percy-herbert-15021'
        ),
        works=[
            (
                'author: The Study of Politics (1963) [Book Reviews of '
                'Books by Oakeshott] — Australian Journal of Politics and '
                'History'
            ),
        ],
    ),
    ('Roucek', 'J.', 'S.'): dict(
        candidate='Joseph Slabey Roucek',
        confidence='medium',
        yob=1902,
        yod=1984,
        affiliation='University of Bridgeport',
        url='https://snaccooperative.org/view/21038783',
        descr=(
            'Joseph Slabey Roucek was a Czech-born American sociologist and'
            ' political scientist, a prolific author and editor on Central '
            'Europe and the Balkans who taught at the University of '
            "Bridgeport and Hofstra. He reviewed Oakeshott's The Social and"
            ' Political Doctrines of Contemporary Europe in two American '
            'journals in 1939.'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://snaccooperative.org/view/21038783'
        ),
        works=[
            (
                'author: A Review of The Social and Political Doctrines of '
                'Contemporary Europe (1939) [Book Reviews of Books by '
                'Oakeshott] — American Sociological Review'
            ),
            (
                'author: A Review of The Social and Political Doctrines of '
                'Contemporary Europe (1939) [Book Reviews of Books by '
                'Oakeshott] — Annals of the American Academy of Political '
                'and Social Science'
            ),
        ],
    ),
    ('Rubinoff', 'L.', ''): dict(
        candidate='Lionel Rubinoff',
        confidence='medium',
        yob=1930,
        affiliation='Trent University',
        url='https://archives.trentu.ca/index.php/lionel-rubinoff',
        descr=(
            'Lionel Rubinoff is a Canadian philosopher who taught at the '
            'University of Toronto and York University before joining Trent'
            ' University in 1971; a Collingwood scholar, he edited '
            "Collingwood's Faith and Reason and wrote The Pornography of "
            'Power. He reviewed Oakeshott\'s On Human Conduct in "On '
            'Theorizing Human Conduct" (1979).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://archives.trentu.ca/index.php/lionel-rubinoff https://w'
            'ww.encyclopedia.com/arts/culture-magazines/rubinoff-lionel'
        ),
        works=[
            (
                'author: On Theorizing Human Conduct (1979) [Book Reviews '
                'of Books by Oakeshott] — Canadian Journal of Political and'
                ' Social Theory'
            ),
        ],
    ),
    ('Sandelius', 'W.', ''): dict(
        candidate='Walter E. Sandelius',
        confidence='medium',
        affiliation='University of Kansas',
        descr=(
            'Walter E. Sandelius was an American political scientist, '
            'professor of political science at the University of Kansas. He'
            " reviewed Oakeshott's The Social and Political Doctrines of "
            'Contemporary Europe in the American Political Science Review '
            '(1939).'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: htt'
            'ps://digital.lib.ku.edu/islandora/object/ku-udk%3A193919/datas'
            'tream/OCR/download'
        ),
        works=[
            (
                'author: A Review of The Social and Political Doctrines of '
                'Contemporary Europe (1939) [Book Reviews of Books by '
                'Oakeshott] — American Political Science Review'
            ),
        ],
    ),
    ('de Crespigny', 'A.', ''): dict(
        candidate='Anthony de Crespigny',
        confidence='medium',
        affiliation='University of Cape Town',
        descr=(
            'Anthony de Crespigny, a political philosopher at the '
            'University of Cape Town, co-edited with Kenneth Minogue '
            'Contemporary Political Philosophers (1975/1976), a survey of '
            'twentieth-century political thinkers that includes a chapter '
            'on Oakeshott.'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: htt'
            'ps://www.cambridge.org/core/journals/government-and-opposition'
            '/article/political-philosophy-now-anthony-de-crespigny-and-ken'
            'neth-minogue-eds-contemporary-political-philosophers-methuen-l'
            'ondon-1976-xvii-296-pages-275/579410970E82289BF427CABBAF278E22'
            ' https://www.schweitzer-online.de/en/buch/Minogue/Contemporary'
            '-Political-Philosophers-Routledge-Revivals/9780415614337/A1100'
            '868/'
        ),
        works=[
            (
                'editor: Contemporary Political Philosophers (1976) [Works '
                'Mentioning Oakeshott]'
            ),
        ],
    ),
    ('Walton', 'C.', ''): dict(
        candidate='Craig Walton',
        confidence='medium',
        yob=1934,
        yod=2007,
        descr=(
            'Craig Walton was an American historian of philosophy who wrote'
            " on Malebranche's ethics and on Hobbes, co-editing a volume on"
            ' Hobbes\'s "Science of Natural Justice" (1987), and reviewed '
            'regularly for the Journal of the History of Philosophy, which '
            "published a memorial notice in 2008. He reviewed Oakeshott's "
            'Hobbes on Civil Association in that journal.'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://dc2.philarchive.org/s/Delvy%20Craig%20Walton '
            'https://www.philosophie.ch/profil/walton-c'
        ),
        works=[
            (
                'author: A Review of Hobbes on Civil Association (1976) '
                '[Book Reviews of Books by Oakeshott] — Journal of the '
                'History of Philosophy'
            ),
        ],
    ),
    ('Whitworth', 'J.', ''): dict(
        candidate='John Whitworth',
        confidence='medium',
        yob=1945,
        yod=2019,
        url='https://en.wikipedia.org/wiki/John_Whitworth_(poet)',
        descr=(
            'John Whitworth was a British poet, educated at Merton College,'
            ' Oxford, known for witty metrical light verse and a frequent '
            'contributor to Quadrant and the Spectator. His collected verse'
            ' includes philosophical patter songs on Oakeshott; "The '
            'Oakeshott Upshot" appeared in Quadrant in 2003.'
        ),
        evidence=(
            'Matched on name, field and period only; no source names this '
            'person as the author of the work. Sources for the details: '
            'https://en.wikipedia.org/wiki/John_Whitworth_(poet) '
            'https://www.ablemusepress.com/node/537 (Selected Poems blurb '
            'mentions patter songs on Oakeshott); https://quadrant.org.au/m'
            'agazine/uncategorized/john-whitworth-1945-2019/'
        ),
        works=[
            (
                'author: The Oakeshott Upshot (2003) [Short Works About '
                'Oakeshott] — Quadrant'
            ),
        ],
    ),
    ('Humkin', 'J.', 'W.'): dict(
        candidate='Joseph Wellington Hunkin',
        confidence='medium',
        affiliation='Gonville and Caius College, Cambridge',
        yob=1887,
        yod=1950,
        url='https://en.wikipedia.org/wiki/Joseph_Hunkin_(bishop)',
        descr=(
            'Joseph Wellington Hunkin, an Anglican clergyman educated at '
            "Gonville and Caius College, Cambridge (Oakeshott's college), "
            'where he was Dean of Chapel after serving as a First World War'
            ' chaplain; he was Bishop of Truro from 1935 to 1950.'
        ),
        evidence=(
            'No "J. W. Humkin" found anywhere; probably a misreading of '
            'Hunkin. J. W. Hunkin was a Caius churchman in Cambridge in '
            '1934, but no source confirms the review. Sources for the '
            'details: https://en.wikipedia.org/wiki/Joseph_Hunkin_(bishop)'
        ),
        works=[
            (
                'author: A Review of Experience and Its Modes (1934) [Book '
                'Reviews of Books by Oakeshott] — Church of England '
                'Newspaper'
            ),
        ],
    ),
}

UNIDENTIFIED = {
    ('Ahn', 'J.', 'H.'): dict(
        evidence=(
            'Searched for J. H. Ahn with the 1991 National Review obituary '
            'of Oakeshott; earlier pass also found nothing. Initials and a '
            'common Korean surname, so no candidate.'
        ),
        works=[
            (
                'author: Michael Oakeshott, R.I.P (1991) [Short Works About'
                ' Oakeshott] — National Review'
            ),
        ],
    ),
    ('Archer', 'J.', 'R.'): dict(
        evidence=(
            'Article confirmed (Journal of Politics 41, 1979, pp. 150-168),'
            ' but no biographical source for J. R. Archer found; common '
            'surname.'
        ),
        works=[
            (
                'author: Oakeshott on Politics (1979) [Short Works About '
                'Oakeshott] — Journal of Politics'
            ),
        ],
    ),
    ('Asthana', 'M.', ''): dict(
        evidence=(
            'Initials only; a 1972 article in the Modern Review (Calcutta) '
            'suggests an Indian author, but nothing identifying was found.'
        ),
        works=[
            (
                'author: Michael Oakeshott Against Scientism in Politics '
                '(1972) [Short Works About Oakeshott] — Modern Review '
                '(Calcutta)'
            ),
        ],
    ),
    ('Balow', 'J.', 'R.'): dict(
        evidence=(
            'Not searched beyond the initials and journal; no scholar J. R.'
            ' Balow could be tied to the 1979 Australian Journal of '
            'Politics and History review.'
        ),
        works=[
            (
                'author: A Review of Experience and Its Modes (1979) [Book '
                'Reviews of Books by Oakeshott] — Australian Journal of '
                'Politics and History'
            ),
        ],
    ),
    ('Bigalke', 'Daniel', ''): dict(
        evidence=(
            'Daniel Bigalke wrote the 2007 review on Buchtips.net (a German'
            ' book-review site), but no biographical information about him '
            'was found.'
        ),
        works=[
            (
                'author: A Review of Michael Oakeshott: Philosoph der '
                'Politik (2007) [Book Reviews of Books About Oakeshott] — '
                'Buchtips.net'
            ),
        ],
    ),
    ('Bradley', 'J.', 'A.'): dict(
        evidence=(
            'J. A. Bradley reviewed for the Heythrop Journal (1977, 1986); '
            'common surname with initials only, and no identifying source '
            'was found.'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1977) [Book Reviews '
                'of Books by Oakeshott] — Heythrop Journal'
            ),
            (
                'author: A Review of On History and Other Essays (1986) '
                '[Book Reviews of Books by Oakeshott] — Heythrop Journal'
            ),
        ],
    ),
    ('Britnell', 'M.', ''): dict(
        evidence=(
            'M. Britnell reviewed in Political Studies (2001); initials '
            'only and no identifying source was found.'
        ),
        works=[
            (
                'author: A Review of Oakeshott and His Contemporaries: '
                'Montaigne, St. Augustine, Hegel, et al. (2001) [Book '
                'Reviews of Books About Oakeshott] — Political Studies'
            ),
        ],
    ),
    ('Brody', 'L.', 'H.'): dict(
        evidence=(
            'L. H. Brody reviewed for Library Journal (2002), probably a '
            'librarian reviewer; no identifying source was found.'
        ),
        works=[
            (
                'author: A Review of The Philosophy of Michael Oakeshott '
                '(2002) [Book Reviews of Books About Oakeshott] — Library '
                'Journal'
            ),
        ],
    ),
    ('Brown', 'J.', 'M.'): dict(
        evidence=(
            'Only the 1953 Political Studies note is known (answered by D. '
            'Krook). There are several J. M. Browns in the LoC authority '
            'file, and none could be tied to the note.'
        ),
        works=[
            (
                "author: A Note on Professor Oakeshott's Introduction to "
                'the Leviathan (1953) [Short Works About Oakeshott] — '
                'Political Studies'
            ),
        ],
    ),
    ('C.', 'L.', 'H.'): dict(
        evidence=(
            'Bare initials (L. H. C.) on a 1982 Heythrop Journal review; '
            'cannot be identified without the journal issue.'
        ),
        works=[
            (
                'author: A Review of Hobbes on Civil Association (1982) '
                '[Book Reviews of Books by Oakeshott] — Heythrop Journal'
            ),
        ],
    ),
    ('Cheeseman', 'Thomas', 'J.'): dict(
        evidence=(
            'Former undergraduate fellow at the Alexander Hamilton '
            'Institute; gave the paper at the 2013 Michael Oakeshott '
            'Association conference (theahi.org; cosmosandtaxis.org PDF). '
            'No affiliation or dates found.'
        ),
        works=[
            (
                'author: Homo Ludens and Civil Association: The Sublime '
                "Nature of Michael Oakeshott's Civil Condition (2014) "
                '[Short Works About Oakeshott] — Cosmos + Taxis'
            ),
        ],
    ),
    ('Christianson', 'E.', ''): dict(
        evidence=(
            'E. Christianson reviewed On History in the Spectator (1983); '
            'initials only and no identifying source was found.'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1983) '
                '[Book Reviews of Books by Oakeshott] — Spectator'
            ),
        ],
    ),
    ('Chauvier', 'S.', ''): dict(
        evidence=(
            'Lead (unverified, from recall): Stephane Chauvier, French '
            'moral and political philosopher (Paris-Sorbonne), would fit a '
            '1998 review in the Revue de Metaphysique et de Morale. A web '
            'search found nothing tying him to the review.'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1998) [Book Reviews '
                'of Books by Oakeshott] — Revue de Métaphysique et de '
                'Morale'
            ),
        ],
    ),
    ('Cocks', 'A.', ''): dict(
        evidence=(
            'Searched for the 1994 Quadrant and Policy (CIS) reviews; no '
            'full name or biography found.'
        ),
        works=[
            (
                'author: A Review of Religion, Politics and the Moral Life '
                '(1994) [Book Reviews of Books by Oakeshott] — Quadrant'
            ),
            (
                'author: A Review of The Achievement of Michael Oakeshott '
                '(1994) [Book Reviews of Books About Oakeshott] — Policy: A'
                ' Journal of Public Policy and Ideas'
            ),
        ],
    ),
    ('Davis', 'H.', ''): dict(
        evidence=(
            'Searched for the 1975 British Journal of Aesthetics article '
            'title; not found in indexes. Initial only.'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1975) [Book Reviews '
                'of Books by Oakeshott] — New Behaviour'
            ),
            (
                'author: Poetry and the Voice of Michael Oakeshott (1975) '
                '[Short Works About Oakeshott] — British Journal of '
                'Aesthetics'
            ),
        ],
    ),
    ('Dowling', 'R.', 'E.'): dict(
        evidence=(
            'Not re-searched beyond previous pass; only the 1959 AJPH '
            'citation known. Possibly the R. E. Dowling who wrote on '
            'pressure-group theory c.1960 (unconfirmed).'
        ),
        works=[
            (
                "author: Oakeshott's Theory of Reason, Tradition, and "
                'Conservatism (1959) [Short Works About Oakeshott] — '
                'Australian Journal of Politics and History'
            ),
        ],
    ),
    ('Engel', 'S.', ''): dict(
        evidence=(
            'Article is by S. M. Engel (J. Philosophy of Education 2007); '
            'no full name or affiliation found.'
        ),
        works=[
            (
                'author: Political Education in/as the Practice of Freedom:'
                ' A Paradoxical Defence from the Perspective of Michael '
                'Oakeshott (2007) [Short Works About Oakeshott] — Journal '
                'of Philosophy of Education'
            ),
        ],
    ),
    ('Fell', 'A.', 'R.'): dict(
        evidence="Queen's Quarterly 1960 reviewer; not identified.",
        works=[
            (
                'author: A Review of The Voice of Poetry in the '
                'Conversation of Mankind: An Essay (1960) [Book Reviews of '
                'Books by Oakeshott] — Queen’s Quarterly'
            ),
        ],
    ),
    ('G.', 'S.', 'J.'): dict(
        evidence='Initials only (Dublin Review, 1939); cannot be identified.',
        works=[
            (
                'author: A Review of The Social and Political Doctrines of '
                'Contemporary Europe (1939) [Book Reviews of Books by '
                'Oakeshott] — Dublin Review'
            ),
        ],
    ),
    ('Goldsmith', 'F.', ''): dict(
        evidence=(
            'Library Journal reviewer (1993); possibly the librarian '
            'Francisca Goldsmith, but nothing ties her to this review.'
        ),
        works=[
            (
                'author: A Review of Morality and Politics in Modern '
                'Europe: The Harvard Lectures (1993) [Book Reviews of Books'
                ' by Oakeshott] — Library Journal'
            ),
        ],
    ),
    ('Hall', 'D.', ''): dict(
        evidence=(
            'Searched for the 1982 Political Studies article title and '
            "possible co-authors; author's full name not found."
        ),
        works=[
            (
                'author: Oakeshott and the Impossibility of Philosophical '
                'Politics (1982) [Short Works About Oakeshott] — Political '
                'Studies'
            ),
        ],
    ),
    ('Hall', 'T.', ''): dict(
        evidence=(
            'Common surname with initial only (Review of Metaphysics 1989; '
            'Crisis 1991); not identified.'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1989) [Book Reviews of Books by '
                'Oakeshott] — Review of Metaphysics'
            ),
            (
                'author: Michael Oakeshott, R.I.P. (1991) [Short Works '
                'About Oakeshott] — Crisis'
            ),
        ],
    ),
    ('Hall', 'W.', 'E.'): dict(
        evidence='Birmingham Post reviewer (1989); not identified.',
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1989) [Book Reviews of Books by '
                'Oakeshott] — Birmingham Post'
            ),
        ],
    ),
    ('Hughes', 'C.', 'J.'): dict(
        evidence=(
            'Common surname; no source found identifying the 1963 '
            'Philosophical Books reviewer.'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1963) [Book Reviews of Books by Oakeshott] — '
                'Philosophical Books'
            ),
        ],
    ),
    ('Huelson', 'R.', ''): dict(
        evidence=(
            'Choice reviews are brief librarian/academic notices; no source'
            ' found identifying R. Huelson.'
        ),
        works=[
            (
                "author: A Review of Sartre's Radicalism and Oakeshott's "
                'Conservatism: The Duplicity of Freedom (1998) [Book '
                'Reviews of Books About Oakeshott] — Choice'
            ),
        ],
    ),
    ('Hunt', 'R.', 'L.'): dict(
        evidence=(
            'Common surname; no source found identifying the 1977 Annals '
            'reviewer of On Human Conduct.'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1977) [Book Reviews '
                'of Books by Oakeshott] — Annals of the American Academy of'
                ' Political and Social Science'
            ),
        ],
    ),
    ('J.M.C.', '', ''): dict(
        evidence=(
            'Initials-only byline in the LSE student magazine Clare Market '
            'Review (1951); no source identifies the writer (earlier pass '
            'also failed).'
        ),
        works=[
            (
                'author: Professor Michael Oakeshott: A Personal Impression'
                ' (1951) [Short Works About Oakeshott] — Clare Market '
                'Review'
            ),
        ],
    ),
    ('Johnson', 'G.', ''): dict(
        evidence=(
            'Common surname with single initial; 1960 Poetry Review '
            'reviewer not identified.'
        ),
        works=[
            (
                'author: A Review of The Voice of Poetry in the '
                'Conversation of Mankind: An Essay (1960) [Book Reviews of '
                'Books by Oakeshott] — Poetry Review'
            ),
        ],
    ),
    ('Johnson', 'Gregory', 'R.'): dict(
        evidence=(
            'The 1997 Review of Metaphysics review of Devigne, Recasting '
            'Conservatism (vol. 50 no. 4, pp. 876-878; '
            'https://dc2.philarchive.org/rec/JOHRC-2) is indexed, but no '
            'biographical source for the reviewer was found. Review of '
            'Metaphysics is edited at the Catholic University of America, '
            'so he may have been a graduate student there; unconfirmed.'
        ),
        works=[
            (
                'author: A Review of Recasting Conservatism: Oakeshott, '
                'Strauss, and the Response to Postmodernism (1997) [Book '
                'Reviews of Books About Oakeshott] — Review of Metaphysics'
            ),
        ],
    ),
    ('Jones', 'R.', 'J. B.'): dict(
        evidence=(
            'Possibly R. J. Barry Jones (international relations, '
            'University of Reading), but no search evidence was found tying'
            ' him to the 1994 Times Higher Education Supplement review; not'
            ' researched further.'
        ),
        works=[
            (
                'author: A Review of Morality and Politics in Modern '
                'Europe: The Harvard Lectures (1994) [Book Reviews of Books'
                ' by Oakeshott] — Times Higher Education Supplement'
            ),
        ],
    ),
    ('Kananen', 'A.', ''): dict(
        evidence=(
            'Editor of the Jyväskylä memorial volume for Iisa Räsänen '
            '(2000); earlier pass found no catalogue record naming editors,'
            ' and the only Kananen found in Finnish political science '
            '(Ilkka) does not match.'
        ),
        works=[
            (
                'editor: Valtapolitiikkaa – analyysejä valtapuheesta: '
                'Muistokirja Iisa Räsäselle (2000) [Works Mentioning '
                'Oakeshott]'
            ),
        ],
    ),
    ('Landau', 'J.', ''): dict(
        evidence=(
            'Wilson Quarterly 1996 reviewer; common surname with single '
            'initial, not identified.'
        ),
        works=[
            (
                'author: A Review of The Politics of Faith and the Politics'
                ' of Scepticism (1996) [Book Reviews of Books by Oakeshott]'
                ' — Wilson Quarterly'
            ),
        ],
    ),
    ('Lawrence', 'R.', ''): dict(
        evidence=(
            'Reviewer in the journal English (1960); common surname with '
            'single initial, not identified.'
        ),
        works=[
            (
                'author: A Review of The Voice of Poetry in the '
                'Conversation of Mankind: An Essay (1960) [Book Reviews of '
                'Books by Oakeshott] — English'
            ),
        ],
    ),
    ('Liddington', 'J.', ''): dict(
        evidence=(
            'Wrote on Oakeshott in Political Studies (1982) and in '
            'Pelczynski & Gray (eds), Conceptions of Liberty in Political '
            'Philosophy (1984) (https://dc2.philarchive.org/rec/LIDOFI); no'
            ' source gives full name, institution or dates.'
        ),
        works=[
            (
                'author: Hall and Modood on Oakeshott (1982) [Short Works '
                'About Oakeshott] — Political Studies'
            ),
            (
                'author: Oakeshott: Freedom in a Modern European State '
                '(1984) [Short Works About Oakeshott]'
            ),
        ],
    ),
    ('Lopp', 'D.', ''): dict(
        evidence=(
            'Philosophical Review reviewer of On Human Conduct (1977); no '
            'source found identifying D. Lopp.'
        ),
        works=[
            (
                'author: A Review of On Human Conduct (1977) [Book Reviews '
                'of Books by Oakeshott] — Philosophical Review'
            ),
        ],
    ),
    ('Miller', 'B.', ''): dict(
        evidence='Common surname with one initial; not searched further.',
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1962) [Book Reviews of Books by Oakeshott] — '
                'Listener'
            ),
        ],
    ),
    ('Miller', 'S.', ''): dict(
        evidence='Common surname with one initial; not searched further.',
        works=[
            (
                'author: A Review of On Human Conduct (1977) [Book Reviews '
                'of Books by Oakeshott] — Partisan Review'
            ),
        ],
    ),
    ('Montoya', 'L.', 'G.'): dict(
        evidence=(
            "Searched for the 2008 JIRD review of Astrov's On World "
            'Politics; no record naming the reviewer found.'
        ),
        works=[
            (
                'author: A Review of On World Politics: R. G. Collingwood, '
                'Michael Oakeshott and Neotraditionalism in International '
                'Relations (2008) [Book Reviews of Books About Oakeshott] —'
                ' Journal of International Relations and Development'
            ),
        ],
    ),
    ('Nelson', 'P.', ''): dict(
        evidence='Common surname with one initial; not searched further.',
        works=[
            (
                'author: A Review of The Political Philosophy of Michael '
                'Oakeshott (1991) [Book Reviews of Books About Oakeshott] —'
                ' Journal of Politics'
            ),
        ],
    ),
    ('Owen', 'B.', 'E.'): dict(
        evidence='Common surname with initials only; not searched further.',
        works=[
            (
                'author: A Review of The Voice of Poetry in the '
                'Conversation of Mankind: An Essay (1960) [Book Reviews of '
                'Books by Oakeshott] — Contemporary Review'
            ),
        ],
    ),
    ('Palmer', 'H.', ''): dict(
        evidence=(
            'Common surname with one initial (possibly the philosopher '
            'Humphrey Palmer, but no evidence).'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1985) '
                '[Book Reviews of Books by Oakeshott] — Philosophical Books'
            ),
        ],
    ),
    ('Payne', 'M.', ''): dict(
        evidence='Common surname with one initial; not searched further.',
        works=[
            (
                'author: A Review of Michael Oakeshott on Hobbes: A Study '
                'in the Renewal of Philosophical Ideas (2003) [Book Reviews'
                ' of Books About Oakeshott] — Network'
            ),
        ],
    ),
    ('Ramachandra', 'G.', 'P.'): dict(
        evidence=(
            'Searched for the 1997 JICPR article; no record naming the '
            'author found. Presumably an Indian philosopher.'
        ),
        works=[
            (
                'author: Oakeshott on Present, Future and Past (1997) '
                '[Short Works About Oakeshott] — Journal of Indian Council '
                'of Philosophical Research'
            ),
        ],
    ),
    ('Rathore', 'L.', 'S.'): dict(
        evidence=(
            'Previous pass: more than one L. S. Rathore in Open Library '
            '(historian of Marwar, agrometeorologist); none confirmed as '
            'the author.'
        ),
        works=[
            (
                'author: Political Ideas of Michael Oakeshott (1980) [Short'
                ' Works About Oakeshott] — Indian Journal of Political '
                'Studies'
            ),
        ],
    ),
    ('Reshaur', 'Ken', ''): dict(
        evidence=(
            'Cambridge Core confirms Ken Reshaur wrote the 1970 CJPS review'
            ' of Politics and Experience (https://cambridge.org/core/journa'
            'ls/canadian-journal-of-political-science-revue-canadienne-de-s'
            'cience-politique/article/preston-king-and-b-c-parekh-eds-polit'
            'ics-and-experience-essays-presented-to-michael-oakeshott-cambr'
            'idge-university-press-1968-pp-424/ED96D0D7BF7E1A38C169B740A6A0'
            '621A), but no biographical information found (a University of '
            'Manitoba search found nothing).'
        ),
        works=[
            (
                'author: A Review of Politics and Experience: Essays '
                'Presented to Professor Michael Oakeshott on the Occasion '
                'of His Retirement (1970) [Book Reviews of Books About '
                'Oakeshott] — Canadian Journal of Political Science'
            ),
        ],
    ),
    ('Rice', 'D.', 'H.'): dict(
        evidence=(
            'Searched for the 1991 Perspectives on Political Science review'
            ' of Franco; no record naming the reviewer found.'
        ),
        works=[
            (
                'author: A Review of The Political Philosophy of Michael '
                'Oakeshott (1991) [Book Reviews of Books About Oakeshott] —'
                ' Perspectives on Political Science'
            ),
        ],
    ),
    ('Rolliston', 'Christopher', ''): dict(
        evidence=(
            'Searched for the 2009 Collingwood and British Idealism Studies'
            ' article under Rolliston/Rollinson; nothing found.'
        ),
        works=[
            (
                "author: Oakeshott's Theory of Tradition Explanation (2009)"
                ' [Short Works About Oakeshott] — Collingwood and British '
                'Idealism Studies'
            ),
        ],
    ),
    ('Rushton', 'M.', ''): dict(
        evidence='Common surname with one initial; not searched further.',
        works=[
            (
                'author: Michael Oakeshott: A Review Essay (1992) [Book '
                'Reviews of Books by Oakeshott] — Review of Politics'
            ),
        ],
    ),
    ('Sanderson', 'J.', 'B.'): dict(
        evidence=(
            'PhilArchive confirms the 1966 AJP article (44(2):210-223) but '
            'conflates the author with the 19th-century Hegel translator J.'
            ' Burdon Sanderson; no biographical information found for the '
            '1960s Durham University Journal reviewer.'
        ),
        works=[
            (
                'author: A Review of On History and Other Essays (1983) '
                '[Book Reviews of Books by Oakeshott] — Durham University '
                'Journal'
            ),
            (
                "author: A Review of Oakeshott's Philosophical Politics "
                '(1966) [Book Reviews of Books About Oakeshott] — Durham '
                'University Journal'
            ),
            (
                'author: A Review of Politics and Experience: Essays '
                'Presented to Professor Michael Oakeshott on the Occasion '
                'of His Retirement (1969) [Book Reviews of Books About '
                'Oakeshott] — Durham University Journal'
            ),
            (
                'author: A Review of Reason, Revolution and Political '
                "Theory: Notes on Oakeshott's 'Rationalism in Politics' "
                '(1967) [Book Reviews of Books About Oakeshott] — Durham '
                'University Journal'
            ),
            (
                'author: Professor Oakeshott on History as a Mode of '
                'Experience (1966) [Short Works About Oakeshott] — '
                'Australasian Journal of Philosophy'
            ),
        ],
    ),
    ('Schulz', 'D.', ''): dict(
        evidence='Common surname with one initial; not searched further.',
        works=[
            (
                'author: A Review of Morality and Politics in Modern '
                'Europe: The Harvard Lectures (1994) [Book Reviews of Books'
                ' by Oakeshott] — Choice'
            ),
        ],
    ),
    ('Seller', 'A.', ''): dict(
        evidence='Surname with one initial; not searched further.',
        works=[
            (
                'author: A Review of Hobbes on Civil Association (1976) '
                '[Book Reviews of Books by Oakeshott] — Philosophical Books'
            ),
        ],
    ),
    ('Pollard', 'D.', 'E. B.'): dict(
        evidence=(
            'Initials only; not identified (no searches turned up a D. E. '
            'B. Pollard linked to Philosophical Studies, Dublin).'
        ),
        works=[
            (
                'author: A Review of Hobbes on Civil Association (1976) '
                '[Book Reviews of Books by Oakeshott] — Philosophical '
                'Studies (Dublin)'
            ),
        ],
    ),
    ('Sherman', 'R.', 'R.'): dict(
        evidence=(
            'Searched "Robert R. Sherman" education reviewer; nothing tying'
            ' any R. R. Sherman to the 1989 Change/Choice reviews.'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1989) [Book Reviews of Books by '
                'Oakeshott] — Change'
            ),
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1989) [Book Reviews of Books by '
                'Oakeshott] — Choice'
            ),
        ],
    ),
    ('Subra', 'L.', ''): dict(
        evidence=(
            'Searched for Leena/L. Subra in Finnish political science '
            '(Jyväskylä); no matches found.'
        ),
        works=[
            (
                'author: Anthony Farr on Oakeshott and Sartre (1999) [Book '
                'Reviews of Books About Oakeshott] — Finnish Yearbook of '
                'Political Thought'
            ),
        ],
    ),
    ('Walsh', 'S.', ''): dict(
        evidence=(
            'Common surname with a single initial; local newspaper (Oxford '
            'Times) review; not searched further.'
        ),
        works=[
            (
                'author: A Review of The Voice of Liberal Learning: Michael'
                ' Oakeshott on Education (1989) [Book Reviews of Books by '
                'Oakeshott] — Oxford Times'
            ),
        ],
    ),
    ('Watmough', 'J.', 'W.'): dict(
        evidence=(
            'Search found no record of Cambridge Conversations (1950) or of'
            ' a J. W. Watmough author; a J. R. Watmough corresponded with '
            'Cambridge University Press 1937-45 (not confirmed same '
            'person).'
        ),
        works=[
            (
                'reviewee: Review of J.W. Watmough, Cambridge Conversations'
                ' (1950) [Book Reviews by Oakeshott] — Cambridge Journal'
            ),
        ],
    ),
    ('Wauchope', 'O.', 'S.'): dict(
        evidence=(
            'Book confirmed: Deviation into Sense: The Nature of '
            'Explanation (Faber, 1948; reviewed in Philosophy, https://reso'
            'lve.cambridge.org/core/journals/philosophy/article/abs/deviati'
            'on-into-sense-the-nature-of-explanation-by-o-s-wauchope-london'
            '-faber-faber-1948-pp-163-price-12s-6d-net/256688C2DC3548736F89'
            'BDD6A7D02A8C), but no biographical information found.'
        ),
        works=[
            (
                'reviewee: Review of O.S. Wauchope, Deviation into Sense '
                '(1949) [Book Reviews by Oakeshott] — Times Literary '
                'Supplement'
            ),
        ],
    ),
    ('Weigall', 'D.', ''): dict(
        evidence='Initial only; review in Ideas and Production (1984); not identified.',
        works=[
            (
                'author: A Review of On History and Other Essays (1984) '
                '[Book Reviews of Books by Oakeshott] — Ideas and '
                'Production'
            ),
        ],
    ),
    ('Weiss', 'V.', ''): dict(
        evidence=(
            'Common surname with initial only; Philosophisches Jahrbuch '
            'review (1978); not identified.'
        ),
        works=[
            (
                'author: A Review of Rationalism in Politics and Other '
                'Essays (1978) [Book Reviews of Books by Oakeshott] — '
                'Philosophisches Jahrbuch'
            ),
        ],
    ),
    ('Wood', 'G.', 'O.'): dict(
        evidence=(
            'Searched for the 1934 TLS reviewer of Experience and Its '
            'Modes; TLS reviews were then anonymous and no G. O. Wood was '
            'found.'
        ),
        works=[
            (
                'author: A Review of Experience and Its Modes (1934) [Book '
                'Reviews of Books by Oakeshott] — Times Literary Supplement'
            ),
        ],
    ),
    ('Zeigler', 'H.', ''): dict(
        evidence=(
            'Choice review (1996); searched Harmon Zeigler (political '
            'scientist) but found nothing tying him to the review.'
        ),
        works=[
            (
                'author: A Review of The Politics of Faith and the Politics'
                ' of Scepticism (1996) [Book Reviews of Books by Oakeshott]'
                ' — Choice'
            ),
        ],
    ),
}
