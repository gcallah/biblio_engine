"""Journal details for journals in the database, used by load_journal_info.

Keyed by the journal's exact name in the database. Each entry may give
descr (a paraphrased one-paragraph description, kept well under the
512-character limit so the results-table popup stays small) and url (the
journal's own site, or a reference page such as Wikipedia for journals no
longer published). Leave out anything we couldn't confirm. "sources"
records where the facts came from.

The first two batches (2026-11-07) cover the 59 journals with three or more
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
    # Second batch (2026-11-07): journals with three or four entries.
    "Contemporary Political Theory": dict(
        descr=(
            "Peer-reviewed quarterly of political theory, published by "
            "Palgrave Macmillan since 2002. It is broad in approach, "
            "ranging from analytic philosophy to post-structuralist, "
            "feminist and critical theory, and welcomes work from "
            "neighbouring fields such as international relations, "
            "geography, anthropology, gender and cultural studies."
        ),
        url="https://link.springer.com/journal/41296",
        sources=[
            "https://www.palgrave.com/gp/journal/41296/authors/aims-scope",
            "https://en.wikipedia.org/wiki/Contemporary_Political_Theory",
        ]),
    "Daily Telegraph": dict(
        descr=(
            "London daily broadsheet newspaper first published in June 1855"
            " as The Daily Telegraph and Courier. It covers national and "
            "international news, politics, business and sport, along with "
            "opinion and commentary. Known for its conservative outlook, it"
            " has backed the Conservative Party at every general election "
            "since 1945, and it absorbed The Morning Post in 1937."
        ),
        url="https://www.telegraph.co.uk/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Daily_Telegraph",
        ]),
    "Durham University Journal": dict(
        descr=(
            "Official journal of Durham University in England, published "
            "from 1876 until it ceased in 1995. In its early decades it "
            "mainly reported news of the university itself; from the "
            "interwar years onward it became a general academic periodical,"
            " carrying scholarly articles unrelated to university business."
        ),
        url="https://en.wikipedia.org/wiki/Durham_University_Journal",
        sources=[
            "https://en.wikipedia.org/wiki/Durham_University_Journal",
            "https://archiveshub.jisc.ac.uk/data/gb33-und-k",
        ]),
    "Ethics": dict(
        descr=(
            "Peer-reviewed journal of moral, political and legal "
            "philosophy, founded in 1890 as the International Journal of "
            "Ethics and renamed Ethics in 1938; published by the University"
            " of Chicago Press since 1923. It draws on social and political"
            " theory, law and economics, and publishes both theoretical "
            "work and applications to current moral questions."
        ),
        url="https://www.journals.uchicago.edu/toc/et/current",
        sources=[
            "https://en.wikipedia.org/wiki/Ethics_(journal)",
        ]),
    "Government and Opposition": dict(
        descr=(
            "Peer-reviewed quarterly of comparative politics, founded in "
            "1965 with Ghita Ionescu as its first editor, and now published"
            " by Cambridge University Press on behalf of Government and "
            "Opposition Ltd. It covers politics in any region and on a wide"
            " range of topics, and also runs substantial review articles."
        ),
        url="https://www.cambridge.org/core/journals/government-and-opposition",
        sources=[
            "https://www.cambridge.org/core/journals/government-and-opposition/information/about-this-journal",
            "https://en.wikipedia.org/wiki/Government_and_Opposition",
        ]),
    "Heythrop Journal": dict(
        descr=(
            "Peer-reviewed journal on the meeting ground of philosophy and "
            "theology, founded in 1960 by Bruno Brinkman SJ at Heythrop "
            "College, London, and now published by Wiley-Blackwell. Its "
            "range includes philosophy of religion, ethics, hermeneutics, "
            "biblical exegesis, religious studies and pastoral theology, "
            "and it encourages dialogue between the two disciplines."
        ),
        url="https://onlinelibrary.wiley.com/journal/14682265",
        sources=[
            "https://en.wikipedia.org/wiki/The_Heythrop_Journal",
        ]),
    "Philosophical Books": dict(
        descr=(
            "British philosophy journal devoted to reviews of new books, "
            "first issued in January 1960 by Basil Blackwell of Oxford. It "
            "aimed to publish informed assessments of worthwhile new "
            "philosophy books soon after they appeared. In 2011 it was "
            "renamed Analytic Philosophy, under which title Wiley still "
            "publishes it."
        ),
        url="https://en.wikipedia.org/wiki/Analytic_Philosophy_(journal)",
        sources=[
            "https://en.wikipedia.org/wiki/Analytic_Philosophy_(journal)",
            "https://libcat.library.tamu.edu/Record/in00000758482/Description",
        ]),
    "Political Studies Review": dict(
        descr=(
            "Peer-reviewed journal of the Political Studies Association of "
            "the UK, published since 2003 and now issued by SAGE. It covers"
            " political science and international relations, and is known "
            "for its review articles and large book review section, "
            "alongside original research and symposia."
        ),
        url="https://journals.sagepub.com/home/psw",
        sources=[
            "https://en.wikipedia.org/wiki/Political_Studies_Review",
        ]),
    "Review of Metaphysics": dict(
        descr=(
            "Quarterly journal of philosophy founded in 1947 by Paul Weiss "
            "and published by the Philosophy Education Society, with the "
            "Catholic University of America as its chief sponsor. Tied to "
            "no school of thought, it publishes work on fundamental "
            "philosophical questions, especially metaphysics and the "
            "history of philosophy, with an extensive book review section."
        ),
        url="https://reviewofmetaphysics.org/",
        sources=[
            "https://reviewofmetaphysics.org/",
            "https://en.wikipedia.org/wiki/The_Review_of_Metaphysics",
        ]),
    "American Scholar": dict(
        descr=(
            "Quarterly magazine published by the Phi Beta Kappa Society "
            "since 1932, named after Ralph Waldo Emerson's 1837 address "
            '"The American Scholar". Written for general readers, it '
            "carries essays, criticism and poetry on public affairs, "
            "literature, science, history and culture."
        ),
        url="https://theamericanscholar.org/",
        sources=[
            "https://theamericanscholar.org/about-us/",
            "https://en.wikipedia.org/wiki/The_American_Scholar_(magazine)",
        ]),
    "Australian Journal of Politics and History": dict(
        descr=(
            "Peer-reviewed journal founded in 1955 by Gordon Greenwood, now"
            " published by Wiley. It covers history, political studies and "
            "international affairs, with particular attention to Australia,"
            " New Zealand and the Asia-Pacific region, and also publishes "
            "work on European politics, intellectual history and the "
            "history of political thought."
        ),
        url="https://onlinelibrary.wiley.com/journal/14678497",
        sources=[
            "https://en.wikipedia.org/wiki/Australian_Journal_of_Politics_and_History",
        ]),
    "British Journal of Educational Studies": dict(
        descr=(
            "Peer-reviewed education journal established in 1952 and "
            "published by Taylor & Francis on behalf of the Society for "
            "Educational Studies. It publishes scholarly, research-based "
            "articles on education, drawing chiefly on historical, "
            "philosophical and sociological analysis."
        ),
        url="https://www.tandfonline.com/journals/rbje20",
        sources=[
            "https://en.wikipedia.org/wiki/British_Journal_of_Educational_Studies",
        ]),
    "Economist": dict(
        descr=(
            "London weekly founded in 1843 by the Scottish economist James "
            "Wilson to campaign for repeal of the Corn Laws; it still calls"
            " itself a newspaper. It covers world affairs, politics, "
            "economics, business and finance, science and technology, and "
            "books and the arts, from a broadly classical-liberal, free-"
            "market position."
        ),
        url="https://www.economist.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Economist",
        ]),
    "First Things": dict(
        descr=(
            "American journal of religion and public life founded in 1990 "
            "by Richard John Neuhaus, who edited it until his death in "
            "2009, and published in New York by the Institute on Religion "
            "and Public Life. It seeks a religiously informed public "
            "philosophy from a chiefly Christian and Jewish standpoint, "
            "covering theology, culture, education, politics and "
            "literature."
        ),
        url="https://www.firstthings.com/",
        sources=[
            "https://en.wikipedia.org/wiki/First_Things",
        ]),
    "History and Theory": dict(
        descr=(
            "Quarterly journal on the theory and philosophy of history, "
            "founded in 1960 by George H. Nadel and published at Wesleyan "
            "University with Wiley. It carries articles and review essays "
            "on the philosophy of history, historiography and its history, "
            "historical method, and the relation of history to other "
            "disciplines, with an annual theme issue."
        ),
        url="https://historyandtheory.org/",
        sources=[
            "https://historyandtheory.org/about/",
            "https://en.wikipedia.org/wiki/History_and_Theory",
        ]),
    "Independent Review": dict(
        descr=(
            "Quarterly peer-reviewed journal of political economy published"
            " since 1996 by the Independent Institute, an American "
            "libertarian think tank. It offers critical analysis of "
            "government policy, drawing on economics, political science, "
            "law, history, philosophy and sociology."
        ),
        url="https://www.independent.org/publications/tir/",
        sources=[
            "https://www.independent.org/publications/tir/",
            "https://en.wikipedia.org/wiki/The_Independent_Review",
        ]),
    "Journal of Philosophy of Education": dict(
        descr=(
            "Journal of the Philosophy of Education Society of Great "
            "Britain, founded in 1967 and published by Oxford University "
            "Press since 2023 (previously Wiley-Blackwell). Drawing on a "
            "wide range of philosophical traditions, it treats fundamental "
            "questions about education and critical analysis of educational"
            " practice and policy."
        ),
        url="https://academic.oup.com/jope",
        sources=[
            "https://academic.oup.com/jope/pages/About",
            "https://en.wikipedia.org/wiki/Journal_of_Philosophy_of_Education",
        ]),
    "Journal of the History of Ideas": dict(
        descr=(
            "Quarterly journal founded in 1940 by Arthur O. Lovejoy and "
            "Philip P. Wiener, published by the University of Pennsylvania "
            "Press since 2006. It covers intellectual and conceptual "
            "history in the broadest sense, across philosophy, literature "
            "and the arts, the natural and social sciences, religion and "
            "political thought."
        ),
        url="https://www.pennpress.org/journals/journal/journal-of-the-history-of-ideas/",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_of_the_History_of_Ideas",
        ]),
    "Listener": dict(
        descr=(
            "Weekly magazine published by the BBC from 1929 until 1991. "
            "Intended as an aid to the intelligent reception of "
            "broadcasting, it printed transcripts of broadcast talks, along"
            " with previews of major literary and musical broadcasts, book "
            "reviews, and listings of the week's more serious programmes."
        ),
        url="https://en.wikipedia.org/wiki/The_Listener_(magazine)",
        sources=[
            "https://en.wikipedia.org/wiki/The_Listener_(magazine)",
        ]),
    "Modern Age": dict(
        descr=(
            "American quarterly of conservative thought, founded in 1957 by"
            " Russell Kirk with the support of publisher Henry Regnery, and"
            " published since 1976 by the Intercollegiate Studies "
            "Institute. Broadly traditionalist in outlook, it carries "
            "essays and book reviews on political philosophy, history, "
            "literature, religion and culture."
        ),
        url="https://modernagejournal.com/",
        sources=[
            "https://en.wikipedia.org/wiki/Modern_Age_(periodical)",
        ]),
    "Modern Language Review": dict(
        descr=(
            "Quarterly scholarly journal published by the Modern Humanities"
            " Research Association since 1905. It prints articles and book "
            "reviews, all in English, on medieval and modern European "
            "languages, literatures and cultures, with sections on English "
            "and American, French, Italian, Hispanic, Germanic, and "
            "Slavonic and East European studies."
        ),
        url="https://www.mhra.org.uk/journals/MLR",
        sources=[
            "https://www.mhra.org.uk/journals/MLR",
            "https://en.wikipedia.org/wiki/Modern_Language_Review",
        ]),
    "New Republic": dict(
        descr=(
            "American magazine of politics and culture founded in 1914 by "
            "Herbert Croly, Walter Lippmann and Walter Weyl. Long a weekly,"
            " it covers national politics, public affairs, books and the "
            "arts. Founded as a liberal and progressive voice, it moved "
            "toward the political centre under owner Martin Peretz."
        ),
        url="https://newrepublic.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_New_Republic",
        ]),
    "Philosophy of the Social Sciences": dict(
        descr=(
            "Peer-reviewed journal founded in 1971 and published by SAGE, "
            "an interdisciplinary forum on the philosophical foundations of"
            " the social sciences. It runs articles and symposia on topics "
            "such as methodology, individualism versus holism, rationality "
            "and the history of social-scientific concepts, without "
            "favouring any single school."
        ),
        url="https://journals.sagepub.com/home/pos",
        sources=[
            "https://en.wikipedia.org/wiki/Philosophy_of_the_Social_Sciences_(journal)",
        ]),
    "Politica": dict(
        descr=(
            "Journal of the London School of Economics and Political "
            "Science, launched in 1934 as a companion to the School's "
            "journal Economica. Economica kept economics, economic history "
            "and statistics, while Politica took the School's other "
            "subjects, chiefly politics and related social studies. Library"
            " records give its run as 1934 to 1939."
        ),
        sources=[
            "https://ideas.repec.org/h/pal/palchp/978-1-137-58274-4_6.html",
            "https://folio.caval.edu.au/Record/c000166010",
        ]),
    "Sunday Telegraph": dict(
        descr=(
            "British national Sunday broadsheet first published on 5 "
            "February 1961 as the Sunday companion to The Daily Telegraph. "
            "Conservative in outlook, it covers news, politics, comment, "
            "business, books and the arts."
        ),
        url="https://www.telegraph.co.uk/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Sunday_Telegraph",
        ]),
    "Time and Tide": dict(
        descr=(
            "British weekly review of politics and literature founded in "
            "1920 by Margaret, Lady Rhondda. It began as a left-leaning "
            "feminist paper, then moved rightward with its owner's views, "
            "and published writers such as Virginia Woolf, George Orwell "
            "and C. S. Lewis. It later became monthly and ceased in 1979, "
            "apart from a brief revival in 1984-86."
        ),
        url="https://en.wikipedia.org/wiki/Time_and_Tide_(magazine)",
        sources=[
            "https://en.wikipedia.org/wiki/Time_and_Tide_(magazine)",
        ]),
    "Utilitas": dict(
        descr=(
            "Interdisciplinary journal founded in 1989 and published by "
            "Cambridge University Press, with the backing of the "
            "International Society for Utilitarian Studies. It covers the "
            "history of utilitarian thought and the fields to which "
            "utilitarianism has contributed: moral and political "
            "philosophy, economic theory, jurisprudence and intellectual "
            "history."
        ),
        url="https://www.cambridge.org/core/journals/utilitas",
        sources=[
            "https://www.cambridge.org/core/journals/utilitas/information/about-this-journal",
            "https://en.wikipedia.org/wiki/Utilitas",
        ]),
    "VoegelinView": dict(
        descr=(
            "Online journal founded in 2009 by Frederick Wagner and "
            "published by the Eric Voegelin Society. It began as a resource"
            " for the study of the political philosopher Eric Voegelin and "
            "has broadened into a general arts and humanities journal, "
            "publishing essays, reviews and interviews on philosophy, "
            "literature, culture and current affairs."
        ),
        url="https://voegelinview.com/",
        sources=[
            "https://voegelinview.com/about/",
        ]),
}
