"""Author details for people in the database, used by load_author_info.

Keyed by (last name, first name, middle name), with "" for a missing
name. Each entry may give affiliation (institution name only), yob, yod
and descr (a short paraphrased description, under 512 characters).
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
}
