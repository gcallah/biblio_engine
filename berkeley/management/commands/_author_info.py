"""Author details for people in the database, used by load_author_info.

Keyed by (last name, first name, middle name), with "" for a missing
name. Each entry may give affiliation (institution name only), yob, yod,
descr (a short paraphrased description, under 512 characters) and url
(a stable page about the person, such as Wikipedia).
Leave out anything we couldn't confirm. "sources" records where each
fact came from.
"""

AUTHOR_INFO = {
    ("Callahan", "Gene", ""): dict(
        affiliation="New York University",
        yob=1959,
        descr=(
            "American economist and political theorist who studied at the "
            "London School of Economics and took his PhD at Cardiff "
            "University. He wrote Economics for Real People, an "
            "introduction to the Austrian school, and Oakeshott on Rome "
            "and America, co-edited a volume comparing Voegelin, Oakeshott "
            "and Hayek, and is a charter member of the Michael Oakeshott "
            "Association."
        ),
        sources=dict(
            affiliation="the user (Gene Callahan), 2026-11-06",
            yob="the user (Gene Callahan), 2026-11-06",
            descr="https://wiki.mises.org/wiki/Gene_Callahan",
        )),
    ('Abel', 'Corey', ''): dict(
        affiliation='Metropolitan State University of Denver',
        descr=(
            'Political theorist who wrote a University of Chicago doctoral '
            'dissertation on Michael Oakeshott after an MSc at the LSE. He has '
            'taught political science and humanities at several Colorado '
            'institutions, including the U.S. Air Force Academy and the '
            'University of Denver, and edited two Imprint Academic collections '
            "on Oakeshott's legacy and conservatism."
        ),
        sources=dict(
            affiliation='https://www.youscribe.loungeup.com/catalogue/ebooks/savoirs/philosophie/meanings-of-michael-oakeshott-s-conservatism-3426256',
            descr='https://gcallah.github.io/Rationalism/AntiRats/bios.html',
        ),),
    ('Adair-Toteff', 'Christopher', ''): dict(
        affiliation='University of South Florida',
        descr=(
            'American scholar of social and political thought and Fellow at the'
            ' Center for Social and Political Thought, University of South '
            "Florida. He has written on Max Weber's sociology of religion, "
            'Raymond Aron and the early Austrian school of economics, and '
            'edited work on Troeltsch and Tönnies; he has also contributed '
            'essays on Oakeshott to Cosmos + Taxis.'
        ),
        sources=dict(
            affiliation='https://www.abbeys.com.au/book/the-early-austrian-school-of-economics-money-value-capital-9781032045511.do',
            descr='https://www.abbeys.com.au/book/the-early-austrian-school-of-economics-money-value-capital-9781032045511.do',
        ),),
    ('Alexander', 'James', ''): dict(
        affiliation='Bilkent University',
        yob=1972,
        descr=(
            'British political theorist who studied history and political '
            'thought at Trinity College, Cambridge, and has taught political '
            'science at Bilkent University in Ankara since 2004. He works on '
            'modern political thought and conservatism and has written '
            "extensively on Oakeshott, including the chapter 'Oakeshott as "
            "Philosopher' in the Cambridge Companion to Oakeshott."
        ),
        sources=dict(
            yob='https://jalexand.bilkent.edu.tr/',
            affiliation='https://catalog.bilkent.edu.tr/instructor/i06727.html',
            descr='https://jalexand.bilkent.edu.tr/publications.html',
        ),),
    ('Ashford', 'N.', ''): dict(
        affiliation='Institute for Humane Studies',
        yob=1952,
        descr=(
            'British-born political scientist, formerly professor of politics '
            'and Jean Monnet Scholar at Staffordshire University, later a '
            'senior programs officer at the Institute for Humane Studies in the'
            ' US. He co-edited A Dictionary of Conservative and Libertarian '
            'Thought and wrote on the New Right and US politics.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Nigel_Ashford',
            affiliation='https://en.wikipedia.org/wiki/Nigel_Ashford',
            descr='https://en.wikipedia.org/wiki/Nigel_Ashford',
        ),),
    ('Astrov', 'Alexander', ''): dict(
        affiliation='Central European University',
        yob=1960,
        descr=(
            'International relations scholar who taught at Central European '
            'University, where he is associate professor emeritus. His book On '
            'World Politics (2005) draws on R. G. Collingwood and Michael '
            "Oakeshott to develop a 'neotraditionalist' approach to "
            'international relations theory.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n2005014633',
            affiliation='https://research.ceu.edu/en/persons/georg-henri-kaup/similar/',
            descr='https://www.palgrave.com/us/book/9781403946546',
        ),),
    ('Auspitz', 'J.', 'L.'): dict(
        descr=(
            'Independent scholar of political philosophy, educated at Harvard '
            'and, as a Marshall Scholar, at Brasenose College, Oxford. A long-'
            'standing interpreter of Oakeshott, he wrote early essays on his '
            'thought, contributed to The Intellectual Legacy of Michael '
            'Oakeshott (2005), and located additional Oakeshott papers later '
            'deposited at the LSE.'
        ),
        sources=dict(
            descr='https://www.commentary.org/author/jlauspitzcommentary-org/',
        ),),
    ('Bakhurst', 'David', ''): dict(
        affiliation="Queen's University",
        descr=(
            'Canadian-based British-trained philosopher, George Whalley '
            'Distinguished University Professor and Charlton Professor of '
            "Philosophy at Queen's University (Ontario), working in "
            'epistemology, Russian philosophy and philosophy of education. '
            'Author of Consciousness and Revolution in Soviet Philosophy and '
            'The Formation of Reason; Fellow of the Royal Society of Canada.'
        ),
        sources=dict(
            affiliation='https://www.queensu.ca/philosophy/people/david-bakhurst',
            descr='https://www.queensu.ca/philosophy/people/david-bakhurst',
        ),),
    ('Ball', 'D.', 'W.'): dict(
        affiliation='OpenAI',
        descr=(
            'AI policy analyst who wrote on Oakeshott and Confucius as a '
            'Hamilton College history undergraduate (class of 2014). He '
            'later held posts at the Manhattan Institute, Hoover Institution '
            'and Mercatus Center, served as White House senior policy advisor '
            'for AI, and became a senior fellow at the Foundation for American '
            'Innovation; by 2026 he was head of strategic futures at OpenAI.'
        ),
        sources=dict(
            affiliation='https://www.thefai.org/profile/dean-ball',
            descr='https://www.thefai.org/profile/dean-ball',
        ),),
    ('Baumgarth', 'W.', ''): dict(
        affiliation='Fordham University',
        yob=1946,
        descr=(
            'American political scientist and associate professor of political '
            'science at Fordham University, where he has chaired the '
            'department. His Harvard doctoral dissertation (1975) dealt with '
            "Hayek's political philosophy, and he has written on conservative "
            'and liberal political thought, including a 1977 study of '
            'Oakeshott.'
        ),
        sources=dict(
            yob='https://wikiberal.org/wiki/William_P._Baumgarth',
            affiliation='https://fordham.edu/academics/departments/political-science/faculty/william-p-baumgarth',
            descr='https://wikiberal.org/wiki/William_P._Baumgarth',
        ),),
    ('Berki', 'R.', 'N.'): dict(
        affiliation='University of Hull',
        yob=1936,
        yod=1991,
        descr=(
            'Robert Nandor Berki was a Hungarian-born British political '
            'theorist who left Hungary after 1956, studied at the LSE and '
            'Cambridge, and taught at the University of Hull from 1967, later '
            'as professor of European political and social theory. He wrote on '
            'Marxism, socialism and the history of political thought, including'
            " a critical analysis of Oakeshott's idea of civil association."
        ),
        sources=dict(
            yob='https://viaf.org/viaf/94635052',
            yod='https://en.wikipedia.org/wiki/Robert_Nandor_Berki',
            affiliation='https://en.wikipedia.org/wiki/Robert_Nandor_Berki',
            descr='https://en.wikipedia.org/wiki/Robert_Nandor_Berki',
        ),),
    ('Bhati', 'P.', 'S.'): dict(
        affiliation='Jai Narain Vyas University',
        descr=(
            'Indian political scientist, former professor and head of the '
            'political science department at Jai Narain Vyas University, '
            'Jodhpur, and a UGC Emeritus Fellow. His work defends normative and'
            ' classical political theory against behaviouralism and includes '
            'studies of Oakeshott, Arendt and Strauss; he co-wrote the 1980 '
            'article on Oakeshott with L. S. Rathore.'
        ),
        sources=dict(
            affiliation='https://www.exoticindia.com/book/details/history-and-politics-essays-in-honour-of-professor-p-s-bhati-naj135',
            descr='https://www.exoticindia.com/book/details/history-and-politics-essays-in-honour-of-professor-p-s-bhati-naj135',
        ),),
    ('Botwinick', 'Aryeh', ''): dict(
        affiliation='Temple University',
        descr=(
            'American political philosopher with a Princeton PhD who taught '
            'political science and Jewish studies at Temple University from '
            '1976 and later moved to its religion department. His work deals '
            'with skepticism, political participation and Jewish thought; books'
            ' include Skepticism and Political Participation, Emmanuel Levinas '
            "and the Limits to Ethics and Michael Oakeshott's Skepticism "
            '(2011).'
        ),
        sources=dict(
            affiliation='https://liberalarts.acquiadev.temple.edu/directory/aryeh-botwinick',
            descr='https://liberalarts.acquiadev.temple.edu/directory/aryeh-botwinick',
        ),),
    ('Boucher', 'David', ''): dict(
        affiliation='Cardiff University',
        yob=1951,
        descr=(
            'Welsh political theorist and scholar of international political '
            'thought at Cardiff University, where he directs the Collingwood '
            'and British Idealism Centre and edits Collingwood and British '
            'Idealism Studies. He has written extensively on R. G. Collingwood,'
            ' British Idealism and Oakeshott.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/David_Boucher_(political_scientist)',
            affiliation='https://profiles.cardiff.ac.uk/staff/boucherde',
            descr='https://en.wikipedia.org/wiki/David_Boucher_(political_scientist)',
        ),),
    ('Boyd', 'Jonathan', ''): dict(
        affiliation='ISM University of Management and Economics',
        descr=(
            'Canadian-born political theorist with a PhD in international '
            'relations from the University of St Andrews. He lectured at the '
            'University of Reading and since 2015 has been an associate '
            'professor at ISM University in Vilnius, teaching international '
            'relations and the history of political thought; he has written on '
            "Hobbes and Oakeshott's reading of Strauss."
        ),
        sources=dict(
            affiliation='https://archive.ism.lt/darbuotojai/jonathan-boyd/',
            descr='https://archive.ism.lt/darbuotojai/jonathan-boyd/',
        ),),
    ('Boyd', 'Richard', ''): dict(
        affiliation='Georgetown University',
        descr=(
            'Political theorist (PhD Rutgers) who teaches in Georgetown '
            "University's government department. His work covers British, "
            'French and American political thought, civil society and '
            'pluralism; he wrote Uncivil Society (2004), which draws on '
            "Oakeshott, and has written on Oakeshott's idea of civil "
            'association and On Human Conduct.'
        ),
        sources=dict(
            affiliation='https://scs.georgetown.edu/faculty/b328388/richard-boyd/',
            descr='https://scs.georgetown.edu/faculty/b328388/richard-boyd/',
        ),),
    ('Brooks', 'D.', ''): dict(
        affiliation='The New York Times',
        yob=1961,
        descr=(
            'Canadian-born American journalist and author, a long-time opinion '
            'columnist for The New York Times and commentator on PBS NewsHour, '
            'known for books such as Bobos in Paradise and The Social Animal. '
            "In a 2003 column he drew on Oakeshott's conservatism in discussing"
            ' contemporary politics.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n99280766',
            affiliation='http://id.loc.gov/authorities/names/n99280766',
            descr='https://en.wikipedia.org/wiki/David_Brooks_(commentator)',
        ),),
    ('Brown', 'Stuart', ''): dict(
        affiliation='Open University',
        yob=1938,
        descr=(
            'British philosopher and historian of philosophy, professor (later '
            'emeritus) of philosophy at the Open University after earlier '
            'teaching at St Andrews. A Leibniz specialist, he wrote the '
            "Historical Dictionary of Leibniz's Philosophy and co-edited "
            'reference works including the Dictionary of Twentieth-Century '
            'British Philosophers (2005) with Hugh Bredin.'
        ),
        sources=dict(
            yob='https://catalogue.bnf.fr/ark:/12148/cb12035220f',
            affiliation='https://www.open.ac.uk/library/digital-archive/program/video:FOUP9001',
            descr='https://www.routledge.com/Biographical-Dictionary-of-Twentieth-Century-Philosophers/Brown-Collinson-Wilkinson/p/book/9780415060431',
        ),),
    ('Bullock', 'A.', ''): dict(
        affiliation='University of Oxford',
        yob=1914,
        yod=2004,
        descr=(
            'British historian (Lord Bullock), best known for Hitler: A Study '
            'in Tyranny and Hitler and Stalin: Parallel Lives. Founding Master '
            "of St Catherine's College, Oxford, and Vice-Chancellor of Oxford "
            'University 1969-73; co-editor of the Fontana dictionaries of '
            'modern thought.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Alan_Bullock',
            yod='https://en.wikipedia.org/wiki/Alan_Bullock',
            affiliation='https://en.wikipedia.org/wiki/Alan_Bullock',
            descr='https://en.wikipedia.org/wiki/Alan_Bullock',
        ),),
    ('Candreva', 'Debra', ''): dict(
        yob=1971,
        descr=(
            'Scholar of political philosophy and author of The Enemies of '
            'Perfection (Lexington, 2005), which argues that Plato was among '
            "the most important influences on Oakeshott's thought. She also "
            'contributed a chapter on Oakeshott and Plato to The Intellectual '
            'Legacy of Michael Oakeshott.'
        ),
        sources=dict(
            yob='https://find.library.upenn.edu/catalog/9936629653503681',
            descr='https://find.library.upenn.edu/catalog/9936629653503681',
        ),),
    ('Chapman', 'J.', 'W.'): dict(
        affiliation='University of Pittsburgh',
        yob=1923,
        yod=2008,
        descr=(
            'American political theorist who taught political science at the '
            'University of Pittsburgh for about thirty years after graduating '
            'from Swarthmore in 1949. He was a long-time co-editor, with J. '
            'Roland Pennock, of NOMOS, the yearbook of the American Society for'
            ' Political and Legal Philosophy, which included the volume '
            'Authority Revisited (1987).'
        ),
        sources=dict(
            yob='https://www.goodreads.com/book/show/3903083',
            yod='https://www.goodreads.com/book/show/3903083',
            affiliation='https://archive.swarthmore.edu/bulletin_2014-2020/summer-2017-issue-iv-volume-cxiv/remembering-john-chapman-%e2%80%9949.html',
            descr='https://archive.swarthmore.edu/bulletin_2014-2020/summer-2017-issue-iv-volume-cxiv/remembering-john-chapman-%e2%80%9949.html',
        ),),
    ('Cheung', 'Chor-Yung', ''): dict(
        affiliation='City University of Hong Kong',
        yob=1957,
        descr=(
            'Hong Kong political theorist who taught politics and public '
            'administration in the Department of Public Policy at City '
            'University of Hong Kong until retiring in 2022. His work centres '
            'on Oakeshott, Hayek and Chinese liberalism; books include The '
            'Quest for Civil Order (2007) and Hayek and Post-War Chinese '
            'Liberalism (2024), and he co-edited The Poetic Character of Human '
            'Activity on Oakeshott.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n2008007771',
            affiliation='https://cosmosandtaxis.org/wp-content/uploads/2014/11/ct_1_3_cheung.pdf',
            descr='https://cosmosandtaxis.org/wp-content/uploads/2014/11/ct_1_3_cheung.pdf',
        ),),
    ('Coats', 'Wendell', 'John'): dict(
        affiliation='Connecticut College',
        descr=(
            'American political theorist who earned his BA and PhD at the '
            'University of Colorado and has taught government at Connecticut '
            'College since 1984, specializing in the history of Western '
            'political philosophy. He has written widely on Oakeshott, '
            'including Oakeshott and His Contemporaries (2000) and Michael '
            "Oakeshott as a Philosopher of the 'Creative' (2019), as well as "
            'works on statesmanship and armed force.'
        ),
        sources=dict(
            affiliation='https://www.conncoll.edu/directories/faculty-profiles/wendell-john-coats-jr/',
            descr='https://www.conncoll.edu/directories/faculty-profiles/wendell-john-coats-jr/',
        ),),
    ('Corey', 'Elizabeth', 'Campbell'): dict(
        affiliation='Baylor University',
        descr=(
            'American political theorist who teaches political science in the '
            'Honors College at Baylor University, where she directs the Honors '
            'Program. She holds a PhD from Louisiana State University and is '
            'the author of Michael Oakeshott on Religion, Aesthetics, and '
            'Politics (2006).'
        ),
        sources=dict(
            affiliation='https://honors.baylor.edu/person/elizabeth-corey-phd',
            descr='https://honors.baylor.edu/sites/g/files/ecbvkj1696/files/2023-12/elizabeth_corey_cv.pdf',
        ),),
    ('Cotellessa', 'S.', ''): dict(
        affiliation='Università Cattolica del Sacro Cuore',
        descr=(
            'Italian historian of political thought with a doctorate in the '
            'history of political doctrines and institutions. His book Il '
            'ragionevole disaccordo (1999) compares how Hayek and Oakeshott '
            'account for the unreasoned rules that sustain social order.'
        ),
        sources=dict(
            affiliation='https://www.skuola.net/universita/appunti-riassunti/storia-delle-dottrine-politiche',
            descr='http://id.loc.gov/authorities/names/n2002105493',
        ),),
    ('Covell', 'Charles', ''): dict(
        yob=1955,
        descr=(
            'British writer on legal and political philosophy, educated at the '
            'City of London School and Gonville and Caius College, Cambridge. '
            'His books include The Defence of Natural Law (1992), which '
            'examines Fuller, Oakeshott, Hayek, Dworkin and Finnis, and The Law'
            ' of Nations in Political Thought (2009), a survey from Vitoria to '
            'Hegel.'
        ),
        sources=dict(
            yob='https://cmu.marmot.org/Record/.b33064234',
            descr='https://www.bokus.com/bok/9780333387764/defence-of-natural-law',
        ),),
    ('Cranston', 'M.', ''): dict(
        affiliation='London School of Economics',
        yob=1920,
        yod=1993,
        descr=(
            'British political philosopher (Maurice Cranston) who held the '
            'chair of political science at the London School of Economics, '
            "Oakeshott's institution. Known for prize-winning biographies of "
            'John Locke and Jean-Jacques Rousseau and for Freedom: A New '
            'Analysis.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Maurice_Cranston',
            yod='https://en.wikipedia.org/wiki/Maurice_Cranston',
            affiliation='https://en.wikipedia.org/wiki/Maurice_Cranston',
            descr='https://en.wikipedia.org/wiki/Maurice_Cranston',
        ),),
    ('Crick', 'B.', ''): dict(
        affiliation='Birkbeck, University of London',
        yob=1929,
        yod=2008,
        descr=(
            'British political theorist (Bernard Crick) who taught at the LSE '
            'and Sheffield before founding the politics department at Birkbeck '
            'College. Best known for In Defence of Politics (1962), a biography'
            ' of George Orwell, and the 1998 Crick Report on citizenship '
            'education; he wrote critical assessments of his former LSE '
            'colleague Oakeshott.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Bernard_Crick',
            yod='https://en.wikipedia.org/wiki/Bernard_Crick',
            affiliation='https://en.wikipedia.org/wiki/Bernard_Crick',
            descr='https://en.wikipedia.org/wiki/Bernard_Crick',
        ),),
    ('Den Uyl', 'D.', 'J.'): dict(
        affiliation='Liberty Fund',
        yob=1950,
        descr=(
            'American philosopher who taught at Bellarmine College, where he '
            'chaired the philosophy department, before becoming vice president '
            'of educational programs at Liberty Fund. He writes on virtue '
            'ethics, classical liberalism and Spinoza, including God, Man, and '
            "Well-Being: Spinoza's Modern Humanism (2008), and co-wrote several"
            ' books with Douglas Rasmussen.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n83046418',
            affiliation='https://en.wikipedia.org/wiki/Douglas_Den_Uyl',
            descr='https://en.wikipedia.org/wiki/Douglas_Den_Uyl',
        ),),
    ('Devigne', 'Robert', ''): dict(
        affiliation='Tufts University',
        descr=(
            'Political theorist and professor of political science at Tufts '
            'University, with a PhD from Columbia (1990). He wrote Recasting '
            'Conservatism (1994), on how Oakeshott, Leo Strauss and their '
            'followers answered postmodernism, and Reforming Liberalism, a '
            'study of J. S. Mill.'
        ),
        sources=dict(
            affiliation='https://tischcollege.tufts.edu/node/19941',
            descr='https://claremontreviewofbooks.com/author/robert-devigne/',
        ),),
    ('Digeser', 'P.', ''): dict(
        affiliation='University of California, Santa Barbara',
        descr=(
            'American political theorist with a Johns Hopkins PhD (1988) who '
            'taught political science at UC Santa Barbara from 1988, becoming '
            'professor in 2005 and later emeritus. Work covers power, identity,'
            ' political forgiveness, friendship and the relation of theory to '
            'practice; books include Our Politics, Our Selves? and Political '
            "Forgiveness. Edited a collection of Richard Flathman's writings "
            'and has written on Flathman and Oakeshott.'
        ),
        sources=dict(
            affiliation='https://polsci.ucsb.edu/people/p-e-digeser',
            descr='https://polsci.ucsb.edu/people/p-e-digeser',
        ),),
    ('Dockstader', 'Jason', ''): dict(
        affiliation='University College Cork',
        descr=(
            'Philosopher at University College Cork whose research centres on '
            'Daoist philosophy and metaethics, including work on the Laozi, '
            'Zhuangzi and Guo Xiang; his Cosmos + Taxis article examines '
            "Oakeshott's use of the Zhuangzi."
        ),
        sources=dict(
            affiliation='https://philpeople.org/departments/university-college-cork/philosophy/publications',
            descr='https://philarchive.org/archive/DOCOSD',
        ),),
    ('Dray', 'W.', 'H.'): dict(
        affiliation='University of Ottawa',
        yob=1921,
        yod=2009,
        descr=(
            'Canadian philosopher of history, educated at Toronto and Oxford, '
            'who taught at the University of Toronto, Trent University and the '
            'University of Ottawa. Known for Laws and Explanation in History '
            '(1957), an anti-positivist account of historical explanation, and '
            "for studies of R. G. Collingwood; he also wrote on Oakeshott's "
            'theory of history.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/William_Herbert_Dray',
            yod='https://en.wikipedia.org/wiki/William_Herbert_Dray',
            affiliation='https://thecanadianencyclopedia.ca/en/article/william-herbert-dray',
            descr='https://thecanadianencyclopedia.ca/en/article/william-herbert-dray',
        ),),
    ('Fairfield', 'Paul', ''): dict(
        affiliation="Queen's University",
        yob=1966,
        descr=(
            "Philosopher and professor of philosophy at Queen's University, "
            'Kingston, where he has taught since 2002; PhD McMaster. He works '
            'in hermeneutics, phenomenology and pragmatism, and co-edited with '
            "David Bakhurst Education and Conversation: Exploring Oakeshott's "
            'Legacy (2016).'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n00084106',
            affiliation='https://www.queensu.ca/philosophy/people/faculty/fairfield-paul',
            descr='https://www.queensu.ca/philosophy/people/faculty/fairfield-paul',
        ),),
    ('Farr', 'Anthony', ''): dict(
        affiliation='University of Westminster',
        descr=(
            "British political theorist and author of Sartre's Radicalism and "
            "Oakeshott's Conservatism: The Duplicity of Freedom (1998), which "
            "contrasts Sartre's belief that humans can remake themselves with "
            "Oakeshott's skepticism about it. According to the book's author "
            'note he taught politics at the London School of Economics and '
            'London Guildhall University and later lectured part-time at the '
            'University of Westminster.'
        ),
        sources=dict(
            affiliation='https://www.palgrave.com/us/book/9780333684498',
            descr='https://www.palgrave.com/us/book/9780333684498',
        ),),
    ('Fear', 'Christopher', ''): dict(
        affiliation='University of Hull',
        descr=(
            'British political theorist, Lecturer in Politics and International'
            ' Relations at the University of Hull, specialising in conservative'
            ' and liberal political thought and the British Idealists; his '
            'doctoral work was on R. G. Collingwood and the history of ideas.'
        ),
        sources=dict(
            affiliation='https://www.hull.ac.uk/staff-directory/christopher-fear',
            descr='https://www.hull.ac.uk/staff-directory/christopher-fear',
        ),),
    ('Feaver', 'G.', ''): dict(
        affiliation='University of British Columbia',
        yod=2008,
        descr=(
            'Political scientist who taught at the University of British '
            'Columbia for over thirty years, later as professor emeritus, with '
            'visiting posts at the LSE and ANU. He worked on biography and '
            'English-language moral and political philosophy, writing From '
            'Status to Contract (1969), a biography of Sir Henry Maine, and '
            'studies of Harold Laski and the Webbs.'
        ),
        sources=dict(
            yod='https://politics.ubc.ca/?p=20649',
            affiliation='https://politics.ubc.ca/?p=20649',
            descr='https://search.law.villanova.edu/Record/25482',
        ),),
    ('Forsyth', 'M.', ''): dict(
        affiliation='University of Leicester',
        yob=1936,
        descr=(
            'British political scientist, born in Hong Kong and educated at '
            'Balliol College, Oxford, who is emeritus professor of politics at '
            'the University of Leicester. He wrote Unions of States (1981) on '
            'confederation and a study of the Abbé Sieyès, and co-edited the '
            'three-volume Political Classics guides.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Murray_Forsyth',
            affiliation='https://en.wikipedia.org/wiki/Murray_Forsyth',
            descr='https://en.wikipedia.org/wiki/Murray_Forsyth',
        ),),
    ('Franco', 'Paul', ''): dict(
        affiliation='Bowdoin College',
        yob=1956,
        descr=(
            'American political theorist and professor of government at Bowdoin'
            ' College, with a PhD from the University of Chicago. A leading '
            'interpreter of Oakeshott, he wrote The Political Philosophy of '
            'Michael Oakeshott (1990) and Michael Oakeshott: An Introduction '
            '(2004) and edited A Companion to Michael Oakeshott; he has also '
            'written on Hegel and Nietzsche.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n88293875',
            affiliation='https://en.wikipedia.org/wiki/Paul_Franco',
            descr='https://en.wikipedia.org/wiki/Paul_Franco',
        ),),
    ('Friedman', 'R.', 'B.'): dict(
        descr=(
            'Political theorist who wrote on the concept of authority, '
            'including the much-reprinted essay On the Concept of Authority in '
            'Political Philosophy (1973) and work on Mill. On Oakeshott he '
            'wrote Oakeshott on the Authority of Law (Ratio Juris, 1989) and a '
            'chapter on the rule of law in The Intellectual Legacy of Michael '
            'Oakeshott (2005).'
        ),
        sources=dict(
            descr='https://dc2.philarchive.org/s/Richard%20B.%20Friedman',
        ),),
    ('Frohnen', 'B.', 'P.'): dict(
        affiliation='Ohio Northern University',
        descr=(
            'American political theorist and legal scholar with a Cornell PhD '
            'in government and an Emory JD, professor of law at Ohio Northern '
            'University and a senior fellow of the Russell Kirk Center. His '
            'work concerns conservatism and constitutional thought; books '
            'include Virtue and the Promise of Conservatism: The Legacy of '
            'Burke and Tocqueville and The New Communitarians and the Crisis of'
            ' Modern Liberalism.'
        ),
        sources=dict(
            affiliation='https://www.onu.edu/directory/bruce-frohnen',
            descr='https://en.wikipedia.org/wiki/Bruce_Frohnen',
        ),),
    ('Fuller', 'Timothy', ''): dict(
        affiliation='Colorado College',
        yob=1940,
        descr=(
            'American political theorist who has taught political science at '
            'Colorado College since 1965 and served as its dean. A former '
            'student and friend of Oakeshott and past president of the Michael '
            'Oakeshott Association, he edited several posthumous Oakeshott '
            'collections, including The Voice of Liberal Learning and The '
            'Politics of Faith and the Politics of Scepticism.'
        ),
        sources=dict(
            affiliation='https://vintage.isi.org/intercollegiate-review/tim-fuller-interview',
            descr='https://www.coloradocollege.edu/iapps/Bulletin/fall97/learning.html',
            yob='https://sactx.aspendiscovery.org/Record/61561',
        ),),
    ('Gerencser', 'Steven', 'Anthony'): dict(
        affiliation='Indiana University South Bend',
        yob=1963,
        descr=(
            'American political theorist with a PhD from the University of '
            'Minnesota who is professor and chair of political science at '
            "Indiana University South Bend. He wrote The Skeptic's Oakeshott "
            "(2000) and articles on Oakeshott's ideas of conversation, "
            'democracy and law.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n99057090',
            affiliation='https://theconversation.com/profiles/steven-gerencser-1440930',
            descr='https://bulletins.iu.edu/iusb/2023-2024/schools/college-of-liberal-arts-and-sciences/political-science/index.shtml',
        ),),
    ('Grabosky', 'P.', ''): dict(
        affiliation='Australian National University',
        yob=1945,
        descr=(
            'American-born Australian criminologist, PhD Northwestern, and '
            'professor emeritus at the Australian National University (RegNet).'
            ' He worked for many years at the Australian Institute of '
            'Criminology and was president of the Australian and New Zealand '
            'Society of Criminology. He writes on regulation, policing and '
            'cybercrime.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n84174779',
            affiliation='https://regnet.anu.edu.au/people/peter-grabosky',
            descr='https://www.policyforum.net/authors/peter-grabosky/index.html',
        ),),
    ('Grant', 'Robert', ''): dict(
        affiliation='University of Glasgow',
        descr=(
            'British scholar of literature and the history of ideas, formerly a'
            ' fellow of Trinity Hall, Cambridge, and lecturer at Sussex, who '
            'taught at the University of Glasgow from 1974 and held a chair in '
            'the History of Ideas there from 2004. He wrote Oakeshott (1990), '
            "the first book-length study of Oakeshott's whole career, and is "
            "writing Oakeshott's official biography."
        ),
        sources=dict(
            affiliation='https://www.gla.ac.uk/schools/critical/staff/robertgrant',
            descr='https://www.gla.ac.uk/schools/critical/staff/robertgrant',
        ),),
    ('Gray', 'J.', 'N.'): dict(
        affiliation='London School of Economics',
        yob=1948,
        descr=(
            'English political philosopher (John Nicholas Gray), emeritus '
            'Professor of European Thought at the London School of Economics, '
            'previously at Oxford. Early work on liberalism, Mill, Hayek and '
            'Oakeshott; later known for critiques of liberal humanism such as '
            'Straw Dogs and Black Mass.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Gray_(philosopher)',
            affiliation='https://en.wikipedia.org/wiki/John_Gray_(philosopher)',
            descr='https://en.wikipedia.org/wiki/John_Gray_(philosopher)',
        ),),
    ('Greenleaf', 'W.', 'H.'): dict(
        affiliation='Swansea University',
        yob=1927,
        yod=2008,
        descr=(
            'British political scientist who studied at the LSE, where '
            "Oakeshott's influence drew him from socialism toward conservatism."
            ' He taught at Hull and was professor of political theory and '
            'government at University College, Swansea (1967-82). His '
            "Oakeshott's Philosophical Politics (1966) was long a standard "
            'introduction; he also wrote the three-volume The British Political'
            ' Tradition.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/W._H._Greenleaf',
            yod='https://en.wikipedia.org/wiki/W._H._Greenleaf',
            affiliation='https://en.wikipedia.org/wiki/W._H._Greenleaf',
            descr='https://en.wikipedia.org/wiki/W._H._Greenleaf',
        ),),
    ('Griffith', 'Guy', ''): dict(
        affiliation='Gonville and Caius College, Cambridge',
        yob=1908,
        yod=1985,
        descr=(
            'English ancient historian and classicist, fellow of Gonville and '
            'Caius College, Cambridge, from 1931 until his death and a '
            'university lecturer from 1937. A close friend of Michael '
            'Oakeshott, he co-wrote with him A Guide to the Classics, or How to'
            ' Pick the Derby Winner (1936), reissued in 1947 as A New Guide to '
            'the Derby.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Guy_Thompson_Griffith',
            yod='https://en.wikipedia.org/wiki/Guy_Thompson_Griffith',
            affiliation='https://en.wikipedia.org/wiki/Guy_Thompson_Griffith',
            descr='https://contemporarythinkers.org/michael-oakeshott/?p=3998',
        ),),
    ('Grosby', 'S.', ''): dict(
        affiliation='Clemson University',
        yob=1951,
        descr=(
            'American scholar of religion and professor emeritus at Clemson '
            'University who works on the ancient Near East, the Hebrew Bible, '
            'religion and nationality, and social and political philosophy. His'
            ' books include Nationalism: A Very Short Introduction (2005); he '
            'has compared the pluralism of Oakeshott, Shils and Weber.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n90726585',
            affiliation='http://id.loc.gov/authorities/names/n90726585',
            descr='https://en.wikipedia.org/wiki/Steven_Grosby',
        ),),
    ('Gunnell', 'J.', 'G.'): dict(
        affiliation='University at Albany',
        yob=1933,
        yod=2024,
        descr=(
            'American political theorist and Distinguished Professor of '
            'political science at the University at Albany, SUNY, later '
            'affiliated with UC Davis. He wrote widely on the history and '
            'identity of political theory as an academic field and on the '
            'philosophy of social science, including The Descent of Political '
            'Theory (1993) and Social Inquiry after Wittgenstein and Kuhn.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n85091841',
            yod='https://core-prod.cambridgecore.org/core/services/aop-cambridge-core/content/view/F5A71D2EB0223AA0773069EF08AC3028/S2766013324000838a.pdf/in-memoriam-john-jack-gunnell.pdf',
            affiliation='https://www.albany.edu/updates/1997/2-5/frontpage.html',
            descr='https://sunypress.edu/Blog/2024/Memories-of-SUNY-Press-author-John-G.-Gunnell',
        ),),
    ('Haddock', 'B.', ''): dict(
        affiliation='Cardiff University',
        descr=(
            'British political theorist and historian of political thought, '
            'professor of modern European social and political thought at '
            'Cardiff University. He has written on Vico, the history of ideas '
            "and Oakeshott; books include Vico's Political Thought (1986) and A"
            ' History of Political Thought: 1789 to the Present.'
        ),
        sources=dict(
            affiliation='https://orca.cardiff.ac.uk/48889/',
            descr='https://banksquarebooks.com/book/9780745631028',
        ),),
    ('Hammer', 'D.', 'C.'): dict(
        affiliation='Franklin & Marshall College',
        descr=(
            'American political theorist, John W. Wetzel Professor of Classics '
            'and Professor of Government at Franklin & Marshall College, with a'
            ' PhD from UC Berkeley. His books cover Roman political thought, '
            'the Iliad as politics and the Puritan tradition in American '
            'political theory; he also wrote on George Bush as an '
            "'Oakeshottian' president (1995)."
        ),
        sources=dict(
            affiliation='https://www.fandm.edu/directory/dean-hammer.html',
            descr='https://www.fandm.edu/directory/dean-hammer.html',
        ),),
    ('Hart', 'J.', ''): dict(
        affiliation='Dartmouth College',
        yob=1930,
        yod=2019,
        descr=(
            'American conservative cultural critic, essayist and columnist who '
            'taught English literature at Dartmouth College for three decades. '
            'He wrote on eighteenth-century English political writers and '
            'defended the Western literary canon, and wrote about Oakeshott in '
            'conservative periodicals including National Review.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n81127052',
            yod='http://id.loc.gov/authorities/names/n81127052',
            affiliation='http://id.loc.gov/authorities/names/n81127052',
            descr='https://en.wikipedia.org/wiki/Jeffrey_Hart',
        ),),
    ('Himmelfarb', 'G.', ''): dict(
        affiliation='City University of New York',
        yob=1922,
        yod=2019,
        descr=(
            'American historian (Gertrude Himmelfarb), professor of history at '
            'the City University of New York and a leading scholar of Victorian'
            ' Britain and its moral and intellectual life. A prominent '
            'conservative public intellectual, she wrote on Lord Acton, J. S. '
            'Mill and Victorian virtues.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Gertrude_Himmelfarb',
            yod='https://en.wikipedia.org/wiki/Gertrude_Himmelfarb',
            affiliation='https://en.wikipedia.org/wiki/Gertrude_Himmelfarb',
            descr='https://en.wikipedia.org/wiki/Gertrude_Himmelfarb',
        ),),
    ('Hobbes', 'Thomas', ''): dict(
        yob=1588,
        yod=1679,
        descr=(
            'English philosopher, author of Leviathan (1651), a founding work '
            'of modern political philosophy and social contract theory. '
            'Oakeshott edited the 1946 Basil Blackwell edition of Leviathan, '
            'whose long introduction became one of his best-known essays.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Thomas_Hobbes',
            yod='https://en.wikipedia.org/wiki/Thomas_Hobbes',
            descr='https://en.wikipedia.org/wiki/Thomas_Hobbes',
        ),),
    ('Honig', 'B.', ''): dict(
        affiliation='Brown University',
        yob=1959,
        descr=(
            'American political theorist specializing in democratic, feminist '
            'and legal theory, who is Nancy Duke Lewis Professor of Modern '
            'Culture and Media and Political Science at Brown University and '
            'formerly taught at Northwestern. She co-edited a volume of essays '
            'on the political thought of Richard Flathman.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n92100707',
            affiliation='http://id.loc.gov/authorities/names/n92100707',
            descr='https://en.wikipedia.org/wiki/Bonnie_Honig',
        ),),
    ('Horton', 'J.', ''): dict(
        affiliation='Keele University',
        descr=(
            'British political philosopher, emeritus professor of political '
            'philosophy at Keele University and formerly at the University of '
            'York, where he directed the Morrell Centre for Studies in '
            'Toleration. He is known for work on political obligation, '
            'toleration, modus vivendi and political realism, and for his '
            'criticism of Rawlsian liberal moralism.'
        ),
        sources=dict(
            affiliation='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6086230/',
            descr='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6086230/',
        ),),
    ('Ikeda', 'Sanford', ''): dict(
        affiliation='Purchase College, State University of New York',
        descr=(
            'American economist of the Austrian school, educated at Grove City '
            'College and New York University, who taught economics at Purchase '
            'College (SUNY), where he is professor emeritus. He works on urban '
            'economics, spontaneous order and the ideas of Jane Jacobs; books '
            'include Dynamics of the Mixed Economy (1997) and A City Cannot Be '
            'a Work of Art (2024).'
        ),
        sources=dict(
            affiliation='https://www.purchase.edu/live/profiles/624-sanford-ikeda',
            descr='https://www.fraserinstitute.org/profile/sanford-ikeda',
        ),),
    ('Isaacs', 'Stuart', ''): dict(
        affiliation='University of West London',
        descr=(
            'British political theorist, author of The Politics and Philosophy '
            'of Michael Oakeshott (Routledge, 2006), which reads Oakeshott as a'
            ' non-foundational thinker and relates his work to Arendt, Rorty '
            'and Rawls.'
        ),
        sources=dict(
            affiliation='https://repository.uwl.ac.uk/id/eprint/7387/',
            descr='https://contemporarythinkers.org/michael-oakeshott/commentary/the-politics-and-philosophy-of-michael-oakeshott/',
        ),),
    ('Johnson', 'N.', ''): dict(
        affiliation='Nuffield College, Oxford',
        yob=1929,
        yod=2006,
        descr=(
            'British political scientist, born in Darlington, who was a '
            'professorial fellow (later emeritus fellow) of Nuffield College, '
            'Oxford, and an expert on the comparative study of political '
            "institutions and the British constitution. He wrote on Oakeshott's"
            ' political philosophy and the British Academy memoir of Oakeshott.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n50038643',
            yod='http://id.loc.gov/authorities/names/n50038643',
            affiliation='http://id.loc.gov/authorities/names/n50038643',
            descr='http://id.loc.gov/authorities/names/n50038643',
        ),),
    ('Kaldis', 'B.', ''): dict(
        affiliation='Hellenic Open University',
        descr=(
            'Philosopher at the Hellenic Open University, Athens, where he has '
            'been professor of philosophy and dean of humanities. He works in '
            'philosophy of science and social science; his 2009 Zygon article '
            "reconstructs and critiques Oakeshott's account of natural science "
            'as a mode of experience.'
        ),
        sources=dict(
            affiliation='http://id.loc.gov/authorities/names/nr94039538',
            descr='https://manwithoutqualities.com/2013/05/17/oakeshott-on-science-as-a-mode-of-experience/',
        ),),
    ('Keens-Soper', 'M.', ''): dict(
        affiliation='University of Leicester',
        descr=(
            'British scholar of political theory and diplomatic thought who '
            'taught in the politics department at the University of Leicester '
            'from 1964. With Murray Forsyth he edited the Oxford Political '
            'Classics volumes, and he co-wrote Diplomatic Theory from '
            "Machiavelli to Kissinger and edited Callieres's The Art of "
            'Diplomacy.'
        ),
        sources=dict(
            affiliation='https://www.palgrave.com/us/book/9780333753651',
            descr='https://cambridge.org/core/journals/utilitas/article/murray-forsyth-and-maurice-keenssoper-eds-the-political-classics-green-to-dworkin-oxford-oxford-university-press-1996-pp-292/7A06AEF6A35F16E7D944D2109DE950ED',
        ),),
    ('Kelly', 'P.', ''): dict(
        affiliation='London School of Economics',
        descr=(
            'British political theorist and professor of political theory at '
            'the London School of Economics, where he has served as a pro-'
            'director. With David Boucher he edited Political Thinkers: From '
            'Socrates to the Present (Oxford University Press, 2003; later '
            'editions), a survey of major figures in the history of political '
            'thought.'
        ),
        sources=dict(
            affiliation='https://researchonline.lse.ac.uk/id/eprint/11330',
            descr='https://timeshighereducation.com/cn/node/106094',
        ),),
    ('Kestenbaum', 'V.', ''): dict(
        yob=1945,
        descr=(
            'American philosopher and Dewey scholar, author of The '
            'Phenomenological Sense of John Dewey (1977) and The Grace and the '
            'Severity of the Ideal: John Dewey and the Transcendent (2002), '
            "which argues that Dewey's thought makes room for the transcendent."
            ' He has also compared Dewey and Oakeshott on the rationality of '
            'conduct.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n82024019',
            descr='https://ndpr.nd.edu/news/the-grace-and-the-severity-of-the-ideal/',
        ),),
    ('King', 'Preston', ''): dict(
        affiliation='Lancaster University',
        yob=1936,
        descr=(
            'American political philosopher and civil rights figure who studied'
            ' at the LSE, where Oakeshott was an influence, after leaving the '
            'US in 1961 over draft charges (pardoned in 2000). He held chairs '
            'in Nairobi, at the University of New South Wales and at Lancaster,'
            ' later teaching at Emory and Morehouse. His books include Fear of '
            'Power, The Ideology of Order and Toleration.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n50048087',
            affiliation='https://en.wikipedia.org/wiki/Preston_King_(academic)',
            descr='https://en.wikipedia.org/wiki/Preston_King_(academic)',
        ),),
    ('Kinzel', 'Till', ''): dict(
        affiliation='Technische Universität Berlin',
        yob=1968,
        descr=(
            'German scholar of English and American literature and intellectual'
            ' historian who took his doctorate (2002) and habilitation (2005) '
            'at the Technical University of Berlin, where he teaches. He has '
            'written on Allan Bloom, Philip Roth, Nicolás Gómez Dávila and J. '
            'G. Hamann, and his Michael Oakeshott: Philosoph der Politik (2007)'
            ' was the first German-language introduction to Oakeshott.'
        ),
        sources=dict(
            yob='https://budapestsummit-archive.mcc.hu/en/till-kinzel',
            affiliation='https://budapestsummit-archive.mcc.hu/en/till-kinzel',
            descr='https://budapestsummit-archive.mcc.hu/en/till-kinzel',
        ),),
    ('Kos', 'Eric', 'S.'): dict(
        affiliation='Madonna University',
        descr=(
            'Political scientist (PhD University of Michigan) who taught at '
            'Siena Heights University in Michigan, from which he retired as '
            'professor, and then taught part-time at Madonna University. A '
            'charter member and former president (2015-17) of the Michael '
            'Oakeshott Association, he wrote on Oakeshott and the ancient '
            'Greeks and edited several Palgrave volumes on Oakeshott.'
        ),
        sources=dict(
            affiliation='https://oll.libertyfund.org/people/eric-s-kos',
            descr='https://oll.libertyfund.org/people/eric-s-kos',
        ),),
    ('Laursen', 'J.-C.', ''): dict(
        affiliation='University of California, Riverside',
        yob=1952,
        descr=(
            'American political theorist and historian of ideas, professor of '
            'political science at the University of California, Riverside, '
            'since 1991, trained at Harvard and Johns Hopkins. He specialises '
            'in the political uses of skepticism, from The Politics of '
            'Skepticism in the Ancients, Montaigne, Hume, and Kant (1992) '
            'onward, and in Enlightenment political thought.'
        ),
        sources=dict(
            yob='https://www.encyclopedia.com/arts/educational-magazines/laursen-john-christian-1952',
            affiliation='https://www.encyclopedia.com/arts/educational-magazines/laursen-john-christian-1952',
            descr='https://www.encyclopedia.com/arts/educational-magazines/laursen-john-christian-1952',
        ),),
    ('Lessnoff', 'M.', 'H.'): dict(
        affiliation='University of Glasgow',
        yob=1940,
        yod=2024,
        descr=(
            'Scottish political theorist who spent about forty years in the '
            'Department of Politics at the University of Glasgow, retiring as '
            'Reader. His books include The Structure of Social Science, Social '
            'Contract, The Spirit of Capitalism and the Protestant Ethic, '
            'Political Philosophers of the Twentieth Century (which includes a '
            'chapter on Oakeshott) and Ernest Gellner and Modernity.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n85209602',
            yod='https://www.gla.ac.uk/schools/socialpolitical/news/archive/2020onwards/headline_1106159_en.html',
            affiliation='https://www.gla.ac.uk/schools/socialpolitical/news/archive/2020onwards/headline_1106159_en.html',
            descr='https://www.gla.ac.uk/schools/socialpolitical/news/archive/2020onwards/headline_1106159_en.html',
        ),),
    ('Letwin', 'Oliver', ''): dict(
        affiliation='House of Commons',
        yob=1956,
        descr=(
            'British Conservative politician and former academic philosopher, '
            'MP for West Dorset 1997-2019 and Chancellor of the Duchy of '
            "Lancaster 2014-16. Son of Shirley Robin Letwin, Oakeshott's friend"
            ' and literary executor; author of Ethics, Emotions and the '
            'Philosophy of the Self.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Oliver_Letwin',
            affiliation='https://en.wikipedia.org/wiki/Oliver_Letwin',
            descr='https://en.wikipedia.org/wiki/Oliver_Letwin',
        ),),
    ('Letwin', 'Shirley', 'Robin'): dict(
        affiliation='London School of Economics',
        yob=1924,
        yod=1993,
        descr=(
            'American-born political philosopher and historian of ideas who '
            'studied under Hayek at the University of Chicago and settled in '
            'London, teaching at the LSE and at Peterhouse, Cambridge. Her '
            'books include The Pursuit of Certainty, The Gentleman in Trollope '
            'and The Anatomy of Thatcherism. A close friend of Oakeshott, she '
            'became his literary executor.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Shirley_Robin_Letwin',
            yod='https://en.wikipedia.org/wiki/Shirley_Robin_Letwin',
            affiliation='https://en.wikipedia.org/wiki/Shirley_Robin_Letwin',
            descr='https://en.wikipedia.org/wiki/Shirley_Robin_Letwin',
        ),),
    ('Mapel', 'D.', ''): dict(
        affiliation='University of Colorado Boulder',
        yob=1952,
        descr=(
            'Political theorist, now emeritus in political science at the '
            'University of Colorado Boulder, with degrees from Colorado '
            'College, the LSE and Johns Hopkins. He works on social justice, '
            'political obligation, international ethics and Hobbes; books '
            'include Social Justice Reconsidered, and he co-edited Traditions '
            'of International Ethics with Terry Nardin.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n88011940',
            affiliation='https://www.colorado.edu/polisci/people/faculty-emeritus/david-r-mapel',
            descr='https://www.colorado.edu/polisci/people/faculty-emeritus/david-r-mapel',
        ),),
    ('Marriott', 'Shal', ''): dict(
        affiliation='McGill University',
        descr=(
            'Political theorist educated at Carleton University and McGill, and'
            ' a PhD candidate in political science at McGill specializing in '
            'political theory. Her research covers the Scottish and French '
            'Enlightenment, Judith Shklar and Oakeshott, and she has been a '
            'Mercatus Center Elinor Ostrom Fellow.'
        ),
        sources=dict(
            affiliation='https://www.iedm.org/shal-marriott/',
            descr='https://mercatus.org/students/fellows/shal-marriott',
        ),),
    ('Marsh', 'Leslie', ''): dict(
        affiliation='University of British Columbia',
        descr=(
            'Philosopher and cognitive scientist, research associate at the '
            'University of British Columbia medical school and formerly at the '
            'New England Institute for Cognitive Science and Evolutionary '
            "Studies. He has written on Hayek's and Oakeshott's theories of "
            'mind and co-edited A Companion to Michael Oakeshott with Paul '
            'Franco.'
        ),
        sources=dict(
            affiliation='https://www.conversationsonphilanthropy.org/?p=1134',
            descr='https://www.conversationsonphilanthropy.org/?p=1134',
        ),),
    ('Mason', 'R.', ''): dict(
        yob=1948,
        descr=(
            'Philosopher who edited Cambridge Minds (1994), a collection of '
            'essays on notable Cambridge thinkers including Oakeshott. His '
            'other books include The God of Spinoza, Before Logic, '
            "Understanding Understanding and Oppenheimer's Choice."
        ),
        sources=dict(
            yob='https://openlibrary.org/authors/OL537008A.json',
            descr='https://openlibrary.org/authors/OL537008A/works.json',
        ),),
    ('Mathie', 'W.', ''): dict(
        affiliation='Brock University',
        descr=(
            'Canadian political scientist who taught politics at Brock '
            'University in St. Catharines, Ontario, where he coordinated the '
            'Liberal Studies program. He has written on Hobbes, including '
            "studies of justice, equity and rhetoric in Hobbes's civil science "
            "and an analysis of Oakeshott's account of Hobbesian morality."
        ),
        sources=dict(
            affiliation='https://www.scribd.com/document/432419780/Hobbes',
            descr='https://scholar.uwindsor.ca/ossaarchive/OSSA2/papersandcommentaries/77',
        ),),
    ('McCabe', 'D.', ''): dict(
        affiliation='Colgate University',
        yob=1963,
        descr=(
            'American political philosopher with a PhD from Northwestern '
            'University who holds the Richard J. and Joan Head Chair in '
            'Philosophy at Colgate University. He is best known for Modus '
            'Vivendi Liberalism: Theory and Practice (2010) and has written and'
            " lectured on Oakeshott's idea of liberal education and the "
            'university.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n2009064989',
            affiliation='https://en.wikipedia.org/wiki/David_McCabe_(philosopher)',
            descr='https://en.wikipedia.org/wiki/David_McCabe_(philosopher)',
        ),),
    ('McIlwain', 'David', ''): dict(
        affiliation='Macquarie University',
        descr=(
            'Scholar of political thought who received his PhD in politics from'
            ' Macquarie University in 2018. His book Michael Oakeshott and Leo '
            'Strauss: The Politics of Renaissance and Enlightenment (2019) '
            'compares the two thinkers on modernity, history, and politics and '
            'religion, and was the subject of a Cosmos + Taxis symposium.'
        ),
        sources=dict(
            affiliation='https://link.springer.com/book/9783030133801',
            descr='https://link.springer.com/book/9783030133801',
        ),),
    ('McInnes', 'N.', ''): dict(
        yob=1924,
        yod=2017,
        descr=(
            'Australian journalist, writer and senior public servant who worked'
            ' as a journalist in Australia, India and France before joining the'
            " Office of National Assessments in 1978 and serving as Australia's"
            ' first Inspector-General of Intelligence and Security (1986-89). '
            'He wrote on Marxism and European communism and contributed essays '
            "to Quadrant and The National Interest, including 'A Skeptical "
            "Conservative' (2000) on Oakeshott."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Neil_McInnes_(1924%E2%80%932017)',
            yod='https://en.wikipedia.org/wiki/Neil_McInnes_(1924%E2%80%932017)',
            descr='https://en.wikipedia.org/wiki/Neil_McInnes_(1924%E2%80%932017)',
        ),),
    ('McIntyre', 'Kenneth', 'B.'): dict(
        affiliation='Sam Houston State University',
        descr=(
            'American political theorist, professor of political science at Sam'
            ' Houston State University, working on philosophy of history, law '
            'and the British Idealists, especially Oakeshott and Collingwood. '
            "Author of The Limits of Political Theory: Oakeshott's Philosophy "
            'of Civil Association and a study of Herbert Butterfield.'
        ),
        sources=dict(
            affiliation='https://shsu.edu/academics/political-science/faculty/mcintyre.html',
            descr='https://shsu.edu/academics/political-science/faculty/mcintyre.html',
        ),),
    ('Mihatov', 'P.', ''): dict(
        descr=(
            'Croatian author who, at the time of his 2008 Synthesis '
            "Philosophica article on Oakeshott's critique of rationalism and "
            "theory of civil association, was affiliated with Croatia's "
            'Ministry of Foreign Affairs and European Integration in Zagreb. '
            "The article contrasts Oakeshott with Foucault's account of power."
        ),
        sources=dict(
            descr='https://hrcak.srce.hr/en/30808',
        ),),
    ('Miller', 'D.', ''): dict(
        affiliation='Nuffield College, Oxford',
        yob=1946,
        descr=(
            'English political theorist and Fellow of the British Academy, long'
            ' an Official Fellow of Nuffield College and Professor of Political'
            ' Theory at Oxford. He is known for work on social justice, '
            'nationality and global justice, and edited The Blackwell '
            'Encyclopaedia of Political Thought (1987).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/David_Miller_(political_theorist)',
            affiliation='https://en.wikipedia.org/wiki/David_Miller_(political_theorist)',
            descr='https://www.encyclopedia.com/arts/culture-magazines/miller-david-leslie',
        ),),
    ('Miller', 'T.', 'H.'): dict(
        affiliation='University of Alabama',
        yob=1965,
        descr=(
            'American political theorist with a PhD from UC San Diego who is '
            'associate professor of political science at the University of '
            'Alabama. He wrote Mortal Gods: Science, Politics, and the Humanist'
            ' Ambitions of Thomas Hobbes (2011) and Friendly Sovereignty '
            "(2022), and has written on Oakeshott's reading of Hobbes."
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n2011021389',
            affiliation='https://psc.ua.edu/people/ted-miller/',
            descr='http://id.loc.gov/authorities/names/n2011021389',
        ),),
    ('Minogue', 'K.', 'R.'): dict(
        affiliation='London School of Economics',
        yob=1930,
        yod=2013,
        descr=(
            'New Zealand-born, Australian-educated political theorist who spent'
            ' his career at the London School of Economics, which he rejoined '
            "in 1956 at Oakeshott's invitation, and where he was professor of "
            'political science from 1984 to 1995. A prominent conservative '
            'thinker, he wrote The Liberal Mind, Alien Powers and The Servile '
            'Mind, as well as several memoirs and essays on Oakeshott.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Kenneth_Minogue',
            yod='https://en.wikipedia.org/wiki/Kenneth_Minogue',
            affiliation='https://en.wikipedia.org/wiki/Kenneth_Minogue',
            descr='https://en.wikipedia.org/wiki/Kenneth_Minogue',
        ),),
    ('Mitchell', 'Mark', 'T.'): dict(
        affiliation='Patrick Henry College',
        descr=(
            'American political theorist, professor and dean of academic '
            'affairs at Patrick Henry College and co-founder of Front Porch '
            'Republic. Author of Michael Polanyi: The Art of Knowing and The '
            'Limits of Liberalism, which draws on Oakeshott, Polanyi and '
            'MacIntyre to defend tradition.'
        ),
        sources=dict(
            affiliation='https://www.phc.edu/news/mark-mitchell-limits-of-liberalism',
            descr='https://www.phc.edu/news/mark-mitchell-limits-of-liberalism',
        ),),
    ('Modood', 'T.', ''): dict(
        affiliation='University of Bristol',
        yob=1952,
        descr=(
            'British political theorist and sociologist, professor at the '
            'University of Bristol since 1997 and founding director of its '
            'Centre for the Study of Ethnicity and Citizenship. He did his PhD '
            'at University College Swansea and published early work on '
            "Oakeshott's idea of philosophy, before becoming a leading writer "
            'on multiculturalism, Muslims in Britain and secularism.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Tariq_Modood',
            affiliation='https://en.wikipedia.org/wiki/Tariq_Modood',
            descr='https://en.wikipedia.org/wiki/Tariq_Modood',
        ),),
    ('Munro', 'D.', 'H.'): dict(
        affiliation='Monash University',
        yob=1911,
        yod=2001,
        descr=(
            'New Zealand-born moral philosopher who taught at Otago and Sydney '
            'before becoming the foundation professor of philosophy at Monash '
            'University (1961-76). His books include Argument of Laughter, '
            "Godwin's Moral Philosophy (1953), Empiricism and Ethics (1967) and"
            ' Ethics and the Environment.'
        ),
        sources=dict(
            yob='https://www.monash.edu/records-archives/archives/collections/personal-archives/monro,-david-hector',
            yod='https://www.monash.edu/records-archives/archives/collections/personal-archives/monro,-david-hector',
            affiliation='https://www.monash.edu/records-archives/archives/collections/personal-archives/monro,-david-hector',
            descr='https://www.monash.edu/records-archives/archives/collections/personal-archives/monro,-david-hector',
        ),),
    ('Müller', 'J.-W.', ''): dict(
        affiliation='Princeton University',
        yob=1970,
        descr=(
            'German political philosopher and historian of political ideas at '
            'Princeton University, whose books include What Is Populism? '
            "(2016). He wrote an essay on Oakeshott's 'happy conservatism' for "
            'the German journal Merkur.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n00037229',
            affiliation='https://en.wikipedia.org/wiki/Jan-Werner_M%C3%BCller',
            descr='https://en.wikipedia.org/wiki/Jan-Werner_M%C3%BCller',
        ),),
    ('Nardin', 'Terry', ''): dict(
        affiliation='National University of Singapore',
        yob=1942,
        descr=(
            'Political theorist, PhD Northwestern (1967), who taught at SUNY '
            'Buffalo and the University of Wisconsin-Milwaukee before moving to'
            ' the National University of Singapore and Yale-NUS College. He '
            'works on international ethics and the history of political '
            'thought; his books include Law, Morality, and the Relations of '
            'States and The Philosophy of Michael Oakeshott (2001).'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n83046006',
            affiliation='http://id.loc.gov/authorities/names/n83046006',
            descr='https://en.wikipedia.org/wiki/Terry_Nardin',
        ),),
    ('Nell', 'Guinevere', 'Liberty'): dict(
        affiliation='Heritage Foundation',
        yob=1976,
        descr=(
            'American economist working in Austrian economics and Soviet '
            "economic history, holding a master's in Soviet economic history "
            'from the University of Warwick; formerly a tax policy analyst at '
            'the Heritage Foundation. She has edited several Palgrave Macmillan'
            ' volumes on Austrian economics and teaches a Marginal Revolution '
            'University course on the Soviet economy.'
        ),
        sources=dict(
            yob='https://catalogue.bnf.fr/ark:/12148/cb16905015s',
            affiliation='https://catalogue.bnf.fr/ark:/12148/cb16905015s',
            descr='https://www.wikiberal.org/wiki/Guinevere_L._Nell',
        ),),
    ('Nelson', 'Scott', 'B.'): dict(
        affiliation='Austrian Economics Center',
        descr=(
            'Scholar affiliated with the Austrian Economics Center, author of a'
            " 2022 Cosmos + Taxis review essay on David McIlwain's Michael "
            'Oakeshott and Leo Strauss that brings out Hayek as one of the '
            "voices in that book's conversation between Oakeshott and Strauss."
        ),
        sources=dict(
            descr='https://cosmosandtaxis.org/wp-content/uploads/2022/02/nelson_ct_vol10_iss_1_2.pdf',
            affiliation='https://cosmosandtaxis.org/wp-content/uploads/2022/02/nelson_ct_vol10_iss_1_2.pdf',
        ),),
    ('Norman', 'Jesse', ''): dict(
        affiliation='House of Commons',
        yob=1962,
        descr=(
            'British Conservative politician and writer, MP for Hereford and '
            'South Herefordshire since 2010 and a former government minister. '
            'Trained in philosophy (PhD, University College London), he edited '
            'The Achievement of Michael Oakeshott (1993) and has written books '
            'on Edmund Burke and Adam Smith.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Jesse_Norman',
            affiliation='https://en.wikipedia.org/wiki/Jesse_Norman',
            descr='https://en.wikipedia.org/wiki/Jesse_Norman',
        ),),
    ("O'Hear", 'A.', ''): dict(
        affiliation='University of Buckingham',
        yob=1942,
        descr=(
            'English philosopher, professor of philosophy and head of education'
            ' at the University of Buckingham, long-time director of the Royal '
            'Institute of Philosophy and editor of Philosophy until 2019, and '
            'co-founder of the Journal of Applied Philosophy. He has written on'
            ' Karl Popper, the philosophy of science, education and '
            'conservatism.'
        ),
        sources=dict(
            yob="https://en.wikipedia.org/wiki/Anthony_O'Hear",
            affiliation="https://en.wikipedia.org/wiki/Anthony_O'Hear",
            descr="https://en.wikipedia.org/wiki/Anthony_O'Hear",
        ),),
    ("O'Sullivan", 'Luke', ''): dict(
        affiliation='National University of Singapore',
        descr=(
            'Historian of ideas specialising in philosophy and politics, '
            'associate professor at the National University of Singapore. He is'
            " a leading editor of Oakeshott's posthumous writings for Imprint "
            'Academic, including the Notebooks, 1922-86, wrote Oakeshott on '
            'History (2003), and co-edited a volume of The Correspondence of '
            'Jeremy Bentham.'
        ),
        sources=dict(
            affiliation='http://id.loc.gov/authorities/names/nb2002079979',
            descr='http://id.loc.gov/authorities/names/nb2002079979',
        ),),
    ("O'Sullivan", 'Noël', ''): dict(
        affiliation='University of Hull',
        descr=(
            'English political philosopher educated at the London School of '
            "Economics and Harvard, who joined the University of Hull's "
            'politics department in 1967 and held a personal chair in political'
            ' philosophy there from 1992, later becoming research professor. '
            'His books include Conservatism, Fascism, Santayana and European '
            'Political Thought since 1945, and he edited The Place of Michael '
            'Oakeshott in Contemporary Western and Non-Western Thought (2017).'
        ),
        sources=dict(
            affiliation='https://en.wikipedia.org/wiki/No%C3%ABl_O%27Sullivan',
            descr='https://en.wikipedia.org/wiki/No%C3%ABl_O%27Sullivan',
        ),),
    ('Oakeshott', 'Michael', ''): dict(
        affiliation='London School of Economics',
        yob=1901,
        yod=1990,
        descr=(
            'English philosopher and political theorist who taught history at '
            'Cambridge before succeeding Harold Laski as Professor of Political'
            ' Science at the London School of Economics (1951-69). His major '
            'works include Experience and Its Modes, Rationalism in Politics '
            'and On Human Conduct, and he is the subject of this bibliography.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Michael_Oakeshott',
            yod='https://en.wikipedia.org/wiki/Michael_Oakeshott',
            affiliation='https://en.wikipedia.org/wiki/Michael_Oakeshott',
            descr='https://en.wikipedia.org/wiki/Michael_Oakeshott',
        ),),
    ('Orr', 'R.', ''): dict(
        affiliation='London School of Economics',
        descr=(
            'New Zealand-educated political theorist who took his PhD at the '
            "LSE, taught at Queen's University Belfast, the University of "
            'Western Australia and Monash, and joined the LSE government '
            'department in 1965 as one of the political theorists around '
            'Oakeshott. He wrote on Machiavelli and on Kant and Gallie, and '
            "offered a personal reading of Oakeshott's thought."
        ),
        sources=dict(
            affiliation='https://manwithoutqualities.com/2014/10/30/a-double-agent-in-the-dream-of-michael-oakeshott/',
            descr='https://manwithoutqualities.com/2014/10/30/a-double-agent-in-the-dream-of-michael-oakeshott/',
        ),),
    ('Orsi', 'Davide', ''): dict(
        affiliation='Cardiff University',
        descr=(
            'Scholar of political philosophy and international relations, with '
            'a PhD in politics and international relations from Cardiff '
            'University (2015), who has taught at Cardiff and served as editor-'
            'at-large of E-International Relations. His book Michael '
            "Oakeshott's Political Philosophy of International Relations (2016)"
            " applies Oakeshott's idea of civil association to international "
            'society.'
        ),
        sources=dict(
            affiliation='http://id.loc.gov/authorities/names/no2018055493',
            descr='http://id.loc.gov/authorities/names/no2018055493',
        ),),
    ('Palonen', 'K.', ''): dict(
        affiliation='University of Jyväskylä',
        yob=1947,
        descr=(
            'Finnish political scientist, professor of political science at the'
            ' University of Jyväskylä 1993-2014 and now emeritus, known for '
            'work on conceptual history, political rhetoric, Max Weber and '
            'parliamentary procedure. He directed the Finnish Centre of '
            'Excellence in Political Thought and Conceptual Change.'
        ),
        sources=dict(
            yob='https://www.nli.org.il/en/authorities/987007302675405171',
            affiliation='https://en.wikipedia.org/wiki/Kari_Palonen',
            descr='https://en.wikipedia.org/wiki/Kari_Palonen',
        ),),
    ('Parekh', 'B.', 'C.'): dict(
        affiliation='University of Westminster',
        yob=1935,
        descr=(
            'Indian-born British political theorist and Labour life peer (Lord '
            'Parekh). He took his PhD at the LSE, taught there and at Glasgow, '
            'then was professor of political theory at Hull (1982-2001) and '
            'later at Westminster. Known for work on Bentham, Marx, Gandhi and '
            'multiculturalism, he co-edited the 1968 Festschrift for '
            "Oakeshott's retirement."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Bhikhu_Parekh',
            affiliation='https://en.wikipedia.org/wiki/Bhikhu_Parekh',
            descr='https://en.wikipedia.org/wiki/Bhikhu_Parekh',
        ),),
    ('Pelczynski', 'Z.', ''): dict(
        affiliation='University of Oxford',
        yob=1925,
        yod=2021,
        descr=(
            'Polish-born British political philosopher who taught politics at '
            'Oxford, as a fellow of Pembroke College, from 1957 to 1992. He was'
            ' a leading figure in the Anglo-American revival of Hegel studies, '
            "beginning with Hegel's Political Writings (1964), and later "
            'supported education and civil society in Poland after 1989.'
        ),
        sources=dict(
            yob='https://www.pmb.ox.ac.uk/news/zbigniew-pelczynski-obe',
            yod='https://www.pmb.ox.ac.uk/news/zbigniew-pelczynski-obe',
            affiliation='https://www.politics.ox.ac.uk/news/memorium-zbigniew-pelczynski-obe-1925-2021',
            descr='https://en.wikipedia.org/wiki/Zbigniew_Pe%C5%82czy%C5%84ski',
        ),),
    ('Pennock', 'J.', 'R.'): dict(
        affiliation='Swarthmore College',
        yob=1906,
        yod=1995,
        descr=(
            'American political scientist who taught at Swarthmore College. He '
            'wrote on administration and the rule of law and edited the '
            "American Society for Political and Legal Philosophy's NOMOS volume"
            ' Authority Revisited (1987).'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n79023337',
            yod='http://id.loc.gov/authorities/names/n79023337',
            affiliation='https://www.wikidata.org/wiki/Q110146701',
            descr='http://id.loc.gov/authorities/names/n79023337',
        ),),
    ('Perret', 'Quentin', ''): dict(
        yob=1978,
        descr=(
            'Author of Oakeshott: le scepticisme en politique (Michalon, 2004),'
            " a short French-language introduction to Oakeshott's political "
            'scepticism.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/no2006013228',
            descr='http://id.loc.gov/authorities/names/no2006013228',
        ),),
    ('Peters', 'R.', 'S.'): dict(
        affiliation='Institute of Education, University of London',
        yob=1919,
        yod=2011,
        descr=(
            'English philosopher, born in India, who taught at Birkbeck College'
            ' and was Professor of the Philosophy of Education at the Institute'
            ' of Education, University of London, from 1962 to 1983. A founder '
            'of analytic philosophy of education, he wrote Ethics and '
            'Education, Hobbes and The Concept of Motivation; his essay on '
            "Oakeshott's philosophy of education appeared in 1968."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/R._S._Peters',
            yod='https://en.wikipedia.org/wiki/R._S._Peters',
            affiliation='https://en.wikipedia.org/wiki/R._S._Peters',
            descr='https://en.wikipedia.org/wiki/R._S._Peters',
        ),),
    ('Pitkin', 'H.', 'F.'): dict(
        affiliation='University of California, Berkeley',
        yob=1931,
        yod=2023,
        descr=(
            'German-born American political theorist (Hanna Fenichel Pitkin), '
            'professor of political science at UC Berkeley, best known for The '
            'Concept of Representation (1967) and later work on Wittgenstein, '
            'Machiavelli and Arendt. She received the Johan Skytte Prize in '
            "2003 and wrote critical reviews of Oakeshott's On Human Conduct."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Hanna_Fenichel_Pitkin',
            yod='https://en.wikipedia.org/wiki/Hanna_Fenichel_Pitkin',
            affiliation='https://polisci.berkeley.edu/150w/hanna-pitkin',
            descr='https://en.wikipedia.org/wiki/Hanna_Fenichel_Pitkin',
        ),),
    ('Plotica', 'Luke', 'Philip'): dict(
        affiliation='Virginia Tech',
        yob=1980,
        descr=(
            'Political theorist, professor of political science at Virginia '
            'Tech. His book Michael Oakeshott and the Conversation of Modern '
            'Political Thought (SUNY Press, 2015) places Oakeshott in dialogue '
            'with modern political thinkers; he has also written on nineteenth-'
            'century individualism and the market economy.'
        ),
        sources=dict(
            yob='https://openlibrary.org/authors/OL8787650A',
            affiliation='https://sunypress.edu/Books/M/Michael-Oakeshott-and-the-Conversation-of-Modern-Political-Thought',
            descr='https://sunypress.edu/Books/M/Michael-Oakeshott-and-the-Conversation-of-Modern-Political-Thought',
        ),),
    ('Podoksik', 'Efraim', ''): dict(
        affiliation='Hebrew University of Jerusalem',
        yob=1973,
        descr=(
            'Israeli political theorist and intellectual historian, born in '
            'Leningrad, who teaches in the Department of Political Science at '
            'the Hebrew University of Jerusalem after a Cambridge PhD. He wrote'
            ' In Defence of Modernity (2003) on Oakeshott, edited The Cambridge'
            ' Companion to Oakeshott (2012), and has also published on Georg '
            'Simmel.'
        ),
        sources=dict(
            yob='https://www.dla-marbach.de/en/catalogue/find/opac/id/PE00637581/',
            affiliation='https://en.politics.huji.ac.il/people/ephraim-podoksik',
            descr='https://en.politics.huji.ac.il/people/ephraim-podoksik',
        ),),
    ('Quinton', 'Anthony', ''): dict(
        affiliation='Trinity College, Oxford',
        yob=1925,
        yod=2010,
        descr=(
            'English philosopher (Lord Quinton of Holywell), fellow of All '
            'Souls and New College, President of Trinity College, Oxford '
            '(1978-87) and chairman of the British Library board. He worked in '
            'metaphysics, philosophy of mind and political philosophy, and '
            'wrote The Politics of Imperfection (1978), tracing English '
            'conservative thought from Hooker to Oakeshott.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n50050567',
            yod='http://id.loc.gov/authorities/names/n50050567',
            affiliation='https://en.wikipedia.org/wiki/Anthony_Quinton',
            descr='https://en.wikipedia.org/wiki/Anthony_Quinton',
        ),),
    ('Rayner', 'J.', 'D.'): dict(
        descr=(
            'Canadian political scientist who was at Lakehead University in '
            "Ontario when he published 'The Legend of Oakeshott's Conservatism'"
            ' (Canadian Journal of Political Science, 1985), which reads '
            "Oakeshott's politics as following from his sceptical philosophy "
            'rather than from conservatism.'
        ),
        sources=dict(
            descr='https://www.cambridge.org/core/journals/canadian-journal-of-political-science-revue-canadienne-de-science-politique/article/legend-of-oakeshotts-conservatism-sceptical-philosophy-and-limited-politics/C198CC9AB172EB8FF079DFA95F00BA10',
        ),),
    ('Reiss', 'H.', 'S.'): dict(
        affiliation='University of Bristol',
        yob=1922,
        yod=2020,
        descr=(
            'German-born British Germanist who fled to Ireland in 1939 and '
            'became professor of German at the University of Bristol, later '
            'emeritus. He wrote on Franz Kafka and on literary form and '
            "politics, and wrote an early German-language study of Oakeshott's "
            'conservative thought.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n50051053',
            yod='http://id.loc.gov/authorities/names/n50051053',
            affiliation='https://en.wikipedia.org/wiki/Hans_Reiss',
            descr='http://id.loc.gov/authorities/names/n50051053',
        ),),
    ('Riley', 'P.', ''): dict(
        affiliation='University of Wisconsin-Madison',
        yob=1941,
        yod=2015,
        descr=(
            'American political theorist and historian of political thought, '
            'Harvard PhD (1968), who held the Michael Oakeshott Professorship '
            'of Political Science at the University of Wisconsin-Madison until '
            '2007 and later taught at Harvard. He wrote Will and Political '
            "Legitimacy and Leibniz' Universal Jurisprudence, and published "
            'several memorial and interpretive essays on Oakeshott.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n82021741',
            yod='https://en.wikipedia.org/wiki/Patrick_T._Riley',
            affiliation='https://en.wikipedia.org/wiki/Patrick_T._Riley',
            descr='https://en.wikipedia.org/wiki/Patrick_T._Riley',
        ),),
    ('Schaefer', 'David', 'Lewis'): dict(
        affiliation='College of the Holy Cross',
        descr=(
            'American political philosopher, professor emeritus of political '
            'science at the College of the Holy Cross, with a PhD from the '
            'University of Chicago. He taught political philosophy and American'
            " political thought, and contributed a response to David McIlwain's"
            ' book on Oakeshott and Leo Strauss to Cosmos + Taxis (2022).'
        ),
        sources=dict(
            affiliation='https://www.holycross.edu/academics/programs/political-science/faculty/david-schaefer',
            descr='https://www.holycross.edu/academics/programs/political-science/faculty/david-schaefer',
        ),),
    ('Scruton', 'R.', ''): dict(
        affiliation='Birkbeck College',
        yob=1944,
        yod=2020,
        descr=(
            'English philosopher and writer on aesthetics and political '
            'philosophy, known for his conservative views, who taught at '
            'Birkbeck College, London, from 1971 to 1992, becoming professor of'
            ' aesthetics. He was founding editor of The Salisbury Review and '
            'wrote more than fifty books.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Roger_Scruton',
            yod='https://en.wikipedia.org/wiki/Roger_Scruton',
            affiliation='https://en.wikipedia.org/wiki/Roger_Scruton',
            descr='https://en.wikipedia.org/wiki/Roger_Scruton',
        ),),
    ('Segal', 'J.', ''): dict(
        affiliation='Kingsborough Community College',
        descr=(
            'Political theorist, associate professor of political science at '
            'Kingsborough Community College, CUNY, and chair of its history, '
            'philosophy and political science department. His Columbia PhD '
            'compared classical republicanism with Arendt and Oakeshott, and he'
            ' has written on Oakeshott in relation to Foucault, Hayek and '
            'Galston.'
        ),
        sources=dict(
            affiliation='https://commons.gc.cuny.edu/members/jpsegal',
            descr='https://commons.gc.cuny.edu/members/jpsegal',
        ),),
    ('Singh', 'Randhir', ''): dict(
        affiliation='University of Delhi',
        yob=1922,
        yod=2016,
        descr=(
            'Indian Marxist political theorist and teacher who taught for about'
            ' twenty years at Delhi College and then in the political science '
            'department of the University of Delhi from 1972 to 1987. His works'
            ' include Of Marxism and Indian Politics and Crisis of Socialism, '
            'and his Reason, Revolution and Political Theory is a Marxist '
            "critique of Oakeshott's Rationalism in Politics."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Randhir_Singh_(academic)',
            yod='https://en.wikipedia.org/wiki/Randhir_Singh_(academic)',
            affiliation='https://en.wikipedia.org/wiki/Randhir_Singh_(academic)',
            descr='https://en.wikipedia.org/wiki/Randhir_Singh_(academic)',
        ),),
    ('Skjönsberg', 'Max', ''): dict(
        affiliation='University of Florida',
        descr=(
            'Intellectual and political historian of eighteenth-century '
            'Britain, author of The Persistence of Party: Ideas of Harmonious '
            'Discord in Eighteenth-Century Britain (Cambridge, 2021). Formerly '
            'a postdoctoral researcher at the University of Liverpool, he '
            'became Associate Professor of Humanities at the University of '
            'Florida in 2025.'
        ),
        sources=dict(
            affiliation='https://hamilton.ufl.edu/wp-content/uploads/2024/01/Dr-Max-Skjonsberg-CV-2026.pdf',
            descr='https://jackmillercenter.org/max-skjonsberg-persistence-party-ideas-harmonious-discord-eighteenth-century-britain/',
        ),),
    ('Sobran', 'J.', ''): dict(
        affiliation='National Review',
        yob=1946,
        yod=2010,
        descr=(
            'American conservative journalist and syndicated columnist who '
            'wrote for National Review from 1972 to 1993, becoming a senior '
            'editor, and was later syndicated through the Los Angeles Times and'
            ' Universal Press Syndicate. His later writings drew accusations of'
            ' antisemitism and led to his dismissal from National Review.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Joseph_Sobran',
            yod='https://en.wikipedia.org/wiki/Joseph_Sobran',
            affiliation='https://en.wikipedia.org/wiki/Joseph_Sobran',
            descr='https://en.wikipedia.org/wiki/Joseph_Sobran',
        ),),
    ('Soininen', 'Suvi', ''): dict(
        affiliation='University of Jyväskylä',
        descr=(
            'Finnish political theorist at the University of Jyväskylä whose '
            "doctoral dissertation, From a 'Necessary Evil' to an Art of "
            "Contingency (2005), studied Oakeshott's conception of political "
            'activity. She has also written a Finnish-language book on '
            'Oakeshott and has worked on parliament in British political '
            'thought.'
        ),
        sources=dict(
            affiliation='https://concepta-net.org/suvi_soininen',
            descr='https://concepta-net.org/suvi_soininen',
        ),),
    ('Spitz', 'D.', ''): dict(
        affiliation='Ohio State University',
        yob=1916,
        yod=1979,
        descr=(
            'Political theorist who taught political science and political '
            'philosophy at Ohio State University from 1947 to 1970 and then at '
            'the City University of New York. A liberal democratic critic of '
            'conservatism, his books include Patterns of Anti-Democratic '
            'Thought and The Real World of Liberalism; his 1976 Political '
            'Theory essay criticised Oakeshott.'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n80117112',
            yod='https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/david-spitz/21D5AD17B47B56C922255C2B1EEB9D79',
            affiliation='https://snaccooperative.org/view/50186424',
            descr='https://snaccooperative.org/view/50186424',
        ),),
    ('Sullivan', 'Andrew', ''): dict(
        affiliation='The Weekly Dish',
        yob=1963,
        descr=(
            'British-born American political writer and blogger who studied at '
            'Magdalen College, Oxford, and took a Harvard PhD in government in '
            '1990 with a dissertation on Oakeshott, published as Intimations '
            'Pursued (2007). He edited The New Republic (1991-96), wrote the '
            'blog The Daily Dish and now publishes the newsletter The Weekly '
            'Dish.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Andrew_Sullivan',
            affiliation='https://en.wikipedia.org/wiki/Andrew_Sullivan',
            descr='https://en.wikipedia.org/wiki/Andrew_Sullivan',
        ),),
    ('Swaine', 'L.', ''): dict(
        affiliation='Dartmouth College',
        descr=(
            'Political theorist (Lucas Swaine), professor of government at '
            'Dartmouth College, working on liberalism, freedom of conscience, '
            'and religion and politics. Author of The Liberal Conscience: '
            'Politics and Principle in a World of Religious Pluralism (2006).'
        ),
        sources=dict(
            affiliation='https://govt.dartmouth.edu/people/lucas-swaine',
            descr='https://govt.dartmouth.edu/people/lucas-swaine',
        ),),
    ('Söderbaum', 'Jakob', ''): dict(
        descr=(
            'Swedish writer on conservative political thought, author of Modern'
            ' konservatism (2020), a survey of the ideas and main currents of '
            'conservatism after Burke. His Cosmos + Taxis essay compares '
            'Oakeshott and Russell Kirk and argues that Oakeshott made '
            'conservatism a doctrine of ordered liberty.'
        ),
        sources=dict(
            descr='https://cosmosandtaxis.org/wp-content/uploads/2025/01/Soderbaum_CT_Vol13_Iss_1_2.pdf',
        ),),
    ('Thompson', 'Martyn', 'P.'): dict(
        affiliation='Tulane University',
        descr=(
            'Political theorist and professor emeritus of political science at '
            'Tulane University, who earned a doctorate at the LSE and a German '
            'Habilitation at Tübingen. He wrote Ideas of Contract in English '
            'Political Thought in the Age of John Locke (1987) and has used '
            "Oakeshott's philosophy to critique the Cambridge School approach "
            'to intellectual history.'
        ),
        sources=dict(
            affiliation='https://liberalarts.tulane.edu/departments/political-science/people/martyn-thompson',
            descr='https://liberalarts.tulane.edu/departments/political-science/people/martyn-thompson',
        ),),
    ('Tregenza', 'Ian', ''): dict(
        affiliation='Macquarie University',
        descr=(
            'Australian political theorist who teaches the history of political'
            ' thought and religion and politics at Macquarie University. His '
            'book Michael Oakeshott on Hobbes (2003), based on a UNSW '
            "doctorate, reads Oakeshott's philosophy through his interpretation"
            ' of Hobbes; he has also written on British idealism in Australia.'
        ),
        sources=dict(
            affiliation='https://researchers.mq.edu.au/en/persons/ian-tregenza/',
            descr='https://researchers.mq.edu.au/en/persons/ian-tregenza/',
        ),),
    ('Trepanier', 'Lee', ''): dict(
        affiliation='Saginaw Valley State University',
        yob=1972,
        descr=(
            'Political scientist with a PhD from Louisiana State University, '
            'who taught political science at Saginaw Valley State University. '
            'He works on political philosophy and Russian political thought, '
            'writing Political Symbols in Russian History (2007), and edited '
            'Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, and Others '
            '(2018).'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n2006093878',
            affiliation='http://id.loc.gov/authorities/names/n2006093878',
            descr='http://id.loc.gov/authorities/names/n2006093878',
        ),),
    ('Turner', 'Stephen', ''): dict(
        affiliation='University of South Florida',
        yob=1951,
        descr=(
            'American philosopher and sociologist (Stephen Park Turner), '
            'Distinguished University Professor of Philosophy at the University'
            ' of South Florida, working on social theory, the theory of '
            'practices, political theory and the philosophy of social science. '
            'Author of The Social Theory of Practices and co-author of The '
            'Impossible Science.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Stephen_Park_Turner',
            affiliation='https://en.wikipedia.org/wiki/Stephen_Park_Turner',
            descr='https://en.wikipedia.org/wiki/Stephen_Park_Turner',
        ),),
    ('Watkins', 'J.', 'W. N.'): dict(
        affiliation='London School of Economics',
        yob=1924,
        yod=1999,
        descr=(
            'British philosopher of science and student of Karl Popper, who '
            'taught at the London School of Economics from the 1950s and '
            "succeeded Popper in his chair in 1970. Author of Hobbes's System "
            'of Ideas (1965) and Science and Scepticism (1984); an early critic'
            " of Oakeshott's political theory (1952)."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_W._N._Watkins',
            yod='https://en.wikipedia.org/wiki/John_W._N._Watkins',
            affiliation='https://en.wikipedia.org/wiki/John_W._N._Watkins',
            descr='https://en.wikipedia.org/wiki/John_W._N._Watkins',
        ),),
    ('Wells', 'H.', ''): dict(
        affiliation='Temple University',
        descr=(
            "American legal historian and law professor at Temple University's "
            'Beasley School of Law, trained in history (PhD, University of '
            'Virginia) and law (JD, Vanderbilt). He works on the history of '
            'corporate and business law and the legal profession; early in his '
            "career he published an essay on Oakeshott's philosophy in the "
            'Journal of the History of Ideas.'
        ),
        sources=dict(
            affiliation='https://law.temple.edu/?p=1448',
            descr='https://law.temple.edu/wp-content/uploads/Wells-cv-2025long.pdf',
        ),),
    ('Williams', 'Kevin', ''): dict(
        affiliation='Dublin City University',
        descr=(
            'Philosopher of education based in Ireland, attached to the '
            'Institute of Education at Dublin City University. He has written '
            "on Oakeshott's philosophy of education since the 1980s, in Irish "
            'and British education journals, and is the author of Education and'
            ' the Voice of Michael Oakeshott (2007).'
        ),
        sources=dict(
            affiliation='https://cosmosandtaxis.org/wp-content/uploads/2025/03/Williams_CT_Vol13_Iss_3_4.pdf',
            descr='https://cosmosandtaxis.org/wp-content/uploads/2025/03/Williams_CT_Vol13_Iss_3_4.pdf',
        ),),
    ('Wolmarans', 'F.', 'G.'): dict(
        affiliation='University of Pretoria',
        descr=(
            "South African political theorist (Frederik Gerhardus 'Gerhard' "
            'Wolmarans) at the University of Pretoria, working on democratic '
            'theory, multiculturalism, African humanism and hermeneutics, and '
            "applying Oakeshott's political theory to the post-1994 South "
            'African state.'
        ),
        sources=dict(
            affiliation='https://www.up.ac.za/political-sciences/dr-gerhard-wolmarans',
            descr='https://www.up.ac.za/political-sciences/staff-profiles/gerhard-wolmarans',
        ),),
    ('Worthington', 'Glenn', ''): dict(
        affiliation='Parliament of Australia',
        descr=(
            'Australian scholar who wrote his doctorate on Oakeshott at the '
            'Australian National University, published as Religious and Poetic '
            'Experience in the Thought of Michael Oakeshott (2005), along with '
            "articles on Oakeshott's views of politics, religion and poetry. He"
            ' later worked for parliamentary committees in the Commonwealth '
            'Parliament of Australia.'
        ),
        sources=dict(
            affiliation='https://vlex.co.uk/vid/contributors-874323169',
            descr='https://vlex.co.uk/vid/contributors-874323169',
        ),),
    ('Wulf', 'S.', 'J.'): dict(
        affiliation='Lawrence University',
        yob=1972,
        descr=(
            'Political theorist, associate professor of government at Lawrence '
            'University since 2002, with a BA from Cornell and a PhD from Yale.'
            ' He works on political authority, obligation, rights and '
            'constitutions, and is the author of A Philosophical Theory of '
            'Citizenship (2008).'
        ),
        sources=dict(
            yob='http://id.loc.gov/authorities/names/n2008010314',
            affiliation='https://www.lawrence.edu/people/steven-wulf/',
            descr='https://www.lawrence.edu/people/steven-wulf/',
        ),),
    ('Arendt', 'H.', ''): dict(
        url='https://en.wikipedia.org/wiki/Hannah_Arendt',
        affiliation='The New School',
        yob=1906,
        yod=1975,
        descr=(
            'German-born American political theorist and philosopher, among'
            ' the most influential political thinkers of the twentieth '
            'century, author of The Origins of Totalitarianism and The '
            'Human Condition. Oakeshott reviewed her essay collection '
            'Between Past and Future in Political Science Quarterly (1962).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Hannah_Arendt',
            yod='https://en.wikipedia.org/wiki/Hannah_Arendt',
            affiliation='https://en.wikipedia.org/wiki/Hannah_Arendt',
            descr='https://en.wikipedia.org/wiki/Hannah_Arendt',
            url='https://en.wikipedia.org/wiki/Hannah_Arendt',
        ),
    ),
    ('Aron', 'R.', ''): dict(
        url='https://en.wikipedia.org/wiki/Raymond_Aron',
        affiliation='Collège de France',
        yob=1905,
        yod=1983,
        descr=(
            'French philosopher, sociologist and political journalist, one '
            'of the leading liberal intellectuals of postwar France and a '
            'critic of Marxism. Oakeshott reviewed the English translation '
            'of his The Opium of the Intellectuals in Time and Tide (1957).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Raymond_Aron',
            yod='https://en.wikipedia.org/wiki/Raymond_Aron',
            affiliation='https://en.wikipedia.org/wiki/Raymond_Aron',
            descr='https://en.wikipedia.org/wiki/Raymond_Aron',
            url='https://en.wikipedia.org/wiki/Raymond_Aron',
        ),
    ),
    ('Avineri', 'S.', ''): dict(
        url='https://en.wikipedia.org/wiki/Shlomo_Avineri',
        affiliation='Hebrew University of Jerusalem',
        yob=1933,
        yod=2023,
        descr=(
            'Israeli political scientist and long-time professor at the '
            'Hebrew University of Jerusalem, known for studies of Hegel, '
            "Marx and Zionist thought. Oakeshott reviewed his Hegel's "
            'Theory of the Modern State in European Studies Review (1975).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Shlomo_Avineri',
            yod='https://en.wikipedia.org/wiki/Shlomo_Avineri',
            affiliation='https://en.wikipedia.org/wiki/Shlomo_Avineri',
            descr='https://en.wikipedia.org/wiki/Shlomo_Avineri',
            url='https://en.wikipedia.org/wiki/Shlomo_Avineri',
        ),
    ),
    ('Ayer', 'A.', 'J.'): dict(
        url='https://en.wikipedia.org/wiki/A._J._Ayer',
        affiliation='University of Oxford',
        yob=1910,
        yod=1989,
        descr=(
            'English philosopher who made his name expounding logical '
            'positivism in Language, Truth and Logic (1936); later Wykeham '
            'Professor of Logic at Oxford. Oakeshott reviewed the '
            'collective volume Studies in Communication, by Ayer and '
            'others, in the Spectator (1956).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/A._J._Ayer',
            yod='https://en.wikipedia.org/wiki/A._J._Ayer',
            affiliation='https://en.wikipedia.org/wiki/A._J._Ayer',
            descr='https://en.wikipedia.org/wiki/A._J._Ayer',
            url='https://en.wikipedia.org/wiki/A._J._Ayer',
        ),
    ),
    ('Barber', 'B.', 'R.'): dict(
        url='https://en.wikipedia.org/wiki/Benjamin_Barber',
        affiliation='University of Maryland',
        yob=1939,
        yod=2017,
        descr=(
            'American political theorist, long at Rutgers and later at the '
            'University of Maryland, best known for Strong Democracy and '
            'Jihad vs. McWorld. His critical essay "Conserving Politics" '
            "(Government and Opposition, 1976) discussed Oakeshott's On "
            'Human Conduct.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Benjamin_Barber',
            yod='https://en.wikipedia.org/wiki/Benjamin_Barber',
            affiliation='https://en.wikipedia.org/wiki/Benjamin_Barber',
            descr='https://en.wikipedia.org/wiki/Benjamin_Barber',
            url='https://en.wikipedia.org/wiki/Benjamin_Barber',
        ),
    ),
    ('Barker', 'E.', ''): dict(
        url='https://en.wikipedia.org/wiki/Ernest_Barker',
        affiliation="King's College London",
        yob=1874,
        yod=1960,
        descr=(
            "English political scientist, Principal of King's College "
            'London (1920-27) and later the first Professor of Political '
            'Science at Cambridge. Oakeshott reviewed his translation of '
            "Gierke's Natural Law and the Theory of Society in the "
            'Cambridge Review (1934).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Ernest_Barker',
            yod='https://en.wikipedia.org/wiki/Ernest_Barker',
            affiliation='https://en.wikipedia.org/wiki/Ernest_Barker',
            descr='https://en.wikipedia.org/wiki/Ernest_Barker',
            url='https://en.wikipedia.org/wiki/Ernest_Barker',
        ),
    ),
    ('Barraclough', 'G.', ''): dict(
        url='https://en.wikipedia.org/wiki/Geoffrey_Barraclough',
        affiliation='Brandeis University',
        yob=1908,
        yod=1984,
        descr=(
            'English historian of medieval Europe and Germany who held '
            'chairs at Liverpool, London, Oxford (Chichele Professor) and '
            'Brandeis. Oakeshott reviewed his History in a Changing World '
            'in the Spectator (1956), and he reviewed the Oakeshott '
            'Festschrift Politics and Experience there (1969).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Geoffrey_Barraclough',
            yod='https://en.wikipedia.org/wiki/Geoffrey_Barraclough',
            affiliation='https://en.wikipedia.org/wiki/Geoffrey_Barraclough',
            descr='https://en.wikipedia.org/wiki/Geoffrey_Barraclough',
            url='https://en.wikipedia.org/wiki/Geoffrey_Barraclough',
        ),
    ),
    ('Beneš', 'E.', ''): dict(
        url='https://en.wikipedia.org/wiki/Edvard_Bene%C5%A1',
        yob=1884,
        yod=1948,
        descr=(
            'Czech statesman, President of Czechoslovakia 1935-38 and '
            '1939-48, who led the government-in-exile during the Second '
            'World War. Oakeshott reviewed the English edition of his '
            'Memoirs in the Spectator (1954).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Edvard_Bene%C5%A1',
            yod='https://en.wikipedia.org/wiki/Edvard_Bene%C5%A1',
            descr='https://en.wikipedia.org/wiki/Edvard_Bene%C5%A1',
            url='https://en.wikipedia.org/wiki/Edvard_Bene%C5%A1',
        ),
    ),
    ('Berdyaev', 'N.', ''): dict(
        url='https://en.wikipedia.org/wiki/Nikolai_Berdyaev',
        yob=1874,
        yod=1948,
        descr=(
            'Russian religious philosopher and Christian existentialist who'
            ' emphasized human freedom and personhood, expelled from Soviet'
            ' Russia in 1922. Oakeshott reviewed the English translation of'
            ' his The Meaning of History in the Cambridge Review (1936).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Nikolai_Berdyaev',
            yod='https://en.wikipedia.org/wiki/Nikolai_Berdyaev',
            descr='https://en.wikipedia.org/wiki/Nikolai_Berdyaev',
            url='https://en.wikipedia.org/wiki/Nikolai_Berdyaev',
        ),
    ),
    ('Berkowitz', 'P.', ''): dict(
        url='https://en.wikipedia.org/wiki/Peter_Berkowitz',
        affiliation='Hoover Institution',
        yob=1959,
        descr=(
            'American political scientist and legal scholar, a senior '
            "fellow at Stanford's Hoover Institution and Director of Policy"
            ' Planning at the US State Department in 2019-21. He reviewed '
            "Oakeshott's The Politics of Faith and the Politics of "
            'Scepticism in First Things (1997).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Peter_Berkowitz',
            affiliation='https://en.wikipedia.org/wiki/Peter_Berkowitz',
            descr='https://en.wikipedia.org/wiki/Peter_Berkowitz',
            url='https://en.wikipedia.org/wiki/Peter_Berkowitz',
        ),
    ),
    ('Bernal', 'J.', 'D.'): dict(
        url='https://en.wikipedia.org/wiki/J._D._Bernal',
        affiliation='Birkbeck College, University of London',
        yob=1901,
        yod=1971,
        descr=(
            'Irish-born physicist who pioneered X-ray crystallography in '
            'molecular biology and wrote widely on science and society from'
            ' a Marxist standpoint. Oakeshott reviewed his essay collection'
            ' The Freedom of Necessity in the Times Literary Supplement '
            '(1949).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/J._D._Bernal',
            yod='https://en.wikipedia.org/wiki/J._D._Bernal',
            affiliation='https://en.wikipedia.org/wiki/J._D._Bernal',
            descr='https://en.wikipedia.org/wiki/J._D._Bernal',
            url='https://en.wikipedia.org/wiki/J._D._Bernal',
        ),
    ),
    ('Bradley', 'F.', 'H.'): dict(
        url='https://en.wikipedia.org/wiki/F._H._Bradley',
        affiliation='Merton College, Oxford',
        yob=1846,
        yod=1924,
        descr=(
            'British idealist philosopher, a Fellow of Merton College, '
            'Oxford, whose chief work was Appearance and Reality (1893) and'
            " who strongly influenced Oakeshott's Experience and Its Modes."
            ' Oakeshott reviewed his Aphorisms (1931) and Collected Essays '
            '(1936).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/F._H._Bradley',
            yod='https://en.wikipedia.org/wiki/F._H._Bradley',
            affiliation='https://en.wikipedia.org/wiki/F._H._Bradley',
            descr='https://en.wikipedia.org/wiki/F._H._Bradley',
            url='https://en.wikipedia.org/wiki/F._H._Bradley',
        ),
    ),
    ('Brogan', 'D.', 'W.'): dict(
        url='https://en.wikipedia.org/wiki/Denis_William_Brogan',
        affiliation='University of Cambridge',
        yob=1900,
        yod=1974,
        descr=(
            'Scottish historian and writer, Professor of Political Science '
            'at Cambridge, noted for his books on American and French '
            'politics. Oakeshott reviewed his The Price of Revolution in '
            'the Spectator (1951).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Denis_William_Brogan',
            yod='https://en.wikipedia.org/wiki/Denis_William_Brogan',
            affiliation='https://en.wikipedia.org/wiki/Denis_William_Brogan',
            descr='https://en.wikipedia.org/wiki/Denis_William_Brogan',
            url='https://en.wikipedia.org/wiki/Denis_William_Brogan',
        ),
    ),
    ('Bromwich', 'D.', ''): dict(
        url='https://en.wikipedia.org/wiki/David_Bromwich',
        affiliation='Yale University',
        descr=(
            'American literary scholar and critic, Sterling Professor of '
            'English at Yale, who writes on Romantic literature, Burke and '
            "politics. He reviewed Oakeshott's The Voice of Liberal "
            'Learning in the New Republic (1989).'
        ),
        sources=dict(
            affiliation='https://en.wikipedia.org/wiki/David_Bromwich',
            descr='https://en.wikipedia.org/wiki/David_Bromwich',
            url='https://en.wikipedia.org/wiki/David_Bromwich',
        ),
    ),
    ('Burckhardt', 'Jacob', ''): dict(
        url='https://en.wikipedia.org/wiki/Jacob_Burckhardt',
        yob=1818,
        yod=1897,
        descr=(
            'Swiss historian of art and culture, author of The Civilization'
            ' of the Renaissance in Italy (1860) and a founder of cultural '
            'history. Oakeshott reviewed The Letters of Jacob Burckhardt, '
            'edited by A. Dru, in Encounter (1954).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Jacob_Burckhardt',
            yod='https://en.wikipedia.org/wiki/Jacob_Burckhardt',
            descr='https://en.wikipedia.org/wiki/Jacob_Burckhardt',
            url='https://en.wikipedia.org/wiki/Jacob_Burckhardt',
        ),
    ),
    ('Burnham', 'J.', ''): dict(
        url='https://en.wikipedia.org/wiki/James_Burnham',
        yob=1905,
        yod=1987,
        descr=(
            'American philosopher and political theorist, a Trotskyist in '
            'the 1930s who became a leading anti-communist and National '
            'Review editor; author of The Managerial Revolution. Oakeshott '
            'reviewed his The Coming Defeat of Communism in the Evening '
            'Standard (1950).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/James_Burnham',
            yod='https://en.wikipedia.org/wiki/James_Burnham',
            descr='https://en.wikipedia.org/wiki/James_Burnham',
            url='https://en.wikipedia.org/wiki/James_Burnham',
        ),
    ),
    ('Butterfield', 'H.', ''): dict(
        url='https://en.wikipedia.org/wiki/Herbert_Butterfield',
        affiliation='University of Cambridge',
        yob=1900,
        yod=1979,
        descr=(
            'English historian and philosopher of history, Regius Professor'
            ' of Modern History and Master of Peterhouse, author of The '
            'Whig Interpretation of History. Oakeshott reviewed his Origins'
            ' of Modern Science (1949), Man and His Past (1955) and George '
            'III and the Historians (1957).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Herbert_Butterfield',
            yod='https://en.wikipedia.org/wiki/Herbert_Butterfield',
            affiliation='https://en.wikipedia.org/wiki/Herbert_Butterfield',
            descr='https://en.wikipedia.org/wiki/Herbert_Butterfield',
            url='https://en.wikipedia.org/wiki/Herbert_Butterfield',
        ),
    ),
    ('Carr', 'E.', 'H.'): dict(
        url='https://en.wikipedia.org/wiki/E._H._Carr',
        yob=1892,
        yod=1982,
        descr=(
            'British historian, diplomat and international-relations '
            'theorist, author of A History of Soviet Russia, The Twenty '
            "Years' Crisis and What Is History?. Oakeshott reviewed his The"
            ' New Society and the first volume of The Bolshevik Revolution '
            '(both 1951).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/E._H._Carr',
            yod='https://en.wikipedia.org/wiki/E._H._Carr',
            descr='https://en.wikipedia.org/wiki/E._H._Carr',
            url='https://en.wikipedia.org/wiki/E._H._Carr',
        ),
    ),
    ('Carritt', 'E.', 'F.'): dict(
        url='https://en.wikipedia.org/wiki/Edgar_Frederick_Carritt',
        affiliation='University College, Oxford',
        yob=1876,
        yod=1964,
        descr=(
            'English philosopher, Fellow of University College, Oxford '
            '(1898-1945), who wrote on aesthetics and moral and political '
            'philosophy. Oakeshott reviewed his Morals and Politics in the '
            'Cambridge Review (1935).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Edgar_Frederick_Carritt',
            yod='https://en.wikipedia.org/wiki/Edgar_Frederick_Carritt',
            affiliation='https://en.wikipedia.org/wiki/Edgar_Frederick_Carritt',
            descr='https://en.wikipedia.org/wiki/Edgar_Frederick_Carritt',
            url='https://en.wikipedia.org/wiki/Edgar_Frederick_Carritt',
        ),
    ),
    ('Catlin', 'G.', 'E. G.'): dict(
        url='https://en.wikipedia.org/wiki/George_Catlin_(political_scientist)',
        affiliation='Cornell University',
        yob=1896,
        yod=1979,
        descr=(
            'English political scientist and philosopher who taught for '
            'years at Cornell and argued for a natural-science model of '
            'politics. Oakeshott reviewed his The Principles of Politics '
            '(1930), and Catlin reviewed Rationalism in Politics in the '
            'Western Political Quarterly (1963).'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/George_Catlin_(political_sci'
                'entist)'
            ),
            yod=(
                'https://en.wikipedia.org/wiki/George_Catlin_(political_sci'
                'entist)'
            ),
            affiliation=(
                'https://en.wikipedia.org/wiki/George_Catlin_(political_sci'
                'entist)'
            ),
            descr=(
                'https://en.wikipedia.org/wiki/George_Catlin_(political_sci'
                'entist)'
            ),
            url=(
                'https://en.wikipedia.org/wiki/George_Catlin_(political_sci'
                'entist)'
            ),
        ),
    ),
    ('Chestov', 'L.', ''): dict(
        url='https://en.wikipedia.org/wiki/Lev_Shestov',
        yob=1866,
        yod=1938,
        descr=(
            'Russian existentialist and religious philosopher (Lev '
            'Shestov), a critic of rationalism and positivism. Oakeshott '
            "reviewed the English translation of his In Job's Balances "
            'in Scrutiny (1933).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Lev_Shestov',
            yod='https://en.wikipedia.org/wiki/Lev_Shestov',
            descr='https://en.wikipedia.org/wiki/Lev_Shestov',
            url='https://en.wikipedia.org/wiki/Lev_Shestov',
        ),
    ),
    ('Bulwer-Lytton', 'Victor', ''): dict(
        url=(
            'https://en.wikipedia.org/wiki/Victor_Bulwer-Lytton,_2nd_Earl_o'
            'f_Lytton'
        ),
        yob=1876,
        yod=1947,
        descr=(
            'British politician and colonial administrator, Governor of '
            "Bengal and head of the League of Nations' Lytton Commission on"
            ' Manchuria. His study Bulwer-Lytton, on his grandfather the '
            'novelist, appeared posthumously in 1948 and was reviewed by '
            'Oakeshott in the Cambridge Journal.'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Victor_Bulwer-Lytton,_2nd_Ea'
                'rl_of_Lytton'
            ),
            yod=(
                'https://en.wikipedia.org/wiki/Victor_Bulwer-Lytton,_2nd_Ea'
                'rl_of_Lytton'
            ),
            descr='https://catalogue.bnf.fr/ark:/12148/cb13739647w',
            url=(
                'https://en.wikipedia.org/wiki/Victor_Bulwer-Lytton,_2nd_Ea'
                'rl_of_Lytton'
            ),
        ),
    ),
    ('Beloff', 'M.', ''): dict(
        url='https://en.wikipedia.org/wiki/Max_Beloff,_Baron_Beloff',
        affiliation='University of Buckingham',
        yob=1913,
        yod=1999,
        descr=(
            'British historian and Conservative life peer, Gladstone '
            'Professor at Oxford and first principal of the University '
            'College of Buckingham (1974-79). He reviewed the Oakeshott '
            'retirement Festschrift Politics and Experience in the '
            'Cambridge Review (1969).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Max_Beloff,_Baron_Beloff',
            yod='https://en.wikipedia.org/wiki/Max_Beloff,_Baron_Beloff',
            affiliation='https://en.wikipedia.org/wiki/Max_Beloff,_Baron_Beloff',
            descr='https://en.wikipedia.org/wiki/Max_Beloff,_Baron_Beloff',
            url='https://en.wikipedia.org/wiki/Max_Beloff,_Baron_Beloff',
        ),
    ),
    ('Bentley', 'M.', ''): dict(
        url='https://en.wikipedia.org/wiki/Michael_Bentley_(historian)',
        affiliation='University of St Andrews',
        yob=1948,
        descr=(
            'English historian of nineteenth- and twentieth-century British'
            ' politics and of historiography, Emeritus Professor at St '
            'Andrews and biographer of Herbert Butterfield. He reviewed '
            "Luke O'Sullivan's Oakeshott on History in the English "
            'Historical Review (2003).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Michael_Bentley_(historian)',
            affiliation='https://en.wikipedia.org/wiki/Michael_Bentley_(historian)',
            descr='https://en.wikipedia.org/wiki/Michael_Bentley_(historian)',
            url='https://en.wikipedia.org/wiki/Michael_Bentley_(historian)',
        ),
    ),
    ('Bebbington', 'D.', 'W.'): dict(
        url='https://en.wikipedia.org/wiki/David_W._Bebbington',
        affiliation='University of Stirling',
        yob=1949,
        descr=(
            'British historian, professor at the University of Stirling, '
            'known for work on evangelicalism and on philosophies of '
            "history (Patterns in History). He reviewed Oakeshott's On "
            'History and Other Essays in British Book News (1983).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/David_W._Bebbington',
            affiliation='https://en.wikipedia.org/wiki/David_W._Bebbington',
            descr='https://en.wikipedia.org/wiki/David_W._Bebbington',
            url='https://en.wikipedia.org/wiki/David_W._Bebbington',
        ),
    ),
    ('Casey', 'J.', ''): dict(
        url='https://en.wikipedia.org/wiki/John_Casey_(academic)',
        affiliation='Gonville and Caius College, Cambridge',
        yob=1939,
        descr=(
            'British academic and journalist, Life Fellow of Gonville and '
            'Caius College, Cambridge, co-founder with Roger Scruton of the'
            ' Conservative Philosophy Group and editor of the Cambridge '
            'Review. He wrote "Mankind in Conversation" on Oakeshott\'s '
            'philosophy in the TLS (1991).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Casey_(academic)',
            affiliation='https://en.wikipedia.org/wiki/John_Casey_(academic)',
            descr='https://en.wikipedia.org/wiki/John_Casey_(academic)',
            url='https://en.wikipedia.org/wiki/John_Casey_(academic)',
        ),
    ),
    ('Coady', 'C.', 'A. J.'): dict(
        url='https://en.wikipedia.org/wiki/C._A._J._Coady',
        affiliation='University of Melbourne',
        yob=1936,
        descr=(
            'Australian philosopher working in epistemology and political '
            'and applied ethics, best known for Testimony: A Philosophical '
            'Study (1990). He reviewed a book titled Oakeshott in the '
            'Philosophical Quarterly (1995).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/C._A._J._Coady',
            affiliation='https://en.wikipedia.org/wiki/C._A._J._Coady',
            descr='https://en.wikipedia.org/wiki/C._A._J._Coady',
            url='https://en.wikipedia.org/wiki/C._A._J._Coady',
        ),
    ),
    ('Charvet', 'J.', ''): dict(
        url='https://en.wikipedia.org/wiki/John_Charvet',
        affiliation='London School of Economics',
        yob=1938,
        yod=2024,
        descr=(
            'British political theorist and Emeritus Professor at the '
            "London School of Economics, Oakeshott's former department, "
            'writing on equality, contractarianism and human rights. He '
            "reviewed Efraim Podoksik's In Defence of Modernity in History "
            'of Political Thought (2004).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Charvet',
            yod='https://en.wikipedia.org/wiki/John_Charvet',
            affiliation='https://en.wikipedia.org/wiki/John_Charvet',
            descr='https://en.wikipedia.org/wiki/John_Charvet',
            url='https://en.wikipedia.org/wiki/John_Charvet',
        ),
    ),
    ('Berns', 'W.', ''): dict(
        url='https://en.wikipedia.org/wiki/Walter_Berns',
        affiliation='Georgetown University',
        yob=1919,
        yod=2015,
        descr=(
            'American constitutional scholar and political philosopher, a '
            'student of Leo Strauss, later at Georgetown and the American '
            "Enterprise Institute. He reviewed Oakeshott's Rationalism in "
            'Politics in the American Political Science Review (1963).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Walter_Berns',
            yod='https://en.wikipedia.org/wiki/Walter_Berns',
            affiliation='https://en.wikipedia.org/wiki/Walter_Berns',
            descr='https://en.wikipedia.org/wiki/Walter_Berns',
            url='https://en.wikipedia.org/wiki/Walter_Berns',
        ),
    ),
    ('Armour', 'L.', ''): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Leslie_Armour',
            yod='https://en.wikipedia.org/wiki/Leslie_Armour',
            affiliation='https://en.wikipedia.org/wiki/Leslie_Armour',
            descr='https://en.wikipedia.org/wiki/Leslie_Armour',
            url='https://en.wikipedia.org/wiki/Leslie_Armour',
        ),
    ),
    ('Charlton', 'B.', ''): dict(
        url='https://en.wikipedia.org/wiki/Bruce_Charlton',
        affiliation='Newcastle University',
        descr=(
            'British medical doctor and theoretical-medicine writer, Reader'
            ' in Evolutionary Psychiatry at Newcastle University and editor'
            " of Medical Hypotheses (2003-10). He reviewed Oakeshott's "
            'Morality and Politics in Modern Europe in Psychological '
            'Medicine (1995).'
        ),
        sources=dict(
            affiliation='https://en.wikipedia.org/wiki/Bruce_Charlton',
            descr='https://en.wikipedia.org/wiki/Bruce_Charlton',
            url='https://en.wikipedia.org/wiki/Bruce_Charlton',
        ),
    ),
    ('Atkins', 'G.', 'G.'): dict(
        url='https://en.wikipedia.org/wiki/Gaius_Glenn_Atkins',
        affiliation='Auburn Theological Seminary',
        yob=1868,
        yod=1956,
        descr=(
            'American Congregational minister and author, professor of '
            'homiletics at Auburn Theological Seminary. Oakeshott reviewed '
            'his The Making of the Christian Mind in the Journal of '
            'Theological Studies (1930).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Gaius_Glenn_Atkins',
            yod='https://en.wikipedia.org/wiki/Gaius_Glenn_Atkins',
            affiliation='https://en.wikipedia.org/wiki/Gaius_Glenn_Atkins',
            descr='https://en.wikipedia.org/wiki/Gaius_Glenn_Atkins',
            url='https://en.wikipedia.org/wiki/Gaius_Glenn_Atkins',
        ),
    ),
    ('Bowie', 'W.', 'R.'): dict(
        url='https://en.wikipedia.org/wiki/Walter_Russell_Bowie',
        yob=1882,
        yod=1969,
        descr=(
            'American Episcopal priest, author, editor and hymn writer, '
            'rector of Grace Church, New York, and later a seminary '
            'professor. Oakeshott reviewed his The Inescapable Christ in '
            'the Journal of Theological Studies (1927).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Walter_Russell_Bowie',
            yod='https://en.wikipedia.org/wiki/Walter_Russell_Bowie',
            descr='https://en.wikipedia.org/wiki/Walter_Russell_Bowie',
            url='https://en.wikipedia.org/wiki/Walter_Russell_Bowie',
        ),
    ),
    ('Blackham', 'H.', 'J.'): dict(
        url='https://en.wikipedia.org/wiki/H._J._Blackham',
        yob=1903,
        yod=2009,
        descr=(
            'British humanist philosopher, writer and educationalist, often'
            ' called the progenitor of modern humanism in Britain. '
            'Oakeshott reviewed his Political Discipline in a Free Society '
            'in the Sunday Telegraph (1961).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/H._J._Blackham',
            yod='https://en.wikipedia.org/wiki/H._J._Blackham',
            descr='https://en.wikipedia.org/wiki/H._J._Blackham',
            url='https://en.wikipedia.org/wiki/H._J._Blackham',
        ),
    ),
    ('Bryson', 'G.', ''): dict(
        url='https://en.wikipedia.org/wiki/Gladys_Bryson',
        affiliation='Smith College',
        yob=1894,
        yod=1952,
        descr=(
            'American sociologist, professor and chair of sociology at '
            'Smith College. Oakeshott reviewed her Man and Society: The '
            'Scottish Inquiry of the Eighteenth Century in the English '
            'Historical Review (1948).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Gladys_Bryson',
            yod='https://en.wikipedia.org/wiki/Gladys_Bryson',
            affiliation='https://en.wikipedia.org/wiki/Gladys_Bryson',
            descr='https://en.wikipedia.org/wiki/Gladys_Bryson',
            url='https://en.wikipedia.org/wiki/Gladys_Bryson',
        ),
    ),
    ('Calleo', 'D.', 'P.'): dict(
        url='https://en.wikipedia.org/wiki/David_P._Calleo',
        affiliation='Johns Hopkins University',
        yob=1934,
        yod=2023,
        descr=(
            'American political scientist at the Johns Hopkins School of '
            'Advanced International Studies, long director of its European '
            'Studies program. Oakeshott reviewed his Coleridge and the Idea'
            ' of the Modern State, in New Society (1966).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/David_P._Calleo',
            yod='https://en.wikipedia.org/wiki/David_P._Calleo',
            affiliation='https://en.wikipedia.org/wiki/David_P._Calleo',
            descr='https://en.wikipedia.org/wiki/David_P._Calleo',
            url='https://en.wikipedia.org/wiki/David_P._Calleo',
        ),
    ),
    ('Carington', 'W.', ''): dict(
        url='https://en.wikipedia.org/wiki/Whately_Carington',
        yod=1947,
        descr=(
            'British parapsychologist (born Walter Whately Smith) known for'
            ' experiments on telepathy. Oakeshott reviewed his posthumous '
            'Matter, Mind, and Meaning in the Times Literary Supplement '
            '(1949).'
        ),
        sources=dict(
            yod='https://en.wikipedia.org/wiki/Whately_Carington',
            descr='https://en.wikipedia.org/wiki/Whately_Carington',
            url='https://en.wikipedia.org/wiki/Whately_Carington',
            yob='https://en.wikipedia.org/wiki/Whately_Carington',
        ),
        yob=1892,
    ),
    ('Britton', 'L.', ''): dict(
        url='https://en.wikipedia.org/wiki/Lionel_Britton',
        yob=1887,
        yod=1971,
        descr=(
            'British working-class novelist and playwright. Oakeshott '
            'reviewed his novel Hunger and Love in the Cambridge Review '
            '(1931).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Lionel_Britton',
            yod='https://en.wikipedia.org/wiki/Lionel_Britton',
            descr='https://en.wikipedia.org/wiki/Lionel_Britton',
            url='https://en.wikipedia.org/wiki/Lionel_Britton',
        ),
    ),
    ('Burns', 'C.', 'D.'): dict(
        url='https://en.wikipedia.org/wiki/C._Delisle_Burns',
        yob=1879,
        yod=1942,
        descr=(
            'English secularist writer and lecturer on philosophy and '
            'politics, later at the University of Glasgow. Oakeshott '
            'reviewed his The Horizon of Experience in the Journal of '
            'Theological Studies (1934).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/C._Delisle_Burns',
            yod='https://en.wikipedia.org/wiki/C._Delisle_Burns',
            descr='https://en.wikipedia.org/wiki/C._Delisle_Burns',
            url='https://en.wikipedia.org/wiki/C._Delisle_Burns',
        ),
    ),
    ('Bowle', 'J.', ''): dict(
        url='https://en.wikipedia.org/wiki/John_Bowle_(historian)',
        affiliation='College of Europe',
        yob=1905,
        yod=1985,
        descr=(
            'English historian and writer, a schoolmaster at Eton, lecturer'
            ' at Wadham College, Oxford, and Professor of Political Theory '
            'at the College of Europe, Bruges. Oakeshott reviewed four of '
            'his books, including Hobbes and His Critics, and Bowle '
            'reviewed Rationalism in Politics (1962).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Bowle_(historian)',
            yod='https://en.wikipedia.org/wiki/John_Bowle_(historian)',
            affiliation='https://en.wikipedia.org/wiki/John_Bowle_(historian)',
            descr='https://en.wikipedia.org/wiki/John_Bowle_(historian)',
            url='https://en.wikipedia.org/wiki/John_Bowle_(historian)',
        ),
    ),
    ('Burleigh', 'J.', 'H. S.'): dict(
        url='https://en.wikipedia.org/wiki/J._H._S._Burleigh',
        yob=1894,
        yod=1985,
        descr=(
            'Scottish minister and scholar, Moderator of the General '
            'Assembly of the Church of Scotland in 1960. Oakeshott reviewed'
            " his study of Augustine's The City of God in the Cambridge "
            'Journal (1951).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/J._H._S._Burleigh',
            yod='https://en.wikipedia.org/wiki/J._H._S._Burleigh',
            descr='https://en.wikipedia.org/wiki/J._H._S._Burleigh',
            url='https://en.wikipedia.org/wiki/J._H._S._Burleigh',
        ),
    ),
    ('Birch', 'F.', ''): dict(
        url='https://en.wikipedia.org/wiki/Frank_Birch',
        yob=1889,
        yod=1956,
        descr=(
            "English historian, actor and cryptographer, educated at King's"
            ' College, Cambridge, who headed the naval section at Bletchley'
            ' Park in the Second World War and later wrote the official '
            'history of British SIGINT. Oakeshott reviewed his This Freedom'
            ' of Ours in the Cambridge Review (1937).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Frank_Birch',
            yod='https://en.wikipedia.org/wiki/Frank_Birch',
            descr=(
                'https://www.barnesandnoble.com/w/this-freedom-of-ours-fran'
                'k-birch/1117677326'
            ),
            url='https://en.wikipedia.org/wiki/Frank_Birch',
        ),
    ),
    ('Bouquet', 'A.', 'C.'): dict(
        url='https://en.wikipedia.org/wiki/A._C._Bouquet',
        affiliation='University of Cambridge',
        yob=1884,
        yod=1976,
        descr=(
            "Anglican priest and theologian, vicar of All Saints', "
            'Cambridge, and Recognised Lecturer in the History and '
            'Comparative Study of Religions at Cambridge. Oakeshott '
            'reviewed his Hulsean Lectures, The Christian Religion and Its '
            'Competitors Today, in the Journal of Theological Studies '
            '(1926).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/A._C._Bouquet',
            yod='https://en.wikipedia.org/wiki/A._C._Bouquet',
            affiliation='https://en.wikipedia.org/wiki/A._C._Bouquet',
            descr='https://en.wikipedia.org/wiki/A._C._Bouquet',
            url='https://en.wikipedia.org/wiki/A._C._Bouquet',
        ),
    ),
    ('Brooke', 'J.', ''): dict(
        url='https://en.wikipedia.org/wiki/John_Brooke_(British_historian)',
        affiliation='Royal Commission on Historical Manuscripts',
        yob=1920,
        yod=1985,
        descr=(
            'British historian of eighteenth-century politics, Lewis '
            "Namier's principal assistant on the History of Parliament and "
            'biographer of George III. Oakeshott reviewed his The Chatham '
            'Administration 1766-1768, in the Spectator (1956).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Brooke_(British_historian)',
            yod='https://en.wikipedia.org/wiki/John_Brooke_(British_historian)',
            affiliation='https://en.wikipedia.org/wiki/John_Brooke_(British_historian)',
            descr='https://en.wikipedia.org/wiki/John_Brooke_(British_historian)',
            url='https://en.wikipedia.org/wiki/John_Brooke_(British_historian)',
        ),
    ),
    ('Campion', 'S.', ''): dict(
        url='https://en.wikipedia.org/wiki/Sarah_Campion_(writer)',
        yob=1906,
        yod=2002,
        descr=(
            'Pen name of Mary Rose Coulton (later Alpers), English-born '
            'novelist, journalist and broadcaster who settled in Australia,'
            ' daughter of the Cambridge historian G. G. Coulton. Oakeshott '
            'reviewed her memoir Father: A Portrait of G. G. Coulton at '
            'Home in the Cambridge Journal (1948).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Sarah_Campion_(writer)',
            yod='https://en.wikipedia.org/wiki/Sarah_Campion_(writer)',
            descr='https://en.wikipedia.org/wiki/Sarah_Campion_(writer)',
            url='https://en.wikipedia.org/wiki/Sarah_Campion_(writer)',
        ),
    ),
    ('Bourke', 'R.', ''): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Richard_Bourke_(academic)',
            affiliation='https://en.wikipedia.org/wiki/Richard_Bourke_(academic)',
            descr='https://en.wikipedia.org/wiki/Richard_Bourke_(academic)',
            url='https://en.wikipedia.org/wiki/Richard_Bourke_(academic)',
        ),
    ),
    ('Altham', 'J.', 'E. J.'): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Jimmy_Altham',
            affiliation='https://en.wikipedia.org/wiki/Jimmy_Altham',
            descr='https://en.wikipedia.org/wiki/Jimmy_Altham',
            url='https://en.wikipedia.org/wiki/Jimmy_Altham',
        ),
    ),
    ('Barrow', 'R.', 'H.'): dict(
        yob=1893,
        descr=(
            'Reginald Haynes Barrow (born 1893), whose Introduction to St. '
            'Augustine: The City of God (Faber, 1950), with selected text, '
            'translation and commentary, was reviewed by Oakeshott in the '
            'Cambridge Journal (1951).'
        ),
        sources=dict(
            yob='https://tuklas.up.edu.ph/Record/UP-99796217601505380',
            descr='https://catalogue.nli.ie/Record/vtls000409032',
        ),
    ),
    ('Brock', 'W.', ''): dict(
        descr=(
            'Werner Brock, philosopher who had been a teaching assistant to'
            " Heidegger and who later introduced Heidegger's Existence and "
            'Being (1949). Oakeshott reviewed his An Introduction to '
            'Contemporary German Philosophy (Cambridge, 1935), based on '
            'lectures at Bedford College, London.'
        ),
        sources=dict(
            descr=(
                'https://www.cambridge.org/core/product/identifier/CBO97818'
                '44653676A010/type/BOOK_PART'
            ),
        ),
    ),
    ('Chiari', 'J.', ''): dict(
        descr=(
            'Joseph Chiari, critic and poet writing in English on French '
            'and English literature and drama, author of studies of '
            'Claudel, French symbolism and T. S. Eliot. Oakeshott reviewed '
            'his Realism and Imagination (1960) in the British Journal of '
            'Aesthetics (1961).'
        ),
        sources=dict(
            descr=(
                'https://archive.spectator.co.uk/article/16th-december-1960'
                '/25/art-real-and-unreal'
            ),
        ),
    ),
    ('Brodie', 'D.', 'M.'): dict(
        descr=(
            'Dorothy Margaret Brodie, editor of the 1948 Cambridge '
            "University Press edition of Edmund Dudley's The Tree of "
            'Commonwealth, prepared from a British Library manuscript; '
            'Oakeshott reviewed the edition in the Cambridge Journal '
            '(1949).'
        ),
        sources=dict(
            descr='https://library.hull.ac.uk/record=b1242295~S3',
        ),
    ),
    ('Belasco', 'P.', 'S.'): dict(
        descr=(
            'Philip Seth Belasco, author of Authority in Church and State '
            '(Allen & Unwin, 1928), a study of seventeenth-century English '
            'controversies over church and state. Oakeshott reviewed it in '
            'the Journal of Theological Studies (1929).'
        ),
        sources=dict(
            descr='https://search.law.villanova.edu/Record/23183',
        ),
    ),
    ('Brown', 'K.', ''): dict(
        descr=(
            'Keith C. Brown, editor of Hobbes Studies (Oxford: Blackwell, '
            '1965), a collection of essays on Hobbes including Keith '
            'Thomas\'s "The Social Origins of Hobbes\'s Political Thought"; '
            'Oakeshott reviewed it in the English Historical Review.'
        ),
        sources=dict(
            descr=(
                'https://cambridge.org/core/journals/dialogue-canadian-phil'
                'osophical-review-revue-canadienne-de-philosophie/article/h'
                'obbes-studies-edited-by-keith-c-brown-oxford-basil-blackwe'
                'll-toronto-copp-clark-publishing-co1965-pp-xi-300-900/458F'
                'DFF34609AA04448416E726D24112'
            ),
        ),
    ),
    ('Beckstein', 'Martin', ''): dict(
        affiliation='University of Zurich',
        url='https://philpeople.org/profiles/martin-beckstein',
        descr=(
            "Political theorist at the University of Zurich's Institute of "
            'Philosophy, working on the interpretation of political texts '
            'and on conservatism. He reviewed both A Companion to Michael '
            'Oakeshott and The Cambridge Companion to Oakeshott in '
            'Political Studies Review (2014).'
        ),
        sources=dict(
            affiliation='https://uni-goettingen.academia.edu/MBeckstein',
            descr='https://philpapers.org/rec/BECROA',
            url='https://philpeople.org/profiles/martin-beckstein',
        ),
    ),
    ('Berard', 'R.', 'N.'): dict(
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
        sources=dict(
            affiliation=(
                'https://www.msvu.ca/academics/faculty-of-education/faculty'
                '-profiles/dr-robert-berard/'
            ),
            descr=(
                'https://cchahistory.ca/journal/CCHA1997/List%20of%20Contri'
                'butors.htm'
            ),
            url=(
                'https://www.msvu.ca/academics/faculty-of-education/faculty'
                '-profiles/dr-robert-berard/'
            ),
        ),
    ),
    ('Cloud', 'Thomas', ''): dict(
        affiliation='Louisiana State University',
        descr=(
            'American political theorist, a PhD student in political '
            "science at Louisiana State University with a master's in "
            'politics from Hillsdale College. He reviewed the collection '
            'Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, and '
            'Others for VoegelinView (2019).'
        ),
        sources=dict(
            affiliation=(
                'https://voegelinview.com/review-of-tradition-v-rationalism'
                '-voegelin-oakeshott-hayek-and-others/'
            ),
            descr=(
                'https://voegelinview.com/review-of-tradition-v-rationalism'
                '-voegelin-oakeshott-hayek-and-others/'
            ),
        ),
    ),
    ('Cole', 'M.', ''): dict(
        url='https://en.wikipedia.org/wiki/Margaret_Cole',
        yob=1893,
        yod=1980,
        descr=(
            'English socialist writer, poet and London local-government '
            'figure, née Postgate, who co-wrote detective novels with her '
            'husband G. D. H. Cole and was long active in the Fabian '
            'Society. Oakeshott reviewed her The Story of Fabian Socialism '
            '(1961) in the Sunday Telegraph.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Margaret_Cole',
            yod='https://en.wikipedia.org/wiki/Margaret_Cole',
            descr='https://en.wikipedia.org/wiki/Margaret_Cole',
            url='https://en.wikipedia.org/wiki/Margaret_Cole',
        ),
    ),
    ('Collingwood', 'R.', 'G.'): dict(
        url='https://en.wikipedia.org/wiki/R._G._Collingwood',
        yob=1889,
        yod=1943,
        affiliation='University of Oxford',
        descr=(
            'English philosopher, historian and archaeologist, Waynflete '
            'Professor of Metaphysical Philosophy at Oxford. He reviewed '
            'Experience and Its Modes in the Cambridge Review (1933), and '
            'Oakeshott in turn reviewed his The Principles of Art (1938) '
            'and the posthumous The Idea of History (1947).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/R._G._Collingwood',
            yod='https://en.wikipedia.org/wiki/R._G._Collingwood',
            affiliation='https://en.wikipedia.org/wiki/R._G._Collingwood',
            descr='https://en.wikipedia.org/wiki/R._G._Collingwood',
            url='https://en.wikipedia.org/wiki/R._G._Collingwood',
        ),
    ),
    ('Cowling', 'M.', ''): dict(
        url='https://en.wikipedia.org/wiki/Maurice_Cowling',
        yob=1926,
        yod=2005,
        affiliation='Peterhouse, Cambridge',
        descr=(
            'British historian and fellow of Peterhouse, Cambridge, for '
            'most of his career, a leading conservative proponent of the '
            '"high politics" school of political history. Oakeshott '
            'reviewed the collection he edited, Conservative Essays (1978),'
            ' in the Daily Telegraph.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Maurice_Cowling',
            yod='https://en.wikipedia.org/wiki/Maurice_Cowling',
            affiliation='https://en.wikipedia.org/wiki/Maurice_Cowling',
            descr='https://en.wikipedia.org/wiki/Maurice_Cowling',
            url='https://en.wikipedia.org/wiki/Maurice_Cowling',
        ),
    ),
    ('Croce', 'B.', ''): dict(
        url='https://en.wikipedia.org/wiki/Benedetto_Croce',
        yob=1866,
        yod=1952,
        descr=(
            'Italian idealist philosopher, historian and liberal senator '
            'who wrote widely on aesthetics, history and historiography and'
            ' was a major influence on Italian intellectual life. Oakeshott'
            ' reviewed the English translation of his Politics and Morals '
            'in Philosophy (1946).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Benedetto_Croce',
            yod='https://en.wikipedia.org/wiki/Benedetto_Croce',
            descr='https://en.wikipedia.org/wiki/Benedetto_Croce',
            url='https://en.wikipedia.org/wiki/Benedetto_Croce',
        ),
    ),
    ('Crossman', 'R.', 'H. S.'): dict(
        url='https://en.wikipedia.org/wiki/Richard_Crossman',
        yob=1907,
        yod=1974,
        affiliation='New Statesman',
        descr=(
            'British Labour politician and former Oxford classics tutor who'
            ' served as a Cabinet minister under Harold Wilson and later '
            'edited the New Statesman; known for his published Cabinet '
            "diaries. He reviewed Oakeshott's inaugural lecture Political "
            'Education in the New Statesman and Nation (1951).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Richard_Crossman',
            yod='https://en.wikipedia.org/wiki/Richard_Crossman',
            affiliation='https://en.wikipedia.org/wiki/Richard_Crossman',
            descr='https://en.wikipedia.org/wiki/Richard_Crossman',
            url='https://en.wikipedia.org/wiki/Richard_Crossman',
        ),
    ),
    ('Curtis', 'L.', ''): dict(
        url='https://en.wikipedia.org/wiki/Lionel_Curtis',
        yob=1872,
        yod=1955,
        descr=(
            'British internationalist author and leading figure of the '
            'Round Table movement, instrumental in founding Chatham House '
            'and associated with the evolution of the Empire into the '
            'Commonwealth. Oakeshott reviewed his Civitas Dei in the '
            'Cambridge Review (1934).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Lionel_Curtis',
            yod='https://en.wikipedia.org/wiki/Lionel_Curtis',
            descr='https://en.wikipedia.org/wiki/Lionel_Curtis',
            url='https://en.wikipedia.org/wiki/Lionel_Curtis',
        ),
    ),
    ('DeMott', 'B.', ''): dict(
        url='https://en.wikipedia.org/wiki/Benjamin_DeMott',
        yob=1924,
        yod=2005,
        affiliation='Amherst College',
        descr=(
            'American English professor and cultural critic, author of more'
            ' than a dozen books and a regular essayist in popular '
            "magazines such as Harper's. He reviewed Rationalism in "
            "Politics in Harper's Magazine (1963)."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Benjamin_DeMott',
            yod='https://en.wikipedia.org/wiki/Benjamin_DeMott',
            affiliation='https://en.wikipedia.org/wiki/Benjamin_DeMott',
            descr='https://en.wikipedia.org/wiki/Benjamin_DeMott',
            url='https://en.wikipedia.org/wiki/Benjamin_DeMott',
        ),
    ),
    ('Driesch', 'H.', ''): dict(
        url='https://en.wikipedia.org/wiki/Hans_Driesch',
        yob=1867,
        yod=1941,
        affiliation='University of Leipzig',
        descr=(
            'German biologist and philosopher known for early experimental '
            'embryology and a neo-vitalist philosophy of entelechy. '
            'Oakeshott reviewed his Ethical Principles in Theory and '
            'Practice in the Journal of Theological Studies (1931).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Hans_Driesch',
            yod='https://en.wikipedia.org/wiki/Hans_Driesch',
            affiliation='https://en.wikipedia.org/wiki/Hans_Driesch',
            descr='https://en.wikipedia.org/wiki/Hans_Driesch',
            url='https://en.wikipedia.org/wiki/Hans_Driesch',
        ),
    ),
    ('Dudley', 'E.', ''): dict(
        url='https://en.wikipedia.org/wiki/Edmund_Dudley',
        yod=1510,
        descr=(
            'English administrator and financial agent of Henry VII, '
            'Speaker of the House of Commons, who was executed for treason '
            'under Henry VIII; he wrote The Tree of Commonwealth while '
            "awaiting execution. Oakeshott reviewed D. M. Brodie's edition "
            'of that work in the Cambridge Journal (1949).'
        ),
        sources=dict(
            yod='https://en.wikipedia.org/wiki/Edmund_Dudley',
            descr='https://en.wikipedia.org/wiki/Edmund_Dudley',
            url='https://en.wikipedia.org/wiki/Edmund_Dudley',
        ),
    ),
    ('Durbin', 'E.', 'F. M.'): dict(
        url='https://en.wikipedia.org/wiki/Evan_Durbin',
        yob=1906,
        yod=1948,
        affiliation='London School of Economics',
        descr=(
            'British economist and Labour politician whose thinking joined '
            'support for economic planning with a belief in the price '
            'mechanism; often described as a leading Labour thinker of the '
            '1940s. Oakeshott reviewed his The Politics of Democratic '
            'Socialism in the Cambridge Review (1940).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Evan_Durbin',
            yod='https://en.wikipedia.org/wiki/Evan_Durbin',
            affiliation='https://en.wikipedia.org/wiki/Evan_Durbin',
            descr='https://en.wikipedia.org/wiki/Evan_Durbin',
            url='https://en.wikipedia.org/wiki/Evan_Durbin',
        ),
    ),
    ('Duverger', 'M.', ''): dict(
        url='https://en.wikipedia.org/wiki/Maurice_Duverger',
        yob=1917,
        yod=2014,
        affiliation='University of Paris (Sorbonne)',
        descr=(
            'French jurist, political scientist and politician who taught '
            'at Bordeaux and the Sorbonne and is known for his comparative '
            'study of party systems. Oakeshott reviewed the English '
            'translation of his Political Parties in the Spectator (1954).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Maurice_Duverger',
            yod='https://en.wikipedia.org/wiki/Maurice_Duverger',
            affiliation='https://en.wikipedia.org/wiki/Maurice_Duverger',
            descr='https://en.wikipedia.org/wiki/Maurice_Duverger',
            url='https://en.wikipedia.org/wiki/Maurice_Duverger',
        ),
    ),
    ('Duxbury', 'Neil', ''): dict(
        url='https://en.wikipedia.org/wiki/Neil_Duxbury',
        affiliation='London School of Economics',
        descr=(
            'British legal scholar and professor of English law at the '
            'London School of Economics, elected a Fellow of the British '
            'Academy in 2010. He reviewed The Defence of Natural Law, a '
            'study including Oakeshott, in the Cambridge Law Journal '
            '(1993).'
        ),
        sources=dict(
            affiliation='https://en.wikipedia.org/wiki/Neil_Duxbury',
            descr='https://en.wikipedia.org/wiki/Neil_Duxbury',
            url='https://en.wikipedia.org/wiki/Neil_Duxbury',
        ),
    ),
    ('Edel', 'A.', ''): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Abraham_Edel',
            yod='https://en.wikipedia.org/wiki/Abraham_Edel',
            affiliation='https://en.wikipedia.org/wiki/Abraham_Edel',
            descr='https://en.wikipedia.org/wiki/Abraham_Edel',
            url='https://en.wikipedia.org/wiki/Abraham_Edel',
        ),
    ),
    ('Emmet', 'D.', ''): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Dorothy_Emmet',
            yod='https://en.wikipedia.org/wiki/Dorothy_Emmet',
            affiliation='https://en.wikipedia.org/wiki/Dorothy_Emmet',
            descr='https://en.wikipedia.org/wiki/Dorothy_Emmet',
            url='https://en.wikipedia.org/wiki/Dorothy_Emmet',
        ),
    ),
    ('Fairlie', 'H.', ''): dict(
        url='https://en.wikipedia.org/wiki/Henry_Fairlie',
        yob=1924,
        yod=1990,
        affiliation='The Spectator',
        descr=(
            'British political journalist and social critic, credited with '
            'popularising the term "the Establishment", who wrote for The '
            'Spectator, The New Republic and other papers. He reviewed '
            'Rationalism in Politics in the Spectator (1962).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Henry_Fairlie',
            yod='https://en.wikipedia.org/wiki/Henry_Fairlie',
            affiliation='https://en.wikipedia.org/wiki/Henry_Fairlie',
            descr='https://en.wikipedia.org/wiki/Henry_Fairlie',
            url='https://en.wikipedia.org/wiki/Henry_Fairlie',
        ),
    ),
    ('Falck', 'C.', ''): dict(
        url='https://en.wikipedia.org/wiki/Colin_Falck',
        yob=1934,
        yod=2020,
        descr=(
            'British literary critic and poet who co-founded the poetry '
            'magazine The Review in 1962 and later taught modern literature'
            ' at York College of Pennsylvania. His "Romanticism in '
            'Politics" in New Left Review (1963) was a critical response to'
            ' Rationalism in Politics.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Colin_Falck',
            yod='https://en.wikipedia.org/wiki/Colin_Falck',
            descr='https://en.wikipedia.org/wiki/Colin_Falck',
            url='https://en.wikipedia.org/wiki/Colin_Falck',
        ),
    ),
    ('Farmer', 'H.', 'H.'): dict(
        url='https://en.wikipedia.org/wiki/Herbert_Henry_Farmer',
        yob=1892,
        yod=1981,
        affiliation='University of Cambridge',
        descr=(
            'British Presbyterian minister and philosopher of religion who '
            'taught at Westminster College, Cambridge, and was Norris-Hulse'
            ' Professor of Divinity at Cambridge. Oakeshott reviewed his '
            'Experience of God in the Journal of Theological Studies '
            '(1930).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Herbert_Henry_Farmer',
            yod='https://en.wikipedia.org/wiki/Herbert_Henry_Farmer',
            affiliation='https://en.wikipedia.org/wiki/Herbert_Henry_Farmer',
            descr='https://en.wikipedia.org/wiki/Herbert_Henry_Farmer',
            url='https://en.wikipedia.org/wiki/Herbert_Henry_Farmer',
        ),
    ),
    ('Feiling', 'K.', ''): dict(
        url='https://en.wikipedia.org/wiki/Keith_Feiling',
        yob=1884,
        yod=1977,
        affiliation='University of Oxford',
        descr=(
            'British historian and biographer, Chichele Professor of Modern'
            ' History at Oxford, known for a conservative reading of '
            'English history. Oakeshott reviewed his What Is Conservatism? '
            'in the Cambridge Review (1930).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Keith_Feiling',
            yod='https://en.wikipedia.org/wiki/Keith_Feiling',
            affiliation='https://en.wikipedia.org/wiki/Keith_Feiling',
            descr='https://en.wikipedia.org/wiki/Keith_Feiling',
            url='https://en.wikipedia.org/wiki/Keith_Feiling',
        ),
    ),
    ('Field', 'G.', 'C.'): dict(
        url='https://en.wikipedia.org/wiki/G._C._Field',
        yob=1887,
        yod=1955,
        affiliation='University of Bristol',
        descr=(
            'British philosopher, Professor of Philosophy at the University'
            ' of Bristol from 1926 to 1952 and its Pro-Vice-Chancellor. '
            'Oakeshott reviewed his Principles and Ideals in Politics in '
            'the Cambridge Journal (1949).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/G._C._Field',
            yod='https://en.wikipedia.org/wiki/G._C._Field',
            affiliation='https://en.wikipedia.org/wiki/G._C._Field',
            descr='https://en.wikipedia.org/wiki/G._C._Field',
            url='https://en.wikipedia.org/wiki/G._C._Field',
        ),
    ),
    ('Filmer', 'Robert', ''): dict(
        url='https://en.wikipedia.org/wiki/Robert_Filmer',
        yod=1653,
        descr=(
            'English political theorist and defender of the divine right of'
            ' kings, whose Patriarcha drew rebuttals from Locke, Sidney and'
            " Tyrrell. Oakeshott reviewed Peter Laslett's 1949 edition of "
            'Patriarcha and Other Political Works in the Cambridge Journal '
            'and Philosophy (1950).'
        ),
        sources=dict(
            yod='https://en.wikipedia.org/wiki/Robert_Filmer',
            descr='https://en.wikipedia.org/wiki/Robert_Filmer',
            url='https://en.wikipedia.org/wiki/Robert_Filmer',
        ),
    ),
    ('Flew', 'A.', ''): dict(
        url='https://en.wikipedia.org/wiki/Antony_Flew',
        yob=1923,
        yod=2010,
        affiliation='University of Reading',
        descr=(
            'English analytic philosopher, best known for his work in the '
            'philosophy of religion, who taught at Oxford, Aberdeen, Keele,'
            ' Reading and York University (Toronto). He reviewed The Voice '
            "of Liberal Learning (1990) and W. H. Greenleaf's Oakeshott's "
            'Philosophical Politics (1967).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Antony_Flew',
            yod='https://en.wikipedia.org/wiki/Antony_Flew',
            affiliation='https://en.wikipedia.org/wiki/Antony_Flew',
            descr='https://en.wikipedia.org/wiki/Antony_Flew',
            url='https://en.wikipedia.org/wiki/Antony_Flew',
        ),
    ),
    ('Forbes', 'D.', ''): dict(
        url='https://en.wikipedia.org/wiki/Duncan_Forbes_(historian)',
        yob=1922,
        yod=1994,
        affiliation='University of Cambridge',
        descr=(
            'Scottish historian and Reader in the History of Political '
            'Thought at Cambridge, known for his work on Hume and the '
            'Scottish Enlightenment. Oakeshott reviewed his The Liberal '
            'Anglican Idea of History in the Cambridge Journal (1953).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Duncan_Forbes_(historian)',
            yod='https://en.wikipedia.org/wiki/Duncan_Forbes_(historian)',
            affiliation='https://en.wikipedia.org/wiki/Duncan_Forbes_(historian)',
            descr='https://en.wikipedia.org/wiki/Duncan_Forbes_(historian)',
            url='https://en.wikipedia.org/wiki/Duncan_Forbes_(historian)',
        ),
    ),
    ('Forster', 'E.', 'M.'): dict(
        url='https://en.wikipedia.org/wiki/E._M._Forster',
        yob=1879,
        yod=1970,
        affiliation="King's College, Cambridge",
        descr=(
            'English novelist and essayist, author of A Room with a View, '
            'Howards End and A Passage to India. Oakeshott reviewed his '
            'essay collection Two Cheers for Democracy in the Cambridge '
            'Journal (1952).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/E._M._Forster',
            yod='https://en.wikipedia.org/wiki/E._M._Forster',
            affiliation='https://en.wikipedia.org/wiki/E._M._Forster',
            descr='https://en.wikipedia.org/wiki/E._M._Forster',
            url='https://en.wikipedia.org/wiki/E._M._Forster',
        ),
    ),
    ('Foster', 'M.', 'B.'): dict(
        url='https://en.wikipedia.org/wiki/Michael_Foster_(philosopher)',
        yob=1903,
        yod=1959,
        affiliation='Christ Church, Oxford',
        descr=(
            'Philosophy tutor at Christ Church, Oxford, who wrote on '
            'political philosophy and on Christian doctrine and the origins'
            ' of modern science. Oakeshott reviewed his The Political '
            'Philosophies of Plato and Hegel in the Cambridge Review '
            '(1935).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Michael_Foster_(philosopher)',
            yod='https://en.wikipedia.org/wiki/Michael_Foster_(philosopher)',
            affiliation='https://en.wikipedia.org/wiki/Michael_Foster_(philosopher)',
            descr='https://en.wikipedia.org/wiki/Michael_Foster_(philosopher)',
            url='https://en.wikipedia.org/wiki/Michael_Foster_(philosopher)',
        ),
    ),
    ('Gale', 'G.', ''): dict(
        url='https://en.wikipedia.org/wiki/George_Gale_(journalist)',
        yob=1927,
        yod=1990,
        affiliation='The Spectator',
        descr=(
            'British journalist who edited The Spectator from 1970 to 1973.'
            ' He reviewed On Human Conduct in the Spectator (1975).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/George_Gale_(journalist)',
            yod='https://en.wikipedia.org/wiki/George_Gale_(journalist)',
            affiliation='https://en.wikipedia.org/wiki/George_Gale_(journalist)',
            descr='https://en.wikipedia.org/wiki/George_Gale_(journalist)',
            url='https://en.wikipedia.org/wiki/George_Gale_(journalist)',
        ),
    ),
    ('Garnett', 'M.', ''): dict(
        url='https://en.wikipedia.org/wiki/Mark_Garnett',
        descr=(
            'British author and commentator on British politics who has '
            'taught at several UK universities, co-author of a biography of'
            ' William Whitelaw and collaborator of Ian Gilmour. He reviewed'
            ' Oakeshott on History in the Conservative History Journal '
            '(2004).'
        ),
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Mark_Garnett',
            url='https://en.wikipedia.org/wiki/Mark_Garnett',
        ),
    ),
    ('Gierke', 'O.', ''): dict(
        url='https://en.wikipedia.org/wiki/Otto_von_Gierke',
        yob=1841,
        yod=1921,
        affiliation='University of Berlin',
        descr=(
            'German legal scholar and historian, known for his multi-volume'
            ' study of the German law of associations. Oakeshott reviewed '
            "Ernest Barker's translation of part of that work, Natural Law "
            'and the Theory of Society, 1500 to 1800, in the Cambridge '
            'Review (1934).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Otto_von_Gierke',
            yod='https://en.wikipedia.org/wiki/Otto_von_Gierke',
            affiliation='https://en.wikipedia.org/wiki/Otto_von_Gierke',
            descr='https://en.wikipedia.org/wiki/Otto_von_Gierke',
            url='https://en.wikipedia.org/wiki/Otto_von_Gierke',
        ),
    ),
    ('Gilmour', 'I.', ''): dict(
        url=(
            'https://en.wikipedia.org/wiki/Ian_Gilmour,_Baron_Gilmour_of_Cr'
            'aigmillar'
        ),
        yob=1926,
        yod=2007,
        descr=(
            'British Conservative politician, Defence Secretary under '
            'Edward Heath and Lord Privy Seal under Margaret Thatcher, and '
            'a writer on conservatism. He reviewed The Voice of Liberal '
            'Learning in the London Review of Books (1990).'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Ian_Gilmour,_Baron_Gilmour_o'
                'f_Craigmillar'
            ),
            yod=(
                'https://en.wikipedia.org/wiki/Ian_Gilmour,_Baron_Gilmour_o'
                'f_Craigmillar'
            ),
            descr=(
                'https://en.wikipedia.org/wiki/Ian_Gilmour,_Baron_Gilmour_o'
                'f_Craigmillar'
            ),
            url=(
                'https://en.wikipedia.org/wiki/Ian_Gilmour,_Baron_Gilmour_o'
                'f_Craigmillar'
            ),
        ),
    ),
    ('Ginsberg', 'M.', ''): dict(
        url='https://en.wikipedia.org/wiki/Morris_Ginsberg',
        yob=1889,
        yod=1970,
        affiliation='London School of Economics',
        descr=(
            'British sociologist who helped establish the discipline in '
            'Britain and was founding chairman of the British Sociological '
            'Association. Oakeshott reviewed his Reason and Unreason in '
            'Society in the English Historical Review (1948).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Morris_Ginsberg',
            yod='https://en.wikipedia.org/wiki/Morris_Ginsberg',
            affiliation='https://en.wikipedia.org/wiki/Morris_Ginsberg',
            descr='https://en.wikipedia.org/wiki/Morris_Ginsberg',
            url='https://en.wikipedia.org/wiki/Morris_Ginsberg',
        ),
    ),
    ('Godley', 'J.', ''): dict(
        url='https://en.wikipedia.org/wiki/John_Godley,_3rd_Baron_Kilbracken',
        yob=1920,
        yod=2006,
        descr=(
            'British-born, later Irish-resident peer (Lord Kilbracken), '
            'wartime naval pilot, journalist and author. Oakeshott reviewed'
            ' his book Tell Me the Next One in the Spectator (1950).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Godley,_3rd_Baron_Kilbracken',
            yod='https://en.wikipedia.org/wiki/John_Godley,_3rd_Baron_Kilbracken',
            descr='https://en.wikipedia.org/wiki/John_Godley,_3rd_Baron_Kilbracken',
            url='https://en.wikipedia.org/wiki/John_Godley,_3rd_Baron_Kilbracken',
        ),
    ),
    ('Gore', 'C.', ''): dict(
        url='https://en.wikipedia.org/wiki/Charles_Gore',
        yob=1853,
        yod=1932,
        descr=(
            'Influential Anglican theologian and successively Bishop of '
            'Worcester, Birmingham and Oxford, founder of the Community of '
            'the Resurrection. Oakeshott reviewed his Can We Then Believe? '
            'in the Journal of Theological Studies (1927).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Charles_Gore',
            yod='https://en.wikipedia.org/wiki/Charles_Gore',
            descr='https://en.wikipedia.org/wiki/Charles_Gore',
            url='https://en.wikipedia.org/wiki/Charles_Gore',
        ),
    ),
    ('Gottfried', 'P.', ''): dict(
        url='https://en.wikipedia.org/wiki/Paul_Gottfried',
        yob=1941,
        affiliation='Elizabethtown College',
        descr=(
            'American paleoconservative political philosopher and '
            'intellectual historian, long a professor of humanities at '
            'Elizabethtown College. He reviewed the expanded edition of '
            'Rationalism in Politics in Modern Age (1992).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Paul_Gottfried',
            affiliation='https://en.wikipedia.org/wiki/Paul_Gottfried',
            descr='https://en.wikipedia.org/wiki/Paul_Gottfried',
            url='https://en.wikipedia.org/wiki/Paul_Gottfried',
        ),
    ),
    ('Gough', 'J.', 'W.'): dict(
        url='https://en.wikipedia.org/wiki/J._W._Gough',
        yob=1900,
        yod=1976,
        affiliation='University of Oxford',
        descr=(
            "Welsh historian known for his studies of John Locke's "
            "political philosophy. Oakeshott reviewed his John Locke's "
            'Political Philosophy in the English Historical Review (1950).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/J._W._Gough',
            yod='https://en.wikipedia.org/wiki/J._W._Gough',
            affiliation='https://en.wikipedia.org/wiki/J._W._Gough',
            descr='https://en.wikipedia.org/wiki/J._W._Gough',
            url='https://en.wikipedia.org/wiki/J._W._Gough',
        ),
    ),
    ('Hamburger', 'J.', ''): dict(
        url='https://en.wikipedia.org/wiki/Joseph_Hamburger',
        yob=1922,
        yod=1997,
        affiliation='Yale University',
        descr=(
            'American historian of nineteenth-century British thought who '
            'taught at Yale for 35 years, writing on James Mill, J. S. Mill'
            " and Macaulay. He reviewed W. H. Greenleaf's Oakeshott's "
            'Philosophical Politics in the American Political Science '
            'Review (1967).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Joseph_Hamburger',
            yod='https://en.wikipedia.org/wiki/Joseph_Hamburger',
            affiliation='https://en.wikipedia.org/wiki/Joseph_Hamburger',
            descr='https://en.wikipedia.org/wiki/Joseph_Hamburger',
            url='https://en.wikipedia.org/wiki/Joseph_Hamburger',
        ),
    ),
    ('Hammond', 'J.', 'L.'): dict(
        url='https://en.wikipedia.org/wiki/John_Lawrence_Hammond',
        yob=1872,
        yod=1949,
        affiliation='Manchester Guardian',
        descr=(
            'British journalist and social historian, often writing jointly'
            ' with his wife Barbara Hammond, who worked on the staff of the'
            ' Manchester Guardian. He reviewed The Social and Political '
            'Doctrines of Contemporary Europe in the Manchester Guardian '
            '(1939).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Lawrence_Hammond',
            yod='https://en.wikipedia.org/wiki/John_Lawrence_Hammond',
            affiliation='https://en.wikipedia.org/wiki/John_Lawrence_Hammond',
            descr='https://en.wikipedia.org/wiki/John_Lawrence_Hammond',
            url='https://en.wikipedia.org/wiki/John_Lawrence_Hammond',
        ),
    ),
    ('Hayter', 'W.', ''): dict(
        url='https://en.wikipedia.org/wiki/William_Hayter_(diplomat)',
        yob=1906,
        yod=1995,
        affiliation='New College, Oxford',
        descr=(
            'British diplomat, Ambassador to the Soviet Union 1953-57 and '
            'later Warden of New College, Oxford. Oakeshott reviewed his '
            'William of Wykeham: Patron of the Arts in the Times Literary '
            'Supplement (1970).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/William_Hayter_(diplomat)',
            yod='https://en.wikipedia.org/wiki/William_Hayter_(diplomat)',
            affiliation='https://en.wikipedia.org/wiki/William_Hayter_(diplomat)',
            descr='https://en.wikipedia.org/wiki/William_Hayter_(diplomat)',
            url='https://en.wikipedia.org/wiki/William_Hayter_(diplomat)',
        ),
    ),
    ('Hearnshaw', 'F.', 'J. C.'): dict(
        url='https://en.wikipedia.org/wiki/F._J._C._Hearnshaw',
        yob=1869,
        yod=1946,
        affiliation="King's College London",
        descr=(
            'English historian specialising in medieval history and noted '
            'for a conservative interpretation of the past. Oakeshott '
            'reviewed the collection he edited, The Social and Political '
            'Ideas of Some Representative Thinkers of the Age of Reaction '
            'and Reconstruction, in the Cambridge Review (1932).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/F._J._C._Hearnshaw',
            yod='https://en.wikipedia.org/wiki/F._J._C._Hearnshaw',
            affiliation='https://en.wikipedia.org/wiki/F._J._C._Hearnshaw',
            descr='https://en.wikipedia.org/wiki/F._J._C._Hearnshaw',
            url='https://en.wikipedia.org/wiki/F._J._C._Hearnshaw',
        ),
    ),
    ('Heckscher', 'G.', ''): dict(
        url='https://en.wikipedia.org/wiki/Gunnar_Heckscher',
        yob=1909,
        yod=1987,
        descr=(
            'Swedish political scientist and Conservative politician who '
            'taught at Uppsala and Stockholm and led the Swedish '
            'Conservative Party in the 1960s. Oakeshott reviewed his The '
            'Study of Comparative Government and Politics in the Spectator '
            '(1957).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Gunnar_Heckscher',
            yod='https://en.wikipedia.org/wiki/Gunnar_Heckscher',
            descr='https://en.wikipedia.org/wiki/Gunnar_Heckscher',
            url='https://en.wikipedia.org/wiki/Gunnar_Heckscher',
        ),
    ),
    ('Heim', 'K.', ''): dict(
        url='https://en.wikipedia.org/wiki/Karl_Heim',
        yob=1874,
        yod=1958,
        affiliation='University of Tübingen',
        descr=(
            'German Protestant theologian, professor of dogmatics at '
            'Münster and Tübingen, known for work on religion and science. '
            'Oakeshott reviewed his The New Divine Order in the Journal of '
            'Theological Studies (1931).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Karl_Heim',
            yod='https://en.wikipedia.org/wiki/Karl_Heim',
            affiliation='https://en.wikipedia.org/wiki/Karl_Heim',
            descr='https://en.wikipedia.org/wiki/Karl_Heim',
            url='https://en.wikipedia.org/wiki/Karl_Heim',
        ),
    ),
    ('Hennis', 'W.', ''): dict(
        url='https://en.wikipedia.org/wiki/Wilhelm_Hennis',
        yob=1923,
        yod=2012,
        affiliation='University of Freiburg',
        descr=(
            'German political scientist who taught at Hannover and Hamburg '
            'before holding a chair at Freiburg. He reviewed On Human '
            'Conduct in the Frankfurter Allgemeine Zeitung (1976).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Wilhelm_Hennis',
            yod='https://en.wikipedia.org/wiki/Wilhelm_Hennis',
            affiliation='https://en.wikipedia.org/wiki/Wilhelm_Hennis',
            descr='https://en.wikipedia.org/wiki/Wilhelm_Hennis',
            url='https://en.wikipedia.org/wiki/Wilhelm_Hennis',
        ),
    ),
    ('Hinsley', 'F.', 'H.'): dict(
        url='https://en.wikipedia.org/wiki/Harry_Hinsley',
        yob=1918,
        yod=1998,
        affiliation='University of Cambridge',
        descr=(
            'English historian and Bletchley Park intelligence officer who '
            'wrote on international relations and the official history of '
            'British wartime intelligence. Oakeshott reviewed his '
            'Sovereignty in the English Historical Review (1968).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Harry_Hinsley',
            yod='https://en.wikipedia.org/wiki/Harry_Hinsley',
            affiliation='https://en.wikipedia.org/wiki/Harry_Hinsley',
            descr='https://en.wikipedia.org/wiki/Harry_Hinsley',
            url='https://en.wikipedia.org/wiki/Harry_Hinsley',
        ),
    ),
    ('Holmes', 'E.', ''): dict(
        url='https://en.wikipedia.org/wiki/Edmond_Holmes',
        yob=1850,
        yod=1936,
        descr=(
            'Anglo-Irish educationalist, writer and poet who argued that '
            'Western thought had become spiritually bankrupt. Oakeshott '
            'reviewed his Philosophy Without Metaphysics in the Journal of '
            'Theological Studies (1931).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Edmond_Holmes',
            yod='https://en.wikipedia.org/wiki/Edmond_Holmes',
            descr='https://en.wikipedia.org/wiki/Edmond_Holmes',
            url='https://en.wikipedia.org/wiki/Edmond_Holmes',
        ),
    ),
    ('Holt', 'J.', 'C.'): dict(
        url='https://en.wikipedia.org/wiki/James_Holt_(historian)',
        yob=1922,
        yod=2014,
        affiliation='University of Cambridge',
        descr=(
            'English medieval historian best known for his work on Magna '
            'Carta, later Master of Fitzwilliam College, Cambridge. '
            'Oakeshott reviewed his Magna Carta in Government and '
            'Opposition (1966).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/James_Holt_(historian)',
            yod='https://en.wikipedia.org/wiki/James_Holt_(historian)',
            affiliation='https://en.wikipedia.org/wiki/James_Holt_(historian)',
            descr='https://en.wikipedia.org/wiki/James_Holt_(historian)',
            url='https://en.wikipedia.org/wiki/James_Holt_(historian)',
        ),
    ),
    ('Dru', 'A.', ''): dict(
        descr=(
            'English Catholic writer and translator who edited and '
            "translated Kierkegaard's journals and translated works by "
            'Péguy, Josef Pieper, Blondel and Hans Urs von Balthasar. '
            'Oakeshott reviewed his edition of The Letters of Jacob '
            'Burckhardt in Encounter (1954).'
        ),
        sources=dict(
            descr='https://about.libertyfund.org/?p=11804',
        ),
    ),
    ('Dunstan', 'G.', 'R.'): dict(
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
        sources=dict(
            yob=(
                'https://archiveshub.ac.uk/search/archives/5b207522-775e-34'
                '3b-abdd-cc1fdb972cd0'
            ),
            yod=(
                'https://archiveshub.ac.uk/search/archives/5b207522-775e-34'
                '3b-abdd-cc1fdb972cd0'
            ),
            affiliation=(
                'https://history.rcplondon.ac.uk/inspiring-physicians/gordo'
                'n-reginald-dunstan'
            ),
            descr=(
                'https://history.rcplondon.ac.uk/inspiring-physicians/gordo'
                'n-reginald-dunstan'
            ),
            url=(
                'https://history.rcplondon.ac.uk/inspiring-physicians/gordo'
                'n-reginald-dunstan'
            ),
        ),
    ),
    ('Gilby', 'T.', ''): dict(
        yob=1902,
        yod=1975,
        url=(
            'https://encyclopedia.com/religion/encyclopedias-almanacs-trans'
            'cripts-and-maps/gilby-thomas'
        ),
        descr=(
            'English Dominican friar and Thomist scholar who directed the '
            "Blackfriars edition of Aquinas's Summa Theologiae. Oakeshott "
            'reviewed his Barbara Celarent, a study of scholastic '
            'dialectic, in the Times Literary Supplement (1949).'
        ),
        sources=dict(
            yob=(
                'https://encyclopedia.com/religion/encyclopedias-almanacs-t'
                'ranscripts-and-maps/gilby-thomas'
            ),
            yod=(
                'https://encyclopedia.com/religion/encyclopedias-almanacs-t'
                'ranscripts-and-maps/gilby-thomas'
            ),
            descr=(
                'https://encyclopedia.com/religion/encyclopedias-almanacs-t'
                'ranscripts-and-maps/gilby-thomas'
            ),
            url=(
                'https://encyclopedia.com/religion/encyclopedias-almanacs-t'
                'ranscripts-and-maps/gilby-thomas'
            ),
        ),
    ),
    ('Franklin', 'J.', 'H.'): dict(
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
        sources=dict(
            yob='https://prabook.com/web/julian_harold.franklin/1697632',
            affiliation='https://www.routledge.com/products/9780754625452',
            descr='https://www.routledge.com/products/9780754625452',
            url='https://prabook.com/web/julian_harold.franklin/1697632',
        ),
    ),
    ('Franks', 'R.', ''): dict(
        affiliation='Western College, Bristol',
        yob=1871,
        yod=1964,
        url='https://commons.ptsem.edu/id/historyofdoctrin01fran',
        descr=(
            'Robert Sleightholme Franks, English Congregational theologian '
            'and Principal of Western College, Bristol, author of A History'
            ' of the Doctrine of the Work of Christ. He reviewed Experience'
            ' and Its Modes in the Congregational Quarterly (1935).'
        ),
        sources=dict(
            yob='https://library.aiu.ac.ke/bib/51670',
            yod='https://library.aiu.ac.ke/bib/51670',
            affiliation='https://commons.ptsem.edu/id/historyofdoctrin01fran',
            descr='https://commons.ptsem.edu/id/historyofdoctrin01fran',
            url='https://commons.ptsem.edu/id/historyofdoctrin01fran',
        ),
    ),
    ('Grant', 'M.', ''): dict(
        descr=(
            'Malcolm Grant, author of A New Argument for God and Survival '
            'and a Solution to the Problem of Supernatural Events (Faber '
            'and Faber, 1934); no further biographical details were found. '
            'Oakeshott reviewed the book in the Cambridge Review (1934).'
        ),
        sources=dict(
            descr='https://catalogue.nli.ie/Record/vtls000402743',
        ),
    ),
    ('Griffith-Jones', 'E.', ''): dict(
        affiliation='Yorkshire United Independent College',
        yob=1860,
        yod=1942,
        url='https://biography.wales/article/s2-GRIF-EBE-1860',
        descr=(
            'Ebenezer Griffith-Jones, Welsh Congregational minister who '
            'held London-area pastorates and was principal of the Yorkshire'
            ' United Independent College, Bradford, 1907-32. Oakeshott '
            'reviewed his book on Providence in the Journal of Theological '
            'Studies (1926).'
        ),
        sources=dict(
            yob='https://biography.wales/article/s2-GRIF-EBE-1860',
            yod='https://biography.wales/article/s2-GRIF-EBE-1860',
            affiliation='https://biography.wales/article/s2-GRIF-EBE-1860',
            descr='https://biography.wales/article/s2-GRIF-EBE-1860',
            url='https://biography.wales/article/s2-GRIF-EBE-1860',
        ),
    ),
    ('Detmer', 'D.', ''): dict(
        affiliation='Purdue University Northwest',
        yob=1958,
        url='https://pnw.edu/people/david-detmer-ph-d',
        descr=(
            'David Detmer, American philosopher and professor (now '
            'emeritus) at Purdue University Northwest (formerly Purdue '
            'Calumet), a Sartre scholar and author of Sartre Explained and '
            "Freedom as a Value. He reviewed Sartre's Radicalism and "
            "Oakeshott's Conservatism in Sartre Studies International "
            '(2000).'
        ),
        sources=dict(
            yob=(
                'https://www.encyclopedia.com/arts/educational-magazines/de'
                'tmer-david-1958'
            ),
            affiliation='https://pnw.edu/people/david-detmer-ph-d',
            descr=(
                'https://www.encyclopedia.com/arts/educational-magazines/de'
                'tmer-david-1958'
            ),
            url='https://pnw.edu/people/david-detmer-ph-d',
        ),
    ),
    ('Eisenach', 'E.', 'J.'): dict(
        affiliation='University of Tulsa',
        url='https://claremontreviewofbooks.com/author/eldon-j-eisenach',
        descr=(
            'Eldon J. Eisenach, American political theorist and professor '
            'of political science at the University of Tulsa, author of '
            'books on American Progressivism and political theology. He '
            'reviewed The Political Philosophy of Michael Oakeshott in '
            'Choice (1991).'
        ),
        sources=dict(
            affiliation='https://claremontreviewofbooks.com/author/eldon-j-eisenach',
            descr='https://claremontreviewofbooks.com/author/eldon-j-eisenach',
            url='https://claremontreviewofbooks.com/author/eldon-j-eisenach',
        ),
    ),
    ('Esler', 'A.', ''): dict(
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
        sources=dict(
            yob=(
                'https://www.encyclopedia.com/arts/culture-magazines/esler-'
                'anthony-james'
            ),
            affiliation=(
                'https://www.encyclopedia.com/arts/culture-magazines/esler-'
                'anthony-james'
            ),
            descr=(
                'https://www.encyclopedia.com/arts/culture-magazines/esler-'
                'anthony-james'
            ),
            url=(
                'https://www.encyclopedia.com/arts/culture-magazines/esler-'
                'anthony-james'
            ),
        ),
    ),
    ('Fahey', 'D.', 'M.'): dict(
        affiliation='Miami University',
        yob=1937,
        url='https://en.wikipedia.org/wiki/David_M._Fahey',
        descr=(
            'David M. Fahey, American historian of modern Britain and of '
            'temperance movements, professor (now emeritus) at Miami '
            'University in Oxford, Ohio. He reviewed On History and Other '
            'Essays in Clio (1984).'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/David_M._Fahey',
            affiliation=(
                'https://miamioh.edu/cas/academics/departments/history/emer'
                'iti-faculty/fahey/index.html'
            ),
            descr='https://en.wikipedia.org/wiki/David_M._Fahey',
            url='https://en.wikipedia.org/wiki/David_M._Fahey',
        ),
    ),
    ('Eccleshall', 'R.', ''): dict(
        affiliation="Queen's University Belfast",
        descr=(
            'Robert Eccleshall, British political theorist in the '
            "Department of Politics at Queen's University Belfast, author "
            'of English Conservatism since the Restoration and writings on '
            'conservative ideology. He reviewed On History and Other Essays'
            ' in Political Studies (1984).'
        ),
        sources=dict(
            affiliation='https://www.librarything.com/author/eccleshallrobert',
            descr='https://www.taylorfrancis.com/books/9780203205181',
        ),
    ),
    ('Hartle', 'A.', ''): dict(
        affiliation='Emory University',
        url='https://philosophy.emory.edu/people/bios/hartle-ann.html',
        descr=(
            'Ann Hartle, American philosopher and professor emerita at '
            'Emory University, known for her books on Montaigne. She '
            'reviewed The Politics of Faith and the Politics of Scepticism '
            'in the Review of Metaphysics (1997).'
        ),
        sources=dict(
            affiliation='https://philosophy.emory.edu/people/bios/hartle-ann.html',
            descr='https://philosophy.emory.edu/people/bios/hartle-ann.html',
            url='https://philosophy.emory.edu/people/bios/hartle-ann.html',
        ),
    ),
    ('Heath', 'E.', ''): dict(
        affiliation='State University of New York at New Paltz',
        url='https://press.uchicago.edu/ucp/books/author/H/E/au25581489.html',
        descr=(
            'Eugene Heath, American philosopher at SUNY New Paltz who '
            'writes on Adam Ferguson and the ethics of markets, author or '
            'editor of Morality and the Market. He reviewed The Politics of'
            ' Faith and the Politics of Scepticism in the Independent '
            'Review (1998).'
        ),
        sources=dict(
            affiliation='https://press.uchicago.edu/ucp/books/author/H/E/au25581489.html',
            descr='https://press.uchicago.edu/ucp/books/author/H/E/au25581489.html',
            url='https://press.uchicago.edu/ucp/books/author/H/E/au25581489.html',
        ),
    ),
    ('Henkel', 'Michael', ''): dict(
        url=(
            'https://www.mohrsiebeck.com/en/book/praxis-und-politik-michael'
            '-oakeshott-im-dialog-9783161525223'
        ),
        descr=(
            'German political scientist (Dr. habil., listed at Erfurt in '
            '2019) who has written on Hermann Heller and on theories of '
            'peace and politics. He co-edited with Oliver W. Lembcke the '
            'volume Praxis und Politik: Michael Oakeshott im Dialog (2013) '
            'and has written on Oakeshott in the Politisches Denken '
            'yearbook.'
        ),
        sources=dict(
            descr=(
                'https://www.mohrsiebeck.com/en/book/praxis-und-politik-mic'
                'hael-oakeshott-im-dialog-9783161525223'
            ),
            url=(
                'https://www.mohrsiebeck.com/en/book/praxis-und-politik-mic'
                'hael-oakeshott-im-dialog-9783161525223'
            ),
        ),
    ),
    ('Dearden', 'R.', 'F.'): dict(
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
        sources=dict(
            yob='https://libmast.utm.my/Record/KOHA-OAI-TEST:472069/Description',
            yod='https://libmast.utm.my/Record/KOHA-OAI-TEST:472069/Description',
            descr='https://libmast.utm.my/Record/KOHA-OAI-TEST:472069/Description',
        ),
    ),
    ('Graham', 'G.', ''): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/L._Gordon_Graham',
            affiliation='https://en.wikipedia.org/wiki/L._Gordon_Graham',
            descr='https://www.gordon-graham.net/philosophy.html',
            url='https://en.wikipedia.org/wiki/L._Gordon_Graham',
        ),
    ),
    ('Crowther', 'I.', ''): dict(
        affiliation='The Salisbury Review',
        descr=(
            'Ian Crowther, British conservative critic and literary editor '
            'of The Salisbury Review, who also wrote for PN Review and '
            'Chronicles. He reviewed the reissue of Experience and Its '
            'Modes in the Salisbury Review (1987).'
        ),
        sources=dict(
            affiliation='https://issuu.com/salisburyreview/docs/autumn_2010',
            descr='https://pnreview.co.uk/contributors/ian-crowther/2873',
        ),
    ),
    ('Locke', 'John', ''): dict(
        descr=(
            'English philosopher and physician of the seventeenth century, '
            'often called the father of liberalism, whose works include the'
            ' Two Treatises of Government and An Essay Concerning Human '
            "Understanding. Oakeshott reviewed Peter Laslett's 1962 "
            'critical edition of the Two Treatises in the Historical '
            'Journal.'
        ),
        url='https://en.wikipedia.org/wiki/John_Locke',
        yob=1632,
        yod=1704,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/John_Locke',
            url='https://en.wikipedia.org/wiki/John_Locke',
            yob='https://en.wikipedia.org/wiki/John_Locke',
            yod='https://en.wikipedia.org/wiki/John_Locke',
        ),
    ),
    ('Machiavelli', 'N.', ''): dict(
        descr=(
            'Florentine diplomat, historian and political writer of the '
            'Italian Renaissance, author of The Prince and the Discourses '
            'on Livy, frequently described as a founder of modern political'
            " thought. Oakeshott reviewed L. J. Walker's 1950 edition of "
            'the Discourses in the Cambridge Journal.'
        ),
        url='https://en.wikipedia.org/wiki/Niccol%C3%B2_Machiavelli',
        yob=1469,
        yod=1527,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Niccol%C3%B2_Machiavelli',
            url='https://en.wikipedia.org/wiki/Niccol%C3%B2_Machiavelli',
            yob='https://en.wikipedia.org/wiki/Niccol%C3%B2_Machiavelli',
            yod='https://en.wikipedia.org/wiki/Niccol%C3%B2_Machiavelli',
        ),
    ),
    ('Marx', 'K.', ''): dict(
        descr=(
            'German philosopher, economist and revolutionary socialist who '
            'developed historical materialism and, with Friedrich Engels, '
            'wrote The Communist Manifesto; his major work is Das Kapital. '
            'Oakeshott reviewed the 1970 English edition of his Critique of'
            " Hegel's Philosophy of Right (ed. J. O'Malley) in the "
            'Spectator.'
        ),
        url='https://en.wikipedia.org/wiki/Karl_Marx',
        yob=1818,
        yod=1883,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Karl_Marx',
            url='https://en.wikipedia.org/wiki/Karl_Marx',
            yob='https://en.wikipedia.org/wiki/Karl_Marx',
            yod='https://en.wikipedia.org/wiki/Karl_Marx',
        ),
    ),
    ('Marcuse', 'H.', ''): dict(
        descr=(
            'German-American philosopher and social critic associated with '
            'the Frankfurt School, later a leading theorist of the New Left'
            ' and author of One-Dimensional Man. He taught at Brandeis and '
            'the University of California, San Diego. Oakeshott reviewed '
            'his Reason and Revolution in the Spectator in 1955.'
        ),
        url='https://en.wikipedia.org/wiki/Herbert_Marcuse',
        yob=1898,
        yod=1979,
        affiliation='University of California, San Diego',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Herbert_Marcuse',
            url='https://en.wikipedia.org/wiki/Herbert_Marcuse',
            yob='https://en.wikipedia.org/wiki/Herbert_Marcuse',
            yod='https://en.wikipedia.org/wiki/Herbert_Marcuse',
            affiliation='https://en.wikipedia.org/wiki/Herbert_Marcuse',
        ),
    ),
    ('Mannheim', 'K.', ''): dict(
        descr=(
            'Hungarian-born sociologist and a founder of the sociology of '
            'knowledge, best known for Ideology and Utopia. After leaving '
            'Germany in 1933 he lectured at the London School of Economics '
            'and became the first professor of sociology at the Institute '
            'of Education, London. Oakeshott reviewed Ideology and Utopia '
            'in the Cambridge Review.'
        ),
        url='https://en.wikipedia.org/wiki/Karl_Mannheim',
        yob=1893,
        yod=1947,
        affiliation='Institute of Education, University of London',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Karl_Mannheim',
            url='https://en.wikipedia.org/wiki/Karl_Mannheim',
            yob='https://en.wikipedia.org/wiki/Karl_Mannheim',
            yod='https://en.wikipedia.org/wiki/Karl_Mannheim',
            affiliation='https://en.wikipedia.org/wiki/Karl_Mannheim',
        ),
    ),
    ('Koestler', 'A.', ''): dict(
        descr=(
            'Budapest-born author and journalist who left the Communist '
            'Party in 1938 and won international fame with the '
            'anti-totalitarian novel Darkness at Noon; he later wrote '
            'widely on science and creativity. Oakeshott reviewed his '
            'Insight and Outlook in the Spectator in 1949.'
        ),
        url='https://en.wikipedia.org/wiki/Arthur_Koestler',
        yob=1905,
        yod=1983,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Arthur_Koestler',
            url='https://en.wikipedia.org/wiki/Arthur_Koestler',
            yob='https://en.wikipedia.org/wiki/Arthur_Koestler',
            yod='https://en.wikipedia.org/wiki/Arthur_Koestler',
        ),
    ),
    ('Joad', 'C.', 'E. M.'): dict(
        descr=(
            'English philosopher and broadcaster who headed the Department '
            'of Philosophy and Psychology at Birkbeck College and became a '
            'public figure through the BBC programme The Brains Trust. '
            'Oakeshott reviewed his book Decadence in the Spectator in '
            '1948.'
        ),
        url='https://en.wikipedia.org/wiki/C._E._M._Joad',
        yob=1891,
        yod=1953,
        affiliation='Birkbeck College, University of London',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/C._E._M._Joad',
            url='https://en.wikipedia.org/wiki/C._E._M._Joad',
            yob='https://en.wikipedia.org/wiki/C._E._M._Joad',
            yod='https://en.wikipedia.org/wiki/C._E._M._Joad',
            affiliation='https://en.wikipedia.org/wiki/C._E._M._Joad',
        ),
    ),
    ('Kirk', 'R.', ''): dict(
        descr=(
            'American political theorist, historian and man of letters '
            'whose The Conservative Mind (1953) shaped postwar '
            'traditionalist conservatism in the United States. Oakeshott '
            'reviewed The Conservative Mind in the Spectator in 1954, and '
            'Kirk reviewed Rationalism in Politics in the Annals of the '
            'American Academy in 1963.'
        ),
        url='https://en.wikipedia.org/wiki/Russell_Kirk',
        yob=1918,
        yod=1994,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Russell_Kirk',
            url='https://en.wikipedia.org/wiki/Russell_Kirk',
            yob='https://en.wikipedia.org/wiki/Russell_Kirk',
            yod='https://en.wikipedia.org/wiki/Russell_Kirk',
        ),
    ),
    ('Laslett', 'P.', ''): dict(
        descr=(
            'English historian at Cambridge whose editions of Filmer and of'
            ' Locke\'s Two Treatises helped launch the "Cambridge School" of'
            ' the history of political thought; he later co-founded the '
            'Cambridge Group for the History of Population and Social '
            'Structure. Oakeshott reviewed several of his editions, and '
            'Laslett reviewed Political Education and Rationalism in '
            'Politics.'
        ),
        url='https://en.wikipedia.org/wiki/Peter_Laslett',
        yob=1915,
        yod=2001,
        affiliation='University of Cambridge',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Peter_Laslett',
            url='https://en.wikipedia.org/wiki/Peter_Laslett',
            yob='https://en.wikipedia.org/wiki/Peter_Laslett',
            yod='https://en.wikipedia.org/wiki/Peter_Laslett',
            affiliation='https://en.wikipedia.org/wiki/Peter_Laslett',
        ),
    ),
    ('Lasswell', 'H.', 'D.'): dict(
        descr=(
            'American political scientist and communications theorist, a '
            'pioneer of the behavioural study of politics, who taught law '
            'and political science at Yale. He reviewed The Social and '
            'Political Doctrines of Contemporary Europe in 1943, and '
            'Oakeshott reviewed his The Analysis of Political Behavior in '
            'the Cambridge Journal.'
        ),
        url='https://en.wikipedia.org/wiki/Harold_Lasswell',
        yob=1902,
        yod=1978,
        affiliation='Yale University',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Harold_Lasswell',
            url='https://en.wikipedia.org/wiki/Harold_Lasswell',
            yob='https://en.wikipedia.org/wiki/Harold_Lasswell',
            yod='https://en.wikipedia.org/wiki/Harold_Lasswell',
            affiliation='https://en.wikipedia.org/wiki/Harold_Lasswell',
        ),
    ),
    ('Macpherson', 'C.', 'B.'): dict(
        descr=(
            'Canadian political theorist at the University of Toronto, '
            'known for his critique of liberal "possessive individualism" '
            'in studies of Hobbes and Locke. He reviewed Politics and '
            'Experience, the 1968 festschrift for Oakeshott, in Political '
            'Science Quarterly.'
        ),
        url='https://en.wikipedia.org/wiki/C._B._Macpherson',
        yob=1911,
        yod=1987,
        affiliation='University of Toronto',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/C._B._Macpherson',
            url='https://en.wikipedia.org/wiki/C._B._Macpherson',
            yob='https://en.wikipedia.org/wiki/C._B._Macpherson',
            yod='https://en.wikipedia.org/wiki/C._B._Macpherson',
            affiliation='https://en.wikipedia.org/wiki/C._B._Macpherson',
        ),
    ),
    ('Kukathas', 'C.', ''): dict(
        descr=(
            'Malaysian-born Australian political theorist, author of The '
            'Liberal Archipelago, who held a chair in political theory at '
            'the LSE before moving to Singapore Management University. He '
            'reviewed the expanded Rationalism in Politics and books on '
            'Oakeshott by Paul Franco and Terry Nardin.'
        ),
        url='https://en.wikipedia.org/wiki/Chandran_Kukathas',
        yob=1957,
        affiliation='Singapore Management University',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Chandran_Kukathas',
            url='https://en.wikipedia.org/wiki/Chandran_Kukathas',
            yob='https://en.wikipedia.org/wiki/Chandran_Kukathas',
            affiliation='https://en.wikipedia.org/wiki/Chandran_Kukathas',
        ),
    ),
    ('Kekes', 'John', ''): dict(
        descr=(
            'American philosopher, professor emeritus at the University at '
            'Albany (SUNY), known for his defence of pluralism and '
            'conservatism. He reviewed A Companion to Michael Oakeshott '
            '(2012) in Notre Dame Philosophical Reviews.'
        ),
        url='https://en.wikipedia.org/wiki/John_Kekes',
        yob=1936,
        affiliation='University at Albany, SUNY',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/John_Kekes',
            url='https://en.wikipedia.org/wiki/John_Kekes',
            yob='https://en.wikipedia.org/wiki/John_Kekes',
            affiliation='https://en.wikipedia.org/wiki/John_Kekes',
        ),
    ),
    ('Jaffa', 'H.', 'V.'): dict(
        descr=(
            'American political philosopher and student of Leo Strauss, '
            'author of Crisis of the House Divided, who taught at Ohio '
            'State and then Claremont McKenna College. He reviewed '
            'Rationalism in Politics in National Review in 1963.'
        ),
        url='https://en.wikipedia.org/wiki/Harry_V._Jaffa',
        yob=1918,
        yod=2015,
        affiliation='Claremont McKenna College',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Harry_V._Jaffa',
            url='https://en.wikipedia.org/wiki/Harry_V._Jaffa',
            yob='https://en.wikipedia.org/wiki/Harry_V._Jaffa',
            yod='https://en.wikipedia.org/wiki/Harry_V._Jaffa',
            affiliation='https://en.wikipedia.org/wiki/Harry_V._Jaffa',
        ),
    ),
    ('Lichtheim', 'G.', ''): dict(
        descr=(
            'German-born writer and intellectual historian of socialism and'
            ' Marxism, who wrote for Commentary and other journals. He '
            'reviewed Rationalism in Politics in Commentary in 1963 under '
            'the title "A Settled Habit of Behaviour".'
        ),
        url='https://en.wikipedia.org/wiki/George_Lichtheim',
        yob=1912,
        yod=1973,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/George_Lichtheim',
            url='https://en.wikipedia.org/wiki/George_Lichtheim',
            yob='https://en.wikipedia.org/wiki/George_Lichtheim',
            yod='https://en.wikipedia.org/wiki/George_Lichtheim',
        ),
    ),
    ('Marshall', 'T.', 'H.'): dict(
        descr=(
            'English sociologist at the London School of Economics, best '
            'known for the essay Citizenship and Social Class, which '
            'distinguished civil, political and social citizenship. '
            'Oakeshott, his LSE colleague, reviewed that book in the '
            'Cambridge Journal.'
        ),
        url='https://en.wikipedia.org/wiki/T._H._Marshall',
        yob=1893,
        yod=1981,
        affiliation='London School of Economics',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/T._H._Marshall',
            url='https://en.wikipedia.org/wiki/T._H._Marshall',
            yob='https://en.wikipedia.org/wiki/T._H._Marshall',
            yod='https://en.wikipedia.org/wiki/T._H._Marshall',
            affiliation='https://en.wikipedia.org/wiki/T._H._Marshall',
        ),
    ),
    ('Macmurray', 'J.', ''): dict(
        descr=(
            'Scottish personalist philosopher who was Grote Professor at '
            'University College London and later held the chair of moral '
            'philosophy at Edinburgh; his Gifford Lectures became The Self '
            'as Agent and Persons in Relation. Oakeshott reviewed his '
            'Interpreting the Universe in the Cambridge Review.'
        ),
        url='https://en.wikipedia.org/wiki/John_Macmurray',
        yob=1891,
        yod=1976,
        affiliation='University of Edinburgh',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/John_Macmurray',
            url='https://en.wikipedia.org/wiki/John_Macmurray',
            yob='https://en.wikipedia.org/wiki/John_Macmurray',
            yod='https://en.wikipedia.org/wiki/John_Macmurray',
            affiliation='https://en.wikipedia.org/wiki/John_Macmurray',
        ),
    ),
    ('Knox', 'T.', 'M.'): dict(
        descr=(
            'British philosopher and translator of Hegel, later professor '
            'of moral philosophy and Principal of the University of St '
            'Andrews. He reviewed Experience and Its Modes in the Oxford '
            'Magazine in 1934.'
        ),
        url='https://en.wikipedia.org/wiki/T._M._Knox',
        yob=1900,
        yod=1980,
        affiliation='University of St Andrews',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/T._M._Knox',
            url='https://en.wikipedia.org/wiki/T._M._Knox',
            yob='https://en.wikipedia.org/wiki/T._M._Knox',
            yod='https://en.wikipedia.org/wiki/T._M._Knox',
            affiliation='https://en.wikipedia.org/wiki/T._M._Knox',
        ),
    ),
    ('Kohn', 'H.', ''): dict(
        descr=(
            'Prague-born American historian and philosopher who pioneered '
            'the academic study of nationalism, teaching at Smith College '
            'and the City College of New York. He reviewed The Social and '
            'Political Doctrines of Contemporary Europe in the Nation in '
            '1939.'
        ),
        url='https://en.wikipedia.org/wiki/Hans_Kohn',
        yob=1891,
        yod=1971,
        affiliation='City College of New York',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Hans_Kohn',
            url='https://en.wikipedia.org/wiki/Hans_Kohn',
            yob='https://en.wikipedia.org/wiki/Hans_Kohn',
            yod='https://en.wikipedia.org/wiki/Hans_Kohn',
            affiliation='https://en.wikipedia.org/wiki/Hans_Kohn',
        ),
    ),
    ('Kolnai', 'A.', ''): dict(
        descr=(
            'Hungarian-born moral and political philosopher in the '
            'phenomenological tradition, author of The War Against the '
            'West, who taught at Laval and later at Bedford College, '
            'London. He reviewed Rationalism in Politics in Philosophy in '
            '1965.'
        ),
        url='https://en.wikipedia.org/wiki/Aurel_Kolnai',
        yob=1900,
        yod=1973,
        affiliation='Bedford College, University of London',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Aurel_Kolnai',
            url='https://en.wikipedia.org/wiki/Aurel_Kolnai',
            yob='https://en.wikipedia.org/wiki/Aurel_Kolnai',
            yod='https://en.wikipedia.org/wiki/Aurel_Kolnai',
            affiliation='https://en.wikipedia.org/wiki/Aurel_Kolnai',
        ),
    ),
    ('Jessop', 'T.', 'E.'): dict(
        descr=(
            'British philosopher best known as an editor and scholar of '
            'George Berkeley, the first Ferens Professor of Philosophy at '
            'Hull (1928-1960). He reviewed Experience and Its Modes in '
            'Philosophy and in the Jahrbuch für die idealistische '
            'Philosophie.'
        ),
        url='https://en.wikipedia.org/wiki/T._E._Jessop',
        yob=1896,
        yod=1980,
        affiliation='University of Hull',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/T._E._Jessop',
            url='https://en.wikipedia.org/wiki/T._E._Jessop',
            yob='https://en.wikipedia.org/wiki/T._E._Jessop',
            yod='https://en.wikipedia.org/wiki/T._E._Jessop',
            affiliation='https://en.wikipedia.org/wiki/T._E._Jessop',
        ),
    ),
    ('Lucas', 'J.', 'R.'): dict(
        descr=(
            'British philosopher, for many years Fellow and Tutor of Merton'
            " College, Oxford, who wrote on free will, Gödel's theorem and "
            'political philosophy. Oakeshott reviewed his The Principles of'
            ' Politics in Political Studies.'
        ),
        url='https://en.wikipedia.org/wiki/John_Lucas_(philosopher)',
        yob=1929,
        yod=2020,
        affiliation='Merton College, Oxford',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/John_Lucas_(philosopher)',
            url='https://en.wikipedia.org/wiki/John_Lucas_(philosopher)',
            yob='https://en.wikipedia.org/wiki/John_Lucas_(philosopher)',
            yod='https://en.wikipedia.org/wiki/John_Lucas_(philosopher)',
            affiliation='https://en.wikipedia.org/wiki/John_Lucas_(philosopher)',
        ),
    ),
    ('Mabbott', 'J.', 'D.'): dict(
        descr=(
            'British classicist and philosopher who was President of St '
            "John's College, Oxford (1963-1969) and author of The State and"
            ' the Citizen and An Introduction to Ethics. Oakeshott reviewed'
            ' The State and the Citizen, and Mabbott reviewed Rationalism '
            'in Politics in Mind.'
        ),
        url='https://en.wikipedia.org/wiki/John_David_Mabbott',
        yob=1898,
        yod=1988,
        affiliation="St John's College, Oxford",
        sources=dict(
            descr='https://en.wikipedia.org/wiki/John_David_Mabbott',
            url='https://en.wikipedia.org/wiki/John_David_Mabbott',
            yob='https://en.wikipedia.org/wiki/John_David_Mabbott',
            yod='https://en.wikipedia.org/wiki/John_David_Mabbott',
            affiliation='https://en.wikipedia.org/wiki/John_David_Mabbott',
        ),
    ),
    ('Mackenzie', 'J.', 'S.'): dict(
        descr=(
            'Scottish idealist philosopher in the tradition of Green and '
            'Bradley who was professor of logic and philosophy at '
            'University College, Cardiff. Oakeshott reviewed his '
            'Fundamental Problems of Life in the Journal of Philosophical '
            'Studies.'
        ),
        url='https://en.wikipedia.org/wiki/John_Stuart_Mackenzie',
        yob=1860,
        yod=1935,
        affiliation='University College, Cardiff',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/John_Stuart_Mackenzie',
            url='https://en.wikipedia.org/wiki/John_Stuart_Mackenzie',
            yob='https://en.wikipedia.org/wiki/John_Stuart_Mackenzie',
            yod='https://en.wikipedia.org/wiki/John_Stuart_Mackenzie',
            affiliation='https://en.wikipedia.org/wiki/John_Stuart_Mackenzie',
        ),
    ),
    ('Mackenzie', 'W.', 'J. M.'): dict(
        descr=(
            'Scottish political scientist, professor of government at '
            'Manchester and later of politics at Glasgow; the Political '
            'Studies Association book prize bears his name. He reviewed '
            'Political Education and Rationalism in Politics in '
            'Universities Quarterly.'
        ),
        url='https://en.wikipedia.org/wiki/W._J._M._Mackenzie',
        yob=1909,
        yod=1996,
        affiliation='University of Glasgow',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/W._J._M._Mackenzie',
            url='https://en.wikipedia.org/wiki/W._J._M._Mackenzie',
            yob='https://en.wikipedia.org/wiki/W._J._M._Mackenzie',
            yod='https://en.wikipedia.org/wiki/W._J._M._Mackenzie',
            affiliation='https://en.wikipedia.org/wiki/W._J._M._Mackenzie',
        ),
    ),
    ('Lavrin', 'J.', ''): dict(
        descr=(
            'Slovene-born critic, translator and historian of literature '
            'who was Professor of Slavonic Studies at the University of '
            'Nottingham and wrote psychological studies of Ibsen, Tolstoy '
            'and Nietzsche. Oakeshott reviewed his Nietzsche in the '
            'Cambridge Journal.'
        ),
        url='https://en.wikipedia.org/wiki/Janko_Lavrin',
        yob=1887,
        yod=1986,
        affiliation='University of Nottingham',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Janko_Lavrin',
            url='https://en.wikipedia.org/wiki/Janko_Lavrin',
            yob='https://en.wikipedia.org/wiki/Janko_Lavrin',
            yod='https://en.wikipedia.org/wiki/Janko_Lavrin',
            affiliation='https://en.wikipedia.org/wiki/Janko_Lavrin',
        ),
    ),
    ('Lindsay', 'J.', ''): dict(
        descr=(
            'Australian-born writer, Marxist critic and prolific novelist '
            'who lived mostly in England, son of the artist Norman Lindsay.'
            ' Oakeshott reviewed his Marxism and Contemporary Science in '
            'the Times Literary Supplement.'
        ),
        url='https://en.wikipedia.org/wiki/Jack_Lindsay',
        yob=1900,
        yod=1990,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Jack_Lindsay',
            url='https://en.wikipedia.org/wiki/Jack_Lindsay',
            yob='https://en.wikipedia.org/wiki/Jack_Lindsay',
            yod='https://en.wikipedia.org/wiki/Jack_Lindsay',
        ),
    ),
    ('Lewis', 'J.', ''): dict(
        descr=(
            'British Unitarian minister and Marxist philosopher associated '
            'with the Communist Party of Great Britain, author of many '
            'books on philosophy and religion. Oakeshott reviewed his '
            'Marxism and the Open Mind in the Spectator in 1957.'
        ),
        url='https://en.wikipedia.org/wiki/John_Lewis_(philosopher)',
        yob=1889,
        yod=1976,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/John_Lewis_(philosopher)',
            url='https://en.wikipedia.org/wiki/John_Lewis_(philosopher)',
            yob='https://en.wikipedia.org/wiki/John_Lewis_(philosopher)',
            yod='https://en.wikipedia.org/wiki/John_Lewis_(philosopher)',
        ),
    ),
    ('Levy', 'H.', ''): dict(
        descr=(
            'Scottish mathematician, philosopher and Marxist activist who '
            'taught mathematics at Imperial College London for many years. '
            'Oakeshott reviewed the collective volume Aspects of '
            'Dialectical Materialism (1934), by Levy and others, in the '
            'Cambridge Review.'
        ),
        url='https://en.wikipedia.org/wiki/Hyman_Levy',
        yob=1889,
        yod=1975,
        affiliation='Imperial College London',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Hyman_Levy',
            url='https://en.wikipedia.org/wiki/Hyman_Levy',
            yob='https://en.wikipedia.org/wiki/Hyman_Levy',
            yod='https://en.wikipedia.org/wiki/Hyman_Levy',
            affiliation='https://en.wikipedia.org/wiki/Hyman_Levy',
        ),
    ),
    ('Macrae', 'D.', 'G.'): dict(
        descr=(
            'Scottish sociologist who spent his career at the London School'
            " of Economics, Oakeshott's institution, becoming Martin White "
            'Professor of Sociology. He reviewed On Human Conduct in the '
            'Sunday Times in 1975.'
        ),
        url='https://en.wikipedia.org/wiki/Donald_Gunn_MacRae',
        yob=1921,
        yod=1997,
        affiliation='London School of Economics',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Donald_Gunn_MacRae',
            url='https://en.wikipedia.org/wiki/Donald_Gunn_MacRae',
            yob='https://en.wikipedia.org/wiki/Donald_Gunn_MacRae',
            yod='https://en.wikipedia.org/wiki/Donald_Gunn_MacRae',
            affiliation='https://en.wikipedia.org/wiki/Donald_Gunn_MacRae',
        ),
    ),
    ('Malcolm', 'N.', ''): dict(
        descr=(
            'English historian and journalist, a leading Hobbes scholar and'
            ' senior research fellow of All Souls College, Oxford, who '
            'earlier wrote for the Spectator and the Daily Telegraph. He '
            'reviewed a book about Oakeshott in the Daily Telegraph in 2004'
            ' ("Modern Philosopher of Tradition").'
        ),
        url='https://en.wikipedia.org/wiki/Noel_Malcolm',
        yob=1956,
        affiliation='All Souls College, Oxford',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Noel_Malcolm',
            url='https://en.wikipedia.org/wiki/Noel_Malcolm',
            yob='https://en.wikipedia.org/wiki/Noel_Malcolm',
            affiliation='https://en.wikipedia.org/wiki/Noel_Malcolm',
        ),
    ),
    ('Marty', 'M.', 'E.'): dict(
        descr=(
            'American Lutheran historian of religion at the University of '
            'Chicago and a longtime editor and columnist of the Christian '
            'Century. He wrote on On Human Conduct in the Christian Century'
            ' in 1991.'
        ),
        url='https://en.wikipedia.org/wiki/Martin_E._Marty',
        yob=1928,
        yod=2025,
        affiliation='University of Chicago',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Martin_E._Marty',
            url='https://en.wikipedia.org/wiki/Martin_E._Marty',
            yob='https://en.wikipedia.org/wiki/Martin_E._Marty',
            yod='https://en.wikipedia.org/wiki/Martin_E._Marty',
            affiliation='https://en.wikipedia.org/wiki/Martin_E._Marty',
        ),
    ),
    ('Kelly', 'D.', ''): dict(
        descr=(
            'British diplomat who served as Minister to Switzerland and '
            'ambassador to Argentina, Turkey and the Soviet Union, and in '
            'retirement wrote on culture and politics. Oakeshott reviewed '
            'his The Hungry Sheep: A Discussion of Modern Civilisation '
            '(1955) in the Daily Telegraph.'
        ),
        url='https://en.wikipedia.org/wiki/David_Kelly_(diplomat)',
        yob=1891,
        yod=1959,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/David_Kelly_(diplomat)',
            url='https://en.wikipedia.org/wiki/David_Kelly_(diplomat)',
            yob='https://en.wikipedia.org/wiki/David_Kelly_(diplomat)',
            yod='https://en.wikipedia.org/wiki/David_Kelly_(diplomat)',
        ),
    ),
    ('Lamprecht', 'S.', 'P.'): dict(
        descr=(
            'American philosopher and historian of philosophy, long '
            'Professor of Philosophy at Amherst College, who wrote on '
            "Locke's moral and political philosophy and on naturalism. He "
            'reviewed Experience and Its Modes in the Journal of Philosophy'
            ' in 1934.'
        ),
        yob=1890,
        affiliation='Amherst College',
        sources=dict(
            descr=(
                'https://www.e-yearbook.com/yearbooks/Amherst_College_Olio_'
                'Yearbook/1935/Page_25.html'
            ),
            yob='https://snaccooperative.org/view/19832522',
            affiliation=(
                'https://www.e-yearbook.com/yearbooks/Amherst_College_Olio_'
                'Yearbook/1935/Page_25.html'
            ),
        ),
    ),
    ('Leff', 'G.', ''): dict(
        descr=(
            'British historian of medieval thought and heresy, author of '
            'Heresy in the Later Middle Ages, who taught from 1965 at the '
            'University of York, where he became emeritus professor. He '
            'reviewed On History and Other Essays in the English Historical'
            ' Review.'
        ),
        yob=1926,
        yod=2020,
        affiliation='University of York',
        sources=dict(
            descr='https://www.york.ac.uk/res/doat/news/leff.html',
            yob='https://www.librarything.com/a/37107',
            yod='https://www.librarything.com/a/37107',
            affiliation='https://www.york.ac.uk/res/doat/news/leff.html',
        ),
    ),
    ('Homberger', 'Eric', ''): dict(
        descr=(
            'American-born scholar of American literature and history who '
            'spent his career at the University of East Anglia, writing on '
            'radical writers and on New York. As a Cambridge graduate '
            'student and editor of the Cambridge Review he co-edited The '
            'Cambridge Mind (1970) with William Janeway and Simon Schama.'
        ),
        yob=1942,
        affiliation='University of East Anglia',
        sources=dict(
            descr=(
                'https://archive.spectator.co.uk/article/31st-october-1970/'
                '21/yanks-at-cambridge'
            ),
            yob=(
                'https://www.encyclopedia.com/arts/educational-magazines/ho'
                'mberger-eric-ross-1942'
            ),
            affiliation=(
                'https://www.encyclopedia.com/arts/educational-magazines/ho'
                'mberger-eric-ross-1942'
            ),
        ),
    ),
    ('Janeway', 'William', ''): dict(
        descr=(
            'American economist and venture capitalist who took a Cambridge'
            ' PhD as a Marshall Scholar and later wrote Doing Capitalism in'
            ' the Innovation Economy; he is an affiliated professor in '
            'economics at Cambridge. He co-edited The Cambridge Mind '
            '(1970), an anthology of the Cambridge Review, having been an '
            'associate editor of the paper.'
        ),
        url='https://en.wikipedia.org/wiki/William_H._Janeway',
        yob=1943,
        affiliation='University of Cambridge',
        sources=dict(
            descr=(
                'https://archive.spectator.co.uk/article/31st-october-1970/'
                '21/yanks-at-cambridge'
            ),
            url='https://en.wikipedia.org/wiki/William_H._Janeway',
            yob='https://en.wikipedia.org/wiki/William_H._Janeway',
            affiliation='https://en.wikipedia.org/wiki/William_H._Janeway',
        ),
    ),
    ('Hopfl', 'H.', 'M.'): dict(
        descr=(
            'Historian of political thought, author of The Christian Polity'
            ' of John Calvin (1982) and Jesuit Political Thought (2004), '
            'who taught politics at Lancaster University. He reviewed The '
            "Skeptic's Oakeshott in History of Political Thought in 2002."
        ),
        yob=1943,
        sources=dict(
            descr=(
                'https://resolve.cambridge.org/core/books/abs/christian-pol'
                'ity-of-john-calvin/introduction/61CB9B67FBA4A2361289FDB92A'
                '2EDA2D'
            ),
            yob='https://catalogo.abie.es/Record/unav.b38384760',
        ),
    ),
    ('Kettler', 'D.', ''): dict(
        descr=(
            'German-born American political theorist, a refugee from Nazi '
            'Germany, who wrote on Adam Ferguson, Karl Mannheim and '
            'intellectual exiles; he taught at Trent University and later '
            'at Bard College. He wrote "The Cheerful Discourses of Michael '
            'Oakeshott", a review of Oakeshott\'s work, in World Politics '
            '(1964).'
        ),
        yob=1930,
        yod=2024,
        affiliation='Bard College',
        sources=dict(
            descr=(
                'https://alums.bard.edu/news/remembrances/david-kettler-res'
                'earch-professor-of-social-studies-2024-10-09'
            ),
            yob=(
                'https://alums.bard.edu/news/remembrances/david-kettler-res'
                'earch-professor-of-social-studies-2024-10-09'
            ),
            yod=(
                'https://alums.bard.edu/news/remembrances/david-kettler-res'
                'earch-professor-of-social-studies-2024-10-09'
            ),
            affiliation=(
                'https://alums.bard.edu/news/remembrances/david-kettler-res'
                'earch-professor-of-social-studies-2024-10-09'
            ),
        ),
    ),
    ('Kimball', 'B.', 'A.'): dict(
        descr=(
            'American historian of education, author of Orators and '
            'Philosophers: A History of the Idea of Liberal Education, and '
            'a Guggenheim Fellow, who is emeritus professor of educational '
            'studies at Ohio State University. In 1990 he reviewed '
            "Oakeshott's writings on education in the American Journal of "
            'Education ("Professions of Language and Reason").'
        ),
        affiliation='Ohio State University',
        sources=dict(
            descr='https://origins.osu.edu/author/bruce-kimball',
            affiliation='https://origins.osu.edu/author/bruce-kimball',
        ),
    ),
    ('Kerwin', 'J.', 'G.'): dict(
        descr=(
            'American political scientist who taught political theory and '
            'constitutional law at the University of Chicago from 1923 to '
            '1961, a prominent liberal Catholic layman and a plaintiff in '
            'Colegrove v. Green. He reviewed The Social and Political '
            'Doctrines of Contemporary Europe in Commonweal (1939) and the '
            'Journal of Political Economy (1943).'
        ),
        yob=1896,
        yod=1977,
        affiliation='University of Chicago',
        sources=dict(
            descr='https://doi.org/10.1017/S0030826900612055',
            yob='https://doi.org/10.1017/S0030826900612055',
            yod='https://doi.org/10.1017/S0030826900612055',
            affiliation='https://doi.org/10.1017/S0030826900612055',
        ),
    ),
    ('Lembcke', 'Oliver', ''): dict(
        descr=(
            'German political scientist working on democratic theory, '
            'judicial governance and the history of constitutional ideas, '
            'who teaches at the Ruhr-Universität Bochum. With Michael '
            'Henkel he edited Praxis und Politik: Michael Oakeshott im '
            'Dialog (2013).'
        ),
        url='https://de.wikipedia.org/wiki/Oliver_Lembcke',
        yob=1969,
        affiliation='Ruhr-Universität Bochum',
        sources=dict(
            descr='https://de.wikipedia.org/wiki/Oliver_Lembcke',
            url='https://de.wikipedia.org/wiki/Oliver_Lembcke',
            yob='https://de.wikipedia.org/wiki/Oliver_Lembcke',
            affiliation='https://de.wikipedia.org/wiki/Oliver_Lembcke',
        ),
    ),
    ('Lively', 'J.', ''): dict(
        descr=(
            'British political theorist, emeritus professor of politics at '
            'the University of Warwick, known for his study Democracy '
            '(1975) and work on utilitarianism; he was married to the '
            'novelist Penelope Lively. Oakeshott reviewed his edition of '
            'The Works of Joseph de Maistre, and Lively reviewed Hobbes on '
            'Civil Association.'
        ),
        url='https://en.wikipedia.org/wiki/Jack_Lively_(political_scientist)',
        yob=1930,
        yod=1998,
        affiliation='University of Warwick',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Jack_Lively_(political_scientist)',
            url='https://en.wikipedia.org/wiki/Jack_Lively_(political_scientist)',
            yob='https://en.wikipedia.org/wiki/Jack_Lively_(political_scientist)',
            yod='https://en.wikipedia.org/wiki/Jack_Lively_(political_scientist)',
            affiliation='https://en.wikipedia.org/wiki/Jack_Lively_(political_scientist)',
        ),
    ),
    ('Lloyd Thomas', 'D.', 'A.'): dict(
        descr=(
            'British political philosopher, author of In Defence of '
            'Liberalism (1988) and a guide to Locke on Government, who '
            "taught at Bedford College and King's College London. He "
            'reviewed On Human Conduct in Mind and the expanded Rationalism'
            ' in Politics in Philosophy.'
        ),
        affiliation="King's College London",
        sources=dict(
            descr='https://www.routledge.com/products/9780415095334',
            affiliation='https://www.routledge.com/products/9780415095334',
        ),
    ),
    ('Martin', 'R.', ''): dict(
        descr=(
            'American philosopher working on personal identity and the '
            'philosophy of history, author of The Past Within Us (1989), '
            'who taught for many years at the University of Maryland before'
            ' moving to Union College. He reviewed Oakeshott on History in '
            'History and Theory (2005).'
        ),
        url='https://www.union.edu/philosophy/faculty-staff/raymond-martin',
        affiliation='Union College',
        sources=dict(
            descr='https://www.union.edu/philosophy/faculty-staff/raymond-martin',
            url='https://www.union.edu/philosophy/faculty-staff/raymond-martin',
            affiliation='https://www.union.edu/philosophy/faculty-staff/raymond-martin',
        ),
    ),
    ('James', 'D.', 'G.'): dict(
        descr=(
            'Welsh literary scholar, Winterstoke Professor of English at '
            'Bristol and then Vice-Chancellor of the University of '
            'Southampton (1952-1965). Oakeshott reviewed his The Life of '
            'Reason: Hobbes, Locke, Bolingbroke (1949) in the Times '
            'Literary Supplement.'
        ),
        url='https://en.wikipedia.org/wiki/David_Gwilym_James',
        yob=1905,
        yod=1968,
        affiliation='University of Southampton',
        sources=dict(
            descr='https://en.wikipedia.org/wiki/David_Gwilym_James',
            url='https://en.wikipedia.org/wiki/David_Gwilym_James',
            yob='https://en.wikipedia.org/wiki/David_Gwilym_James',
            yod='https://en.wikipedia.org/wiki/David_Gwilym_James',
            affiliation='https://en.wikipedia.org/wiki/David_Gwilym_James',
        ),
    ),
    ('Jones', 'W.', 'T.'): dict(
        descr=(
            'American historian of philosophy, author of the multi-volume A'
            ' History of Western Philosophy, who taught at Pomona College '
            'for over three decades and later at Caltech. Oakeshott '
            'reviewed his Masters of Political Thought, vol. 2: Machiavelli'
            ' to Bentham in the Cambridge Journal.'
        ),
        yob=1910,
        yod=1998,
        affiliation='Pomona College',
        sources=dict(
            descr='https://www.pomona.edu/node/3311',
            yob='https://api.philpapers.org/rec/YOUWTJ',
            yod='https://api.philpapers.org/rec/YOUWTJ',
            affiliation='https://www.pomona.edu/node/3311',
        ),
    ),
    ('Jascalevich', 'A.', 'A.'): dict(
        descr=(
            'Author of Three Conceptions of Mind: Their Bearing on the '
            'Denaturalization of the Mind in History (Columbia University '
            'Press, 1926), a historical study of the views of mind of '
            'Aristotle, Augustine and Descartes that began as a Columbia '
            'dissertation; his first name is given as Alexander. Oakeshott '
            'reviewed the book in the Cambridge Review.'
        ),
        sources=dict(
            descr='https://catalog.hathitrust.org/Record/000428158',
        ),
    ),
    ('McNeilly', 'F.', 'S.'): dict(
        descr=(
            'Philosopher (Frederic Stewart McNeilly), author of The Anatomy'
            " of Leviathan (1968), a study reading Hobbes's political "
            'science as formal and conventionalist. He reviewed W. H. '
            "Greenleaf's Oakeshott's Philosophical Politics in "
            'Philosophical Books in 1967.'
        ),
        sources=dict(
            descr='https://theses.univ-nantes.fr/vufind/Record/PPN005431786/Details',
        ),
    ),
    ('McKerrow', 'J.', 'C.'): dict(
        descr=(
            'British physician and philosopher, author of Religion and '
            'History (1934), which argued that there had never been an '
            'Apostolic Age. Oakeshott reviewed the book in the Journal of '
            'Theological Studies.'
        ),
        url='https://en.wikipedia.org/wiki/James_Clark_McKerrow',
        yob=1887,
        yod=1965,
        sources=dict(
            descr='https://en.wikipedia.org/wiki/James_Clark_McKerrow',
            url='https://en.wikipedia.org/wiki/James_Clark_McKerrow',
            yob='https://en.wikipedia.org/wiki/James_Clark_McKerrow',
            yod='https://en.wikipedia.org/wiki/James_Clark_McKerrow',
        ),
    ),
    ('Michaelis', 'G.', ''): dict(
        descr=(
            'German scholar (Gottfried Michaelis) whose Göttingen '
            'dissertation, Richard Hooker als politischer Denker (1933), '
            'studied Hooker in the history of natural-law theories of the '
            'state in sixteenth- and seventeenth-century England. Oakeshott'
            ' reviewed it in the Journal of Theological Studies.'
        ),
        sources=dict(
            descr='https://find.library.upenn.edu/catalog/997899243503681',
        ),
    ),
    ('Lavau', 'G.', ''): dict(
        descr=(
            'French political scientist and public lawyer (Georges Lavau) '
            'who taught at Grenoble and became known for studies of parties'
            ' and the French Communist Party; he later directed the Revue '
            'française de science politique. He reviewed Rationalism in '
            'Politics in that journal in 1964.'
        ),
        url='https://www.universalis.fr/encyclopedie/georges-lavau/',
        yob=1918,
        yod=1990,
        sources=dict(
            descr='https://www.universalis.fr/encyclopedie/georges-lavau/',
            url='https://www.universalis.fr/encyclopedie/georges-lavau/',
            yob='https://www.universalis.fr/encyclopedie/georges-lavau/',
            yod='https://www.universalis.fr/encyclopedie/georges-lavau/',
        ),
    ),
    ('Marshall', 'J.', ''): dict(
        descr=(
            'American writer (James Marshall) who was president of the New '
            'York City Board of Education; his Swords and Symbols: The '
            'Technique of Sovereignty (1939) treated fascism and communism '
            'as kindred. Oakeshott reviewed the book in Philosophy.'
        ),
        yob=1896,
        yod=1986,
        sources=dict(
            descr=(
                'https://www.jta.org/archive/james-marshall-hits-fascism-co'
                'mmunism-in-new-book'
            ),
            yob='https://find.library.upenn.edu/catalog/9910265913503681',
            yod='https://find.library.upenn.edu/catalog/9910265913503681',
        ),
    ),
    ('Minogue', 'V.', ''): dict(
        yob=1931,
        affiliation='Swansea University',
        descr=(
            'Valerie Pearson Minogue, British scholar of French literature '
            'who taught at Cardiff and Queen Mary College, London, before a'
            ' professorship at Swansea; she wrote on Nathalie Sarraute and '
            'Zola. She was the first wife of Kenneth Minogue. Her 1960 '
            'Twentieth Century article "Philosopher Go Home!" responded to '
            "Oakeshott's The Voice of Poetry in the Conversation of "
            'Mankind.'
        ),
        url=(
            'https://www.encyclopedia.com/arts/culture-magazines/minogue-va'
            'lerie-pearson'
        ),
        sources=dict(
            yob=(
                'https://www.encyclopedia.com/arts/culture-magazines/minogu'
                'e-valerie-pearson'
            ),
            affiliation=(
                'https://www.encyclopedia.com/arts/culture-magazines/minogu'
                'e-valerie-pearson'
            ),
            descr=(
                'https://www.encyclopedia.com/arts/culture-magazines/minogu'
                'e-valerie-pearson'
            ),
            identity=(
                'https://repository.bilkent.edu.tr/items/aaa05d62-6b79-4320'
                '-81a3-ef82793b9611/full'
            ),
            url=(
                'https://www.encyclopedia.com/arts/culture-magazines/minogu'
                'e-valerie-pearson'
            ),
        ),
    ),
    ('Money-Kyrle', 'R.', 'E.'): dict(
        yob=1898,
        yod=1980,
        affiliation='British Psychoanalytical Society',
        descr=(
            'Roger Ernle Money-Kyrle was a British psychoanalyst, '
            'influenced by Viennese logical positivism, who applied '
            'psychoanalysis to social and political questions. Oakeshott '
            'reviewed his Psychoanalysis and Politics (1951) in the Times '
            'Literary Supplement.'
        ),
        url='https://en.wikipedia.org/wiki/Roger_Money-Kyrle',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Roger_Money-Kyrle',
            yod='https://en.wikipedia.org/wiki/Roger_Money-Kyrle',
            affiliation='https://en.wikipedia.org/wiki/Roger_Money-Kyrle',
            descr='https://en.wikipedia.org/wiki/Roger_Money-Kyrle',
            url='https://en.wikipedia.org/wiki/Roger_Money-Kyrle',
        ),
    ),
    ('Morgan', 'C.', ''): dict(
        yob=1894,
        yod=1958,
        affiliation='The Times',
        descr=(
            'Charles Langbridge Morgan was an English novelist and '
            'playwright, long the drama critic of The Times, whose novels '
            'explore art, love and death. Oakeshott reviewed his essay '
            'collection Liberties of the Mind (1951) in the Spectator.'
        ),
        url='https://en.wikipedia.org/wiki/Charles_Langbridge_Morgan',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Charles_Langbridge_Morgan',
            yod='https://en.wikipedia.org/wiki/Charles_Langbridge_Morgan',
            affiliation='https://en.wikipedia.org/wiki/Charles_Langbridge_Morgan',
            descr='https://en.wikipedia.org/wiki/Charles_Langbridge_Morgan',
            url='https://en.wikipedia.org/wiki/Charles_Langbridge_Morgan',
        ),
    ),
    ('Morris', 'C.', 'R.'): dict(
        yob=1898,
        yod=1990,
        affiliation='University of Leeds',
        descr=(
            'Charles Richard Morris, later Lord Morris of Grasmere, was a '
            'philosopher and tutor at Balliol College, Oxford, who went on '
            'to become Vice-Chancellor of the University of Leeds. '
            'Oakeshott reviewed his Idealistic Logic (1933) in the '
            'Cambridge Review.'
        ),
        url=(
            'https://en.wikipedia.org/wiki/Charles_Morris,_Baron_Morris_of_'
            'Grasmere'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Charles_Morris,_Baron_Morris'
                '_of_Grasmere'
            ),
            yod=(
                'https://en.wikipedia.org/wiki/Charles_Morris,_Baron_Morris'
                '_of_Grasmere'
            ),
            affiliation=(
                'https://en.wikipedia.org/wiki/Charles_Morris,_Baron_Morris'
                '_of_Grasmere'
            ),
            descr=(
                'https://en.wikipedia.org/wiki/Charles_Morris,_Baron_Morris'
                '_of_Grasmere'
            ),
            url=(
                'https://en.wikipedia.org/wiki/Charles_Morris,_Baron_Morris'
                '_of_Grasmere'
            ),
        ),
    ),
    ('Mount', 'F.', ''): dict(
        yob=1939,
        affiliation='Times Literary Supplement',
        descr=(
            'Sir Ferdinand Mount is a British novelist, journalist and '
            "political commentator who headed Margaret Thatcher's Number 10"
            ' Policy Unit (1982-83) and edited the Times Literary '
            'Supplement (1991-2002). He wrote on Oakeshott in National '
            'Review (1975) and reviewed The Voice of Liberal Learning in '
            'the Sunday Telegraph (1989).'
        ),
        url='https://en.wikipedia.org/wiki/Ferdinand_Mount',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Ferdinand_Mount',
            affiliation='https://en.wikipedia.org/wiki/Ferdinand_Mount',
            descr='https://en.wikipedia.org/wiki/Ferdinand_Mount',
            url='https://en.wikipedia.org/wiki/Ferdinand_Mount',
        ),
    ),
    ('Munz', 'P.', ''): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Peter_Munz',
            yod='https://en.wikipedia.org/wiki/Peter_Munz',
            affiliation='https://en.wikipedia.org/wiki/Peter_Munz',
            descr='https://en.wikipedia.org/wiki/Peter_Munz',
            url='https://en.wikipedia.org/wiki/Peter_Munz',
        ),
    ),
    ('Needham', 'J.', ''): dict(
        yob=1900,
        yod=1995,
        affiliation='Gonville and Caius College, Cambridge',
        descr=(
            'Joseph Needham was a Cambridge biochemist and historian of '
            'science, later Master of Gonville and Caius College, best '
            'known for initiating Science and Civilisation in China. '
            'Oakeshott reviewed the volume he edited, Science, Religion and'
            ' Reality (1926), in the Journal of Theological Studies.'
        ),
        url='https://en.wikipedia.org/wiki/Joseph_Needham',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Joseph_Needham',
            yod='https://en.wikipedia.org/wiki/Joseph_Needham',
            affiliation='https://en.wikipedia.org/wiki/Joseph_Needham',
            descr='https://en.wikipedia.org/wiki/Joseph_Needham',
            url='https://en.wikipedia.org/wiki/Joseph_Needham',
        ),
    ),
    ('Nemoianu', 'V.', ''): dict(
        yob=1940,
        yod=2025,
        affiliation='Catholic University of America',
        descr=(
            'Virgil Nemoianu was a Romanian-American literary critic, '
            'comparatist and philosopher of culture who taught for many '
            'years at the Catholic University of America. He reviewed Paul '
            "Franco's Michael Oakeshott: An Introduction in the Review of "
            'Metaphysics.'
        ),
        url='https://en.wikipedia.org/wiki/Virgil_Nemoianu',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Virgil_Nemoianu',
            yod='https://en.wikipedia.org/wiki/Virgil_Nemoianu',
            affiliation='https://en.wikipedia.org/wiki/Virgil_Nemoianu',
            descr='https://en.wikipedia.org/wiki/Virgil_Nemoianu',
            url='https://en.wikipedia.org/wiki/Virgil_Nemoianu',
        ),
    ),
    ('Oman', 'J.', ''): dict(
        yob=1860,
        yod=1939,
        affiliation='Westminster College, Cambridge',
        descr=(
            'John Wood Oman was a Scottish Presbyterian theologian and '
            'minister who taught systematic theology at Westminster '
            "College, Cambridge. He reviewed Oakeshott's Experience and Its"
            ' Modes in the Journal of Theological Studies (1934).'
        ),
        url='https://en.wikipedia.org/wiki/John_Wood_Oman',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Wood_Oman',
            yod='https://en.wikipedia.org/wiki/John_Wood_Oman',
            affiliation='https://en.wikipedia.org/wiki/John_Wood_Oman',
            descr='https://en.wikipedia.org/wiki/John_Wood_Oman',
            url='https://en.wikipedia.org/wiki/John_Wood_Oman',
        ),
    ),
    ('Passmore', 'J.', ''): dict(
        yob=1914,
        yod=2004,
        affiliation='Australian National University',
        descr=(
            'John Passmore was an Australian philosopher and historian of '
            'philosophy, professor at the Australian National University, '
            'who also wrote on the philosophy of education. He reviewed '
            "Oakeshott's The Voice of Liberal Learning in the Times "
            'Literary Supplement (1989).'
        ),
        url='https://en.wikipedia.org/wiki/John_Passmore',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Passmore',
            yod='https://en.wikipedia.org/wiki/John_Passmore',
            affiliation='https://en.wikipedia.org/wiki/John_Passmore',
            descr='https://en.wikipedia.org/wiki/John_Passmore',
            url='https://en.wikipedia.org/wiki/John_Passmore',
        ),
    ),
    ('Perry', 'R.', 'B.'): dict(
        yob=1876,
        yod=1957,
        affiliation='Harvard University',
        descr=(
            'Ralph Barton Perry was an American philosopher at Harvard, a '
            'leader of the new realism and biographer of William James. '
            'Oakeshott reviewed his General Theory of Value (1927) in the '
            'Cambridge Review and his Puritanism and Democracy (1948) in '
            'Philosophy.'
        ),
        url='https://en.wikipedia.org/wiki/Ralph_Barton_Perry',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Ralph_Barton_Perry',
            yod='https://en.wikipedia.org/wiki/Ralph_Barton_Perry',
            affiliation='https://en.wikipedia.org/wiki/Ralph_Barton_Perry',
            descr='https://en.wikipedia.org/wiki/Ralph_Barton_Perry',
            url='https://en.wikipedia.org/wiki/Ralph_Barton_Perry',
        ),
    ),
    ('Plamenatz', 'J.', ''): dict(
        yob=1912,
        yod=1975,
        affiliation='University of Oxford',
        descr=(
            'John Plamenatz was a Montenegrin-born political philosopher '
            'who spent his career at Oxford, known for work on political '
            'obligation and democracy. Oakeshott reviewed his The English '
            'Utilitarians (1950), and Plamenatz reviewed Rationalism in '
            'Politics in the British Journal of Sociology (1963).'
        ),
        url='https://en.wikipedia.org/wiki/John_Plamenatz',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Plamenatz',
            yod='https://en.wikipedia.org/wiki/John_Plamenatz',
            affiliation='https://en.wikipedia.org/wiki/John_Plamenatz',
            descr='https://en.wikipedia.org/wiki/John_Plamenatz',
            url='https://en.wikipedia.org/wiki/John_Plamenatz',
        ),
    ),
    ('Pocock', 'J.', 'G. A.'): dict(
        yob=1924,
        yod=2023,
        affiliation='Johns Hopkins University',
        descr=(
            'J. G. A. Pocock was a New Zealand historian of political '
            'thought, long at Johns Hopkins, known for The Machiavellian '
            'Moment and work on political discourse. He reviewed '
            "Oakeshott's On History and Other Essays in the Times Literary "
            'Supplement (1983).'
        ),
        url='https://en.wikipedia.org/wiki/J._G._A._Pocock',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/J._G._A._Pocock',
            yod='https://en.wikipedia.org/wiki/J._G._A._Pocock',
            affiliation='https://en.wikipedia.org/wiki/J._G._A._Pocock',
            descr='https://en.wikipedia.org/wiki/J._G._A._Pocock',
            url='https://en.wikipedia.org/wiki/J._G._A._Pocock',
        ),
    ),
    ('Polanyi', 'M.', ''): dict(
        yob=1891,
        yod=1976,
        affiliation='University of Manchester',
        descr=(
            'Michael Polanyi was a Hungarian-British chemist turned '
            'philosopher at the University of Manchester, critic of '
            'positivism and central planning. Oakeshott reviewed his '
            'Personal Knowledge (1958) in Encounter.'
        ),
        url='https://en.wikipedia.org/wiki/Michael_Polanyi',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Michael_Polanyi',
            yod='https://en.wikipedia.org/wiki/Michael_Polanyi',
            affiliation='https://en.wikipedia.org/wiki/Michael_Polanyi',
            descr='https://en.wikipedia.org/wiki/Michael_Polanyi',
            url='https://en.wikipedia.org/wiki/Michael_Polanyi',
        ),
    ),
    ('Powell', 'J.', 'E.'): dict(
        yob=1912,
        yod=1998,
        descr=(
            'Enoch Powell was a British classical scholar and Conservative,'
            ' later Ulster Unionist, politician and minister. He reviewed '
            "Oakeshott's The Voice of Liberal Learning in the Independent "
            '(1989) and the expanded Rationalism in Politics in Economic '
            'Affairs (1991).'
        ),
        url='https://en.wikipedia.org/wiki/Enoch_Powell',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Enoch_Powell',
            yod='https://en.wikipedia.org/wiki/Enoch_Powell',
            descr='https://en.wikipedia.org/wiki/Enoch_Powell',
            url='https://en.wikipedia.org/wiki/Enoch_Powell',
        ),
    ),
    ('Powys', 'J.', 'C.'): dict(
        yob=1872,
        yod=1963,
        descr=(
            'John Cowper Powys was an English novelist, lecturer and '
            'essayist, author of Wolf Solent and A Glastonbury Romance. '
            'Oakeshott reviewed his The Meaning of Culture (1930) in the '
            'Cambridge Review.'
        ),
        url='https://en.wikipedia.org/wiki/John_Cowper_Powys',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Cowper_Powys',
            yod='https://en.wikipedia.org/wiki/John_Cowper_Powys',
            descr='https://en.wikipedia.org/wiki/John_Cowper_Powys',
            url='https://en.wikipedia.org/wiki/John_Cowper_Powys',
        ),
    ),
    ('Powys', 'L.', ''): dict(
        yob=1884,
        yod=1939,
        descr=(
            'Llewelyn Powys was a British essayist and novelist, younger '
            'brother of John Cowper and T. F. Powys. Oakeshott reviewed his'
            ' The Pathetic Fallacy (1930) in the Cambridge Review.'
        ),
        url='https://en.wikipedia.org/wiki/Llewelyn_Powys',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Llewelyn_Powys',
            yod='https://en.wikipedia.org/wiki/Llewelyn_Powys',
            descr='https://en.wikipedia.org/wiki/Llewelyn_Powys',
            url='https://en.wikipedia.org/wiki/Llewelyn_Powys',
        ),
    ),
    ('Pratt', 'J.', 'B.'): dict(
        yob=1875,
        yod=1944,
        affiliation='Williams College',
        descr=(
            'James Bissett Pratt was an American philosopher of religion '
            'and critical realist who held the Mark Hopkins chair of '
            'philosophy at Williams College. Oakeshott reviewed his '
            'Adventures in Philosophy and Religion (1931) in the Cambridge '
            'Review.'
        ),
        url='https://en.wikipedia.org/wiki/James_Bissett_Pratt',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/James_Bissett_Pratt',
            yod='https://en.wikipedia.org/wiki/James_Bissett_Pratt',
            affiliation='https://en.wikipedia.org/wiki/James_Bissett_Pratt',
            descr='https://en.wikipedia.org/wiki/James_Bissett_Pratt',
            url='https://en.wikipedia.org/wiki/James_Bissett_Pratt',
        ),
    ),
    ('Radcliffe', 'Cyril', 'John'): dict(
        yob=1899,
        yod=1977,
        affiliation='University of Warwick',
        descr=(
            'Cyril Radcliffe, 1st Viscount Radcliffe, was a British lawyer '
            'and Law Lord, best known for drawing the partition boundary in'
            ' India, and first chancellor of the University of Warwick. '
            'Oakeshott reviewed his Reith Lectures, The Problem of Power '
            '(1952), in the Spectator.'
        ),
        url=(
            'https://en.wikipedia.org/wiki/Cyril_Radcliffe,_1st_Viscount_Ra'
            'dcliffe'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Cyril_Radcliffe,_1st_Viscoun'
                't_Radcliffe'
            ),
            yod=(
                'https://en.wikipedia.org/wiki/Cyril_Radcliffe,_1st_Viscoun'
                't_Radcliffe'
            ),
            affiliation=(
                'https://en.wikipedia.org/wiki/Cyril_Radcliffe,_1st_Viscoun'
                't_Radcliffe'
            ),
            descr=(
                'https://en.wikipedia.org/wiki/Cyril_Radcliffe,_1st_Viscoun'
                't_Radcliffe'
            ),
            url=(
                'https://en.wikipedia.org/wiki/Cyril_Radcliffe,_1st_Viscoun'
                't_Radcliffe'
            ),
        ),
    ),
    ('Raphael', 'D.', 'D.'): dict(
        yob=1916,
        yod=2015,
        affiliation='Imperial College London',
        descr=(
            'David Daiches Raphael was a British moral and political '
            'philosopher who taught at Glasgow and Reading and was '
            'professor of philosophy at Imperial College London; he wrote '
            "widely on Adam Smith. He reviewed Oakeshott's Rationalism in "
            'Politics (Political Studies, 1964) and On Human Conduct '
            '(Political Quarterly, 1975).'
        ),
        url='https://en.wikipedia.org/wiki/D._D._Raphael',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/D._D._Raphael',
            yod='https://en.wikipedia.org/wiki/D._D._Raphael',
            affiliation='https://en.wikipedia.org/wiki/D._D._Raphael',
            descr='https://en.wikipedia.org/wiki/D._D._Raphael',
            url='https://en.wikipedia.org/wiki/D._D._Raphael',
        ),
    ),
    ('Rashdall', 'H.', ''): dict(
        yob=1858,
        yod=1924,
        affiliation='New College, Oxford',
        descr=(
            'Hastings Rashdall was an English philosopher, theologian and '
            'historian of medieval universities, a fellow of New College, '
            'Oxford and later Dean of Carlisle, known for ideal '
            'utilitarianism. Oakeshott reviewed his posthumously published '
            'God and Man (1930) in the Cambridge Review.'
        ),
        url='https://en.wikipedia.org/wiki/Hastings_Rashdall',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Hastings_Rashdall',
            yod='https://en.wikipedia.org/wiki/Hastings_Rashdall',
            affiliation='https://en.wikipedia.org/wiki/Hastings_Rashdall',
            descr='https://en.wikipedia.org/wiki/Hastings_Rashdall',
            url='https://en.wikipedia.org/wiki/Hastings_Rashdall',
        ),
    ),
    ('Read', 'H.', ''): dict(
        yob=1893,
        yod=1968,
        descr=(
            'Sir Herbert Read was an English poet, art historian and '
            'critic, a prominent anarchist and co-founder of the Institute '
            'of Contemporary Arts. Oakeshott reviewed his Anarchy and Order'
            ' (1954) in the Spectator.'
        ),
        url='https://en.wikipedia.org/wiki/Herbert_Read',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Herbert_Read',
            yod='https://en.wikipedia.org/wiki/Herbert_Read',
            descr='https://en.wikipedia.org/wiki/Herbert_Read',
            url='https://en.wikipedia.org/wiki/Herbert_Read',
        ),
    ),
    ('Renier', 'G.', 'J.'): dict(
        yob=1892,
        yod=1962,
        affiliation='University College London',
        descr=(
            'Gustaaf Johannes Renier was a Dutch-born historian, professor '
            'of Dutch history at University College London. Oakeshott '
            'reviewed his History, Its Purpose and Method (1951) in the '
            'Philosophical Quarterly.'
        ),
        url='https://en.wikipedia.org/wiki/G._J._Renier',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/G._J._Renier',
            yod='https://en.wikipedia.org/wiki/G._J._Renier',
            affiliation='https://en.wikipedia.org/wiki/G._J._Renier',
            descr='https://en.wikipedia.org/wiki/G._J._Renier',
            url='https://en.wikipedia.org/wiki/G._J._Renier',
        ),
    ),
    ('Roberts', 'M.', ''): dict(
        yob=1902,
        yod=1948,
        affiliation='College of St Mark and St John',
        descr=(
            'Michael Roberts (William Edward Roberts) was an English poet, '
            'critic, broadcaster and teacher, later principal of the '
            'College of St Mark and St John in Chelsea. Oakeshott reviewed '
            'his The Modern Mind (1937) in Scrutiny.'
        ),
        url='https://en.wikipedia.org/wiki/Michael_Roberts_(writer)',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Michael_Roberts_(writer)',
            yod='https://en.wikipedia.org/wiki/Michael_Roberts_(writer)',
            affiliation='https://en.wikipedia.org/wiki/Michael_Roberts_(writer)',
            descr='https://en.wikipedia.org/wiki/Michael_Roberts_(writer)',
            url='https://en.wikipedia.org/wiki/Michael_Roberts_(writer)',
        ),
    ),
    ('Rorty', 'R.', ''): dict(
        yob=1931,
        yod=2007,
        affiliation='Stanford University',
        descr=(
            'Richard Rorty was an American pragmatist philosopher, author '
            'of Philosophy and the Mirror of Nature, who taught at '
            "Princeton, Virginia and Stanford. He reviewed Oakeshott's On "
            'Human Conduct in Social Theory and Practice (1976) and later '
            "drew on Oakeshott's idea of conversation."
        ),
        url='https://en.wikipedia.org/wiki/Richard_Rorty',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Richard_Rorty',
            yod='https://en.wikipedia.org/wiki/Richard_Rorty',
            affiliation='https://en.wikipedia.org/wiki/Richard_Rorty',
            descr='https://en.wikipedia.org/wiki/Richard_Rorty',
            url='https://en.wikipedia.org/wiki/Richard_Rorty',
        ),
    ),
    ('Rossiter', 'C.', ''): dict(
        yob=1917,
        yod=1970,
        affiliation='Cornell University',
        descr=(
            'Clinton Rossiter was an American historian and political '
            'scientist at Cornell, author of The American Presidency and '
            'Seedtime of the Republic. Oakeshott reviewed his Conservatism '
            'in America (1956) in the Spectator.'
        ),
        url='https://en.wikipedia.org/wiki/Clinton_Rossiter',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Clinton_Rossiter',
            yod='https://en.wikipedia.org/wiki/Clinton_Rossiter',
            affiliation='https://en.wikipedia.org/wiki/Clinton_Rossiter',
            descr='https://en.wikipedia.org/wiki/Clinton_Rossiter',
            url='https://en.wikipedia.org/wiki/Clinton_Rossiter',
        ),
    ),
    ('Runciman', 'W.', 'G.'): dict(
        yob=1934,
        yod=2020,
        affiliation='Trinity College, Cambridge',
        descr=(
            'W. G. (Garry) Runciman, 3rd Viscount Runciman of Doxford, was '
            'a British historical sociologist and fellow of Trinity '
            'College, Cambridge. Oakeshott reviewed Philosophy, Politics '
            'and Society (2nd series), which he co-edited with Peter '
            'Laslett, in the Philosophical Quarterly.'
        ),
        url=(
            'https://en.wikipedia.org/wiki/Garry_Runciman,_3rd_Viscount_Run'
            'ciman_of_Doxford'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Garry_Runciman,_3rd_Viscount'
                '_Runciman_of_Doxford'
            ),
            yod=(
                'https://en.wikipedia.org/wiki/Garry_Runciman,_3rd_Viscount'
                '_Runciman_of_Doxford'
            ),
            affiliation=(
                'https://en.wikipedia.org/wiki/Garry_Runciman,_3rd_Viscount'
                '_Runciman_of_Doxford'
            ),
            descr=(
                'https://en.wikipedia.org/wiki/Garry_Runciman,_3rd_Viscount'
                '_Runciman_of_Doxford'
            ),
            url=(
                'https://en.wikipedia.org/wiki/Garry_Runciman,_3rd_Viscount'
                '_Runciman_of_Doxford'
            ),
        ),
    ),
    ('Ruthnaswamy', 'M.', ''): dict(
        yob=1885,
        yod=1977,
        affiliation='Annamalai University',
        descr=(
            'Mariadas Ruthnaswamy was an Indian educationist, writer and '
            'politician in Madras, president of the Madras Legislative '
            'Council and later Vice-Chancellor of Annamalai University. '
            'Oakeshott reviewed his book on the state in the Cambridge '
            'Review (1933).'
        ),
        url='https://en.wikipedia.org/wiki/Mariadas_Ruthnaswamy',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Mariadas_Ruthnaswamy',
            yod='https://en.wikipedia.org/wiki/Mariadas_Ruthnaswamy',
            affiliation='https://en.wikipedia.org/wiki/Mariadas_Ruthnaswamy',
            descr='https://en.wikipedia.org/wiki/Mariadas_Ruthnaswamy',
            url='https://en.wikipedia.org/wiki/Mariadas_Ruthnaswamy',
        ),
    ),
    ('Ryan', 'A.', ''): dict(
        yob=1940,
        affiliation='University of Oxford',
        descr=(
            'Alan Ryan is a British political philosopher, professor of '
            'politics at Oxford and Warden of New College (1996-2009), '
            'known for work on J. S. Mill and liberalism. He reviewed '
            "Oakeshott's On Human Conduct in the Listener (1975)."
        ),
        url='https://en.wikipedia.org/wiki/Alan_Ryan',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Alan_Ryan',
            affiliation='https://en.wikipedia.org/wiki/Alan_Ryan',
            descr='https://en.wikipedia.org/wiki/Alan_Ryan',
            url='https://en.wikipedia.org/wiki/Alan_Ryan',
        ),
    ),
    ('Ryle', 'G.', ''): dict(
        yob=1900,
        yod=1976,
        affiliation='University of Oxford',
        descr=(
            'Gilbert Ryle was an Oxford philosopher of ordinary language, '
            'known for his critique of Cartesian dualism and the phrase '
            '"ghost in the machine". Oakeshott reviewed his The Concept of '
            'Mind in the Spectator (1950).'
        ),
        url='https://en.wikipedia.org/wiki/Gilbert_Ryle',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Gilbert_Ryle',
            yod='https://en.wikipedia.org/wiki/Gilbert_Ryle',
            affiliation='https://en.wikipedia.org/wiki/Gilbert_Ryle',
            descr='https://en.wikipedia.org/wiki/Gilbert_Ryle',
            url='https://en.wikipedia.org/wiki/Gilbert_Ryle',
        ),
    ),
    ('Salvemini', 'G.', ''): dict(
        yob=1873,
        yod=1957,
        affiliation='Harvard University',
        descr=(
            'Gaetano Salvemini was an Italian historian and anti-fascist '
            'politician who taught Italian civilization at Harvard during '
            'his exile. Oakeshott reviewed his Mazzini (1956) in the '
            'Spectator.'
        ),
        url='https://en.wikipedia.org/wiki/Gaetano_Salvemini',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Gaetano_Salvemini',
            yod='https://en.wikipedia.org/wiki/Gaetano_Salvemini',
            affiliation='https://en.wikipedia.org/wiki/Gaetano_Salvemini',
            descr='https://en.wikipedia.org/wiki/Gaetano_Salvemini',
            url='https://en.wikipedia.org/wiki/Gaetano_Salvemini',
        ),
    ),
    ('Santayana', 'G.', ''): dict(
        yob=1863,
        yod=1952,
        affiliation='Harvard University',
        descr=(
            'George Santayana was a Spanish-born American philosopher, poet'
            ' and novelist who taught at Harvard before settling in Europe.'
            ' Oakeshott reviewed his last major work, Dominations and '
            'Powers (1951), in the Spectator.'
        ),
        url='https://en.wikipedia.org/wiki/George_Santayana',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/George_Santayana',
            yod='https://en.wikipedia.org/wiki/George_Santayana',
            affiliation='https://en.wikipedia.org/wiki/George_Santayana',
            descr='https://en.wikipedia.org/wiki/George_Santayana',
            url='https://en.wikipedia.org/wiki/George_Santayana',
        ),
    ),
    ('Schama', 'Simon', ''): dict(
        yob=1945,
        affiliation='Columbia University',
        descr=(
            'Sir Simon Schama is an English historian and broadcaster, '
            'author of Citizens and A History of Britain, now at Columbia '
            "University; in 1966-76 he was a fellow of Christ's College, "
            'Cambridge. He co-edited The Cambridge Mind (1970), an '
            'anthology from the Cambridge Review that includes Oakeshott.'
        ),
        url='https://en.wikipedia.org/wiki/Simon_Schama',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Simon_Schama',
            affiliation='https://en.wikipedia.org/wiki/Simon_Schama',
            descr='https://en.wikipedia.org/wiki/Simon_Schama',
            url='https://en.wikipedia.org/wiki/Simon_Schama',
        ),
    ),
    ('Searle', 'J.', 'R.'): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Searle',
            yod='https://en.wikipedia.org/wiki/John_Searle',
            affiliation='https://en.wikipedia.org/wiki/John_Searle',
            descr='https://en.wikipedia.org/wiki/John_Searle',
            url='https://en.wikipedia.org/wiki/John_Searle',
        ),
    ),
    ('Sellars', 'R.', 'W.'): dict(
        yob=1880,
        yod=1973,
        affiliation='University of Michigan',
        descr=(
            'Roy Wood Sellars was a Canadian-born American philosopher of '
            'critical realism and evolutionary naturalism who taught at the'
            ' University of Michigan; father of Wilfrid Sellars. Oakeshott '
            'reviewed his The Principles and Problems of Philosophy (1927) '
            'in the Cambridge Review.'
        ),
        url='https://en.wikipedia.org/wiki/Roy_Wood_Sellars',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Roy_Wood_Sellars',
            yod='https://en.wikipedia.org/wiki/Roy_Wood_Sellars',
            affiliation='https://en.wikipedia.org/wiki/Roy_Wood_Sellars',
            descr='https://en.wikipedia.org/wiki/Roy_Wood_Sellars',
            url='https://en.wikipedia.org/wiki/Roy_Wood_Sellars',
        ),
    ),
    ('Selsam', 'H.', ''): dict(
        yob=1903,
        yod=1970,
        affiliation='Jefferson School of Social Science',
        descr=(
            'Howard Selsam was an American Marxist philosopher who taught '
            'at Brooklyn College and directed the Jefferson School of '
            'Social Science. Oakeshott reviewed his Socialism and Ethics '
            '(1949) in the Cambridge Journal.'
        ),
        url='https://en.wikipedia.org/wiki/Howard_Selsam',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Howard_Selsam',
            yod='https://en.wikipedia.org/wiki/Howard_Selsam',
            affiliation='https://en.wikipedia.org/wiki/Howard_Selsam',
            descr='https://en.wikipedia.org/wiki/Howard_Selsam',
            url='https://en.wikipedia.org/wiki/Howard_Selsam',
        ),
    ),
    ('Neill', 'Edmund', ''): dict(
        affiliation="St Peter's College, Oxford",
        descr=(
            'Edmund Neill is a British scholar of modern political thought,'
            " a lecturer at St Peter's College, Oxford, and author of "
            'Michael Oakeshott (Continuum, 2010) in the Major Conservative '
            'and Libertarian Thinkers series. He also reviewed The '
            'Sceptical Idealist, a study of Oakeshott as a critic of the '
            'Enlightenment, in the English Historical Review.'
        ),
        sources=dict(
            affiliation=(
                'https://origin-www.alibris.com/Michael-Oakeshott-Dr-Edmund'
                '-Neill/book/11629212?qcond=6'
            ),
            descr='https://catalogue.bnf.fr/ark:/12148/cb42154781p',
        ),
    ),
    ('Moore', 'C.', ''): dict(
        yob=1956,
        affiliation='The Spectator',
        url=(
            'https://en.wikipedia.org/wiki/Charles_Moore,_Baron_Moore_of_Et'
            'chingham'
        ),
        descr=(
            'Charles Moore, later Lord Moore of Etchingham, is an English '
            'journalist who edited the Spectator (1984-90), the Sunday '
            'Telegraph and the Daily Telegraph, and wrote the authorised '
            'biography of Margaret Thatcher. As Spectator editor he '
            "reviewed Oakeshott's The Voice of Liberal Learning there in "
            'June 1989 ("Answer came there none").'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Charles_Moore,_Baron_Moore_o'
                'f_Etchingham'
            ),
            affiliation=(
                'https://en.wikipedia.org/wiki/Charles_Moore,_Baron_Moore_o'
                'f_Etchingham'
            ),
            url=(
                'https://en.wikipedia.org/wiki/Charles_Moore,_Baron_Moore_o'
                'f_Etchingham'
            ),
            descr=(
                'https://archive.spectator.co.uk/article/17th-june-1989/28/'
                'answer-came-there-none'
            ),
        ),
    ),
    ('Myers', 'D.', 'G.'): dict(
        yob=1952,
        yod=2014,
        affiliation='Ohio State University',
        url='https://en.wikipedia.org/wiki/D._G._Myers_(literary_critic)',
        descr=(
            'David G. Myers was an American literary critic who taught at '
            'Texas A&M and Ohio State and wrote The Elephants Teach, a '
            'history of creative writing. His American Scholar review of '
            'Oakeshott\'s The Voice of Liberal Learning, "Learning to Be '
            'Human", contrasted Oakeshott\'s idea of conversation with '
            "Richard Rorty's."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/D._G._Myers_(literary_critic)',
            yod='https://en.wikipedia.org/wiki/D._G._Myers_(literary_critic)',
            affiliation='https://en.wikipedia.org/wiki/D._G._Myers_(literary_critic)',
            url='https://en.wikipedia.org/wiki/D._G._Myers_(literary_critic)',
            descr=(
                'https://dgmyers.blogspot.com/p/the-voice-of-liberal-learni'
                'ng-michael.html'
            ),
        ),
    ),
    ('Morgan', 'W.', 'J.'): dict(
        affiliation='Cardiff University',
        url='https://profiles.cardiff.ac.uk/emeritus/w-john-morgan',
        descr=(
            'W. John Morgan is a British scholar of the political economy '
            'of education, emeritus professor at the University of '
            'Nottingham (where he held a UNESCO Chair) and honorary '
            'professor and Leverhulme Emeritus Fellow at Cardiff '
            'University; he chaired the UK National Commission for UNESCO. '
            'He reviewed The Place of Michael Oakeshott in Contemporary '
            'Western and Non-Western Thought (2017).'
        ),
        sources=dict(
            affiliation='https://profiles.cardiff.ac.uk/emeritus/w-john-morgan',
            url='https://profiles.cardiff.ac.uk/emeritus/w-john-morgan',
            descr='https://orca.cardiff.ac.uk/143905',
        ),
    ),
    ('Mullender', 'R.', ''): dict(
        affiliation='Newcastle University',
        url='https://www.ncl.ac.uk/law/people/profile/richardmullender.html',
        descr=(
            'Richard Mullender is a British legal theorist, Professor of '
            'Law and Legal Theory at Newcastle Law School, who previously '
            "lectured at Exeter. He reviewed Paul Franco's Michael "
            'Oakeshott: An Introduction in History of Political Thought.'
        ),
        sources=dict(
            affiliation='https://www.ncl.ac.uk/law/people/profile/richardmullender.html',
            url='https://www.ncl.ac.uk/law/people/profile/richardmullender.html',
            descr='https://eprints.ncl.ac.uk/168504',
        ),
    ),
    ("O'Malley", 'J.', ''): dict(
        affiliation='Marquette University',
        descr=(
            "Joseph O'Malley was an American scholar of Marx at Marquette "
            'University who edited and co-translated (with Annette Jolin) '
            "Marx's Critique of Hegel's Philosophy of Right for Cambridge "
            'University Press (1970). Oakeshott reviewed this edition in '
            'the Spectator.'
        ),
        sources=dict(
            affiliation=(
                'https://cambridge.org/core/journals/dialogue-canadian-phil'
                'osophical-review-revue-canadienne-de-philosophie/article/a'
                'bs/critique-of-hegels-philosophy-of-rightkarl-marx-joseph-'
                'omalley-editor-cambridge-cambridge-university-press-1977-f'
                'irst-paperback-edition-pp-lxvii-153-595/C798AD52539B817EC5'
                '5DBC88465DA48B'
            ),
            descr=(
                'https://core-cms.cambridgecore.org/core/journals/review-of'
                '-politics/article/fundamental-marxist-text-karl-marx-criti'
                'que-of-hegels-philosophy-of-right-edited-with-an-introduct'
                'ion-by-joseph-omalley-translated-by-annette-jolin-and-jose'
                'ph-omalley-cambridge-university-press-1970-pp-216-950/AC05'
                'D8AFBFE43F9A6BF91228C454C78B'
            ),
        ),
    ),
    ('Orton', 'W.', 'A.'): dict(
        yob=1889,
        yod=1952,
        affiliation='Smith College',
        url='https://snaccooperative.org/view/44327180',
        descr=(
            'William Aylott Orton was an English-born economist and social '
            'thinker, educated at Cambridge and London, who taught '
            'economics at Smith College in Massachusetts for thirty years. '
            'Oakeshott reviewed his book The Liberal Tradition in the '
            'English Historical Review (1947).'
        ),
        sources=dict(
            yob=(
                'https://www.encyclopedia.com/religion/encyclopedias-almana'
                'cs-transcripts-and-maps/orton-william-aylott'
            ),
            yod=(
                'https://www.encyclopedia.com/religion/encyclopedias-almana'
                'cs-transcripts-and-maps/orton-william-aylott'
            ),
            affiliation='https://snaccooperative.org/view/36488949',
            descr='https://snaccooperative.org/view/44327180',
            url='https://snaccooperative.org/view/44327180',
        ),
    ),
    ('Partridge', 'P.', 'H.'): dict(
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
        sources=dict(
            yob='https://adb.anu.edu.au/biography/partridge-percy-herbert-15021',
            yod='https://adb.anu.edu.au/biography/partridge-percy-herbert-15021',
            affiliation='https://adb.anu.edu.au/biography/partridge-percy-herbert-15021',
            descr='https://adb.anu.edu.au/biography/partridge-percy-herbert-15021',
            url='https://adb.anu.edu.au/biography/partridge-percy-herbert-15021',
        ),
    ),
    ('Passant', 'E.', 'J.'): dict(
        yob=1890,
        yod=1959,
        url='https://viaf.org/viaf/190718177',
        descr=(
            'Ernest James Passant was a British historian of modern '
            'Germany, author of A Short History of Germany, 1815-1945 '
            "(Cambridge University Press). He reviewed Oakeshott's The "
            'Social and Political Doctrines of Contemporary Europe in '
            'Philosophy (1939).'
        ),
        sources=dict(
            yob='https://viaf.org/viaf/190718177',
            yod='https://viaf.org/viaf/190718177',
            url='https://viaf.org/viaf/190718177',
            descr='https://viaf.org/viaf/190718177',
        ),
    ),
    ('Peterson', 'R.', 'A.'): dict(
        affiliation='The Pilgrim Academy',
        url=(
            'https://fee.org/articles/book-review-rationalism-in-politics-a'
            'nd-other-essays-by-michael-oakeshott/'
        ),
        descr=(
            'Robert A. Peterson was an American educator, headmaster of The'
            ' Pilgrim Academy in Egg Harbor City, New Jersey, who wrote for'
            ' The Freeman, National Review and Human Events. He reviewed '
            "the expanded edition of Oakeshott's Rationalism in Politics in"
            ' The Freeman (June 1992).'
        ),
        sources=dict(
            affiliation=(
                'https://fee.org/articles/book-review-rationalism-in-politi'
                'cs-and-other-essays-by-michael-oakeshott/'
            ),
            descr=(
                'https://fee.org/articles/book-review-rationalism-in-politi'
                'cs-and-other-essays-by-michael-oakeshott/'
            ),
            url=(
                'https://fee.org/articles/book-review-rationalism-in-politi'
                'cs-and-other-essays-by-michael-oakeshott/'
            ),
        ),
    ),
    ('Pfannenstill', 'B.', ''): dict(
        yob=1909,
        yod=1995,
        affiliation='Lund University',
        url='https://sv.wikipedia.org/wiki/Bertil_Pfannenstill',
        descr=(
            'Bertil Pfannenstill was a Swedish philosopher and sociologist '
            'at Lund University, where he became docent in practical '
            'philosophy and later headed the sociology department. His Lund'
            " doctoral thesis, Bernard Bosanquet's Philosophy of the State "
            '(1936), was reviewed by Oakeshott in Philosophy.'
        ),
        sources=dict(
            yob='https://sv.wikipedia.org/wiki/Bertil_Pfannenstill',
            yod='https://sv.wikipedia.org/wiki/Bertil_Pfannenstill',
            affiliation='https://sv.wikipedia.org/wiki/Bertil_Pfannenstill',
            descr='https://sv.wikipedia.org/wiki/Bertil_Pfannenstill',
            url='https://sv.wikipedia.org/wiki/Bertil_Pfannenstill',
        ),
    ),
    ('Roucek', 'J.', 'S.'): dict(
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
        sources=dict(
            yob='https://snaccooperative.org/view/21038783',
            yod='https://snaccooperative.org/view/21038783',
            affiliation='https://snaccooperative.org/view/21038783',
            descr='https://snaccooperative.org/view/21038783',
            url='https://snaccooperative.org/view/21038783',
        ),
    ),
    ('Rubinoff', 'L.', ''): dict(
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
        sources=dict(
            yob=(
                'https://www.encyclopedia.com/arts/culture-magazines/rubino'
                'ff-lionel'
            ),
            affiliation='https://archives.trentu.ca/index.php/lionel-rubinoff',
            url='https://archives.trentu.ca/index.php/lionel-rubinoff',
            descr=(
                'https://www.encyclopedia.com/arts/culture-magazines/rubino'
                'ff-lionel'
            ),
        ),
    ),
    ('Sandelius', 'W.', ''): dict(
        affiliation='University of Kansas',
        descr=(
            'Walter E. Sandelius was an American political scientist, '
            'professor of political science at the University of Kansas. He'
            " reviewed Oakeshott's The Social and Political Doctrines of "
            'Contemporary Europe in the American Political Science Review '
            '(1939).'
        ),
        sources=dict(
            affiliation=(
                'https://digital.lib.ku.edu/islandora/object/ku-udk%3A19391'
                '9/datastream/OCR/download'
            ),
            descr=(
                'https://digital.lib.ku.edu/islandora/object/ku-udk%3A19391'
                '9/datastream/OCR/download'
            ),
        ),
    ),
    ('Selwyn', 'E.', 'G.'): dict(
        affiliation='Winchester Cathedral',
        yob=1885,
        yod=1959,
        url='https://en.wikipedia.org/wiki/Gordon_Selwyn',
        descr=(
            'Edward Gordon Selwyn was an English Anglican priest and '
            'theologian, Warden of Radley College and later Dean of '
            'Winchester (1931-1958). He edited the liberal Anglo-Catholic '
            'journal Theology from 1920 to 1934. Oakeshott reviewed the '
            'collection he edited, Essays Catholic and Critical, in the '
            'Journal of Theological Studies.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Gordon_Selwyn',
            yod='https://en.wikipedia.org/wiki/Gordon_Selwyn',
            affiliation='https://en.wikipedia.org/wiki/Gordon_Selwyn',
            descr='https://en.wikipedia.org/wiki/Gordon_Selwyn',
            url='https://en.wikipedia.org/wiki/Gordon_Selwyn',
        ),
    ),
    ('Shackleton', 'R.', ''): dict(
        affiliation='University of Oxford',
        yob=1919,
        yod=1986,
        url='https://en.wikipedia.org/wiki/Robert_Shackleton',
        descr=(
            'Robert Shackleton was an English scholar of French literature '
            "who taught at Brasenose College, Oxford, served as Bodley's "
            'Librarian (1966-1979) and then held the Marshal Foch chair of '
            'French Literature. He was a leading authority on Montesquieu; '
            'Oakeshott reviewed his Montesquieu: A Critical Biography in '
            'the Modern Language Review.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Robert_Shackleton',
            yod='https://en.wikipedia.org/wiki/Robert_Shackleton',
            affiliation='https://en.wikipedia.org/wiki/Robert_Shackleton',
            descr='https://en.wikipedia.org/wiki/Robert_Shackleton',
            url='https://en.wikipedia.org/wiki/Robert_Shackleton',
        ),
    ),
    ('Sheen', 'F.', 'J.'): dict(
        affiliation='Catholic University of America',
        yob=1895,
        yod=1979,
        url='https://en.wikipedia.org/wiki/Fulton_J._Sheen',
        descr=(
            'Fulton J. Sheen was an American Catholic theologian and '
            'philosopher who taught at the Catholic University of America '
            'and later became a bishop, serving as Bishop of Rochester '
            '(1966-1969). He became widely known as a radio and television '
            'preacher. Oakeshott reviewed his Religion without God in the '
            'Journal of Theological Studies.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Fulton_J._Sheen',
            yod='https://en.wikipedia.org/wiki/Fulton_J._Sheen',
            affiliation='https://en.wikipedia.org/wiki/Fulton_J._Sheen',
            descr='https://en.wikipedia.org/wiki/Fulton_J._Sheen',
            url='https://en.wikipedia.org/wiki/Fulton_J._Sheen',
        ),
    ),
    ('Shklar', 'J.', ''): dict(
        affiliation='Harvard University',
        yob=1928,
        yod=1992,
        url='https://en.wikipedia.org/wiki/Judith_N._Shklar',
        descr=(
            'Judith N. Shklar was a Latvian-born American political '
            'theorist and historian of political thought, especially of the'
            ' Enlightenment, who became John Cowles Professor of Government'
            " at Harvard. She reviewed Oakeshott's On Human Conduct in the "
            'Times Literary Supplement under the title "Purposes and '
            'Procedures".'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Judith_N._Shklar',
            yod='https://en.wikipedia.org/wiki/Judith_N._Shklar',
            affiliation='https://en.wikipedia.org/wiki/Judith_N._Shklar',
            descr='https://en.wikipedia.org/wiki/Judith_N._Shklar',
            url='https://en.wikipedia.org/wiki/Judith_N._Shklar',
        ),
    ),
    ('Sibley', 'M.', 'Q.'): dict(
        affiliation='University of Minnesota',
        yob=1912,
        yod=1989,
        url='https://en.wikipedia.org/wiki/Mulford_Q._Sibley',
        descr=(
            'Mulford Q. Sibley was an American political scientist at the '
            'University of Minnesota who wrote widely on pacifism, '
            'utopianism and civil disobedience and was a controversial '
            "advocate of socialism and pacifism. He reviewed Oakeshott's "
            'The Social and Political Doctrines of Contemporary Europe in '
            'the American Political Science Review.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Mulford_Q._Sibley',
            yod='https://en.wikipedia.org/wiki/Mulford_Q._Sibley',
            affiliation='https://en.wikipedia.org/wiki/Mulford_Q._Sibley',
            descr='https://en.wikipedia.org/wiki/Mulford_Q._Sibley',
            url='https://en.wikipedia.org/wiki/Mulford_Q._Sibley',
        ),
    ),
    ('Skinner', 'Q.', ''): dict(
        affiliation='University of Cambridge',
        yob=1940,
        url='https://en.wikipedia.org/wiki/Quentin_Skinner',
        descr=(
            'Quentin Skinner is a British intellectual historian and a '
            'founder of the "Cambridge School" of the history of political '
            'thought; he was Regius Professor of History at Cambridge '
            '(1996-2008). Oakeshott reviewed his The Foundations of Modern '
            'Political Thought in the Historical Journal.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Quentin_Skinner',
            affiliation='https://en.wikipedia.org/wiki/Quentin_Skinner',
            descr='https://en.wikipedia.org/wiki/Quentin_Skinner',
            url='https://en.wikipedia.org/wiki/Quentin_Skinner',
        ),
    ),
    ('Smith', 'L.', 'P.'): dict(
        yob=1865,
        yod=1946,
        url='https://en.wikipedia.org/wiki/Logan_Pearsall_Smith',
        descr=(
            'Logan Pearsall Smith was an American-born British essayist and'
            ' critic, educated at Harvard and Oxford, noted for his '
            'aphorisms and for his writing on English usage. Oakeshott '
            'reviewed his collection of aphorisms, Afterthoughts, in the '
            'Cambridge Review.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Logan_Pearsall_Smith',
            yod='https://en.wikipedia.org/wiki/Logan_Pearsall_Smith',
            descr='https://en.wikipedia.org/wiki/Logan_Pearsall_Smith',
            url='https://en.wikipedia.org/wiki/Logan_Pearsall_Smith',
        ),
    ),
    ('Speck', 'W.', 'A.'): dict(
        affiliation='University of Leeds',
        yob=1938,
        yod=2017,
        url='https://en.wikipedia.org/wiki/W._A._Speck',
        descr=(
            'William Arthur Speck was a British historian of late '
            'seventeenth- and eighteenth-century Britain and America who '
            'taught at Newcastle and Hull before holding the chair of '
            "Modern History at Leeds. He reviewed Oakeshott's On History "
            'and Other Essays.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/W._A._Speck',
            yod='https://en.wikipedia.org/wiki/W._A._Speck',
            affiliation='https://en.wikipedia.org/wiki/W._A._Speck',
            descr='https://en.wikipedia.org/wiki/W._A._Speck',
            url='https://en.wikipedia.org/wiki/W._A._Speck',
        ),
    ),
    ('Spence', 'J.', 'E.'): dict(
        affiliation="King's College London",
        yob=1931,
        yod=2025,
        url='https://en.wikipedia.org/wiki/Jack_Spence_(political_scientist)',
        descr=(
            'John Edward (Jack) Spence was a British scholar of diplomacy '
            'and South African politics and Professor of Diplomacy in the '
            "Department of War Studies at King's College London. He "
            "reviewed a 2019 book on Oakeshott's political philosophy of "
            'international relations in International Affairs.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Jack_Spence_(political_scientist)',
            yod='https://en.wikipedia.org/wiki/Jack_Spence_(political_scientist)',
            affiliation='https://en.wikipedia.org/wiki/Jack_Spence_(political_scientist)',
            descr='https://en.wikipedia.org/wiki/Jack_Spence_(political_scientist)',
            url='https://en.wikipedia.org/wiki/Jack_Spence_(political_scientist)',
        ),
    ),
    ('Stebbing', 'L.', 'S.'): dict(
        affiliation='Bedford College, London',
        yob=1885,
        yod=1943,
        url='https://en.wikipedia.org/wiki/Susan_Stebbing',
        descr=(
            'L. Susan Stebbing was a British analytic philosopher, a '
            'founder of the journal Analysis in 1933 and the first woman to'
            ' hold a chair of philosophy in the United Kingdom, at Bedford '
            "College, London. She reviewed Oakeshott's Experience and Its "
            'Modes in Mind in 1934.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Susan_Stebbing',
            yod='https://en.wikipedia.org/wiki/Susan_Stebbing',
            affiliation='https://en.wikipedia.org/wiki/Susan_Stebbing',
            descr='https://en.wikipedia.org/wiki/Susan_Stebbing',
            url='https://en.wikipedia.org/wiki/Susan_Stebbing',
        ),
    ),
    ('Stenton', 'Doris', 'Mary'): dict(
        affiliation='University of Reading',
        yob=1894,
        yod=1971,
        url='https://en.wikipedia.org/wiki/Doris_Mary_Stenton',
        descr=(
            'Doris Mary Stenton, Lady Stenton, was an English medieval '
            'historian associated with Reading and known for her editions '
            'of legal records and her work reviving the Pipe Roll Society. '
            'Oakeshott reviewed her The English Woman in History in the '
            'Spectator.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Doris_Mary_Stenton',
            yod='https://en.wikipedia.org/wiki/Doris_Mary_Stenton',
            affiliation='https://en.wikipedia.org/wiki/Doris_Mary_Stenton',
            descr='https://en.wikipedia.org/wiki/Doris_Mary_Stenton',
            url='https://en.wikipedia.org/wiki/Doris_Mary_Stenton',
        ),
    ),
    ('Sternberg', 'F.', ''): dict(
        yob=1895,
        yod=1963,
        url='https://en.wikipedia.org/wiki/Fritz_Sternberg',
        descr=(
            'Fritz Sternberg was a German economist, sociologist and '
            'Marxist theorist and a socialist politician, author of works '
            'on imperialism and on the crisis of capitalism. Oakeshott '
            'reviewed his How to Stop the Russians Without War in the '
            'Cambridge Journal.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Fritz_Sternberg',
            yod='https://en.wikipedia.org/wiki/Fritz_Sternberg',
            descr='https://en.wikipedia.org/wiki/Fritz_Sternberg',
            url='https://en.wikipedia.org/wiki/Fritz_Sternberg',
        ),
    ),
    ('Strauss', 'L.', ''): dict(
        affiliation='University of Chicago',
        yob=1899,
        yod=1973,
        url='https://en.wikipedia.org/wiki/Leo_Strauss',
        descr=(
            'Leo Strauss was a German-American political philosopher and '
            'historian of political thought, influential for his readings '
            'of classical political philosophy and his thesis of esoteric '
            'writing. Oakeshott reviewed his The Political Philosophy of '
            'Hobbes in the Cambridge Review and in Philosophy.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Leo_Strauss',
            yod='https://en.wikipedia.org/wiki/Leo_Strauss',
            affiliation='https://en.wikipedia.org/wiki/Leo_Strauss',
            descr='https://en.wikipedia.org/wiki/Leo_Strauss',
            url='https://en.wikipedia.org/wiki/Leo_Strauss',
        ),
    ),
    ('Sumption', 'J.', ''): dict(
        yob=1948,
        url='https://en.wikipedia.org/wiki/Jonathan_Sumption,_Lord_Sumption',
        descr=(
            'Jonathan Sumption is a British medieval historian, barrister '
            'and former Justice of the Supreme Court of the United Kingdom '
            "(2012-2018). He reviewed Oakeshott's writings in the Spectator"
            ' in 2004 under the title "Sworn Enemy of the Gradgrinds".'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Jonathan_Sumption,_Lord_Sumption',
            descr='https://en.wikipedia.org/wiki/Jonathan_Sumption,_Lord_Sumption',
            url='https://en.wikipedia.org/wiki/Jonathan_Sumption,_Lord_Sumption',
        ),
    ),
    ('The Bow Group', '', ''): dict(
        url='https://en.wikipedia.org/wiki/Bow_Group',
        descr=(
            'The Bow Group is a British conservative think tank founded in '
            '1951, the oldest of its kind, whose members have included many'
            ' senior Conservative politicians. Oakeshott reviewed its '
            'publication The Conservative Opportunity in New Society.'
        ),
        sources=dict(
            descr='https://en.wikipedia.org/wiki/Bow_Group',
            url='https://en.wikipedia.org/wiki/Bow_Group',
        ),
    ),
    ('Thomson', 'D.', ''): dict(
        affiliation='Sidney Sussex College, Cambridge',
        yob=1912,
        yod=1970,
        url='https://en.wikipedia.org/wiki/David_Thomson_(historian)',
        descr=(
            'David Thomson was an English historian of modern Britain and '
            'Europe, long associated with Sidney Sussex College, Cambridge,'
            ' of which he became Master; his books include Europe Since '
            'Napoleon. Oakeshott reviewed his The Aims of History in the '
            'English Historical Review.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/David_Thomson_(historian)',
            yod='https://en.wikipedia.org/wiki/David_Thomson_(historian)',
            affiliation='https://en.wikipedia.org/wiki/David_Thomson_(historian)',
            descr='https://en.wikipedia.org/wiki/David_Thomson_(historian)',
            url='https://en.wikipedia.org/wiki/David_Thomson_(historian)',
        ),
    ),
    ('Tomlin', 'E.', 'W. F.'): dict(
        affiliation='British Council',
        yob=1913,
        yod=1988,
        url='https://en.wikipedia.org/wiki/E._W._F._Tomlin',
        descr=(
            'E. W. F. Tomlin was a British essayist and writer on '
            'philosophy who served with the British Council, heading it in '
            'Japan (1961-1967); he wrote on R. G. Collingwood, T. S. Eliot '
            'and Wyndham Lewis. Oakeshott reviewed his The Great '
            'Philosophers in the Times Literary Supplement.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/E._W._F._Tomlin',
            yod='https://en.wikipedia.org/wiki/E._W._F._Tomlin',
            affiliation='https://en.wikipedia.org/wiki/E._W._F._Tomlin',
            descr='https://en.wikipedia.org/wiki/E._W._F._Tomlin',
            url='https://en.wikipedia.org/wiki/E._W._F._Tomlin',
        ),
    ),
    ('Urban', 'W.', 'M.'): dict(
        affiliation='Yale University',
        yob=1873,
        yod=1952,
        url='https://en.wikipedia.org/wiki/Wilbur_Marshall_Urban',
        descr=(
            'Wilbur Marshall Urban was an American philosopher of language '
            'and value, influenced by Ernst Cassirer, who taught at '
            'Dartmouth and Yale and was president of the American '
            'Philosophical Association. Oakeshott reviewed his Beyond '
            'Realism and Idealism in the Times Literary Supplement.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Wilbur_Marshall_Urban',
            yod='https://en.wikipedia.org/wiki/Wilbur_Marshall_Urban',
            affiliation='https://en.wikipedia.org/wiki/Wilbur_Marshall_Urban',
            descr='https://en.wikipedia.org/wiki/Wilbur_Marshall_Urban',
            url='https://en.wikipedia.org/wiki/Wilbur_Marshall_Urban',
        ),
    ),
    ('Utley', 'T.', 'E.'): dict(
        yob=1921,
        yod=1988,
        url='https://en.wikipedia.org/wiki/T._E._Utley',
        descr=(
            'T. E. (Peter) Utley was a British Tory journalist and writer, '
            'blind from childhood, educated at Corpus Christi College, '
            'Cambridge. Oakeshott reviewed Documents of Modern Political '
            'Thought, which Utley compiled with J. S. Maclure, in Crossbow.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/T._E._Utley',
            yod='https://en.wikipedia.org/wiki/T._E._Utley',
            descr='https://en.wikipedia.org/wiki/T._E._Utley',
            url='https://en.wikipedia.org/wiki/T._E._Utley',
        ),
    ),
    ('Valéry', 'P.', ''): dict(
        yob=1871,
        yod=1945,
        url='https://en.wikipedia.org/wiki/Paul_Valéry',
        descr=(
            'Paul Valéry was a French poet, essayist and philosopher whose '
            'prose writings ranged over art, history, literature and '
            'politics. Oakeshott reviewed his Descartes in the Cambridge '
            'Journal.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Paul_Valéry',
            yod='https://en.wikipedia.org/wiki/Paul_Valéry',
            descr='https://en.wikipedia.org/wiki/Paul_Valéry',
            url='https://en.wikipedia.org/wiki/Paul_Valéry',
        ),
    ),
    ('Voegelin', 'E.', ''): dict(
        affiliation='Louisiana State University',
        yob=1901,
        yod=1985,
        url='https://en.wikipedia.org/wiki/Eric_Voegelin',
        descr=(
            'Eric Voegelin was a German-born American political philosopher'
            ' who taught at Vienna, Louisiana State University and Munich, '
            'and later worked at the Hoover Institution. Oakeshott reviewed'
            ' his The New Science of Politics in the Times Literary '
            'Supplement.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Eric_Voegelin',
            yod='https://en.wikipedia.org/wiki/Eric_Voegelin',
            affiliation='https://en.wikipedia.org/wiki/Eric_Voegelin',
            descr='https://en.wikipedia.org/wiki/Eric_Voegelin',
            url='https://en.wikipedia.org/wiki/Eric_Voegelin',
        ),
    ),
    ('Waldron', 'J.', ''): dict(
        affiliation='New York University',
        yob=1953,
        url='https://en.wikipedia.org/wiki/Jeremy_Waldron',
        descr=(
            'Jeremy Waldron is a New Zealand legal and political '
            'philosopher, University Professor at New York University '
            'School of Law and formerly Chichele Professor of Social and '
            'Political Theory at Oxford. He reviewed a book about Oakeshott'
            ' in the Times Literary Supplement in 1990 ("Politics Without '
            'Purpose?").'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Jeremy_Waldron',
            affiliation='https://en.wikipedia.org/wiki/Jeremy_Waldron',
            descr='https://en.wikipedia.org/wiki/Jeremy_Waldron',
            url='https://en.wikipedia.org/wiki/Jeremy_Waldron',
        ),
    ),
    ('Wallas', 'G.', ''): dict(
        affiliation='London School of Economics',
        yob=1858,
        yod=1932,
        url='https://en.wikipedia.org/wiki/Graham_Wallas',
        descr=(
            'Graham Wallas was an English social psychologist, '
            'educationalist and political thinker, a leading Fabian and '
            'co-founder of the London School of Economics. Oakeshott '
            'reviewed his posthumous collection Men and Ideas in '
            'Philosophy.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Graham_Wallas',
            yod='https://en.wikipedia.org/wiki/Graham_Wallas',
            affiliation='https://en.wikipedia.org/wiki/Graham_Wallas',
            descr='https://en.wikipedia.org/wiki/Graham_Wallas',
            url='https://en.wikipedia.org/wiki/Graham_Wallas',
        ),
    ),
    ('Walsh', 'W.', 'H.'): dict(
        affiliation='University of Edinburgh',
        yob=1913,
        yod=1986,
        url='https://en.wikipedia.org/wiki/W._H._Walsh',
        descr=(
            'W. H. Walsh was a British philosopher and Kant scholar, a '
            'Fellow of Merton College, Oxford, and later Professor of Logic'
            ' and Metaphysics at Edinburgh; he wrote influentially on the '
            'philosophy of history. Oakeshott reviewed his An Introduction '
            "to Philosophy of History, and Walsh reviewed Oakeshott's On "
            'History and Other Essays.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/W._H._Walsh',
            yod='https://en.wikipedia.org/wiki/W._H._Walsh',
            affiliation='https://en.wikipedia.org/wiki/W._H._Walsh',
            descr='https://en.wikipedia.org/wiki/W._H._Walsh',
            url='https://en.wikipedia.org/wiki/W._H._Walsh',
        ),
    ),
    ('Warnock', 'G.', 'J.'): dict(
        affiliation='University of Oxford',
        yob=1923,
        yod=1995,
        url='https://en.wikipedia.org/wiki/Geoffrey_Warnock',
        descr=(
            'Sir Geoffrey Warnock was an English philosopher in the Oxford '
            'ordinary-language tradition, Principal of Hertford College and'
            " Vice-Chancellor of Oxford University. He reviewed Oakeshott's"
            ' On Human Conduct in Encounter ("The Minefields of Moral '
            'Philosophy").'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Geoffrey_Warnock',
            yod='https://en.wikipedia.org/wiki/Geoffrey_Warnock',
            affiliation='https://en.wikipedia.org/wiki/Geoffrey_Warnock',
            descr='https://en.wikipedia.org/wiki/Geoffrey_Warnock',
            url='https://en.wikipedia.org/wiki/Geoffrey_Warnock',
        ),
    ),
    ('Warnock', 'M.', ''): dict(
        affiliation='Girton College, Cambridge',
        yob=1924,
        yod=2019,
        url='https://en.wikipedia.org/wiki/Mary_Warnock,_Baroness_Warnock',
        descr=(
            'Mary Warnock was an English philosopher of ethics, education '
            'and mind and a writer on existentialism, best known for '
            'chairing the inquiry behind the Human Fertilisation and '
            'Embryology Act 1990; she was Mistress of Girton College. She '
            "reviewed Oakeshott's On Human Conduct in New Society."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Mary_Warnock,_Baroness_Warnock',
            yod='https://en.wikipedia.org/wiki/Mary_Warnock,_Baroness_Warnock',
            affiliation='https://en.wikipedia.org/wiki/Mary_Warnock,_Baroness_Warnock',
            descr='https://en.wikipedia.org/wiki/Mary_Warnock,_Baroness_Warnock',
            url='https://en.wikipedia.org/wiki/Mary_Warnock,_Baroness_Warnock',
        ),
    ),
    ('Webb', 'C.', 'C. J.'): dict(
        affiliation='University of Oxford',
        yob=1865,
        yod=1954,
        url='https://en.wikipedia.org/wiki/Clement_Charles_Julian_Webb',
        descr=(
            'Clement C. J. Webb was an English philosopher and theologian '
            'at Oxford, Fellow of Magdalen and the first Nolloth Professor '
            'of the Philosophy of the Christian Religion (1920-1930). '
            'Oakeshott reviewed his The Historical Element in Religion in '
            'the Journal of Theological Studies.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Clement_Charles_Julian_Webb',
            yod='https://en.wikipedia.org/wiki/Clement_Charles_Julian_Webb',
            affiliation='https://en.wikipedia.org/wiki/Clement_Charles_Julian_Webb',
            descr='https://en.wikipedia.org/wiki/Clement_Charles_Julian_Webb',
            url='https://en.wikipedia.org/wiki/Clement_Charles_Julian_Webb',
        ),
    ),
    ('Weldon', 'T.', 'D.'): dict(
        affiliation='Magdalen College, Oxford',
        yob=1896,
        yod=1958,
        url='https://en.wikipedia.org/wiki/Thomas_Dewar_Weldon',
        descr=(
            'T. D. (Harry) Weldon was a British philosopher and '
            'long-serving fellow and philosophy tutor at Magdalen College, '
            'Oxford. Oakeshott reviewed his The Vocabulary of Politics in '
            'the Spectator.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Thomas_Dewar_Weldon',
            yod='https://en.wikipedia.org/wiki/Thomas_Dewar_Weldon',
            affiliation='https://en.wikipedia.org/wiki/Thomas_Dewar_Weldon',
            descr='https://en.wikipedia.org/wiki/Thomas_Dewar_Weldon',
            url='https://en.wikipedia.org/wiki/Thomas_Dewar_Weldon',
        ),
    ),
    ('Wheare', 'K.', 'C.'): dict(
        affiliation='University of Oxford',
        yob=1907,
        yod=1979,
        url='https://en.wikipedia.org/wiki/Kenneth_Wheare',
        descr=(
            'Sir Kenneth Wheare was an Australian-born scholar of '
            'government who spent his career at Oxford, where he was the '
            'first Gladstone Professor of Government; he was an authority '
            'on Commonwealth constitutions. Oakeshott reviewed his '
            'Government by Committee in the Spectator.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Kenneth_Wheare',
            yod='https://en.wikipedia.org/wiki/Kenneth_Wheare',
            affiliation='https://en.wikipedia.org/wiki/Kenneth_Wheare',
            descr='https://en.wikipedia.org/wiki/Kenneth_Wheare',
            url='https://en.wikipedia.org/wiki/Kenneth_Wheare',
        ),
    ),
    ('Whistler', 'L.', ''): dict(
        yob=1912,
        yod=2000,
        url='https://en.wikipedia.org/wiki/Laurence_Whistler',
        descr=(
            'Sir Laurence Whistler was a British poet and glass engraver, '
            "the first recipient of the King's Gold Medal for Poetry and "
            'first President of the Guild of Glass Engravers. Oakeshott '
            'reviewed his The English Festivals in the Cambridge Journal.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Laurence_Whistler',
            yod='https://en.wikipedia.org/wiki/Laurence_Whistler',
            descr='https://en.wikipedia.org/wiki/Laurence_Whistler',
            url='https://en.wikipedia.org/wiki/Laurence_Whistler',
        ),
    ),
    ('Whitehead', 'A.', 'N.'): dict(
        affiliation='Harvard University',
        yob=1861,
        yod=1947,
        url='https://en.wikipedia.org/wiki/Alfred_North_Whitehead',
        descr=(
            'Alfred North Whitehead was an English mathematician and '
            'philosopher, co-author with Bertrand Russell of Principia '
            'Mathematica and founder of process philosophy; he later taught'
            ' at Harvard. Oakeshott reviewed his Adventures of Ideas in the'
            ' Journal of Theological Studies.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Alfred_North_Whitehead',
            yod='https://en.wikipedia.org/wiki/Alfred_North_Whitehead',
            affiliation='https://en.wikipedia.org/wiki/Alfred_North_Whitehead',
            descr='https://en.wikipedia.org/wiki/Alfred_North_Whitehead',
            url='https://en.wikipedia.org/wiki/Alfred_North_Whitehead',
        ),
    ),
    ('Williams', 'F.', ''): dict(
        affiliation='Daily Herald',
        yob=1903,
        yod=1970,
        url=(
            'https://en.wikipedia.org/wiki/Francis_Williams,_Baron_Francis-'
            'Williams'
        ),
        descr=(
            'Francis Williams (Lord Francis-Williams) was a British '
            'journalist and author, editor of the Daily Herald (1936-1940) '
            'and later an adviser to Clement Attlee. Oakeshott reviewed his'
            ' The Triple Challenge in the Cambridge Journal.'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Francis_Williams,_Baron_Fran'
                'cis-Williams'
            ),
            yod=(
                'https://en.wikipedia.org/wiki/Francis_Williams,_Baron_Fran'
                'cis-Williams'
            ),
            affiliation=(
                'https://en.wikipedia.org/wiki/Francis_Williams,_Baron_Fran'
                'cis-Williams'
            ),
            descr=(
                'https://en.wikipedia.org/wiki/Francis_Williams,_Baron_Fran'
                'cis-Williams'
            ),
            url=(
                'https://en.wikipedia.org/wiki/Francis_Williams,_Baron_Fran'
                'cis-Williams'
            ),
        ),
    ),
    ('Wilson', 'T.', ''): dict(
        affiliation='University of Glasgow',
        yob=1916,
        yod=2001,
        url='https://en.wikipedia.org/wiki/Thomas_Wilson_(economist)',
        descr=(
            'Thomas Wilson was a Belfast-born British economist, a Fellow '
            'of University College, Oxford (1946-1958) and then Adam Smith '
            'Professor of Political Economy at Glasgow. Oakeshott reviewed '
            'his Modern Capitalism and Economic Progress in the Cambridge '
            'Journal.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Thomas_Wilson_(economist)',
            yod='https://en.wikipedia.org/wiki/Thomas_Wilson_(economist)',
            affiliation='https://en.wikipedia.org/wiki/Thomas_Wilson_(economist)',
            descr='https://en.wikipedia.org/wiki/Thomas_Wilson_(economist)',
            url='https://en.wikipedia.org/wiki/Thomas_Wilson_(economist)',
        ),
    ),
    ('Wollheim', 'R.', ''): dict(
        affiliation='University College London',
        yob=1923,
        yod=2003,
        url='https://en.wikipedia.org/wiki/Richard_Wollheim',
        descr=(
            'Richard Wollheim was a British philosopher of mind and art, '
            'Grote Professor of Mind and Logic at University College London'
            ' and later a professor at Columbia and Berkeley. He reviewed '
            "Oakeshott's The Voice of Poetry in the Conversation of Mankind"
            ' in the Spectator.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Richard_Wollheim',
            yod='https://en.wikipedia.org/wiki/Richard_Wollheim',
            affiliation='https://en.wikipedia.org/wiki/Richard_Wollheim',
            descr='https://en.wikipedia.org/wiki/Richard_Wollheim',
            url='https://en.wikipedia.org/wiki/Richard_Wollheim',
        ),
    ),
    ('Wood', 'H.', 'G.'): dict(
        affiliation='University of Birmingham',
        yob=1879,
        yod=1963,
        url='https://en.wikipedia.org/wiki/H._G._Wood',
        descr=(
            'H. G. Wood was a British Quaker theologian and New Testament '
            'scholar who taught at Woodbrooke College and became the first '
            'Edward Cadbury Professor of Theology at Birmingham. Oakeshott '
            'reviewed his Christianity and the Nature of History, his 1933 '
            'Hulsean Lectures, in the Cambridge Review and the Journal of '
            'Theological Studies.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/H._G._Wood',
            yod='https://en.wikipedia.org/wiki/H._G._Wood',
            affiliation='https://en.wikipedia.org/wiki/H._G._Wood',
            descr='https://en.wikipedia.org/wiki/H._G._Wood',
            url='https://en.wikipedia.org/wiki/H._G._Wood',
        ),
    ),
    ('Woodbridge', 'F.', 'J. E.'): dict(
        affiliation='Columbia University',
        yob=1867,
        yod=1940,
        url='https://en.wikipedia.org/wiki/Frederick_James_Eugene_Woodbridge',
        descr=(
            'F. J. E. Woodbridge was a Canadian-born American realist '
            'philosopher who spent much of his career at Columbia '
            'University as professor and dean and edited the Journal of '
            'Philosophy. Oakeshott reviewed his The Realm of Mind in the '
            'Cambridge Review.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Frederick_James_Eugene_Woodbridge',
            yod='https://en.wikipedia.org/wiki/Frederick_James_Eugene_Woodbridge',
            affiliation='https://en.wikipedia.org/wiki/Frederick_James_Eugene_Woodbridge',
            descr='https://en.wikipedia.org/wiki/Frederick_James_Eugene_Woodbridge',
            url='https://en.wikipedia.org/wiki/Frederick_James_Eugene_Woodbridge',
        ),
    ),
    ('de Burgh', 'W.', 'G.'): dict(
        affiliation='University of Reading',
        yob=1866,
        yod=1943,
        url='https://en.wikipedia.org/wiki/William_de_Burgh_(philosopher)',
        descr=(
            'W. G. de Burgh was an English philosopher, Professor of '
            'Philosophy at Reading, who helped build the college into a '
            "university. He reviewed Oakeshott's Experience and Its Modes "
            'in the Hibbert Journal and his Social and Political Doctrines '
            'of Contemporary Europe in Mind; Oakeshott later reviewed de '
            "Burgh's The Life of Reason."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/William_de_Burgh_(philosopher)',
            yod='https://en.wikipedia.org/wiki/William_de_Burgh_(philosopher)',
            affiliation='https://en.wikipedia.org/wiki/William_de_Burgh_(philosopher)',
            descr='https://en.wikipedia.org/wiki/William_de_Burgh_(philosopher)',
            url='https://en.wikipedia.org/wiki/William_de_Burgh_(philosopher)',
        ),
    ),
    ('de Jouvenel', 'B.', ''): dict(
        yob=1903,
        yod=1987,
        url='https://en.wikipedia.org/wiki/Bertrand_de_Jouvenel',
        descr=(
            'Bertrand de Jouvenel was a French political philosopher, '
            'political economist and futurologist who taught at '
            'universities in France, Britain and the United States. '
            'Oakeshott reviewed his The Ethics of Redistribution and his '
            'Sovereignty.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Bertrand_de_Jouvenel',
            yod='https://en.wikipedia.org/wiki/Bertrand_de_Jouvenel',
            descr='https://en.wikipedia.org/wiki/Bertrand_de_Jouvenel',
            url='https://en.wikipedia.org/wiki/Bertrand_de_Jouvenel',
        ),
    ),
    ('de Maistre', 'Joseph', ''): dict(
        yob=1753,
        yod=1821,
        url='https://en.wikipedia.org/wiki/Joseph_de_Maistre',
        descr=(
            'Joseph de Maistre was a Savoyard lawyer, diplomat and '
            'political philosopher, a defender of monarchy after the French'
            ' Revolution and a founding figure of modern conservatism. '
            'Oakeshott reviewed The Works of Joseph de Maistre, edited by '
            'J. Lively, in New Society.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Joseph_de_Maistre',
            yod='https://en.wikipedia.org/wiki/Joseph_de_Maistre',
            descr='https://en.wikipedia.org/wiki/Joseph_de_Maistre',
            url='https://en.wikipedia.org/wiki/Joseph_de_Maistre',
        ),
    ),
    ('de Ruggiero', 'G.', ''): dict(
        affiliation='Sapienza University of Rome',
        yob=1888,
        yod=1948,
        url='https://en.wikipedia.org/wiki/Guido_De_Ruggiero',
        descr=(
            'Guido De Ruggiero was an Italian idealist historian of '
            'philosophy, liberal political thinker and politician who '
            "taught at Messina and Rome. He reviewed Oakeshott's The Social"
            ' and Political Doctrines of Contemporary Europe in Politica.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Guido_De_Ruggiero',
            yod='https://en.wikipedia.org/wiki/Guido_De_Ruggiero',
            affiliation='https://en.wikipedia.org/wiki/Guido_De_Ruggiero',
            descr='https://en.wikipedia.org/wiki/Guido_De_Ruggiero',
            url='https://en.wikipedia.org/wiki/Guido_De_Ruggiero',
        ),
    ),
    ('von Kuehnelt-Leddihn', 'E.', ''): dict(
        yob=1909,
        yod=1999,
        url='https://en.wikipedia.org/wiki/Erik_von_Kuehnelt-Leddihn',
        descr=(
            'Erik von Kuehnelt-Leddihn was an Austrian writer on politics, '
            'history and theology, a self-described "conservative '
            'arch-liberal" who criticised democracy and opposed '
            'totalitarianism. Oakeshott reviewed his Liberty or Equality in'
            ' the Spectator.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Erik_von_Kuehnelt-Leddihn',
            yod='https://en.wikipedia.org/wiki/Erik_von_Kuehnelt-Leddihn',
            descr='https://en.wikipedia.org/wiki/Erik_von_Kuehnelt-Leddihn',
            url='https://en.wikipedia.org/wiki/Erik_von_Kuehnelt-Leddihn',
        ),
    ),
    ('Warrender', 'H.', ''): dict(
        affiliation='University of Sheffield',
        yob=1922,
        yod=1985,
        url='https://archives.sheffield.ac.uk/agents/people/432',
        descr=(
            'Howard Warrender was a British political theorist and Hobbes '
            'scholar, Professor of Political Theory and Institutions at '
            'Sheffield from 1972 until his death; he edited the Latin and '
            "English versions of Hobbes's De Cive (1983). Oakeshott "
            'reviewed his The Political Philosophy of Hobbes: His Theory of'
            ' Obligation in the Spectator.'
        ),
        sources=dict(
            yob='https://archives.sheffield.ac.uk/agents/people/432',
            yod='https://archives.sheffield.ac.uk/agents/people/432',
            affiliation='https://archives.sheffield.ac.uk/agents/people/432',
            descr='https://archives.sheffield.ac.uk/agents/people/432',
            url='https://archives.sheffield.ac.uk/agents/people/432',
        ),
    ),
    ('Spragens', 'T.', 'A.'): dict(
        affiliation='Duke University',
        descr=(
            'Thomas A. Spragens, Jr. is an American political theorist at '
            'Duke University and author of The Politics of Motion: The '
            'World of Thomas Hobbes (1973), on how Hobbes reworked '
            'Aristotelian cosmology. Oakeshott reviewed that book in '
            'Government and Opposition ("Logos and Telos"), and Spragens '
            "reviewed Oakeshott's Hobbes on Civil Association in the "
            'American Political Science Review.'
        ),
        sources=dict(
            affiliation=(
                'https://www.schweitzer-online.de/en/buch/Spragens/Politics'
                '-Motion/9780813154671/A24447066/'
            ),
            descr=(
                'https://www.schweitzer-online.de/en/buch/Spragens/Politics'
                '-Motion/9780813154671/A24447066/'
            ),
        ),
    ),
    ('Whittaker', 'T.', ''): dict(
        yob=1856,
        yod=1935,
        url='https://en.wikipedia.org/wiki/Thomas_Whittaker_(metaphysician)',
        descr=(
            'Thomas Whittaker was an English metaphysician and critic, '
            'trained in science at Oxford, known for The Neo-Platonists and'
            ' other works on the history of philosophy and metaphysics. '
            'Oakeshott reviewed his The Metaphysics of Evolution, a '
            'collection of essays first published in Mind, in the Cambridge'
            ' Review.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Thomas_Whittaker_(metaphysician)',
            yod='https://en.wikipedia.org/wiki/Thomas_Whittaker_(metaphysician)',
            descr='https://en.wikipedia.org/wiki/Thomas_Whittaker_(metaphysician)',
            url='https://en.wikipedia.org/wiki/Thomas_Whittaker_(metaphysician)',
        ),
    ),
    ('Wilson', 'F.', 'G.'): dict(
        affiliation='University of Illinois',
        yob=1901,
        yod=1976,
        url='https://en.wikipedia.org/wiki/Francis_Wilson_(political_scientist)',
        descr=(
            'Francis Graham Wilson was an American political scientist and '
            'scholar of public opinion, professor at the University of '
            'Illinois (1939-1967) and a significant figure in the postwar '
            'American conservative intellectual movement. He wrote '
            '"Oakeshott and Conservatism" (1963) in the University Bookman.'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Francis_Wilson_(political_sc'
                'ientist)'
            ),
            yod=(
                'https://en.wikipedia.org/wiki/Francis_Wilson_(political_sc'
                'ientist)'
            ),
            affiliation=(
                'https://en.wikipedia.org/wiki/Francis_Wilson_(political_sc'
                'ientist)'
            ),
            descr=(
                'https://en.wikipedia.org/wiki/Francis_Wilson_(political_sc'
                'ientist)'
            ),
            url=(
                'https://en.wikipedia.org/wiki/Francis_Wilson_(political_sc'
                'ientist)'
            ),
        ),
    ),
    ('Vossenkuhl', 'W.', ''): dict(
        affiliation='Ludwig-Maximilians-Universität München',
        yob=1945,
        descr=(
            'Wilhelm Vossenkuhl is a German philosopher, known for work on '
            'ethics and on Wittgenstein, who taught at Bayreuth and held a '
            'chair of philosophy at LMU Munich until 2010/11. He reviewed '
            "Oakeshott's On Human Conduct in German periodicals in "
            '1976-1977, including "Die Lebensform des Menschen" in the '
            'Zeitschrift für philosophische Forschung.'
        ),
        sources=dict(
            yob=(
                'https://www.philosophie.uni-muenchen.de/lehreinheiten/phil'
                'osophie_1/personen/vossenkuhl/cv_v.doc'
            ),
            affiliation=(
                'https://www.philosophie.uni-muenchen.de/lehreinheiten/phil'
                'osophie_1/personen/vossenkuhl/cv_v.doc'
            ),
            descr=(
                'https://www.philosophie.uni-muenchen.de/lehreinheiten/phil'
                'osophie_1/personen/vossenkuhl/cv_v.doc'
            ),
        ),
    ),
    ('Tseng', 'Roy', ''): dict(
        affiliation='Academia Sinica',
        url=(
            'https://www.rchss.sinica.edu.tw/members/43ffaa44-13e8-4594-887'
            'a-13b9008fc541?page_id=45'
        ),
        descr=(
            'Roy Tseng (Tseng Kuo-hsiang) is a Taiwanese political '
            'theorist, research fellow at the Center for Political Thought '
            "of Academia Sinica's Research Center for Humanities and Social"
            ' Sciences, who wrote an LSE doctoral thesis on Oakeshott. He '
            'is the author of The Sceptical Idealist: Michael Oakeshott as '
            'a Critic of the Enlightenment (2003) and of work on Confucian '
            'liberalism.'
        ),
        sources=dict(
            affiliation=(
                'https://www.rchss.sinica.edu.tw/members/43ffaa44-13e8-4594'
                '-887a-13b9008fc541?page_id=45'
            ),
            descr=(
                'https://etheses.lse.ac.uk/view/creators/Tseng=3AKuo-Shiang'
                '_Roy=3A=3A.default.html'
            ),
            url=(
                'https://www.rchss.sinica.edu.tw/members/43ffaa44-13e8-4594'
                '-887a-13b9008fc541?page_id=45'
            ),
        ),
    ),
    ('Smith', 'T.', 'W.'): dict(
        affiliation='University of South Florida St. Petersburg',
        descr=(
            'Thomas W. Smith is an American political theorist on the '
            'faculty of the University of South Florida St. Petersburg. He '
            'wrote "Michael Oakeshott on History, Practice and Political '
            'Theory" in History of Political Thought (1996).'
        ),
        sources=dict(
            affiliation='https://digitalcommons.usf.edu/fac_publications/494',
            descr='https://digitalcommons.usf.edu/fac_publications/494',
        ),
    ),
    ('Smith', 'S.', 'B.'): dict(
        affiliation='Yale University',
        yob=1951,
        url='https://en.wikipedia.org/wiki/Steven_B._Smith_(political_scientist)',
        descr=(
            'Steven B. Smith is an American political philosopher, Alfred '
            'Cowles Professor of Political Science at Yale and formerly '
            'Master of Branford College, known for work on Hegel, Spinoza '
            "and Leo Strauss. He reviewed Oakeshott's On History and Other "
            "Essays in the Review of Politics and Devigne's Recasting "
            'Conservatism in the American Political Science Review (1994).'
        ),
        sources=dict(
            yob=(
                'https://en.wikipedia.org/wiki/Steven_B._Smith_(political_s'
                'cientist)'
            ),
            affiliation=(
                'https://en.wikipedia.org/wiki/Steven_B._Smith_(political_s'
                'cientist)'
            ),
            descr=(
                'https://en.wikipedia.org/wiki/Steven_B._Smith_(political_s'
                'cientist)'
            ),
            url=(
                'https://en.wikipedia.org/wiki/Steven_B._Smith_(political_s'
                'cientist)'
            ),
            identity=(
                'https://econpapers.repec.org/RePEc:cup:apsrev:v:88:y:1994:'
                'i:04:p:971-972_09'
            ),
        ),
    ),
    ('Thro', 'L.', 'J.'): dict(
        descr=(
            'Linus J. Thro, S.J., was a Jesuit philosopher and '
            'long-standing book reviewer for The Modern Schoolman (Saint '
            'Louis University), with reviews from 1950 to 2000; he edited a'
            ' 1984 Festschrift for James D. Collins. He reviewed '
            "Oakeshott's Hobbes on Civil Association in The Modern "
            'Schoolman.'
        ),
        sources=dict(
            descr='https://dc2.philarchive.org/s/Linus%20J.%20Thro',
        ),
    ),
    ('Swaim', 'B.', ''): dict(
        descr=(
            'Barton Swaim is an American writer and critic, author of '
            'Scottish Men of Letters and the New Public Sphere. He reviewed'
            " Oakeshott's Lectures in the History of Political Thought in "
            'the Weekly Standard in April 2008 ("The Right Stuff").'
        ),
        sources=dict(
            descr='https://www.washingtonexaminer.com/?p=1851819',
        ),
    ),
    ('Walker', 'L.', 'J.'): dict(
        descr=(
            'Leslie J. Walker, S.J., was a Jesuit scholar whose two-volume '
            "translation of Machiavelli's Discourses, with introduction and"
            ' notes (1950), became a standard English version. Oakeshott '
            'reviewed that edition in the Cambridge Journal.'
        ),
        sources=dict(
            descr=(
                'https://www.routledge.com/The-Discourses-of-Niccolo-Machia'
                'velli/Walker/p/book/9780415051255'
            ),
        ),
    ),
    ('de Crespigny', 'A.', ''): dict(
        affiliation='University of Cape Town',
        descr=(
            'Anthony de Crespigny, a political philosopher at the '
            'University of Cape Town, co-edited with Kenneth Minogue '
            'Contemporary Political Philosophers (1975/1976), a survey of '
            'twentieth-century political thinkers that includes a chapter '
            'on Oakeshott.'
        ),
        sources=dict(
            affiliation=(
                'https://www.schweitzer-online.de/en/buch/Minogue/Contempor'
                'ary-Political-Philosophers-Routledge-Revivals/978041561433'
                '7/A1100868/'
            ),
            descr=(
                'https://www.cambridge.org/core/journals/government-and-opp'
                'osition/article/political-philosophy-now-anthony-de-crespi'
                'gny-and-kenneth-minogue-eds-contemporary-political-philoso'
                'phers-methuen-london-1976-xvii-296-pages-275/579410970E822'
                '89BF427CABBAF278E22'
            ),
        ),
    ),
    ('Van de Putte', 'A.', ''): dict(
        affiliation='KU Leuven',
        yod=2020,
        descr=(
            'André Van de Putte was a Belgian philosopher, trained in '
            'classics, philosophy and law and formerly a lawyer, who became'
            ' emeritus professor and dean of the Institute of Philosophy '
            '(Hoger Instituut voor Wijsbegeerte) at KU Leuven; he wrote on '
            'the university, society and Catholicism. He reviewed The '
            'Intellectual Legacy of Michael Oakeshott in the Tijdschrift '
            'voor Filosofie.'
        ),
        sources=dict(
            yod=(
                'https://journal.unpar.ac.id/index.php/melintas/article/dow'
                'nload/6290/3897/19115'
            ),
            affiliation=(
                'https://journal.unpar.ac.id/index.php/melintas/article/dow'
                'nload/6290/3897/19115'
            ),
            descr=(
                'https://journal.unpar.ac.id/index.php/melintas/article/dow'
                'nload/6290/3897/19115'
            ),
        ),
    ),
    ('Verschaffel', 'B.', ''): dict(
        affiliation='Ghent University',
        yob=1956,
        url='https://www.lannoocampus.be/nl/bart-verschaffel',
        descr=(
            'Bart Verschaffel is a Belgian philosopher and professor in the'
            ' architecture department of Ghent University, writing on '
            'cultural philosophy, aesthetics and architectural and art '
            'theory. In the mid-1980s he also wrote on the theory of '
            'history in the Tijdschrift voor Filosofie, where he reviewed '
            "Oakeshott's On History and Other Essays."
        ),
        sources=dict(
            yob='https://www.lannoocampus.be/nl/bart-verschaffel',
            affiliation='https://www.lannoocampus.be/nl/bart-verschaffel',
            descr='https://www.lannoocampus.be/nl/bart-verschaffel',
            url='https://www.lannoocampus.be/nl/bart-verschaffel',
            identity='https://dc2.philarchive.org/s/Bart%20Verschaffel',
        ),
    ),
    ('Walton', 'C.', ''): dict(
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
        sources=dict(
            yob='https://dc2.philarchive.org/s/Delvy%20Craig%20Walton',
            yod='https://dc2.philarchive.org/s/Delvy%20Craig%20Walton',
            descr='https://www.philosophie.ch/profil/walton-c',
        ),
    ),
    ('Wearne', 'Eric', ''): dict(
        affiliation='Georgia Gwinnett College',
        descr=(
            'Eric Wearne is an American education scholar in the School of '
            'Education at Georgia Gwinnett College, working on education '
            'policy and school choice; he was earlier Deputy Director of '
            "the Georgia Governor's Office of Student Achievement. He "
            "reviewed Education and Conversation: Exploring Oakeshott's "
            'Legacy in Education Review (2017).'
        ),
        sources=dict(
            affiliation='https://edrev.asu.edu/index.php/ER/article/view/2182',
            descr='https://edrev.asu.edu/index.php/ER/article/view/2182',
        ),
    ),
    ('Whitworth', 'J.', ''): dict(
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
        sources=dict(
            yob='https://en.wikipedia.org/wiki/John_Whitworth_(poet)',
            yod='https://en.wikipedia.org/wiki/John_Whitworth_(poet)',
            descr='https://en.wikipedia.org/wiki/John_Whitworth_(poet)',
            url='https://en.wikipedia.org/wiki/John_Whitworth_(poet)',
            identity=(
                'https://www.ablemusepress.com/node/537 (Selected Poems '
                'blurb mentions patter songs on Oakeshott); https://quadran'
                't.org.au/magazine/uncategorized/john-whitworth-1945-2019/'
            ),
        ),
    ),
    ('Gardner', 'P.', ''): dict(
        affiliation='University of Oxford',
        yob=1846,
        yod=1937,
        url='https://en.wikipedia.org/wiki/Percy_Gardner',
        descr=(
            'Percy Gardner, English classical archaeologist and '
            'numismatist, Lincoln Professor of Classical Archaeology at '
            'Oxford and a liberal Anglican modernist. Oakeshott reviewed '
            'his Modernism in the English Church (1926) in the Journal of '
            'Theological Studies.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Percy_Gardner',
            yod='https://en.wikipedia.org/wiki/Percy_Gardner',
            affiliation='https://en.wikipedia.org/wiki/Percy_Gardner',
            descr=(
                'https://archive.spectator.co.uk/article/11th-december-1926'
                '/21/liberal-and-conservative'
            ),
            url='https://en.wikipedia.org/wiki/Percy_Gardner',
        ),
    ),
    ('Giorgini', 'G.', ''): dict(
        affiliation='University of Bologna',
        url='https://www.unibo.it/sitoweb/giovanni.giorgini/en',
        descr=(
            'Giovanni Giorgini, Italian historian of political thought and '
            'professor at the University of Bologna, who translated '
            'Rationalism in Politics into Italian. He reviewed The Politics'
            ' of Faith and the Politics of Scepticism in Political Studies.'
        ),
        sources=dict(
            affiliation='https://www.unibo.it/sitoweb/giovanni.giorgini/en',
            descr=(
                'https://imusic.au/books/9780300105339/michael-oakeshott-19'
                '96-the-politics-of-faith-and-the-politics-of-scepticism-pa'
                'perback-book'
            ),
            url='https://www.unibo.it/sitoweb/giovanni.giorgini/en',
        ),
    ),
    ('Whittaker', 'E.', 'T.'): dict(
        affiliation='University of Edinburgh',
        yob=1873,
        yod=1956,
        url='https://en.wikipedia.org/wiki/E._T._Whittaker',
        descr=(
            'Sir Edmund Taylor Whittaker was a British mathematician, '
            'mathematical physicist and historian of science, long based at'
            ' Edinburgh. Oakeshott reviewed his lecture The Modern Approach'
            " to Descartes' Problem in the Cambridge Journal."
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/E._T._Whittaker',
            yod='https://en.wikipedia.org/wiki/E._T._Whittaker',
            affiliation='https://en.wikipedia.org/wiki/E._T._Whittaker',
            descr='https://en.wikipedia.org/wiki/E._T._Whittaker',
            url='https://en.wikipedia.org/wiki/E._T._Whittaker',
        ),
    ),
    ('Widgery', 'A.', 'G.'): dict(
        affiliation='Duke University',
        yob=1887,
        yod=1968,
        url='https://www.ncpedia.org/biography/widgery-alban-gregory',
        descr=(
            'Alban Gregory Widgery was an English-born philosopher of '
            'religion who chaired the philosophy department at Duke '
            'University from 1930 to 1946 and taught there until 1952. '
            'Oakeshott reviewed his Contemporary Thought of Great Britain '
            '(1927) in the Cambridge Review.'
        ),
        sources=dict(
            yob='https://www.ncpedia.org/biography/widgery-alban-gregory',
            yod='https://www.ncpedia.org/biography/widgery-alban-gregory',
            affiliation='https://www.ncpedia.org/biography/widgery-alban-gregory',
            descr='https://www.ncpedia.org/biography/widgery-alban-gregory',
            url='https://www.ncpedia.org/biography/widgery-alban-gregory',
        ),
    ),
    ('Tilby', 'A.', 'W.'): dict(
        yob=1880,
        yod=1948,
        url='https://en.wikipedia.org/wiki/A._Wyatt_Tilby',
        descr=(
            'A. Wyatt Tilby was a British author, journalist and traveller.'
            ' Oakeshott reviewed his Right: A Study in Physical and Moral '
            'Order in the Journal of Theological Studies.'
        ),
        sources=dict(
            yob='https://en.wikipedia.org/wiki/A._Wyatt_Tilby',
            yod='https://en.wikipedia.org/wiki/A._Wyatt_Tilby',
            descr='https://en.wikipedia.org/wiki/A._Wyatt_Tilby',
            url='https://en.wikipedia.org/wiki/A._Wyatt_Tilby',
        ),
    ),
    ('Thorson', 'T.', 'L.'): dict(
        affiliation='University of Toronto',
        descr=(
            'Thomas Landon Thorson was a political scientist, author of The'
            ' Logic of Democracy (1962), who was at the University of '
            'Toronto when he reviewed Politics and Experience, the '
            "Festschrift for Oakeshott's retirement, in the American "
            'Political Science Review (1969).'
        ),
        sources=dict(
            affiliation=(
                'https://econpapers.repec.org/RePEc:cup:apsrev:v:63:y:1969:'
                'i:03:p:934-935_25'
            ),
            descr=(
                'https://econpapers.repec.org/RePEc:cup:apsrev:v:63:y:1969:'
                'i:03:p:934-935_25'
            ),
        ),
    ),
    ('Pickles', 'D.', 'M.'): dict(
        yob=1903,
        yod=1994,
        descr=(
            'Dorothy Maud Pickles was a British historian, university '
            'teacher and broadcaster who wrote on French politics and '
            'political ideas. Oakeshott reviewed her Introduction to '
            'Politics (1951) in the Times Literary Supplement.'
        ),
        url='https://en.wikipedia.org/wiki/Dorothy_Pickles',
        sources=dict(
            yob='https://en.wikipedia.org/wiki/Dorothy_Pickles',
            yod='https://en.wikipedia.org/wiki/Dorothy_Pickles',
            descr='https://en.wikipedia.org/wiki/Dorothy_Pickles',
            url='https://en.wikipedia.org/wiki/Dorothy_Pickles',
        ),
    ),
    ('Jacob', 'S.', 'M.'): dict(
        descr=(
            "Sydney Montague Jacob, author of Notes on Descartes' Règles "
            "pour la direction de l'esprit (1948, privately published and "
            'sold by the International Book Club). Oakeshott reviewed it in'
            ' the Cambridge Journal (1949).'
        ),
        sources=dict(
            identity='https://dc2.philarchive.org/rec/JACNOD',
            descr='https://dc2.philarchive.org/rec/JACNOD',
        ),
    ),
    ('Martet', 'J.', ''): dict(
        yob=1886,
        yod=1940,
        descr=(
            "Jean Martet, french writer who was Georges Clemenceau's "
            'secretary from 1915 and published his conversations with '
            'Clemenceau; the English version, Clemenceau, translated by '
            'Milton Waldman, appeared in 1930. Oakeshott reviewed it in the'
            ' Cambridge Review.'
        ),
        sources=dict(
            identity=(
                'https://www.awm.gov.au/collection/LIB2110 https://archive.'
                'spectator.co.uk/article/22nd-february-1930/27/the-tiger-of'
                '-france https://www.thriftbooks.com/w/clemenceau_jean-mart'
                'et/17228808/'
            ),
            descr='https://www.awm.gov.au/collection/LIB2110',
        ),
    ),
    ('Hunkin', 'J.', 'W.'): dict(
        affiliation='Gonville and Caius College, Cambridge',
        yob=1887,
        yod=1950,
        url='https://en.wikipedia.org/wiki/Joseph_Hunkin_(bishop)',
        descr=(
            'Joseph Wellington Hunkin, an anglican clergyman educated at '
            "Gonville and Caius College, Cambridge (Oakeshott's college), "
            'where he was Dean of Chapel after serving as a First World War'
            ' chaplain; he was Bishop of Truro from 1935 to 1950. He '
            'reviewed Experience and Its Modes in the Church of England '
            'Newspaper (1934).'
        ),
        sources=dict(
            identity='https://en.wikipedia.org/wiki/Joseph_Hunkin_(bishop',
            descr='https://en.wikipedia.org/wiki/Joseph_Hunkin_(bishop',
        ),
    ),
}
