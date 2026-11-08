"""Journal details for journals in the database, used by load_journal_info.

Keyed by the journal's exact name in the database. Each entry may give
descr (a paraphrased one-paragraph description, kept well under the
512-character limit so the results-table popup stays small) and url (the
journal's own site, or a reference page such as Wikipedia for journals no
longer published). Leave out anything we couldn't confirm. "sources"
records where the facts came from.

The first batch (2026-11-07) covers the 31 journals with five or more
entries.
"""

JOURNAL_INFO = {
    "Spectator": dict(
        descr=(
            "British weekly magazine of politics and culture, first "
            "published in London in 1828 by Robert Stephen Rintoul and the "
            "oldest surviving magazine in the world. Liberal in its early "
            "years and conservative in outlook today, it mixes political "
            "commentary and current affairs with reviews of books, music, "
            "opera, film and television."
        ),
        url="https://www.spectator.co.uk/",
        sources=["https://en.wikipedia.org/wiki/The_Spectator"]),
    "Cambridge Review": dict(
        descr=(
            "Periodical of the University of Cambridge, published by its "
            "students from October 1879 until it ceased in 1998. Over its "
            "long run it printed writing by figures such as Bertrand "
            "Russell, Ludwig Wittgenstein, Michael Oakeshott, John Rawls "
            "and Simon Schama. An anthology, The Cambridge Mind (1970), "
            "gathers material from its first ninety years."
        ),
        sources=[
            "https://catalog.crl.edu/Record/c81e4297-f15c-545e-8fed-d77dbd4807dd/Description",
            "https://cambridgereview.cargo.site/About-the-CHR-1",
        ]),
    "Cosmos + Taxis": dict(
        descr=(
            "Open-access journal, publishing issues since 2013, concerned "
            "that the presuppositions of the liberal tradition have been "
            "eroded or misused by overly rationalist and constructivist "
            "thinking. It treats complexity and emergent order in accessible "
            "terms, with an emphasis on political economy and social "
            "philosophy, drawing on the Scottish tradition, Austrian "
            "economics and non-Cartesian philosophy, while holding to no "
            "single school of thought."
        ),
        url="https://cosmosandtaxis.org",
        sources=["https://cosmosandtaxis.org (Aims + Scope)",
                 "https://cosmosandtaxis.org/masthead-2/"]),
    "Times Literary Supplement": dict(
        descr=(
            "London review of books and ideas, founded in 1902 as a "
            "supplement to The Times and published on its own from 1914. It "
            "covers literature and current affairs through reviews and "
            "essays on new books by scholars and writers. It was a weekly "
            "for most of its history and moved to a fortnightly schedule "
            "in 2025."
        ),
        url="https://www.the-tls.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Times_Literary_Supplement"]),
    "Cambridge Journal": dict(
        descr=(
            "Monthly review published in Cambridge by Bowes & Bowes from "
            "October 1947 to September 1954 (seven volumes). It aimed to "
            "bring Cambridge scholarship in history, politics, philosophy, "
            "science and sociology to a general educated audience. Michael "
            "Oakeshott was one of its editors, and his essay \"Rationalism "
            "in Politics\" first appeared in its opening volume."
        ),
        sources=[
            "https://libcat.library.tamu.edu/Record/in00000267559/Description",
            "https://archive.spectator.co.uk/article/14th-november-1947/5/the-appearance-of-the-first-number-of-the-cambridg",
            "https://contemporarythinkers.org/michael-oakeshott/biography/",
        ]),
    "Collingwood and British Idealism Studies": dict(
        descr=(
            "Journal of the R.G. Collingwood Society, the Bradley Society and "
            "the Collingwood and British Idealism Centre at Cardiff "
            "University. It began in the 1990s as Collingwood Studies and "
            "now incorporates Bradley Studies. It covers Collingwood and the "
            "British Idealists in philosophy, politics, ethics, history of "
            "ideas and social thought."
        ),
        url="https://sites.cardiff.ac.uk/collingwood/publications",
        sources=[
            "https://sites.cardiff.ac.uk/collingwood/publications",
            "https://www.cardiff.ac.uk/research/explore/research-units/the-british-idealism-and-collingwood-centre",
        ]),
    "Journal of Theological Studies": dict(
        descr=(
            "Scholarly journal of theology founded in 1899 and published by "
            "Oxford University Press. It spans the whole range of "
            "theological research, scholarship and interpretation, and also "
            "prints ancient and modern texts, inscriptions and documents "
            "that appear there in print for the first time."
        ),
        url="https://academic.oup.com/jts",
        sources=["https://academic.oup.com/jts/pages/About"]),
    "Political Studies": dict(
        descr=(
            "Peer-reviewed journal of the Political Studies Association of "
            "the UK, founded in 1953 with Wilfrid Harrison as first editor "
            "and now published by SAGE. It publishes original research "
            "across political science and international relations, with no "
            "commitment to a single method or theoretical approach."
        ),
        url="https://journals.sagepub.com/home/PSX",
        sources=["https://www.psa.ac.uk/political-studies",
                 "https://en.wikipedia.org/wiki/Political_Studies_(journal)"]),
    "Political Theory": dict(
        descr=(
            "Peer-reviewed journal subtitled \"An International Journal of "
            "Political Philosophy\", published by SAGE since 1973. It is an "
            "interdisciplinary forum for political philosophy approached "
            "from philosophical, ideological and methodological angles, on "
            "themes such as liberalism, democratic theory, popular "
            "sovereignty, human rights and critical theory."
        ),
        url="https://journals.sagepub.com/home/ptx",
        sources=["https://en.wikipedia.org/wiki/Political_Theory_(journal)"]),
    "History of Political Thought": dict(
        descr=(
            "Quarterly journal founded in 1980 by Janet Coleman and Iain "
            "Hampsher-Monk and published by Imprint Academic. It is devoted "
            "to the historical study of political ideas and the "
            "methodological problems of that study, and publishes refereed "
            "articles together with book reviews and bibliographical "
            "surveys."
        ),
        url="https://imprint.co.uk/product/hpt/",
        sources=["https://imprint.co.uk/product/hpt/"]),
    "Review of Politics": dict(
        descr=(
            "Quarterly journal founded in 1939 at the University of Notre "
            "Dame by Waldemar Gurian, now published for the university by "
            "Cambridge University Press. It publishes research across "
            "political theory, including the history of political thought, "
            "comparative political thought, critical theory, and politics "
            "and literature, with a substantial book review section."
        ),
        url="https://www.cambridge.org/core/journals/review-of-politics",
        sources=[
            "https://www.cambridge.org/core/journals/review-of-politics/information/about-this-journal"]),
    "Philosophy": dict(
        descr=(
            "Journal of the Royal Institute of Philosophy, published since "
            "1926, first as the Journal of Philosophical Studies and as "
            "Philosophy from 1931; now issued by Cambridge University Press. "
            "It aims to bridge specialist philosophy and a wider educated "
            "public, asking contributors to write clearly and without "
            "needless jargon."
        ),
        url="https://www.cambridge.org/core/journals/philosophy",
        sources=[
            "https://www.cambridge.org/core/journals/philosophy/information/about-this-journal",
            "https://en.wikipedia.org/wiki/Philosophy_(journal)",
        ]),
    "American Political Science Review": dict(
        descr=(
            "Flagship peer-reviewed journal of the American Political "
            "Science Association, published since 1906 and now issued by "
            "Cambridge University Press. It publishes research articles and "
            "review essays from across the discipline, including political "
            "theory, American politics, public policy, comparative politics "
            "and international relations."
        ),
        url="https://www.cambridge.org/core/journals/american-political-science-review",
        sources=[
            "https://www.cambridge.org/core/journals/american-political-science-review/information/about-this-journal"]),
    "English Historical Review": dict(
        descr=(
            "The oldest surviving English-language academic journal of "
            "history, founded in 1886 with Mandell Creighton as first editor "
            "and now published by Oxford University Press. It covers any "
            "region and period from late antiquity to the present, with "
            "political history long central, and carries extensive book "
            "reviews."
        ),
        url="https://academic.oup.com/ehr",
        sources=["https://academic.oup.com/ehr/pages/About"]),
    "European Journal of Political Theory": dict(
        descr=(
            "Peer-reviewed quarterly founded in 2002 and published by SAGE. "
            "It covers political theory in the broadest geographical, "
            "historical and ideological sense, including analytic political "
            "philosophy, comparative political thought and the history of "
            "ideas, with particular attention to European scholarship."
        ),
        url="https://journals.sagepub.com/home/EPT",
        sources=[
            "https://en.wikipedia.org/wiki/European_Journal_of_Political_Theory"]),
    "Times Higher Education Supplement": dict(
        descr=(
            "British publication on higher education, launched in 1971 as "
            "The Times Higher Education Supplement, an offshoot of the Times "
            "Educational Supplement, and relaunched as the magazine Times "
            "Higher Education in 2008. It reports news and opinion on "
            "universities and academic life, and is now also known for its "
            "world university rankings."
        ),
        url="https://www.timeshighereducation.com",
        sources=["https://en.wikipedia.org/wiki/Times_Higher_Education"]),
    "Philosophical Quarterly": dict(
        descr=(
            "General philosophy journal founded in 1950 and published on "
            "behalf of the Scots Philosophical Association and the "
            "University of St Andrews, now by Oxford University Press. It "
            "publishes articles, discussions and book reviews across "
            "philosophy, favouring original work of broad philosophical "
            "interest."
        ),
        url="https://academic.oup.com/pq",
        sources=["https://academic.oup.com/pq/pages/About"]),
    "Journal of Politics": dict(
        descr=(
            "Peer-reviewed journal founded in 1939, published by the "
            "University of Chicago Press on behalf of the Southern Political "
            "Science Association. A general political science journal, it "
            "publishes research across all fields of the discipline."
        ),
        url="https://www.journals.uchicago.edu/toc/jop/current",
        sources=["https://en.wikipedia.org/wiki/The_Journal_of_Politics"]),
    "Choice": dict(
        descr=(
            "Review publication of the Association of College & Research "
            "Libraries, a division of the American Library Association, "
            "issued since 1964. Subject specialists write short evaluative "
            "reviews of new academic books and digital resources, several "
            "thousand a year, to guide academic librarians in building "
            "their collections."
        ),
        url="https://www.choice360.org",
        sources=["https://www.ala.org/acrl-choice/about",
                 "https://en.wikipedia.org/wiki/Choice_(publisher)"]),
    "Political Science Reviewer": dict(
        descr=(
            "Annual journal founded in 1971 by George W. Carey, long "
            "published by the Intercollegiate Studies Institute, devoted to "
            "article-length critical reviews of major works in political "
            "science and related fields, especially political theory and "
            "philosophy. It is now edited at Arizona State University."
        ),
        url="https://politicalsciencereviewer.com/",
        sources=["https://scetl.asu.edu/news-and-media/journals",
                 "https://oll.libertyfund.org/people/george-w-carey"]),
    "Salisbury Review": dict(
        descr=(
            "British quarterly magazine of conservative thought, founded in "
            "1982 by the Salisbury Group with Roger Scruton as its first "
            "editor. It publishes essays, commentary and reviews on "
            "politics, public life, social policy, education, religion and "
            "the arts, from a traditional, intellectual conservative "
            "standpoint."
        ),
        url="https://www.salisburyreview.com/",
        sources=["https://www.salisburyreview.com/",
                 "https://en.wikipedia.org/wiki/The_Salisbury_Review"]),
    "Quadrant": dict(
        descr=(
            "Australian review of ideas, literature and politics, founded in "
            "Sydney in 1956 by James McAuley and Richard Krygier under the "
            "auspices of the Australian Committee for Cultural Freedom. It "
            "publishes essays, commentary and reviews on culture, politics "
            "and history, along with poetry and fiction."
        ),
        url="https://quadrant.org.au/",
        sources=["https://en.wikipedia.org/wiki/Quadrant_(magazine)"]),
    "National Review": dict(
        descr=(
            "American magazine of conservative opinion, founded in 1955 by "
            "William F. Buckley Jr. It carries news analysis, commentary, "
            "essays and book reviews on politics, society and culture, and "
            "played a central part in shaping the post-war American "
            "conservative movement."
        ),
        url="https://www.nationalreview.com/",
        sources=["https://en.wikipedia.org/wiki/National_Review"]),
    "Zygon: Journal of Religion & Science": dict(
        descr=(
            "Peer-reviewed journal, founded in 1966, devoted to the "
            "relationship between religion and the sciences. It is sponsored "
            "by the Institute on Religion in an Age of Science and the "
            "Center for Advanced Study in Religion and Science. Its name, "
            "from the Greek for 'yoke', reflects its aim of bringing values "
            "and knowledge together."
        ),
        url="https://www.zygonjournal.org/",
        sources=["https://en.wikipedia.org/wiki/Zygon_(journal)"]),
    "Mind": dict(
        descr=(
            "Philosophy journal founded in 1876 by Alexander Bain, with "
            "George Croom Robertson as its first editor. Published by Oxford "
            "University Press on behalf of the Mind Association, it is a "
            "generalist journal that takes work in every area, style and "
            "tradition of philosophy, including its history."
        ),
        url="https://academic.oup.com/mind",
        sources=["https://academic.oup.com/mind/pages/About"]),
    "Clare Market Review": dict(
        descr=(
            "Student journal of the London School of Economics, founded in "
            "1905 and later published by the LSE Students' Union. "
            "Politically unaligned, it gave students an outlet for essays, "
            "reviews, criticism and creative writing outside academic "
            "constraints. It lapsed in 1973 and was revived in 2008."
        ),
        url="https://en.wikipedia.org/wiki/Clare_Market_Review",
        sources=["https://en.wikipedia.org/wiki/Clare_Market_Review"]),
    "Encounter": dict(
        descr=(
            "Anglo-American magazine of literature, politics and culture, "
            "published in London from 1953 to 1991. Founded by Stephen "
            "Spender and Irving Kristol and later edited by Melvin Lasky, it "
            "was sponsored by the Congress for Cultural Freedom, whose "
            "covert CIA funding caused a scandal in 1967. It was a major "
            "Cold War forum for anti-communist intellectuals."
        ),
        url="https://en.wikipedia.org/wiki/Encounter_(magazine)",
        sources=["https://en.wikipedia.org/wiki/Encounter_(magazine)"]),
    "Canadian Journal of Political Science": dict(
        descr=(
            "Peer-reviewed journal of the Canadian Political Science "
            "Association, established in 1968 when it split off from the "
            "Canadian Journal of Economics and Political Science. Published "
            "by Cambridge University Press, it accepts work in English and "
            "French across all fields of political science."
        ),
        url="https://www.cambridge.org/core/journals/canadian-journal-of-political-science-revue-canadienne-de-science-politique",
        sources=[
            "https://www.cambridge.org/core/journals/canadian-journal-of-political-science-revue-canadienne-de-science-politique/information/about-this-journal"]),
    "Society": dict(
        descr=(
            "Social science and public policy journal founded in 1963 by "
            "Irving Louis Horowitz as Transaction and long published by "
            "Transaction Publishers; Springer has published it since 2003. "
            "It carries research articles, commentary, forums and book "
            "reviews, chiefly in sociology and political science."
        ),
        url="https://link.springer.com/journal/12115",
        sources=["https://en.wikipedia.org/wiki/Society_(journal)"]),
    "New Society": dict(
        descr=(
            "British weekly magazine of social inquiry and comment, "
            "published from 1962 to 1988, when it merged into the New "
            "Statesman. Edited first by Timothy Raison and then Paul Barker, "
            "it covered sociology, anthropology, psychology, social policy "
            "and social history, along with reportage on everyday British "
            "life."
        ),
        url="https://en.wikipedia.org/wiki/New_Society",
        sources=["https://en.wikipedia.org/wiki/New_Society"]),
    "Annals of the American Academy of Political and Social Science": dict(
        descr=(
            "Journal of the American Academy of Political and Social Science "
            "(founded 1889), published continuously since 1890 and by SAGE "
            "since 1981. Each issue is a themed collection of "
            "interdisciplinary articles on a single question in the "
            "political and social sciences, often bearing on public policy."
        ),
        url="https://www.aapss.org/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Annals_of_the_American_Academy_of_Political_and_Social_Science"]),
}
