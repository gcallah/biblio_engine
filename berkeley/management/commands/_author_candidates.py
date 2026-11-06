"""Possible matches for authors we could not confirm. NOT loaded.

CANDIDATES: a likely identity was found, but no source ties that person
to the work in the bibliography. Each entry is in the same format as
_author_info.py, plus "candidate" (who we think it is), "evidence" and
"works". Once a match is confirmed, move the entry (without candidate,
evidence and works) into _author_info.py and run load_author_info.

UNIDENTIFIED: no match found yet; "evidence" records what was tried and
any lead worth following.

Researched 2026-11-06; many lookups stopped when the web-search limit ran
out, so the unidentified list is worth a second pass.
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
}

UNIDENTIFIED = {
    ('Ahn', 'J.', 'H.'): dict(
        evidence=(
            'No identifiable scholar named J. H. Ahn found in connection with '
            'the 1991 National Review obituary of Oakeshott; searches returned '
            'nothing.'
        ),
        works=[
            'author: Michael Oakeshott, R.I.P (1991) — National Review',
        ]),
    ('Archer', 'J.', 'R.'): dict(
        evidence=(
            'Article confirmed (Journal of Politics 41, 1979, pp.150-168) but '
            'no reliable biographical information found for the author.'
        ),
        works=[
            'author: Oakeshott on Politics (1979) — Journal of Politics',
        ]),
    ('Asthana', 'M.', ''): dict(
        evidence=(
            'Initials only; a 1972 article in the Modern Review (Calcutta) '
            'suggests an Indian author, but no identifying information found. '
            'Left blank.'
        ),
        works=[
            'author: Michael Oakeshott Against Scientism in Politics (1972) — Modern Review (Calcutta)',
        ]),
    ('Brown', 'J.', 'M.'): dict(
        evidence=(
            'Only the 1953 Political Studies note is known (answered by D. '
            'Krook). Several J. M. Browns in LoC authority file; none could be '
            'tied to this note.'
        ),
        works=[
            "author: A Note on Professor Oakeshott's Introduction to the Leviathan (1953) — Political Studies",
        ]),
    ('Cheeseman', 'Thomas', 'J.'): dict(
        evidence=(
            'The author was a former undergraduate fellow at the Alexander '
            'Hamilton Institute and gave the paper at the 2013 Michael '
            'Oakeshott Association conference (theahi.org; cosmosandtaxis.org '
            'PDF). No current affiliation or dates found, so left blank.'
        ),
        works=[
            "author: Homo Ludens and Civil Association: The Sublime Nature of Michael Oakeshott's Civil Condition (2014) — Cosmos + Taxis",
        ]),
    ('Davis', 'H.', ''): dict(
        evidence=(
            'Initial only. Search did not surface the 1975 British Journal of '
            "Aesthetics article or its author's full name; left blank to avoid "
            'misidentification.'
        ),
        works=[
            'author: Poetry and the Voice of Michael Oakeshott (1975) — British Journal of Aesthetics',
        ]),
    ('Dowling', 'R.', 'E.'): dict(
        evidence=(
            'R. E. Dowling: only the 1959 AJPH citation found; no biographical '
            'source identifies this author. Possibly the R. E. Dowling who '
            'wrote on pressure-group theory c.1960, but unconfirmed; left '
            'blank.'
        ),
        works=[
            "author: Oakeshott's Theory of Reason, Tradition, and Conservatism (1959) — Australian Journal of Politics and History",
        ]),
    ('Engel', 'S.', ''): dict(
        evidence=(
            'Article is by S. M. Engel (J. Philosophy of Education 2007, pp. '
            '325-349), but no source gave a full name or affiliation, so the '
            'person could not be identified.'
        ),
        works=[
            'author: Political Education in/as the Practice of Freedom: A Paradoxical Defence from the Perspective of Michael Oakeshott (2007) — Journal of Philosophy of Education',
        ]),
    ('Hall', 'D.', ''): dict(
        evidence=(
            'Could not identify the author of the 1982 Political Studies '
            'article beyond the initial; left blank.'
        ),
        works=[
            'author: Oakeshott and the Impossibility of Philosophical Politics (1982) — Political Studies',
        ]),
    ('Hall', 'T.', ''): dict(
        evidence=(
            "T. Hall, author of a 1991 Crisis magazine piece on Oakeshott's "
            'death: no source found identifying this author; initials only, '
            'left blank.'
        ),
        works=[
            'author: Michael Oakeshott, R.I.P. (1991) — Crisis',
        ]),
    ('J.M.C.', '', ''): dict(
        evidence=(
            "'J.M.C.' is an initials-only byline in the LSE student magazine "
            'Clare Market Review (1951); no source identifies the writer.'
        ),
        works=[
            'author: Professor Michael Oakeshott: A Personal Impression (1951) — Clare Market Review',
        ]),
    ('Kananen', 'A.', ''): dict(
        evidence=(
            "Could not identify the editor 'A. Kananen' of the Jyväskylä "
            'memorial volume for Iisa Räsänen (2000). Catalogue records (Finna,'
            ' National Library of Finland) were not reachable and search '
            'results named no editors; the only Kananen found in Finnish '
            'political science is Ilkka Kananen, whose initial does not match. '
            'Left blank.'
        ),
        works=[
            'editor: Valtapolitiikkaa – analyysejä valtapuheesta: Muistokirja Iisa Räsäselle (2000) — University of Jyväskylä',
        ]),
    ('Katzoff', 'C.', ''): dict(
        evidence=(
            'No reliable information found on the author of the 1992 Journal of'
            ' Philosophical Research article; first name not confirmed.'
        ),
        works=[
            'author: Oakeshott and the Practice of Politics (1992) — Journal of Philosophical Research',
        ]),
    ('Liddington', 'J.', ''): dict(
        evidence=(
            'J. Liddington wrote on Oakeshott in Political Studies (1982) and '
            'in Pelczynski & Gray (eds), Conceptions of Liberty in Political '
            'Philosophy (1984) (https://dc2.philarchive.org/rec/LIDOFI). No '
            'source found giving his full name, institution or dates; left '
            'blank.'
        ),
        works=[
            'author: Hall and Modood on Oakeshott (1982) — Political Studies',
            'author: Oakeshott: Freedom in a Modern European State (1984)',
        ]),
    ('Neill', 'Edmund', ''): dict(
        evidence=(
            'Not researched: the shared web-search budget ran out before this '
            'person could be looked up and direct fetches of likely sources '
            'failed. Left blank; retry later. Candidate: Edmund Neill, '
            'historian of modern British political thought, author of Michael '
            'Oakeshott (Continuum, 2010).'
        ),
        works=[
            'author: Michael Oakeshott (2010) — Continuum',
        ]),
    ('Osbourne', 'J.', 'W.'): dict(
        evidence=(
            'Not researched: the shared web-search budget ran out before this '
            'person could be looked up and direct fetches of likely sources '
            'failed. Left blank; retry later. Name possibly misspelled '
            '(Osborne?); author of a 1985 Modern Age article on Anthony Powell '
            'and Oakeshott.'
        ),
        works=[
            'author: Anthony Powell and Michael Oakeshott (1985) — Modern Age',
        ]),
    ('Price', 'R.', ''): dict(
        evidence=(
            'Possibly Russell Price (senior lecturer in politics at Lancaster, '
            "translator of Machiavelli), but no source links him to 'Memories "
            "of Michael Oakeshott' (Cambridge Review 1991). Left blank."
        ),
        works=[
            'author: Memories of Michael Oakeshott (1991) — Cambridge Review',
        ]),
    ('Ramachandra', 'G.', 'P.'): dict(
        evidence=(
            'No information found on the author of the 1997 JICPR article '
            'beyond the initials; presumably an Indian philosopher but not '
            'identifiable.'
        ),
        works=[
            'author: Oakeshott on Present, Future and Past (1997) — Journal of Indian Council of Philosophical Research',
        ]),
    ('Rathore', 'L.', 'S.'): dict(
        evidence=(
            'L. S. Rathore (Indian Journal of Political Studies, 1980): Open '
            'Library lists more than one L. S. Rathore (a historian of the '
            'Rathores of Marwar and an agrometeorologist); could not confirm '
            'which, if any, wrote this article. Left blank.'
        ),
        works=[
            'author: Political Ideas of Michael Oakeshott (1980) — Indian Journal of Political Studies',
        ]),
    ('Rolliston', 'Christopher', ''): dict(
        evidence=(
            'Not researched: the shared web-search budget ran out before this '
            'person could be looked up and direct fetches of likely sources '
            'failed. Left blank; retry later. Name possibly misspelled '
            '(Rollinson?); 2009 Collingwood and British Idealism Studies '
            'article.'
        ),
        works=[
            "author: Oakeshott's Theory of Tradition Explanation (2009) — Collingwood and British Idealism Studies",
        ]),
    ('Sanderson', 'J.', 'B.'): dict(
        evidence=(
            'J. B. Sanderson (Australasian Journal of Philosophy, 1966): could '
            "not identify; Open Library's only J. B. Sanderson is a biologist "
            '(unrelated). Web search budget exhausted before further checks.'
        ),
        works=[
            'author: Professor Oakeshott on History as a Mode of Experience (1966) — Australasian Journal of Philosophy',
        ]),
    ('Smith', 'T.', 'W.'): dict(
        evidence=(
            'T. W. Smith (History of Political Thought, 1996): possibly Thomas '
            'W. Smith, a US political theorist, but could not confirm (web '
            'search budget exhausted); left blank.'
        ),
        works=[
            'author: Michael Oakeshott on History, Practice and Political Theory (1996) — History of Political Thought',
        ]),
    ('Tseng', 'Roy', ''): dict(
        evidence=(
            'Not researched: the shared web-search budget ran out before this '
            'person could be looked up and direct fetches of likely sources '
            'failed. Left blank; retry later. Candidate: Roy Tseng, Taiwanese '
            'political theorist (Imprint Academic author); affiliation '
            'unverified.'
        ),
        works=[
            'author: The Sceptical Idealist: Michael Oakeshott as a Critic of the Enlightenment (2003) — Imprint Academic',
            'author: Oakeshott and a Re-understanding of ‘Confucian Liberalism’ (2016) — Collingwood and British Idealism Studies',
        ]),
    ('Whitworth', 'J.', ''): dict(
        evidence=(
            'No source found identifying the J. Whitworth who wrote "The '
            'Oakeshott Upshot" in Quadrant (2003). Not guessed.'
        ),
        works=[
            'author: The Oakeshott Upshot (2003) — Quadrant',
        ]),
    ('de Crespigny', 'A.', ''): dict(
        evidence=(
            'Not researched: the shared web-search budget ran out before this '
            'person could be looked up and direct fetches of likely sources '
            'failed. Left blank; retry later. Candidate: Anthony de Crespigny, '
            'co-editor with Kenneth Minogue of Contemporary Political '
            'Philosophers (1976); no sourced details.'
        ),
        works=[
            'editor: Contemporary Political Philosophers (1976) — Methuen',
        ]),
}
