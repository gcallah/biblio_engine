"""Journal details for journals in the database, used by load_journal_info.

Keyed by the journal's exact name in the database. Each entry may give
descr (a paraphrased one-paragraph description, kept well under the
512-character limit so the results-table popup stays small) and url (the
journal's own site, or a reference page such as Wikipedia for journals no
longer published). Leave out anything we couldn't confirm. "sources"
records where the facts came from.

The batches of 2026-11-07 cover every journal we could identify; a few
obscure titles are left out.
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
    # Third batch (2026-11-07): journals with two entries.
    "Australasian Journal of Philosophy": dict(
        descr=(
            "Quarterly peer-reviewed journal of the Australasian "
            "Association of Philosophy, founded in 1923 as the Australasian"
            " Journal of Psychology and Philosophy and renamed in 1947. "
            "Among the longest-running philosophy journals in English, it "
            "accepts original work in every branch of philosophy and its "
            "history."
        ),
        url="https://www.tandfonline.com/journals/rajp20",
        sources=[
            "https://en.wikipedia.org/wiki/Australasian_Journal_of_Philosophy",
            "https://aap.org.au/editorial-policy",
        ]),
    "Australian and New Zealand Journal of Criminology": dict(
        descr=(
            "Peer-reviewed journal founded in 1968 as the principal journal"
            " of the Australian and New Zealand Society of Criminology. It "
            "carries research on crime and criminal justice, including "
            "theory, empirical studies and policy analysis, with particular"
            " attention to Australasia. In 2021 it was renamed the Journal "
            "of Criminology."
        ),
        url="https://journals.sagepub.com/home/anj",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_of_Criminology",
        ]),
    "British Book News": dict(
        descr=(
            "Monthly guide to new British books, begun in 1940 by the "
            "National Book Council and renamed British Book News in 1941. "
            "Later produced by the National Book League for the British "
            "Council, and published by the British Council itself from 1957"
            " to 1992, it carried short reviews and notices of current "
            "British publications."
        ),
        sources=[
            "https://discovery.nypl.org/research/research-catalog/bib/b11259713",
            "https://orlando.cambridge.org/organizations/e7823f36-f264-492c-87db-ecb7bf375c27",
        ]),
    "British Journal for the History of Philosophy": dict(
        descr=(
            "Peer-reviewed journal of the British Society for the History "
            "of Philosophy, published since 1993. It publishes articles on "
            "the history of philosophy, and has helped widen the "
            "philosophical canon to include neglected figures and "
            "traditions."
        ),
        url="https://www.tandfonline.com/journals/rbjh20",
        sources=[
            "https://en.wikipedia.org/wiki/British_Journal_for_the_History_of_Philosophy",
        ]),
    "British Journal of Aesthetics": dict(
        descr=(
            "Journal of the British Society of Aesthetics, founded in 1960 "
            "with Harold Osborne as its first editor. It publishes "
            "philosophical work on beauty, aesthetic experience and "
            "judgment, criticism, and the nature of the arts, from "
            "painting, music and literature to film, dance and "
            "architecture, with an extensive book review section."
        ),
        url="https://academic.oup.com/bjaesthetics",
        sources=[
            "https://academic.oup.com/bjaesthetics/pages/About",
            "https://en.wikipedia.org/wiki/British_Journal_of_Aesthetics",
        ]),
    "Christian Century": dict(
        descr=(
            "American Protestant magazine founded in 1884 in Des Moines as "
            "the Christian Oracle, a Disciples of Christ paper, and renamed"
            " Christian Century in 1900. Later nondenominational and based "
            "in Chicago, it became a leading voice of liberal mainline "
            "Protestantism, covering religious news, theological, moral and"
            " cultural issues, and books and the arts."
        ),
        url="https://www.christiancentury.org",
        sources=[
            "https://en.wikipedia.org/wiki/The_Christian_Century",
        ]),
    "Collingwood Studies": dict(
        descr=(
            "Journal of the R.G. Collingwood Society, produced by "
            "Collingwood scholars at Cardiff, publishing studies of the "
            "philosophy, history and thought of R.G. Collingwood. Its first"
            " issues appeared in the 1990s under this title; it continues "
            "as Collingwood and British Idealism Studies, which widened its"
            " scope to the British Idealists."
        ),
        url="https://sites.cardiff.ac.uk/collingwood/publications",
        sources=[
            "https://sites.cardiff.ac.uk/collingwood/publications",
            "https://libcat.library.tamu.edu/Record/in00002226880",
        ]),
    "Commentary": dict(
        descr=(
            "American monthly magazine founded in 1945 by the American "
            "Jewish Committee, covering politics, Judaism, Israel, and "
            "social and cultural questions. Long anti-Communist, it moved "
            "from liberalism toward neoconservatism under Norman Podhoretz,"
            " editor from 1960 to 1995, and became a leading forum for "
            "neoconservative thought."
        ),
        url="https://www.commentary.org",
        sources=[
            "https://en.wikipedia.org/wiki/Commentary_(magazine)",
        ]),
    "Commonweal": dict(
        descr=(
            "American journal of opinion founded in New York in 1924 by "
            "Michael Williams and run by Catholic lay people rather than "
            "the Church hierarchy. Generally liberal in outlook, it "
            "publishes editorials, essays and commentary on politics, "
            "religion and culture, along with poetry and reviews of books, "
            "film and theatre."
        ),
        url="https://www.commonwealmagazine.org",
        sources=[
            "https://en.wikipedia.org/wiki/Commonweal_(magazine)",
        ]),
    "Contemporary Review": dict(
        descr=(
            "British review founded in 1866, covering international and "
            "domestic affairs, politics, literature and the arts, history, "
            "travel and religion, with a regular section of book reviews. "
            "In its later years it appeared less often, and its print "
            "edition ended in 2012-13."
        ),
        url="https://en.wikipedia.org/wiki/The_Contemporary_Review",
        sources=[
            "https://en.wikipedia.org/wiki/Contemporary_Review",
            "https://libcat.library.tamu.edu/Record/in00002778730",
        ]),
    "Crossbow": dict(
        descr=(
            "Journal of the Bow Group, the British Conservative think tank "
            "founded in 1951. Begun in London in 1957 as a quarterly "
            "journal of politics, it carried articles on policy and "
            "political ideas from a Conservative perspective."
        ),
        sources=[
            "https://makula.mak.ac.ug/bib/360784",
            "https://en.wikipedia.org/wiki/Bow_Group",
        ]),
    "Frankfurter allgemeine Zeitung": dict(
        descr=(
            "German national daily newspaper founded in Frankfurt am Main "
            "on 1 November 1949. Widely regarded as one of Germany's "
            "newspapers of record and generally described as liberal-"
            "conservative, it covers national and international politics, "
            "business and culture."
        ),
        url="https://www.faz.net",
        sources=[
            "https://en.wikipedia.org/wiki/Frankfurter_Allgemeine_Zeitung",
        ]),
    "Hibbert Journal": dict(
        descr=(
            "British quarterly review of religion, theology and philosophy,"
            " issued by the Hibbert Trust from October 1902 to 1968. L.P. "
            "Jacks edited it from its founding until 1948. It served as a "
            "forum for discussion of religious, theological and "
            "philosophical questions."
        ),
        url="https://en.wikipedia.org/wiki/The_Hibbert_Journal",
        sources=[
            "https://en.wikipedia.org/wiki/Hibbert_Journal",
        ]),
    "Historical Journal": dict(
        descr=(
            "Peer-reviewed history journal published by Cambridge "
            "University Press. It began in 1923 as the Cambridge Historical"
            " Journal and took its present title in 1958, signalling a "
            "broader outlook. It covers British, European and world history"
            " from the fifteenth century onward, with research articles and"
            " historiographical and review essays."
        ),
        url="https://www.cambridge.org/core/journals/historical-journal",
        sources=[
            "https://www.cambridge.org/core/journals/historical-journal/information/about-this-journal",
            "https://en.wikipedia.org/wiki/The_Historical_Journal",
        ]),
    "History of European Ideas": dict(
        descr=(
            "Peer-reviewed journal of intellectual history, established in "
            "1980 and published by Routledge. It covers the history of "
            "European ideas from the Renaissance onward across political, "
            "philosophical, theological, historiographical, literary and "
            "cultural thought, with occasional editions of texts and themed"
            " special issues."
        ),
        url="https://www.tandfonline.com/journals/rhei20",
        sources=[
            "https://en.wikipedia.org/wiki/History_of_European_Ideas",
        ]),
    "Indian Journal of Political Science": dict(
        descr=(
            "Quarterly peer-reviewed journal edited and published by the "
            "Indian Political Science Association, first issued in 1939. It"
            " carries research articles on political science, public "
            "administration, international relations and governance, in "
            "India and around the world."
        ),
        url="https://www.ijps.net.in",
        sources=[
            "https://ideasofindia.org/project/indian-journal-of-political-science",
            "https://ijps.net.in/view/about.html",
        ]),
    "Journal of Philosophy": dict(
        descr=(
            "Monthly philosophy journal published from Columbia University "
            "since its founding in 1904 as The Journal of Philosophy, "
            "Psychology, and Scientific Methods; it later adopted its "
            "shorter title. It publishes articles of current philosophical "
            "interest, especially work on the boundaries between philosophy"
            " and other disciplines."
        ),
        url="https://www.journalofphilosophy.org/",
        sources=[
            "http://www.journalofphilosophy.org/generalinfo.html",
            "https://en.wikipedia.org/wiki/The_Journal_of_Philosophy",
        ]),
    "Law & Liberty": dict(
        descr=(
            "Online magazine published by Liberty Fund, launched in January"
            " 2012 as the Library of Law and Liberty. It publishes essays, "
            "book reviews, forum debates and podcasts on law, political "
            "thought, policy, economics, education and culture, mostly from"
            " classical liberal, conservative and libertarian contributors."
        ),
        url="https://lawliberty.org/",
        sources=[
            "https://lawliberty.org/about/",
            "https://overlawyered.com/2012/01/new-liberty-fund-law-site-and-an-interview",
        ]),
    "Library Journal": dict(
        descr=(
            "American trade publication for librarians, founded in 1876 by "
            "Melvil Dewey. It carries news of the library world, with an "
            "emphasis on public libraries, and features on professional "
            "practice. It is especially known for its book review section, "
            "which reviews several hundred popular and academic books each "
            "month."
        ),
        url="https://www.libraryjournal.com/",
        sources=[
            "https://en.wikipedia.org/wiki/Library_Journal",
        ]),
    "Manchester Guardian": dict(
        descr=(
            "British daily newspaper founded in Manchester in 1821 by the "
            "cotton merchant John Edward Taylor. Traditionally aligned with"
            " the Liberal Party, it became more radical under the long "
            "editorship of C. P. Scott. It was renamed The Guardian in "
            "1959, began printing in London in 1961, and continues under "
            "that name."
        ),
        url="https://www.theguardian.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Guardian",
        ]),
    "New Statesman and Nation": dict(
        descr=(
            "London weekly review of politics and literature, founded in "
            "1913 as the New Statesman by Sidney and Beatrice Webb with "
            "Fabian support. A 1931 merger with the Liberal weekly The "
            "Nation and Athenaeum produced the title New Statesman and "
            "Nation, used until 1964. A left-wing paper, it was also known "
            "for its books and arts pages."
        ),
        url="https://www.newstatesman.com/",
        sources=[
            "https://en.wikipedia.org/wiki/New_Statesman",
        ]),
    "Notre Dame Philosophical Reviews": dict(
        descr=(
            "Online-only journal of philosophy book reviews, published by "
            "the University of Notre Dame's Department of Philosophy since "
            "January 2002. It is devoted entirely to substantive reviews of"
            " recent philosophical books, commissioned and vetted by an "
            "international editorial board."
        ),
        url="https://ndpr.nd.edu/",
        sources=[
            "https://ndpr.nd.edu/about/",
        ]),
    "Perspectives on Political Science": dict(
        descr=(
            "Quarterly peer-reviewed journal established in 1990 through "
            "the merger of Perspective and Teaching Political Science. Its "
            "main focus is political philosophy, and it combines articles "
            "with symposia on topics such as classic texts, literature, "
            "religion, constitutional law and liberal education, as well as"
            " long book reviews."
        ),
        url="https://www.tandfonline.com/journals/vpps20",
        sources=[
            "https://en.wikipedia.org/wiki/Perspectives_on_Political_Science",
        ]),
    "Perspectives on Politics": dict(
        descr=(
            "Peer-reviewed journal of the American Political Science "
            "Association, established in 2003 and published by Cambridge "
            "University Press. It aims to foster broad, synthetic "
            "discussion across political science and with a wider public, "
            "highlighting important topics and reflecting on the discipline"
            " and why it matters."
        ),
        url="https://www.cambridge.org/core/journals/perspectives-on-politics",
        sources=[
            "https://www.cambridge.org/core/journals/perspectives-on-politics/information/about-this-journal",
            "https://en.wikipedia.org/wiki/Perspectives_on_Politics",
        ]),
    "Philosophical Studies (Dublin)": dict(
        descr=(
            "Annual journal of the Philosophical Society of St Patrick's "
            "College, Maynooth, Ireland, published from 1951 to about 1992 "
            "with support from the National University of Ireland. It aimed"
            " to develop the Catholic philosophical tradition through "
            "analysis of contemporary problems, publishing articles, book "
            "reviews, critical notices and surveys of work abroad."
        ),
        sources=[
            "https://pdcnet.org/philstudies/Philosophical-Studies",
            "https://catalogue.nli.ie/Record/vtls000012557",
        ]),
    "Political Research Quarterly": dict(
        descr=(
            "Peer-reviewed political science journal of the Western "
            "Political Science Association. Founded in 1948 at the "
            "University of Utah as the Western Political Quarterly, it took"
            " its present name in the early 1990s. It publishes original "
            "research in all areas of political science, drawing on varied "
            "methods and theoretical approaches."
        ),
        url="https://journals.sagepub.com/home/prq",
        sources=[
            "https://en.wikipedia.org/wiki/Political_Research_Quarterly",
            "https://wpsanet.org/publication/pqr.php",
        ]),
    "Political Science Quarterly": dict(
        descr=(
            "American scholarly journal founded in 1886 by Columbia "
            "University's John W. Burgess, the journal of the Academy of "
            "Political Science. It covers government, politics, public "
            "policy and foreign affairs without a fixed ideological or "
            "methodological line, aims to be readable by general readers as"
            " well as specialists, and has a large book review section."
        ),
        url="https://academic.oup.com/psq",
        sources=[
            "https://academic.oup.com/psq/pages/about",
            "https://en.wikipedia.org/wiki/Political_Science_Quarterly",
        ]),
    "Psychological Medicine": dict(
        descr=(
            "Peer-reviewed psychiatry journal founded in 1969 by Michael "
            "Shepherd, who edited it until 1993. It publishes original "
            "research in clinical psychiatry and the related biological, "
            "psychological and social sciences, on the causes, course, "
            "treatment and public health impact of mental disorders."
        ),
        url="https://www.cambridge.org/core/journals/psychological-medicine",
        sources=[
            "https://www.cambridge.org/core/journals/psychological-medicine/information/about-this-journal",
            "https://en.wikipedia.org/wiki/Psychological_Medicine",
        ]),
    "Scrutiny": dict(
        descr=(
            "British literary quarterly founded in Cambridge in 1932 by L. "
            "C. Knights and F. R. Leavis, with Leavis as its principal "
            "editor until it closed in 1953. Its main concern was literary "
            "criticism, setting out a sweeping revaluation of English "
            "literature, but many contributors also wrote on education, "
            "culture and politics."
        ),
        url="https://en.wikipedia.org/wiki/Scrutiny_(journal)",
        sources=[
            "https://en.wikipedia.org/wiki/Scrutiny_(journal)",
        ]),
    "Social Theory and Practice": dict(
        descr=(
            "Peer-reviewed quarterly of social philosophy, begun in 1970 "
            "and published by the Department of Philosophy at Florida State"
            " University. It takes up theoretical and applied questions in "
            "social, political, legal, economic, educational and moral "
            "philosophy, including critical studies of classic and "
            "contemporary social philosophers."
        ),
        url="https://pdcnet.org/soctheory",
        sources=[
            "https://pdcnet.org/soctheory",
            "https://en.wikipedia.org/wiki/Social_Theory_and_Practice",
        ]),
    "The World and I": dict(
        descr=(
            "American monthly magazine launched in 1986 by The Washington "
            "Times and edited for years by political scientist Morton A. "
            "Kaplan. It carried articles by scholars and experts on "
            "politics, economics, world affairs, culture, the arts, science"
            " and books. The print edition ended in 2004; it continued "
            "online until 2018."
        ),
        url="https://en.wikipedia.org/wiki/The_World_and_I",
        sources=[
            "https://en.wikipedia.org/wiki/The_World_and_I",
        ]),
    "Tijdschrift voor Filosofie": dict(
        descr=(
            "Dutch-language philosophy journal founded in Leuven in 1939, "
            "titled Tijdschrift voor Philosophie until 1962, and based at "
            "the Institute of Philosophy of KU Leuven. It is open to all "
            "schools of thought and every field of philosophy, publishing "
            "articles, discussions and reviews."
        ),
        sources=[
            "https://www.jstor.org/journal/tijdfilo",
            "https://relbib.de/Record/129502391/Details",
        ]),
    "Times": dict(
        descr=(
            "British national daily newspaper founded in London by John "
            "Walter in 1785 as The Daily Universal Register and renamed The"
            " Times in 1788. Long regarded as a British newspaper of "
            "record, it covers domestic and international news, politics, "
            "business and the arts, along with comment, letters and "
            "obituaries."
        ),
        url="https://www.thetimes.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Times",
        ]),
    "Tradition and Discovery": dict(
        descr=(
            "Refereed journal of the Polanyi Society, devoted to the work "
            "and legacy of the scientist and philosopher Michael Polanyi. "
            "It publishes articles and reviews linking Polanyi's post-"
            "critical thought to other thinkers in philosophy, religion and"
            " social thought, and to the many fields, from science to "
            "economics, that Polanyi wrote about."
        ),
        url="https://polanyisociety.org/tradition-discovery/",
        sources=[
            "https://pdcnet.org/traddisc/Tradition-and-Discovery",
            "https://polanyisociety.org/tradition-discovery/",
        ]),
    "Universities Quarterly": dict(
        descr=(
            "British quarterly on universities and higher education, first "
            "published in the late 1940s amid postwar debate about the "
            "growth and purposes of the universities. It dealt with "
            "university policy, teaching, governance and the place of "
            "higher education in society, and in 1987 continued as Higher "
            "Education Quarterly."
        ),
        sources=[
            "https://libcat.library.tamu.edu/Record/in00000437589/Similar",
            "https://srhe.ac.uk/publications/higher-education-quarterly/",
        ]),
    "Weekly Standard": dict(
        descr=(
            "American magazine of political news, analysis and commentary "
            "founded in 1995 by William Kristol and Fred Barnes. Published "
            "in Washington, it was widely seen as a leading voice of "
            "neoconservatism, and also ran essays and reviews on books and "
            "culture. It ceased publication in December 2018."
        ),
        url="https://en.wikipedia.org/wiki/The_Weekly_Standard",
        sources=[
            "https://en.wikipedia.org/wiki/The_Weekly_Standard",
        ]),
    "Western Political Quarterly": dict(
        descr=(
            "Political science quarterly first published by the University "
            "of Utah in 1948, and later the official journal of the Western"
            " Political Science Association. It published research across "
            "the discipline, from American and comparative politics to "
            "international relations and political theory, and was renamed "
            "Political Research Quarterly in the early 1990s."
        ),
        url="https://en.wikipedia.org/wiki/Political_Research_Quarterly",
        sources=[
            "https://en.wikipedia.org/wiki/Political_Research_Quarterly",
            "https://scholarly-societies.org/history/WesternPoliticalQ.html",
        ]),
    "Zeitschrift für Politik": dict(
        descr=(
            "German political science journal founded in 1907 by Adolf "
            "Grabowsky and Richard Schmidt, revived as a new series in "
            "1954, and the organ of the Hochschule für Politik München. It "
            "covers political science in its full range, from political "
            "theory and philosophy to comparative politics, international "
            "relations, political sociology and law."
        ),
        url="https://www.nomos-elibrary.de/zeitschrift/0044-3360",
        sources=[
            "https://www.inlibra.com/en/journal/view/issn/0044-3360",
            "https://krimdok.uni-tuebingen.de/Record/129457612",
        ]),
    # Fourth batch (2026-11-07): journals with one entry.
    "Academic Questions": dict(
        descr=(
            "Quarterly journal of the National Association of Scholars, "
            "launched in 1987, the year the association was founded. It "
            "examines American higher education, especially the interplay "
            "of politics, ideology, scholarship and teaching, and runs "
            "themed issues with articles, book reviews and commentary on "
            "the state of the university."
        ),
        url="https://www.nas.org/academic-questions",
        sources=[
            "https://en.wikipedia.org/wiki/Academic_Questions",
            "https://nas.org/about-us",
        ]),
    "American Enterprise": dict(
        descr=(
            "The American Enterprise was a public policy magazine of the "
            "American Enterprise Institute in Washington, D.C., founded in "
            "1990 by merging earlier AEI publications. Appearing about "
            "eight times a year, it generally argued for free-market "
            "economics and a neoconservative foreign policy. It closed in "
            "2006 and was followed by The American."
        ),
        url="https://en.wikipedia.org/wiki/The_American_Enterprise",
        sources=[
            "https://en.wikipedia.org/wiki/The_American_Enterprise",
        ]),
    "American Journal of Education": dict(
        descr=(
            "Quarterly education journal published by the University of "
            "Chicago Press, appearing since 1893 and known as School Review"
            " until 1979. It aims to bring together the varied intellectual"
            " and methodological strands of educational scholarship, "
            "publishing empirical research from many traditions. Not to be "
            "confused with Henry Barnard's 19th-century journal of the same"
            " name."
        ),
        url="https://www.journals.uchicago.edu/journals/aje",
        sources=[
            "https://en.wikipedia.org/wiki/American_Journal_of_Education",
        ]),
    "American Sociological Review": dict(
        descr=(
            "Flagship journal of the American Sociological Association, "
            "established in 1936 when the association's members voted to "
            "found a journal independent of the University of Chicago's "
            "American Journal of Sociology. Published bimonthly, it carries"
            " peer-reviewed research and theory from across the field of "
            "sociology."
        ),
        url="https://journals.sagepub.com/home/asr",
        sources=[
            "https://en.wikipedia.org/wiki/American_Sociological_Review",
            "https://journals.sagepub.com/home/asr",
        ]),
    "American Spectator": dict(
        descr=(
            "Conservative American magazine of news and politics, founded "
            "in 1967 in Bloomington, Indiana, by R. Emmett Tyrrell Jr. and "
            "Wladyslaw Pleszczynski as The Alternative: An American "
            "Spectator; it took its present title in 1977. Long a monthly, "
            "it ended regular monthly print issues in 2014 and continues "
            "mainly online. Unrelated to the British Spectator."
        ),
        url="https://spectator.org/",
        sources=[
            "https://en.wikipedia.org/wiki/The_American_Spectator",
        ]),
    "Annali dell'Istituto Storico Italo-Germanico in Trento": dict(
        descr=(
            "Multilingual yearbook of the Istituto Storico Italo-Germanico "
            "(Italian-German Historical Institute) in Trento, now part of "
            "the Fondazione Bruno Kessler, launched in 1975. It publishes "
            "research on Italian and German history from the Middle Ages to"
            " recent times in a European setting, with attention to "
            "relations among Italy, Austria and Germany."
        ),
        url="https://www.rivisteweb.it/issn/0392-0011",
        sources=[
            "https://www.rivisteweb.it/issn/0392-0011/presentazione",
            "https://isig.fbk.eu/en/publications/categories/annali-istituto-storico-italo-germanico-en/",
        ]),
    "Annual Review of Political Science": dict(
        descr=(
            "Annual journal from the nonprofit publisher Annual Reviews, "
            "first published in 1998. It carries commissioned review essays"
            " surveying research across political science, including "
            "political theory, international relations, political economy, "
            "political behavior, comparative and American politics, public "
            "policy and methodology."
        ),
        url="https://www.annualreviews.org/content/journals/polisci",
        sources=[
            "https://en.wikipedia.org/wiki/Annual_Review_of_Political_Science",
        ]),
    "Australian Journal of Political Science": dict(
        descr=(
            "Official journal of the Australian Political Studies "
            "Association, founded in 1966 as Politics and renamed in 1990. "
            "It publishes peer-reviewed work across political studies and "
            "international relations, including Australian and comparative "
            "politics, public policy, political theory and foreign policy, "
            "with an emphasis on Australia but open to international work."
        ),
        url="https://www.tandfonline.com/journals/cajp20",
        sources=[
            "https://en.wikipedia.org/wiki/Australian_Journal_of_Political_Science",
            "https://www.tandfonline.com/cajp19",
        ]),
    "Bibliographie de la Philosophie": dict(
        descr=(
            "International bibliography of philosophical publications, "
            "begun in 1937 under the Institut international de "
            "collaboration philosophique (later the Institut International "
            "de Philosophie) and published in Paris by Vrin. Issued "
            "semiannually at first, it became a quarterly in 1954, "
            "recording new books in philosophy from many countries."
        ),
        sources=[
            "https://nantilus.univ-nantes.fr/vufind/Record/PPN039220664/Description",
            "https://media.diba.cat/diba/fitxers/arxiu/fulletons/bib_21531_1938_baixa.pdf",
            "https://katalog.ub.uni-heidelberg.de/titel/1086070",
        ]),
    "Birmingham Post": dict(
        descr=(
            "Regional newspaper for Birmingham and the English Midlands, "
            "founded in 1857 by John Feeney and John Jaffray as the "
            "Birmingham Daily Post and later renamed the Birmingham Post. "
            "It is generally seen as a direct descendant of the Birmingham "
            "Journal (1825-1869) and covers local and regional news, "
            "business and public affairs."
        ),
        url="https://www.birminghampost.co.uk/",
        sources=[
            "https://en.wikipedia.org/wiki/Birmingham_Post",
            "https://en.wikipedia.org/wiki/Sir_John_Jaffray,_1st_Baronet",
        ]),
    "British Journal of Political Science": dict(
        descr=(
            "Peer-reviewed journal published by Cambridge University Press "
            "since 1971, with Brian Barry as its first editor. It covers "
            "political science broadly across countries and specialisms, "
            "including political theory, political behaviour, public policy"
            " and international relations, and often draws on neighbouring "
            "fields such as economics, sociology and philosophy."
        ),
        url="https://www.cambridge.org/core/journals/british-journal-of-political-science",
        sources=[
            "https://Www.Wikipedia.org/wiki/British_Journal_of_Political_Science",
            "https://core-prod.cambridgecore.org/core/journals/british-journal-of-political-science/information",
            "https://www.sudoc.fr/04890015X",
        ]),
    "British Journal of Sociology": dict(
        descr=(
            "Quarterly sociology journal established in 1950 at the London "
            "School of Economics, founded chiefly by Morris Ginsberg and T."
            " H. Marshall, and still published for the LSE. It covers all "
            "areas of sociology and publishes theoretical and empirical "
            "work by scholars worldwide; it is one of the main sociology "
            "journals in the UK."
        ),
        url="https://onlinelibrary.wiley.com/journal/14684446",
        sources=[
            "https://en.wikipedia.org/wiki/British_Journal_of_Sociology",
        ]),
    "Buchtips.net": dict(
        descr=(
            "German-language book-review website running since 2002. It "
            "publishes reviews by readers and contributors, along with "
            "author profiles, articles and news, covering crime fiction and"
            " thrillers, historical and literary fiction, and nonfiction. "
            "By its own count it holds more than 9,000 reviews."
        ),
        url="https://www.buchtips.net/",
        sources=[
            "https://www.buchtips.net/",
        ]),
    "Cambridge Journal of Education": dict(
        descr=(
            "Peer-reviewed journal published since 1971 on behalf of the "
            "University of Cambridge Faculty of Education. It covers all "
            "areas of education and favours work that links academic "
            "research with classroom practice, addressing teachers, "
            "theorists and policy makers and encouraging comparison between"
            " education systems and cultures."
        ),
        url="https://www.tandfonline.com/journals/ccje20",
        sources=[
            "https://www.educ.cam.ac.uk/research/cje/",
            "https://www.fachportal-paedagogik.de/zeitschriften/cambridge-journal-of-education-123/",
        ]),
    "Cambridge Law Journal": dict(
        descr=(
            "Law journal of the University of Cambridge, founded in 1921 as"
            " a student publication of the Cambridge University Law "
            "Society, with Arthur Goodhart as its first faculty editor. The"
            " Faculty of Law took over its management in 1954. Published by"
            " Cambridge University Press, it is the longest-established "
            "university law journal in the UK."
        ),
        url="https://www.cambridge.org/core/journals/cambridge-law-journal",
        sources=[
            "https://en.wikipedia.org/wiki/Cambridge_Law_Journal",
            "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/09388675EAD79D58AE3B9EB030CC8BB9/S0008197321000660a.pdf/the-past-present-and-future-of-the-cambridge-law-journal.pdf",
        ]),
    "Canadian Journal of Political and Social Theory": dict(
        descr=(
            "Canadian journal of political and social theory founded and "
            "edited by Arthur and Marilouise Kroker; its first issue "
            "appeared in 1977 and the print run ended in 1991. It published"
            " theoretical work on politics, society and culture. The "
            "Krokers relaunched it online in 1993 as CTheory, one of the "
            "first online-only academic journals."
        ),
        url="https://en.wikipedia.org/wiki/CTheory",
        sources=[
            "https://en.wikipedia.org/wiki/CTheory",
            "https://journals.uvic.ca/index.php/ctheory/article/view/13776/4540",
            "https://journals.uvic.ca/index.php/ctheory/about",
        ]),
    "Change": dict(
        descr=(
            "Change: The Magazine of Higher Learning is an American "
            "magazine on contemporary issues in higher education, "
            "originally sponsored by the American Association for Higher "
            "Education. Using a magazine format rather than that of an "
            "academic journal, it reports on trends and examines "
            "educational programs, policies and practices in colleges and "
            "universities."
        ),
        url="https://www.tandfonline.com/journals/vchn20",
        sources=[
            "https://en.wikipedia.org/wiki/Change:_The_Magazine_of_Higher_Learning",
            "https://www.tandfonline.com/journals/vchn20/about-this-journal",
        ]),
    "Church of England Newspaper": dict(
        descr=(
            "Independent Anglican newspaper from London, generally "
            "evangelical in outlook. It traces its origins to The Record, "
            "founded in 1828, which merged at the end of 1948 with the "
            "Church Family Newspaper (first issued 1894) to form the Church"
            " of England Newspaper."
        ),
        url="https://en.wikipedia.org/wiki/Church_of_England_Newspaper",
        sources=[
            "https://en.wikipedia.org/wiki/Church_of_England_Newspaper",
            "https://www.christiantoday.com/news/church-of-england-newspaper-suspends-print-operations",
        ]),
    "Claremont Review of Books": dict(
        descr=(
            "Quarterly review published by the Claremont Institute, a "
            "conservative think tank. A first version ran briefly in the "
            "mid-1980s; it was revived in 2000 under Charles R. Kesler. "
            "Through essays and book reviews it takes up American politics "
            "and public policy at the level of ideas, with the aim of "
            "renewing statesmanship and citizenship."
        ),
        url="https://claremontreviewofbooks.com/",
        sources=[
            "https://en.wikipedia.org/wiki/Claremont_Review_of_Books",
            "https://claremontreviewofbooks.com/about-us/",
        ]),
    "Clio": dict(
        descr=(
            "Clio: A Journal of Literature, History, and the Philosophy of "
            "History is an interdisciplinary peer-reviewed journal begun in"
            " 1971 and now published by Purdue University Fort Wayne. It "
            "covers literature informed by historical understanding, "
            "historical writing read as literature, and speculative and "
            "analytic philosophy of history."
        ),
        url="https://www.pfw.edu/clio/",
        sources=[
            "https://www.pfw.edu/clio/",
            "https://libcat.library.tamu.edu/Record/in00002778418/Description",
            "https://heibib.ub.uni-heidelberg.de/search/Record/129534390",
        ]),
    "Common Review": dict(
        descr=(
            "The Common Review was the magazine of the Great Books "
            "Foundation, published quarterly from 2001 to 2011 and founded "
            "by Peter Temes, a former president of the foundation. It "
            "specialized in nonfiction essays about books and ideas, and "
            "also carried reviews of new books, letters and editorials."
        ),
        url="https://en.wikipedia.org/wiki/The_Common_Review",
        sources=[
            "https://en.wikipedia.org/wiki/The_Common_Review",
        ]),
    "Conference for the Study of Political Thought International Newsletter": dict(
        descr=(
            "Newsletter of the Conference for the Study of Political "
            "Thought (CSPT), an international, interdisciplinary society "
            "founded in Toronto in 1967 by J. G. A. Pocock, Melvin Richter "
            "and Neal Wood to promote the study of political thought, past "
            "and present. Sent to members, it reported on conferences and "
            "chapters and carried announcements of members' publications."
        ),
        url="https://www.icspt.org/",
        sources=[
            "https://www.icspt.org/about-cspt",
            "https://www.historians.org/affiliated-society/international-conference-for-the-study-of-political-thought",
            "https://umsl.edu/library/archives/graduateschool/6-6-4.htm",
        ]),
    "Congregational Quarterly": dict(
        descr=(
            "The Congregational Quarterly: A Review of Religious Life and "
            "Thought was a British quarterly published in London from 1923 "
            "to 1958, at first by the Congregational Union of England and "
            "Wales and from late 1934 by the Independent Press. Not to be "
            "confused with an earlier American journal of the same name."
        ),
        sources=[
            "https://ci.nii.ac.jp/ncid/AA00124381",
            "https://archive.org/details/congregationalq10uniogoog",
        ]),
    "Conservative History Journal": dict(
        descr=(
            "Journal of the Conservative History Group, a society founded "
            "in 2002 by Iain Dale for people interested in the history of "
            "the British Conservative Party. First published in 2003 and "
            "issued once a year, it carries illustrated articles on the "
            "party's history, its leaders and its politics."
        ),
        sources=[
            "https://www.alistairlexden.org.uk/node/6264",
            "https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/211559",
        ]),
    "Crisis": dict(
        descr=(
            "American Catholic magazine founded in 1982 by Ralph McInerny "
            "and Michael Novak as Catholicism in Crisis: A Journal of Lay "
            "Catholic Opinion, and renamed Crisis in 1986. It covers "
            "theology, spirituality and politics, with arts and culture "
            "added later. It appeared in print until 2007 and has since "
            "been published online."
        ),
        url="https://crisismagazine.com/",
        sources=[
            "https://crisismagazine.com/opinion/crisis-magazine-turns-40",
            "https://en.wikipedia.org/wiki/Sophia_Institute_Press",
        ]),
    "Curriculum": dict(
        descr=(
            "British periodical on the school and college curriculum, "
            "published from 1980 to 2001 (volumes 1-22) by Studies in "
            "Education, a small education publisher based in Nafferton and "
            "Driffield, East Yorkshire, which also issued books on "
            "curriculum studies."
        ),
        sources=[
            "https://consulta-ccn.prd.ibict.br/vufind/Record/2126c",
            "https://libcat.library.tamu.edu/Record/in00000653008",
        ]),
    "Dissent": dict(
        descr=(
            "American quarterly of politics, social and cultural criticism,"
            " founded in 1954 by a group of New York intellectuals "
            "including Irving Howe and Lewis Coser. Associated with "
            "democratic socialism, it was meant to stake out a left "
            "position between Western liberalism and Soviet communism, and "
            "publishes essays, political philosophy and some fiction and "
            "poetry."
        ),
        url="https://www.dissentmagazine.org/",
        sources=[
            "https://en.wikipedia.org/wiki/Dissent_(American_magazine)",
        ]),
    "Dublin Review": dict(
        descr=(
            "Catholic quarterly founded in 1836 by Michael Joseph Quin, "
            "Nicholas Wiseman and Daniel O'Connell. Despite its name it was"
            " edited and published in London. It addressed educated "
            "Catholics and presented Catholic views to other readers, "
            "covering theology, literature, history, politics and art. "
            "Briefly retitled the Wiseman Review (1961-65), it merged into "
            "The Month in 1969."
        ),
        url="https://en.wikipedia.org/wiki/Dublin_Review_(Catholic_periodical)",
        sources=[
            "https://en.wikipedia.org/wiki/Dublin_Review_(Catholic_periodical)",
            "https://encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/dublin-review",
        ]),
    "Economic Affairs": dict(
        descr=(
            "Journal of the Institute of Economic Affairs, the London free-"
            "market think tank, founded in 1980. It publishes articles that"
            " apply economic principles and analysis to questions of public"
            " policy, markets and government."
        ),
        url="https://onlinelibrary.wiley.com/journal/14680270",
        sources=[
            "https://en.wikipedia.org/wiki/Economic_Affairs_(journal)",
        ]),
    "Education Review": dict(
        descr=(
            "Open-access journal of book reviews in education, established "
            "in 1998 by Gene V. Glass and based at Arizona State "
            "University. Also known as Reseñas Educativas / Resenhas "
            "Educativas, it publishes reviews and essay reviews of recent "
            "scholarly books on education in English, Spanish and "
            "Portuguese."
        ),
        url="https://edrev.asu.edu/",
        sources=[
            "https://en.wikipedia.org/wiki/Education_Review",
            "https://edrev.asu.edu/index.php/ER/issue/archive",
        ]),
    "English": dict(
        descr=(
            "Journal of literary criticism published for the English "
            "Association since 1936. It carries essays on authors and texts"
            " written in English, aimed at university and college readers, "
            "along with a substantial book review section and, unusually "
            "for an academic journal, original poetry."
        ),
        url="https://academic.oup.com/english",
        sources=[
            "https://academic.oup.com/english/pages/About",
            "https://content.wellcomecollection.org/works/d8yfcmer",
        ]),
    "Erasmus": dict(
        descr=(
            "Erasmus: Speculum Scientiarum was an international bulletin of"
            " contemporary scholarship, issued by Éditions du Panthéon from"
            " 1947, with Rudolf Jud as its first editor. Published in "
            "French and German, it surveyed and reviewed new scholarly work"
            " across the disciplines."
        ),
        sources=[
            "https://ulb-cardcatalogues.uibk.ac.at/Record/card_0000000232860",
            "https://catalogue.nli.ie/Record/vtls000418532",
            "https://www.ag.ch/staatsarchiv/suche/detail.aspx?ID=376194",
        ]),
    "Esprit": dict(
        descr=(
            "French review founded in Paris in 1932 by Emmanuel Mounier. It"
            " was the main organ of the personalist movement in the 1930s "
            "and has since remained a leading forum for philosophy, "
            "politics, literature and commentary on current affairs."
        ),
        url="https://esprit.presse.fr/",
        sources=[
            "https://en.wikipedia.org/wiki/Esprit_(magazine)",
        ]),
    "European History Quarterly": dict(
        descr=(
            "Peer-reviewed history journal covering European history from "
            "the later Middle Ages to the period after 1945. It was founded"
            " in 1971 as European Studies Review and took its present title"
            " in 1984."
        ),
        url="https://journals.sagepub.com/home/ehq",
        sources=[
            "https://en.wikipedia.org/wiki/European_History_Quarterly",
        ]),
    "European Legacy": dict(
        descr=(
            "The European Legacy: Toward New Paradigms, founded in 1996, is"
            " the journal of the International Society for the Study of "
            "European Ideas. A multidisciplinary peer-reviewed journal, it "
            "studies the philosophical, historical, ideological and "
            "cultural foundations of modern Europe and Europe's relations "
            "with the rest of the world."
        ),
        url="https://www.tandfonline.com/journals/cele20",
        sources=[
            "https://en.wikipedia.org/wiki/The_European_Legacy",
            "https://informahealthcare.com/journals/cele20/about-this-journal",
            "https://catalog-legacy.osaarchivum.org/catalog/BY1lq0X4",
        ]),
    "European Studies Review": dict(
        descr=(
            "History journal founded in 1971 and published by SAGE. It "
            "covered European history from the later Middle Ages onward. In"
            " 1984 it was renamed European History Quarterly, the title "
            "under which it still appears."
        ),
        url="https://en.wikipedia.org/wiki/European_History_Quarterly",
        sources=[
            "https://en.wikipedia.org/wiki/European_History_Quarterly",
        ]),
    "Evening Standard": dict(
        descr=(
            "London newspaper descended from The Standard, founded in 1827."
            " An evening edition began in 1859, and the paper has appeared "
            "under the Evening Standard name for much of its history. It "
            "covers London and national news, politics, business and the "
            "arts."
        ),
        url="https://www.standard.co.uk/",
        sources=[
            "https://en.wikipedia.org/wiki/Evening_Standard",
        ]),
    "Finnish Yearbook of Political Thought": dict(
        descr=(
            "Annual founded in 1997 by the Finnish publisher SoPhi at the "
            "University of Jyväskylä, covering political theory, rhetoric "
            "and conceptual history. It appeared under this title for "
            "volumes 1-7 (1997-2003), then was renamed Redescriptions in "
            "2004 and took on an international editorial board."
        ),
        url="https://journal-redescriptions.org/",
        sources=[
            "https://journal-redescriptions.org/about",
            "https://jyx.jyu.fi/handle/123456789/48139",
            "https://reseau-mirabel.info/revue/7084",
        ]),
    "Freeman": dict(
        descr=(
            "The Freeman was an American libertarian magazine of economics "
            "and politics, published by the Foundation for Economic "
            "Education from the mid-1950s until its last print issue in "
            "2016. It also appeared as The Freeman: Ideas on Liberty, and "
            "it promoted free markets, limited government and a non-"
            "interventionist foreign policy."
        ),
        url="https://en.wikipedia.org/wiki/The_Freeman_(magazine)",
        sources=[
            "https://en.wikipedia.org/wiki/The_Freeman_(magazine)",
        ]),
    "Gazette Telegraph (Colorado Springs)": dict(
        descr=(
            "Daily newspaper of Colorado Springs, Colorado, whose roots go "
            "back to The Colorado Springs Gazette of 1873. It was called "
            "the Gazette-Telegraph from a 1946 merger with the Evening "
            "Telegraph until 1997, when it became The Gazette."
        ),
        url="https://gazette.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Gazette_(Colorado_Springs)",
        ]),
    "Governance": dict(
        descr=(
            "Governance: An International Journal of Policy, "
            "Administration, and Institutions was founded in 1988 and is "
            "sponsored by the International Political Science Association's"
            " research committee on the structure and organization of "
            "government. It covers executive politics, public policy, "
            "public administration and the organization of the state."
        ),
        url="https://onlinelibrary.wiley.com/journal/14680491",
        sources=[
            "https://en.wikipedia.org/wiki/Governance_(journal)",
        ]),
    "Guardian": dict(
        descr=(
            "British national daily, founded in Manchester in 1821 as The "
            "Manchester Guardian. It was renamed The Guardian in 1959 and "
            "began printing in London in 1961. A liberal, broadly centre-"
            "left paper, it is regarded as one of Britain's newspapers of "
            "record."
        ),
        url="https://www.theguardian.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Guardian",
        ]),
    "Harper’s Magazine": dict(
        descr=(
            "American monthly founded in New York in 1850 by Harper & "
            "Brothers as Harper's New Monthly Magazine. One of the oldest "
            "general-interest magazines in the United States, it publishes "
            "essays, reporting, fiction and criticism on politics, society,"
            " culture and the arts."
        ),
        url="https://harpers.org/",
        sources=[
            "https://en.wikipedia.org/wiki/Harper%27s_Magazine",
        ]),
    "History": dict(
        descr=(
            "Journal of the Historical Association in the UK, founded in "
            "1912 and the Association's journal since 1916. It covers all "
            "periods and areas of historical scholarship, with original "
            "articles, historiographical surveys and an extensive book "
            "review section."
        ),
        url="https://onlinelibrary.wiley.com/journal/1468229x",
        sources=[
            "https://en.wikipedia.org/wiki/History_(journal)",
        ]),
    "History Teacher": dict(
        descr=(
            "The History Teacher is an American peer-reviewed quarterly "
            "published by the Society for History Education. It began in "
            "1940 as a bulletin at the University of Notre Dame and took "
            "its present form in 1967. It covers the teaching of history in"
            " schools, colleges and universities, with articles on "
            "historiography and reviews of textbooks and monographs."
        ),
        url="https://www.thehistoryteacher.org/",
        sources=[
            "https://en.wikipedia.org/wiki/The_History_Teacher",
        ]),
    "Hobbes Studies": dict(
        descr=(
            "Peer-reviewed journal founded in 1988 and devoted to Thomas "
            "Hobbes. It publishes research on his philosophical, political,"
            " historical, literary, religious and scientific ideas, and on "
            "how his work has been received."
        ),
        url="https://brill.com/view/journals/hobs/hobs-overview.xml",
        sources=[
            "https://en.wikipedia.org/wiki/Hobbes_Studies",
        ]),
    "Independent": dict(
        descr=(
            "British national newspaper founded in 1986 by three former "
            "Daily Telegraph journalists, Andreas Whittam Smith, Stephen "
            "Glover and Matthew Symonds, as a politically independent "
            "daily. It printed as a broadsheet and later as a compact, and "
            "has been online-only since its last print edition in March "
            "2016."
        ),
        url="https://www.independent.co.uk/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Independent",
        ]),
    "Indian Journal of Political Studies": dict(
        descr=(
            "Indian political science periodical issued from 1977 by the "
            "Department of Political Science of the University of Jodhpur, "
            "Rajasthan. It publishes scholarly articles on political "
            "science, practical politics and world affairs."
        ),
        sources=[
            "https://find.library.upenn.edu/catalog/991383503681",
        ]),
    "Intercollegiate Review": dict(
        descr=(
            "American conservative journal of ideas begun in 1965 by the "
            "Intercollegiate Society of Individualists and later published "
            "by its successor, the Intercollegiate Studies Institute, an "
            "organisation working with college students. Print issues ended"
            " in 2016, and the title was later relaunched online."
        ),
        url="https://intercollegiatereview.com/",
        sources=[
            "https://libcat.library.tamu.edu/Record/in00002787941/Description",
            "https://en.wikipedia.org/wiki/Intercollegiate_Studies_Institute",
            "https://blog.acton.org/?p=49334",
        ]),
    "International Affairs": dict(
        descr=(
            "Peer-reviewed international relations journal founded in 1922 "
            "by the Royal Institute of International Affairs (Chatham "
            "House) in London and published bimonthly by Oxford University "
            "Press. It pairs scholarly analysis with policy relevance and "
            "carries an extensive book review section ranging across "
            "disciplines and regions."
        ),
        url="https://academic.oup.com/ia",
        sources=[
            "https://en.wikipedia.org/wiki/International_Affairs_(journal)",
        ]),
    "International History Review": dict(
        descr=(
            "Peer-reviewed journal, founded by Edward Ingram, Gordon Martel"
            " and Ian Muggridge, that publishes research on the history of "
            "international relations and the history of international "
            "thought. It is published by Routledge."
        ),
        url="https://www.tandfonline.com/journals/rinh20",
        sources=[
            "https://en.wikipedia.org/wiki/The_International_History_Review",
        ]),
    "International Relations": dict(
        descr=(
            "Quarterly peer-reviewed journal of international relations "
            "founded in 1960 and published by SAGE in association with the "
            "David Davies Memorial Institute. Alongside research articles "
            "it runs review essays, interviews, debates and forums on world"
            " politics."
        ),
        url="https://journals.sagepub.com/home/ire",
        sources=[
            "https://en.wikipedia.org/wiki/International_Relations_(journal)",
        ]),
    "International Studies in Philosophy": dict(
        descr=(
            "Peer-reviewed philosophy journal founded in 1969 by Augusto "
            "Guzzo and Giorgio Tonelli as Studi Internazionali di "
            "Filosofia, renamed in 1974. Edited for many years at SUNY "
            "Binghamton, it printed articles mainly in English, with some "
            "in Italian, French and German. Publication was suspended in "
            "2008; the Philosophy Documentation Center took it over in "
            "2011."
        ),
        url="https://www.pdcnet.org/intstudphil",
        sources=[
            "https://en.wikipedia.org/wiki/International_Studies_in_Philosophy",
            "https://pdcnet.org/intstudphil",
        ]),
    "Irish Educational Studies": dict(
        descr=(
            "Refereed journal associated with the Educational Studies "
            "Association of Ireland and published by Taylor & Francis. It "
            "covers education from primary schooling to higher education, "
            "drawing on sociology, psychology, history, philosophy, "
            "politics, economics and curriculum studies, and links Irish "
            "questions to international debates."
        ),
        url="https://www.tandfonline.com/journals/ries20",
        sources=[
            "https://www.tandfonline.com/journals/ries20/about-this-journal",
            "https://files.taylorandfrancis.com/ries-cfp.pdf",
        ]),
    "Jahrbuch für die idealistische Philosophie": dict(
        descr=(
            "German-language yearbook devoted to idealist philosophy, "
            "issued under the title Idealismus: Jahrbuch für die "
            "idealistische Philosophie. It was edited by Ernst Harms, and "
            "its first volume was published in 1934 by Rascher in Zürich."
        ),
        sources=[
            "https://cambridge.org/core/journals/philosophy/article/abs/idealismus-jahrbuch-fur-die-idealistische-philosophie-edited-by-ernst-harms-vol-i-zurich-rascher-co1934-pp-280-price-10-mks/48E60FCC1F30F448875DF5C1AD066D1E",
        ]),
    "Journal for the Theory of Social Behaviour": dict(
        descr=(
            "Quarterly peer-reviewed journal founded in 1971 by Rom Harré "
            "and Paul Secord to promote an alternative to the positivist "
            "approach then common in social psychology. It publishes "
            "theoretical work on the study of social behaviour and is "
            "published by Wiley-Blackwell."
        ),
        url="https://onlinelibrary.wiley.com/journal/14685914",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_for_the_Theory_of_Social_Behaviour",
        ]),
    "Journal of Applied Philosophy": dict(
        descr=(
            "Peer-reviewed journal founded in 1984 and published by Wiley-"
            "Blackwell on behalf of the Society for Applied Philosophy. It "
            "applies philosophical analysis to practical questions in areas"
            " such as medicine, the environment, science, law, politics, "
            "economics and education."
        ),
        url="https://onlinelibrary.wiley.com/journal/14685930",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_of_Applied_Philosophy",
        ]),
    "Journal of Classical Sociology": dict(
        descr=(
            "Quarterly peer-reviewed journal, founded in 2001 and published"
            " by SAGE, that covers all aspects of classical sociology, from"
            " the discipline's founding thinkers and the history of social "
            "theory to the bearing of classical ideas on current debate."
        ),
        url="https://journals.sagepub.com/home/jcs",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_of_Classical_Sociology",
        ]),
    "Journal of Educational Administration and History": dict(
        descr=(
            "Journal founded in 1968 at the University of Leeds, under its "
            "Department of Education, and later published by Routledge. It "
            "studies educational leadership, administration and policy, "
            "chiefly from a historical angle but also through other "
            "approaches drawing on economics, philosophy, politics and "
            "sociology."
        ),
        url="https://www.tandfonline.com/journals/cjeh20",
        sources=[
            "https://www.tandfonline.com/journals/cjeh20/about-this-journal",
            "https://ci.nii.ac.jp/ncid/AA00251797?l=en",
        ]),
    "Journal of Educational Thought": dict(
        descr=(
            "Canadian journal published since 1967 by the Faculty of "
            "Education (now Werklund School of Education) at the University"
            " of Calgary. It carries speculative, critical and historical "
            "writing on the theory and practice of education, covering "
            "philosophy, curriculum, administration, comparative education,"
            " psychology and sociology."
        ),
        url="https://journalhosting.ucalgary.ca/index.php/jet",
        sources=[
            "https://journalhosting.ucalgary.ca/index.php/jet/about",
            "https://werklund.ucalgary.ca/JET",
        ]),
    "Journal of Indian Council of Philosophical Research": dict(
        descr=(
            "Refereed philosophy journal of the Indian Council of "
            "Philosophical Research, a body set up in 1977 by India's "
            "Ministry of Education. The journal began in 1983 under "
            "founding editor D. P. Chattopadhyaya; Springer has published "
            "it since 2015."
        ),
        url="https://link.springer.com/journal/40961",
        sources=[
            "https://icpr.in/historical-profile",
            "https://heibib.ub.uni-heidelberg.de/search/Record/169133893/Details",
            "https://portal.issn.org/resource/ISSN/2363-9962",
        ]),
    "Journal of International Relations and Development": dict(
        descr=(
            "Peer-reviewed journal of international relations and "
            "international political economy, begun in 1984 to promote "
            "scholarship by Central and East European authors. In the late "
            "1990s it was relaunched as the official journal of the Central"
            " and East European International Studies Association, linked "
            "to the University of Ljubljana's Centre of International "
            "Relations."
        ),
        url="https://link.springer.com/journal/41268",
        sources=[
            "https://www.fdv.uni-lj.si/en/research/research-centres/department-of-political-science/centre-of-international-relations/news/journal-of-international-relations-and-development",
        ]),
    "Journal of Philosophical Research": dict(
        descr=(
            "Annual peer-reviewed philosophy journal published by the non-"
            "profit Philosophy Documentation Center. It began in 1975 as "
            "Philosophy Research Archives and accepts articles in English "
            "or French from any philosophical orientation and in every area"
            " of the discipline."
        ),
        url="https://www.pdcnet.org/jpr",
        sources=[
            "https://www.pdcnet.org/jpr",
            "https://en.wikipedia.org/wiki/Journal_of_Philosophical_Research",
        ]),
    "Journal of Philosophical Studies": dict(
        descr=(
            "British philosophy journal launched in January 1926 by the "
            "British Institute of Philosophical Studies and published by "
            "Macmillan. In 1931 it was renamed Philosophy, the title under "
            "which it continues as the journal of the Royal Institute of "
            "Philosophy."
        ),
        url="https://en.wikipedia.org/wiki/Philosophy_(journal)",
        sources=[
            "https://royalinstitutephilosophy.org/timeline/",
            "https://wellcomecollection.org/works/sypaj78x",
            "https://en.wikipedia.org/wiki/Philosophy_(journal)",
        ]),
    "Journal of Political Economy": dict(
        descr=(
            "Peer-reviewed economics journal founded in 1892 by J. Laurence"
            " Laughlin at the University of Chicago and published by the "
            "University of Chicago Press. It covers both theoretical and "
            "empirical economics."
        ),
        url="https://www.journals.uchicago.edu/toc/jpe/current",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_of_Political_Economy",
        ]),
    "Journal of the British Society for Phenomenology": dict(
        descr=(
            "Journal of the British Society for Phenomenology, a society "
            "founded in 1967 by Wolfe Mays. It publishes work on "
            "phenomenology and existential philosophy, together with "
            "related contributions from other areas of philosophy, the "
            "humanities and the human sciences. It is now published by "
            "Taylor & Francis."
        ),
        url="https://www.tandfonline.com/journals/rbsp20",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_of_the_British_Society_for_Phenomenology",
        ]),
    "Journal of the History of Philosophy": dict(
        descr=(
            "Quarterly peer-reviewed journal founded in 1963 and sponsored "
            "by the Eastern Division of the American Philosophical "
            "Association. It covers the history of Western philosophy from "
            "antiquity to the modern era and is published by Johns Hopkins "
            "University Press."
        ),
        url="https://www.press.jhu.edu/journals/journal-history-philosophy",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_of_the_History_of_Philosophy",
        ]),
    "Journal of the Philosophy of History": dict(
        descr=(
            "Peer-reviewed journal founded in 2007 by Frank Ankersmit and "
            "published by Brill three times a year. It examines history and"
            " historiography philosophically: knowledge of the past, "
            "historical explanation and understanding, and the ethics and "
            "aesthetics of history-writing. It also runs reviews and review"
            " essays."
        ),
        url="https://brill.com/view/journals/jph/jph-overview.xml",
        sources=[
            "https://en.wikipedia.org/wiki/Journal_of_the_Philosophy_of_History",
        ]),
    "Kenton, OH Times": dict(
        descr=(
            "The Kenton Times, a daily newspaper in Kenton, the county seat"
            " of Hardin County in northwest Ohio. It was formed in 1953 by "
            "merging the Kenton Daily Democrat with the Kenton News and "
            "Republican, and it covers local news, sports and civic "
            "affairs."
        ),
        url="https://www.kentontimes.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Kenton_Times",
        ]),
    "LSE": dict(
        descr=(
            "L.S.E.: The Magazine of the London School of Economics and "
            "Political Science, the School's own periodical, published in "
            "London from at least the 1960s. It was later continued under "
            "the title LSE Magazine."
        ),
        sources=[
            "https://dev-www.nypl.org/research/research-catalog/bib/b10916816",
        ]),
    "LSE Magazine": dict(
        descr=(
            "Magazine of the London School of Economics and Political "
            "Science for its alumni, continuing the earlier L.S.E. magazine"
            " and later succeeded by LSE Connect. It carried School news "
            "and articles by LSE academics on current affairs and policy."
        ),
        sources=[
            "https://europeansources.info/eso_tax_series_titles/lse-magazine",
            "https://dev-www.nypl.org/research/research-catalog/bib/b10916816",
            "https://econbiz.de/Record/lse-magazine-the-alumni-magazine-of-the-london-school-of-economics-and-political-science/10004905106",
        ]),
    "Law Quarterly Review": dict(
        descr=(
            "Peer-reviewed quarterly law journal founded in 1885 with Sir "
            "Frederick Pollock, Corpus Professor of Jurisprudence at "
            "Oxford, as its first editor, and published by Sweet & Maxwell."
            " It publishes scholarship on the common law throughout the "
            "world."
        ),
        url="https://en.wikipedia.org/wiki/Law_Quarterly_Review",
        sources=[
            "https://en.wikipedia.org/wiki/Law_Quarterly_Review",
        ]),
    "Law, Culture and the Humanities": dict(
        descr=(
            "Peer-reviewed journal founded in 2005, published by SAGE for "
            "the Association for the Study of Law, Culture and the "
            "Humanities. Appearing three times a year, it treats law as a "
            "humanistic subject, with work on legal history, legal theory "
            "and jurisprudence, law and literature, law and cultural "
            "studies, and legal hermeneutics."
        ),
        url="http://lch.sagepub.com/",
        sources=[
            "https://en.wikipedia.org/wiki/Law,_Culture_and_the_Humanities",
        ]),
    "London Quarterly and Holborn Review": dict(
        descr=(
            "British Methodist quarterly published by the Epworth Press "
            "from 1932 to 1968. It was formed when the London Quarterly "
            "Review merged with the Holborn Review, and covered theology, "
            "church affairs, literature and ideas. In 1968 it merged with "
            "the Church Quarterly Review to form The Church Quarterly."
        ),
        sources=[
            "https://preview.wellcomecollection.org/works/px3p4n74",
            "https://en.wikipedia.org/wiki/The_Church_Quarterly_Review",
            "https://libcat.library.tamu.edu/Record/in00003226992/Description",
        ]),
    "London Review of Books": dict(
        descr=(
            "British literary magazine founded in 1979 and published twice "
            "a month. Most of its content is long essays framed as book "
            "reviews of fiction and non-fiction. It also runs political and"
            " social essays and short pieces on film and exhibitions."
        ),
        url="https://www.lrb.co.uk/",
        sources=[
            "https://en.wikipedia.org/wiki/London_Review_of_Books",
        ]),
    "Merkur": dict(
        descr=(
            "German monthly review of ideas founded in 1947 and published "
            'in Stuttgart, subtitled "Deutsche Zeitschrift für europäisches'
            ' Denken" (German journal for European thought). It carries '
            "essays and criticism on politics, philosophy, literature, "
            "culture and society, and is one of Germany's leading "
            "intellectual periodicals."
        ),
        url="https://www.merkur-zeitschrift.de/",
        sources=[
            "https://en.wikipedia.org/wiki/Merkur_(magazine)",
        ]),
    "Metaphilosophy": dict(
        descr=(
            "Peer-reviewed philosophy journal founded in 1970 by Terrell "
            "Ward Bynum and Richard Reese, published by Wiley-Blackwell. It"
            " covers philosophy about philosophy: the nature, aims and "
            "methods of the discipline, its relation to other fields, and "
            "why philosophical questions so seldom reach agreed answers."
        ),
        url="https://onlinelibrary.wiley.com/journal/14679973",
        sources=[
            "https://en.wikipedia.org/wiki/Metaphilosophy_(journal)",
        ]),
    "Methodist Recorder": dict(
        descr=(
            "Independent British weekly newspaper founded in 1861 and "
            "published continuously since then. It covers news and current "
            "affairs in the Methodist community, both in Britain and in "
            "Methodist churches around the world."
        ),
        url="http://www.methodistrecorder.co.uk/",
        sources=[
            "https://en.wikipedia.org/wiki/Methodist_Recorder",
            "https://britishonlinearchives.com/download-media/640",
        ]),
    "Modern Review (Calcutta)": dict(
        descr=(
            "English-language monthly founded in Calcutta in 1907 by "
            "Ramananda Chatterjee, who edited it for decades, and published"
            " until 1995. Aimed at English-reading Indians, it became a "
            "leading forum for the nationalist intelligentsia, carrying "
            "essays on politics, society, literature and the arts."
        ),
        url="https://en.wikipedia.org/wiki/Modern_Review_(Calcutta)",
        sources=[
            "https://en.wikipedia.org/wiki/Modern_Review_(Calcutta)",
            "https://en.wikipedia.org/wiki/The_Modern_Review",
        ]),
    "Modern Schoolman": dict(
        descr=(
            "Peer-reviewed philosophy quarterly founded in 1925 and "
            "published by the Department of Philosophy at Saint Louis "
            "University. It published articles and reviews across the major"
            " areas of philosophy, ancient to modern, and was renamed Res "
            "Philosophica in 2013."
        ),
        url="http://www.resphilosophica.org/",
        sources=[
            "https://en.wikipedia.org/wiki/Res_Philosophica",
        ]),
    "Nation": dict(
        descr=(
            "American magazine of politics and culture founded in 1865, "
            "published weekly for most of its history. Progressive and "
            "left-leaning, it covers politics and current affairs alongside"
            " the arts, law, the environment and international affairs."
        ),
        url="https://www.thenation.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Nation",
        ]),
    "National Interest": dict(
        descr=(
            "American magazine of international affairs founded in 1985 by "
            "Irving Kristol. Associated with the realist school of foreign "
            "policy, it publishes essays and commentary on international "
            "relations, strategy, diplomacy and American foreign policy."
        ),
        url="https://nationalinterest.org/",
        sources=[
            "https://en.wikipedia.org/wiki/The_National_Interest",
        ]),
    "New Era in Home and School": dict(
        descr=(
            "Journal of the New Education Fellowship (from 1966 the World "
            "Education Fellowship), the international progressive-education"
            " movement. It began in 1920 as Education for the New Era, "
            "edited by Beatrice Ensor, and was later retitled The New Era "
            "in Education. It covered child-centred schooling, educational "
            "reform and teaching practice."
        ),
        sources=[
            "https://archiveshub.ac.uk/search/archives/bbe8e28c-281e-3436-a8a6-a9ad1f719f63",
            "https://libcat.library.tamu.edu/Record/in00000229623/Description",
            "https://archives.ucl.ac.uk/CalmView/rdf/catalog/WEF/B/6/1/18",
        ]),
    "New Left Review": dict(
        descr=(
            "British journal of the left founded in 1960 when the editorial"
            " boards of The New Reasoner and Universities and Left Review "
            "merged. Published every two months, it covers world politics, "
            "the global economy, social theory, philosophy and culture from"
            " a socialist perspective."
        ),
        url="https://newleftreview.org/",
        sources=[
            "https://en.wikipedia.org/wiki/New_Left_Review",
        ]),
    "New Literary History": dict(
        descr=(
            "Journal of theory and interpretation founded in 1969 by Ralph "
            "Cohen at the University of Virginia and published by Johns "
            "Hopkins University Press. It prints essays on literary theory,"
            " literary history and interpretation, and welcomes work from "
            "other disciplines that bears on the study of literature and "
            "culture."
        ),
        url="http://newliteraryhistory.org/",
        sources=[
            "https://en.wikipedia.org/wiki/New_Literary_History",
        ]),
    "New York Review of Books": dict(
        descr=(
            "American magazine founded in 1963 by Robert Silvers and "
            "Barbara Epstein, published about twenty times a year. It is "
            "best known for long review-essays on books, and also covers "
            "literature, culture, politics, science and current affairs."
        ),
        url="https://www.nybooks.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_New_York_Review_of_Books",
        ]),
    "New York Times": dict(
        descr=(
            "American daily newspaper founded in 1851 and based in New York"
            " City, reporting national and international news, with "
            "opinion, cultural coverage and book reviews."
        ),
        url="https://www.nytimes.com/",
        sources=[
            "https://en.wikipedia.org/wiki/The_New_York_Times",
        ]),
    "News Weekly": dict(
        descr=(
            "Australian conservative magazine published by the National "
            "Civic Council, a Christian lobby group. It was first published"
            " in 1943 under the title Freedom, and covers politics, social "
            "and family policy, religion and international affairs from "
            "that organisation's standpoint."
        ),
        url="https://www.newsweekly.com.au/",
        sources=[
            "https://en.wikipedia.org/wiki/News_Weekly",
        ]),
    "Nottingham Guardian": dict(
        descr=(
            "Daily newspaper in Nottingham, England, published under this "
            "title from 1905 to 1953, continuing the Nottingham Daily "
            "Guardian (1861–1905). In 1953 it merged with the Nottingham "
            "Journal to form the Guardian Journal, which ran until 1973."
        ),
        url="https://en.wikipedia.org/wiki/Nottingham_Guardian",
        sources=[
            "https://en.wikipedia.org/wiki/Nottingham_Guardian",
            "https://en.wikipedia.org/wiki/Nottingham_Journal",
        ]),
    "Observer": dict(
        descr=(
            "British Sunday newspaper first published in 1791, described as"
            " the world's oldest Sunday newspaper. For many years the "
            "Sunday sister paper of The Guardian, it covers news, politics,"
            " culture and books."
        ),
        url="https://observer.co.uk/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Observer",
        ]),
    "Oideas": dict(
        descr=(
            "Journal of the Irish Department of Education, published from "
            "1968 to 2010. It carried articles by department staff and "
            "outside writers on education in Ireland, including policy, "
            "curriculum, teaching and educational thought. The views "
            "expressed were the authors' own, not official policy."
        ),
        sources=[
            "https://www.bildungsserver.de/kurznachricht_e.html?nummer=312",
            "https://www.dcu.ie/sites/default/files/carpe/O%27Leary%20%282006%29.pdf",
        ]),
    "Osgoode Hall Law Journal": dict(
        descr=(
            "Peer-reviewed Canadian law journal published by Osgoode Hall "
            "Law School of York University in Toronto, in continuous "
            "publication since 1958. It publishes legal scholarship across "
            "the field and is known for interdisciplinary work."
        ),
        url="https://digitalcommons.osgoode.yorku.ca/ohlj/",
        sources=[
            "https://en.wikipedia.org/wiki/Osgoode_Hall_Law_Journal",
            "https://digitalcommons.osgoode.yorku.ca/ohlj/",
        ]),
    "Oxford Magazine": dict(
        descr=(
            "Review magazine published in Oxford since 1883, traditionally "
            "weekly in term time and distributed with the University "
            "Gazette. It comments on University of Oxford affairs, serving "
            "as a forum where members of Congregation debate academic "
            "policy, and also prints poetry and essays. Past contributors "
            "include Tolkien, Auden and Dorothy L. Sayers."
        ),
        url="https://en.wikipedia.org/wiki/Oxford_Magazine",
        sources=[
            "https://en.wikipedia.org/wiki/Oxford_Magazine",
        ]),
    "Oxford Times": dict(
        descr=(
            "Weekly local newspaper for Oxford and Oxfordshire, founded in "
            "1862 as a broadsheet and now in compact format. It reports "
            "local news, culture and community affairs; in 1922 it printed "
            "an early private edition of T. E. Lawrence's Seven Pillars of "
            "Wisdom."
        ),
        url="https://en.wikipedia.org/wiki/The_Oxford_Times",
        sources=[
            "https://en.wikipedia.org/wiki/The_Oxford_Times",
        ]),
    "Partisan Review": dict(
        descr=(
            "American literary and political quarterly founded in New York "
            "in 1934 and edited for decades by Philip Rahv and William "
            "Phillips. Starting in the Communist orbit, it turned anti-"
            "Stalinist in 1937 and became a leading voice of the New York "
            "Intellectuals in literature, politics and culture. Later based"
            " at Rutgers and then Boston University, it ceased in 2003."
        ),
        url="https://en.wikipedia.org/wiki/Partisan_Review",
        sources=[
            "https://en.wikipedia.org/wiki/Partisan_Review",
        ]),
    "Philosophical Review": dict(
        descr=(
            "Quarterly philosophy journal published continuously since 1892"
            " and edited by the Sage School of Philosophy at Cornell "
            "University, now with Duke University Press. It publishes "
            "original articles across analytic philosophy on topics of "
            "broad interest to philosophers, together with book reviews."
        ),
        url="https://read.dukeupress.edu/the-philosophical-review",
        sources=[
            "https://en.wikipedia.org/wiki/The_Philosophical_Review",
        ]),
    "Philosophisches Jahrbuch": dict(
        descr=(
            "German philosophy journal founded in 1888 under the auspices "
            "of the Görres-Gesellschaft, a Catholic learned society, and "
            "published by Verlag Karl Alber since 1953. Appearing twice a "
            "year, it is peer reviewed and covers a broad range of "
            "systematic and historical philosophy."
        ),
        sources=[
            "https://relbib.de/Record/129075310/Details",
            "https://verlag-alber.de/en/journals/",
        ]),
    "Philosophy in Review": dict(
        descr=(
            "Open-access online journal that publishes reviews of new books"
            " in all areas of and approaches to philosophy. Founded in 1981"
            " as Canadian Philosophical Reviews, it took its present name "
            "in 1997 and has been published by the University of Victoria "
            "in Canada since 2010."
        ),
        url="https://journals.uvic.ca/index.php/pir/index",
        sources=[
            "https://en.wikipedia.org/wiki/Philosophy_in_Review",
        ]),
    "Poetry Review": dict(
        descr=(
            "Poetry magazine of the Poetry Society in London, founded in "
            "1912 and quarterly since 1952. It publishes new poems, essays "
            "and reviews, and has printed work by Hardy, Frost, Pound, "
            "Auden, Larkin and many others."
        ),
        url="https://poetrysociety.org.uk/publications-section/the-poetry-review/",
        sources=[
            "https://en.wikipedia.org/wiki/The_Poetry_Review",
        ]),
    "Policy: A Journal of Public Policy and Ideas": dict(
        descr=(
            "Quarterly magazine of the Centre for Independent Studies, a "
            "classical-liberal think tank in Australia and New Zealand. It "
            "ran essays on public policy, economics, politics and ideas in "
            "a scholarly but accessible style, and ceased publication in "
            "2018."
        ),
        sources=[
            "https://devfeature-collection.sl.nsw.gov.au/record/74VvGBQKa0gg",
            "https://www.cis.org.au/app/uploads/2018/06/policy-winter18-editorial.pdf",
        ]),
    "Political Quarterly": dict(
        descr=(
            "British journal of politics and public policy, first published"
            " in 1914 and refounded in 1930 by Leonard Woolf, Kingsley "
            "Martin and William Robson. It publishes accessible, plainly "
            "written articles on UK and international politics and policy "
            "for both academic and general readers."
        ),
        url="https://politicalquarterly.org.uk",
        sources=[
            "https://en.wikipedia.org/wiki/The_Political_Quarterly",
        ]),
    "Politics": dict(
        descr=(
            "Peer-reviewed journal of the Political Studies Association of "
            "the UK, published with SAGE. A generalist journal, it "
            "publishes original research and teaching-related scholarship "
            "across politics, political theory and international studies, "
            "open to all approaches and methods."
        ),
        url="https://journals.sagepub.com/home/pol",
        sources=[
            "https://www.sagepub.com/en-gb/afr/politics/journal202481",
        ]),
    "Politisches Denken": dict(
        descr=(
            "German yearbook of political thought (Jahrbuch Politisches "
            "Denken), published since 1991 in cooperation with the Deutsche"
            " Gesellschaft zur Erforschung des Politischen Denkens and "
            "issued by Duncker & Humblot. It carries peer-reviewed "
            "interdisciplinary research on political thought and its "
            "relation to political practice."
        ),
        url="https://elibrary.duncker-humblot.com/zeitschriften/jpd",
        sources=[
            "https://www.duncker-humblot.de/en/zeitschrift/jahrbuch-politisches-denken-jpd-25/?page_id=0",
            "https://elibrary.duncker-humblot.com/zeitschriften/jpd",
        ]),
    "Presidential Studies Quarterly": dict(
        descr=(
            "Quarterly peer-reviewed political science journal devoted to "
            "the scholarly study of the American presidency, published for "
            "the Center for the Study of the Presidency and Congress. It "
            "began in 1971 as Center House Bulletin and took its present "
            "name in 1974."
        ),
        url="https://onlinelibrary.wiley.com/journal/17415705",
        sources=[
            "https://en.wikipedia.org/wiki/Presidential_Studies_Quarterly",
        ]),
    "Proceedings of the British Academy": dict(
        descr=(
            "Series published by the British Academy since 1905. Until 1991"
            " its annual volumes held lectures, papers read at the Academy "
            "and memoirs (obituaries) of deceased Fellows; since 1992 it "
            "has issued themed volumes of essays, often from Academy "
            "conferences, while memoirs moved to a separate series."
        ),
        url="https://www.thebritishacademy.ac.uk/publishing/proceedings-british-academy/",
        sources=[
            "https://en.wikipedia.org/wiki/Proceedings_of_the_British_Academy",
        ]),
    "Public Administration": dict(
        descr=(
            "Peer-reviewed quarterly journal founded by the Royal Institute"
            " of Public Administration in the UK, first issued in 1923 as "
            "the Journal of Public Administration. It publishes research, "
            "theory and practice in public administration, public policy, "
            "public management and the theory of public organizations."
        ),
        url="https://onlinelibrary.wiley.com/journal/14679299",
        sources=[
            "https://en.wikipedia.org/wiki/Public_Administration_(journal)",
        ]),
    "Publishers Weekly": dict(
        descr=(
            "American weekly trade magazine of the book business, founded "
            "in 1872 by Frederick Leypoldt. Aimed at publishers, "
            "booksellers, librarians and literary agents, it reports "
            "industry news and is best known for its prepublication reviews"
            " of new books."
        ),
        url="https://www.publishersweekly.com",
        sources=[
            "https://en.wikipedia.org/wiki/Publishers_Weekly",
        ]),
    "Queen’s Quarterly": dict(
        descr=(
            "Canadian quarterly of literary and academic writing on "
            "cultural topics, published by Queen's University at Kingston, "
            "Ontario, since 1893. It prints essays, articles, reviews, "
            "short stories and poetry."
        ),
        url="https://www.queensu.ca/quarterly/",
        sources=[
            "https://en.wikipedia.org/wiki/Queen%27s_Quarterly",
        ]),
    "Radical Philosophy": dict(
        descr=(
            "British journal of socialist and feminist philosophy, founded "
            "in 1972 as a forum for theoretical work arising from the "
            "radical movements of the 1960s. Run by an editorial collective"
            " and broadly associated with the New Left, it publishes "
            "articles, reviews and commentary in critical theory and "
            "philosophy; it is now open access."
        ),
        url="https://www.radicalphilosophy.com",
        sources=[
            "https://en.wikipedia.org/wiki/Radical_Philosophy",
        ]),
    "Ratio Juris": dict(
        descr=(
            "International quarterly journal of jurisprudence and "
            "philosophy of law, associated with the University of Bologna. "
            "It offers a cross-cultural forum for philosophical work on "
            "law, welcoming contributors from legal, philosophical, "
            "political, cultural and linguistic backgrounds."
        ),
        url="https://onlinelibrary.wiley.com/journal/14679337",
        sources=[
            "https://international.vlex.com/vid/issue-information-1116619504",
        ]),
    "Redescriptions": dict(
        descr=(
            "Peer-reviewed open-access journal on political thought, "
            "conceptual history and feminist theory, begun in 1997 as a "
            "yearbook. Named after a rhetorical move that alters how a "
            "concept is used, it studies conceptual change and political "
            "agency across disciplines. It is now published by Helsinki "
            "University Press."
        ),
        url="https://www.journal-redescriptions.org",
        sources=[
            "https://reference-global.com/journal/UHJRPTCHFT",
            "https://www.hup.fi/site/journals",
        ]),
    "Revue Française de Science Politique": dict(
        descr=(
            "Leading French journal of political science and political "
            "sociology, founded in 1951 by the Fondation nationale des "
            "sciences politiques and the Association française de science "
            "politique and published by Presses de Sciences Po. It appears "
            "six times a year."
        ),
        url="https://fr.wikipedia.org/wiki/Revue_fran%C3%A7aise_de_science_politique",
        sources=[
            "https://fr.wikipedia.org/wiki/Revue_fran%C3%A7aise_de_science_politique",
        ]),
    "Revue de Métaphysique et de Morale": dict(
        descr=(
            "French philosophy journal founded in 1893 by Xavier Léon, Léon"
            " Brunschvicg and Élie Halévy, quarterly since 1920 and "
            "published by Presses Universitaires de France. It runs "
            "thematic dossiers, individual articles, critical discussions "
            "and reviews on current philosophical debates and the history "
            "of philosophy."
        ),
        url="https://en.wikipedia.org/wiki/Revue_de_m%C3%A9taphysique_et_de_morale",
        sources=[
            "https://en.wikipedia.org/wiki/Revue_de_m%C3%A9taphysique_et_de_morale",
            "https://univ-droit.fr/recherche/actualites-de-la-recherche/parutions/20534-revue-de-metaphysique-et-de-morale-41711",
        ]),
    "Rivista di Storia Della Filosofia": dict(
        descr=(
            "Italian quarterly on the history of philosophy, founded in "
            "1946 by Mario Dal Pra and published by FrancoAngeli. It "
            "combines philosophical history with philologically careful "
            "research and has issued monographic numbers on figures such as"
            " Hume, Kant, Hegel and Quine."
        ),
        url="https://francoangeli.it/riviste/sommario/45",
        sources=[
            "https://francoangeli.it/riviste/sommario/45",
        ]),
    "Sartre Studies International": dict(
        descr=(
            "Peer-reviewed journal founded in 1997 and published twice a "
            "year by Berghahn Books with the UK and North American Sartre "
            "societies. It covers philosophical, literary and political "
            "questions arising from existentialism and the work of Jean-"
            "Paul Sartre, with reviews and news of related events."
        ),
        url="https://www.berghahnjournals.com/view/journals/sartre-studies/sartre-studies-overview.xml",
        sources=[
            "https://en.wikipedia.org/wiki/Sartre_Studies_International",
        ]),
    "Simmel Studies": dict(
        descr=(
            "Journal of the Georg Simmel-Gesellschaft, devoted to research "
            "on the sociologist and philosopher Georg Simmel and work "
            "inspired by him. Founded by Otthein Rammstedt at Bielefeld as "
            "the Simmel Newsletter, it became a journal and, after a pause "
            "from 2009, was relaunched as a digital new series."
        ),
        url="https://simmelstudies.org",
        sources=[
            "https://erudit.org/en/journals/sst/",
            "https://simmelstudies.org/",
        ]),
    "Social Science Journal": dict(
        descr=(
            "The Social Science Journal is the official peer-reviewed "
            "quarterly of the Western Social Science Association. It "
            "publishes scholarly work across the social sciences, broadly "
            "understood, drawing authors from many countries, and carries "
            "research notes on work in progress as well as a book review "
            "section."
        ),
        url="https://www.tandfonline.com/journals/ussj20",
        sources=[
            "https://www.tandfonline.com/journals/ussj20/about-this-journal",
            "https://wssaweb.com/journal",
        ]),
    "Social Science Quarterly": dict(
        descr=(
            "Social Science Quarterly is the journal of the Southwestern "
            "Social Science Association. It began in 1920 as the "
            "Southwestern Political Science Quarterly and took its present "
            "name in 1968 to stress an interdisciplinary rather than "
            "regional focus. It covers political science, sociology, "
            "economics, history, geography and related fields, favouring "
            "work that bridges disciplines."
        ),
        url="https://onlinelibrary.wiley.com/journal/15406237",
        sources=[
            "https://www.sudoc.fr/083850694",
            "https://collections.briscoecenter.org/repositories/2/resources/2416",
        ]),
    "Studies in Comparative Communism": dict(
        descr=(
            "Studies in Comparative Communism was a scholarly journal "
            "comparing communist political systems, published under that "
            "title from 1968 to 1992. It succeeded Communist Affairs and, "
            "after the collapse of the Soviet bloc, was renamed Communist "
            "and Post-Communist Studies in 1993, widening its scope to "
            "post-communist transformation."
        ),
        url="https://en.wikipedia.org/wiki/Communist_and_Post-Communist_Studies",
        sources=[
            "https://en.wikipedia.org/wiki/Communist_and_Post-Communist_Studies",
            "https://www.jstor.org/journals/00393592",
        ]),
    "Studies: An Irish Quarterly Review": dict(
        descr=(
            "Studies is a quarterly review published by the Irish Jesuits "
            "since 1912. It examines Irish social, political, cultural and "
            "economic questions from a Christian perspective and also "
            "carries essays on literature, history, philosophy and "
            "religion. Contributors over the years have included Patrick "
            "Pearse, Sean Lemass and J. M. Keynes."
        ),
        url="https://www.studiesirishreview.ie",
        sources=[
            "https://en.wikipedia.org/wiki/Studies_(journal)",
            "https://www.studiesirishreview.ie/history/",
        ]),
    "Studium Generale": dict(
        descr=(
            "Studium Generale was a German interdisciplinary journal "
            "published by Springer in Berlin from 1947 to 1971. Its "
            "subtitle described it as a journal for the unity of the "
            "sciences, their philosophical foundations and consequences, "
            "and it brought together contributions from the natural "
            "sciences, humanities and philosophy."
        ),
        sources=[
            "https://katalog.lib.cas.cz/Record/000453739",
        ]),
    "Sunday Times": dict(
        descr=(
            "The Sunday Times is a British national Sunday newspaper, "
            "founded in 1821 as The New Observer and renamed The Sunday "
            "Times in 1822. A quality paper known for investigative "
            "reporting, it covers news, politics, business, culture and "
            "books. It has shared ownership with The Times since 1966."
        ),
        url="https://www.thetimes.com",
        sources=[
            "https://en.wikipedia.org/wiki/The_Sunday_Times",
        ]),
    "Synthesis Philosophica": dict(
        descr=(
            "Synthesis Philosophica is the international journal of the "
            "Croatian Philosophical Society in Zagreb, published twice a "
            "year since 1986. Conceived as a journal for integrative "
            "thought, it welcomes a plurality of philosophical positions "
            "and neglected topics, and publishes peer-reviewed articles and"
            " book reviews in English, German and French."
        ),
        url="https://hrcak.srce.hr/synthesis-philosophica",
        sources=[
            "https://www.hrfd.hr/synthesis-philosophica/",
            "https://hrcak.srce.hr/synthesis-philosophica",
        ]),
    "The American Conservative": dict(
        descr=(
            "The American Conservative is an American magazine of politics,"
            " foreign affairs and culture, founded in 2002 by Pat Buchanan,"
            " Scott McConnell and Taki Theodoracopulos partly in opposition"
            " to the Iraq War. It is associated with traditionalist and "
            "paleoconservative views, including a non-interventionist "
            "foreign policy, and is based in Washington, D.C."
        ),
        url="https://www.theamericanconservative.com",
        sources=[
            "https://en.wikipedia.org/wiki/The_American_Conservative",
            "https://www.theamericanconservative.com/about-us/",
        ]),
    "The University Bookman": dict(
        descr=(
            "The University Bookman is a conservative review of books "
            "founded by Russell Kirk in 1960, who edited it from his home "
            "in Mecosta, Michigan, until his death. Originally a quarterly "
            "devoted almost entirely to book reviews, it is published by "
            "the Russell Kirk Center and discusses books bearing on "
            "culture, education and the common good."
        ),
        url="https://kirkcenter.org/bookman/",
        sources=[
            "https://kirkcenter.org/essays/defending-the-right-and-the-good/",
            "https://kirkcenter.org/highlights/the-university-bookman-at-60-a-retrospective/",
        ]),
    "Triumph": dict(
        descr=(
            "Triumph was a monthly American magazine published by L. Brent "
            "Bozell Jr. from 1966 to 1976. Written from a traditionalist "
            "Catholic perspective, it offered commentary on religious, "
            "philosophical, political and cultural questions and became a "
            "voice of the Catholic right after the Second Vatican Council."
        ),
        url="https://en.wikipedia.org/wiki/Triumph_(magazine)",
        sources=[
            "https://en.wikipedia.org/wiki/Triumph_(magazine)",
        ]),
    "Twentieth Century": dict(
        descr=(
            "The Twentieth Century was a British periodical of literature, "
            "politics and ideas, the final title of The Nineteenth Century,"
            " founded by James Knowles in 1877. It took the name The "
            "Twentieth Century in 1951, appeared irregularly from the late "
            "1960s and ceased in 1972."
        ),
        url="https://en.wikipedia.org/wiki/The_Nineteenth_Century_(periodical)",
        sources=[
            "https://en.wikipedia.org/wiki/The_Nineteenth_Century_(periodical)",
            "https://library.holycross.edu/Record/b1170383/Description",
        ]),
    "Universities Bookman": dict(
        descr=(
            "The University Bookman (sometimes cited as Universities "
            "Bookman), the conservative review of books founded by Russell "
            "Kirk in 1960. Originally a quarterly devoted almost entirely "
            "to book reviews, it was edited by Kirk from Mecosta, Michigan,"
            " and is now published by the Russell Kirk Center."
        ),
        url="https://kirkcenter.org/bookman/",
        sources=[
            "https://kirkcenter.org/essays/defending-the-right-and-the-good/",
        ]),
    "Valóság": dict(
        descr=(
            "Valóság is a Hungarian social-science journal launched in "
            "December 1958 by the Society for the Dissemination of "
            "Scientific Knowledge (TIT). Rather than competing with "
            "specialist journals, it set out to bring high-level work in "
            "the social sciences to a broad educated readership."
        ),
        url="https://hu.wikipedia.org/wiki/Valóság_(folyóirat,_1958–)",
        sources=[
            "https://wikiwand.com/hu/Valóság_(folyóirat,_1958–)",
        ]),
    "Világosság": dict(
        descr=(
            "Világosság is a Hungarian journal of philosophy and the "
            "humanities, published in Budapest since 1960. Regarded early "
            "on as an unusually serious intellectual journal, it publishes "
            "essays and studies in philosophy and related humanistic and "
            "social-scientific fields."
        ),
        sources=[
            "https://www.relbib.de/Record/130866563",
            "https://www.mek.oszk.hu/13400/13461/html/htm/c/npt82.htm",
        ]),
    "Virginia Quarterly Review": dict(
        descr=(
            "The Virginia Quarterly Review is a literary and public-affairs"
            " magazine published by the University of Virginia in "
            "Charlottesville since 1925. It prints fiction, poetry, essays,"
            " criticism, long-form journalism and photojournalism for a "
            "general literary readership."
        ),
        url="https://www.vqronline.org",
        sources=[
            "https://en.wikipedia.org/wiki/Virginia_Quarterly_Review",
            "https://www.vqronline.org/about-vqr",
        ]),
    "Wall Street Journal": dict(
        descr=(
            "The Wall Street Journal is an American daily newspaper founded"
            " in New York in 1889 by Charles Dow, Edward Jones and Charles "
            "Bergstresser and published by Dow Jones & Company. It "
            "concentrates on business, finance and economics, and also "
            "covers national and international news, opinion and books."
        ),
        url="https://www.wsj.com",
        sources=[
            "https://en.wikipedia.org/wiki/The_Wall_Street_Journal",
        ]),
    "Wilson Quarterly": dict(
        descr=(
            "The Wilson Quarterly is a general-interest magazine of ideas "
            "produced by the Woodrow Wilson International Center for "
            "Scholars in Washington, D.C. Founded in 1976, it presents "
            "scholarship on politics, history, international affairs and "
            "culture for general readers; it moved to digital-only "
            "publication in 2012."
        ),
        url="https://www.wilsonquarterly.com",
        sources=[
            "https://en.wikipedia.org/wiki/The_Wilson_Quarterly",
            "https://www.wilsonquarterly.com/about/",
        ]),
    "Wisconsin Bookwatch": dict(
        descr=(
            "Wisconsin Bookwatch is a monthly book-review newsletter of the"
            " Midwest Book Review, based in Oregon, Wisconsin. It carries "
            "short reviews written by the Review's staff, aimed at "
            "librarians and general readers, as one of several Bookwatch "
            "publications the organisation issues."
        ),
        url="https://www.midwestbookreview.com",
        sources=[
            "https://en.wikipedia.org/wiki/Midwest_Book_Review",
            "https://midwestbookreview.com/wbw/nov_06.htm",
        ]),
    "Wisconsin Law Journal": dict(
        descr=(
            "The Wisconsin Law Journal is a Milwaukee-based legal newspaper"
            " written for Wisconsin attorneys and judges. Long issued "
            "weekly, it reports legal news and court decisions, with case "
            "analysis and a database of verdicts and settlements."
        ),
        url="https://wislawjournal.com",
        sources=[
            "https://wislawjournal.com/about",
            "https://descubridor.academia.cl/Record/ssj0022239/Description",
            "https://wisblawg.law.wisc.edu/2007/11/08/wisconsin-law-journal-site-has-new-look-new-features/",
        ]),
    "World Politics": dict(
        descr=(
            "World Politics is a quarterly journal of international "
            "relations and comparative politics, founded in 1948 at the "
            "Yale Institute of International Studies and moved in 1951 to "
            "Princeton's Center of International Studies. It publishes "
            "theoretical and empirical research and review articles, and is"
            " published by Johns Hopkins University Press."
        ),
        url="https://press.jhu.edu/journals/world-politics",
        sources=[
            "https://en.wikipedia.org/wiki/World_Politics",
            "https://international.princeton.edu/news/world-politics-journal-celebrates-75-years-look-back-and-forward",
        ]),
    "Zeitschrift für philosophische Forschung": dict(
        descr=(
            "The Zeitschrift für philosophische Forschung is a German "
            "philosophy journal founded in 1946. Published since 1950 in "
            "Meisenheim and later by Vittorio Klostermann in Frankfurt am "
            "Main, it is a general academic journal of philosophy carrying "
            "articles and reviews."
        ),
        sources=[
            "https://www.dla-marbach.de/en/catalogue/find/opac/id/EZB124918/",
            "https://oeaw.ac.at/resources/Record/990001230240504498?lng=cs",
        ]),
}
