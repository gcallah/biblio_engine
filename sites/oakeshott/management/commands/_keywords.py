"""Keywords for entries in the database, used by load_keywords.

An entry gets a keyword only when it is strongly about it: the term is
in its title (or the title of the book it reviews), or its abstract
makes it a central subject. BOOK_KEYWORDS also go to every review of
that book. ENTRY_KEYWORDS are keyed by (title, reviewed title, year,
where): "where" is the journal name, "in: <book title>" for a chapter,
or the publisher name for a book; "reviewed title" is the review field
(a book not in the bibliography), usually blank.

The second set (BOOK_KEYWORDS_2, ENTRY_KEYWORDS_2, 2026-11-20) tags the
keywords the editors added on the site, by the same rule; it is kept
apart so that an entry tagged in both sets is not silently overwritten
by a repeated dictionary key. POSSIBLE lists entries that may deserve
one of those keywords but are not plainly about it; load_keywords puts
each group on the editors' to-do page as an open question.
"""

KEYWORDS = [
    'idealism',
    'rationalism',
    'civil association',
    'enterprise association',
    'poetry',
    'aesthetics',
    'morality',
    'religion',
    'philosophy of science',
    'philosophy of history',
    'politics of faith',
    'politics of scepticism',
    'Hobbes',
    # added by the editors on the site, 2026-11-19; tagged in the second
    # set below
    'nomocracy',
    'jurisprudence',
    'teleocracy',
    'pluralism',
    'Collingwood',
    'Bradley',
    'Hegel',
    'ethics',
    'moral philosophy',
    'political philosophy',
]

BOOK_KEYWORDS = {
    'Experience and Its Modes':
        ['idealism', 'philosophy of history', 'philosophy of science'],
    'Hobbes on Civil Association':
        ['Hobbes', 'civil association'],
    'Michael Oakeshott as a Philosopher of the "Creative" and Other Essays':
        ['poetry'],
    'Michael Oakeshott on Hobbes: A Study in the Renewal of Philosophical Ideas':
        ['Hobbes'],
    'Michael Oakeshott on Religion, Aesthetics, and Politics':
        ['religion', 'aesthetics'],
    "Michael Oakeshott's Political Philosophy of International Relations: Civil Association and International Society":
        ['civil association'],
    'Morality and Politics in Modern Europe: The Harvard Lectures':
        ['morality'],
    'Oakeshott on History':
        ['philosophy of history'],
    'Oakeshott on Rome and America':
        ['rationalism'],
    "Oakeshott's Skepticism, Politics, and Aesthetics":
        ['aesthetics'],
    'Oakeshott: le scepticisme en politique':
        ['politics of scepticism'],
    'On History and Other Essays':
        ['philosophy of history'],
    'On Human Conduct':
        ['civil association', 'enterprise association'],
    'Rationalism in Politics and Other Essays':
        ['rationalism'],
    'Rationalism in Politics and Other Essays: New and Expanded Edition':
        ['rationalism'],
    "Reason, Revolution and Political Theory: Notes on Oakeshott's 'Rationalism in Politics'":
        ['rationalism'],
    'Religion, Politics and the Moral Life':
        ['religion', 'morality'],
    'Religious and Poetic Experience in the Thought of Michael Oakeshott':
        ['religion', 'poetry', 'morality'],
    'The Enemies of Perfection: Oakeshott, Plato, and the Critique of Rationalism':
        ['rationalism'],
    "The Limits of Political Theory: Oakeshott's Philosophy of Civil Association":
        ['civil association'],
    'The Politics and Philosophy of Michael Oakeshott':
        ['morality'],
    'The Politics of Faith and the Politics of Scepticism':
        ['politics of faith', 'politics of scepticism'],
    'The Politics of Imperfection: The Religious and Secular Traditions of Conservative Thought in England from Hooker to Oakeshott':
        ['religion'],
    'The Sceptical Idealist: Michael Oakeshott as a Critic of the Enlightenment':
        ['idealism', 'rationalism'],
    "The Skeptic's Oakeshott":
        ['Hobbes'],
    'The Voice of Poetry in the Conversation of Mankind: An Essay':
        ['poetry', 'aesthetics'],
    'Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, and Others':
        ['rationalism'],
    'What is History? and Other Essays':
        ['philosophy of history'],
}

ENTRY_KEYWORDS = {
    ('', 'Science, Religion and Reality', 1926, 'Journal of Theological Studies'):
        ['religion', 'philosophy of science'],
    ('', 'The Christian Religion and Its Competitors Today', 1926, 'Journal of Theological Studies'):
        ['religion'],
    ('', 'Modernism in the Church of England', 1927, 'Journal of Theological Studies'):
        ['religion'],
    ('', 'Experiences of God', 1930, 'Journal of Theological Studies'):
        ['religion'],
    ('', 'God and Man', 1930, 'Cambridge Review'):
        ['religion'],
    ('', 'The Making of the Christian Mind', 1930, 'Journal of Theological Studies'):
        ['religion'],
    ('', 'Adventures in Philosophy and Religion', 1931, 'Cambridge Review'):
        ['religion'],
    ('', 'Ethical Principles in Theory and Practice', 1931, 'Journal of Theological Studies'):
        ['morality'],
    ('', 'Religion without God', 1931, 'Journal of Theological Studies'):
        ['religion'],
    ('', 'Idealistic Logic', 1933, 'Cambridge Review'):
        ['idealism'],
    ('', 'A New Argument for God’s Survival', 1934, 'Cambridge Review'):
        ['religion'],
    ('', 'Christianity and the Nature of History', 1935, 'Cambridge Review'):
        ['religion', 'philosophy of history'],
    ('', 'Christianity and the Nature of History', 1935, 'Journal of Theological Studies'):
        ['religion', 'philosophy of history'],
    ('', 'Morals and Politics', 1935, 'Cambridge Review'):
        ['morality'],
    ('', 'Religion and History', 1935, 'Journal of Theological Studies'):
        ['religion'],
    ('', 'Right: A Study in Physical and Moral Order', 1935, 'Journal of Theological Studies'):
        ['morality'],
    ('', 'The Historical Element in Religion', 1936, 'Journal of Theological Studies'):
        ['religion'],
    ('', 'The Meaning of History', 1936, 'Cambridge Review'):
        ['philosophy of history'],
    ('', 'The Political Philosophy of Hobbes', 1936, 'Cambridge Review'):
        ['Hobbes'],
    ('', 'The Political Philosophy of Hobbes', 1937, 'Philosophy'):
        ['Hobbes'],
    ('Dr. Leo Strauss on Hobbes', '', 1937, 'Politica'):
        ['Hobbes'],
    ('', 'The Principles of Art', 1938, 'Cambridge Review'):
        ['aesthetics'],
    ('', 'Politics and Morals', 1946, 'Philosophy'):
        ['morality'],
    ('Introduction to Leviathan', '', 1946, 'in: Leviathan, or the Matter, Forme and Power of a Commonwealth Ecclesiasticall and Civil'):
        ['Hobbes'],
    ('Leviathan, or the Matter, Forme and Power of a Commonwealth Ecclesiasticall and Civil', '', 1946, 'Basil Blackwell'):
        ['Hobbes'],
    ('', 'The Idea of History', 1947, 'English Historical Review'):
        ['philosophy of history'],
    ('The "Collective Dream of Civilisation"', '', 1947, 'Listener'):
        ['Hobbes'],
    ('', 'Why We Read History', 1948, 'Cambridge Journal'):
        ['philosophy of history'],
    ('', 'Socialism and Ethics', 1949, 'Cambridge Journal'):
        ['morality'],
    ('', 'The Life of Reason: Hobbes, Locke, Bolingbroke', 1949, 'Times Literary Supplement'):
        ['Hobbes'],
    ('', 'Beyond Realism and Idealism', 1950, 'Times Literary Supplement'):
        ['idealism'],
    ('', 'History, Its Purpose and Method', 1951, 'Philosophical Quarterly'):
        ['philosophy of history'],
    ('', 'Hobbes and His Critics', 1951, 'Time and Tide'):
        ['Hobbes'],
    ('', 'The City of God', 1951, 'Cambridge Journal'):
        ['religion'],
    ('', 'An Introduction to Philosophy of History', 1952, 'Philosophical Quarterly'):
        ['philosophy of history'],
    ('', 'The Ethics of Redistribution', 1952, 'Clare Market Review'):
        ['morality'],
    ('', 'The Liberal Anglican Idea of History', 1953, 'Cambridge Journal'):
        ['philosophy of history'],
    ("A Note on Professor Oakeshott's Introduction to the Leviathan", '', 1953, 'Political Studies'):
        ['Hobbes'],
    ('', 'The Political Philosophy of Thomas Hobbes', 1957, 'Spectator'):
        ['Hobbes'],
    ('The Moral Life in the Writings of Thomas Hobbes', '', 1962, 'in: Rationalism in Politics and Other Essays'):
        ['morality', 'Hobbes'],
    ('Professor Oakeshott on History as a Mode of Experience', '', 1966, 'Australasian Journal of Philosophy'):
        ['philosophy of history'],
    ('', 'Hobbes Studies', 1967, 'English Historical Review'):
        ['Hobbes'],
    ("Michael Oakeshott's Theory of History", '', 1968, 'in: Politics and Experience: Essays Presented to Professor Michael Oakeshott on the Occasion of His Retirement'):
        ['philosophy of history'],
    ('', 'The Aims of History', 1971, 'English Historical Review'):
        ['philosophy of history'],
    ('Michael Oakeshott Against Scientism in Politics', '', 1972, 'Modern Review (Calcutta)'):
        ['rationalism'],
    ('Logos and Telos', 'The Politics of Motion: The World of Thomas Hobbes', 1974, 'Government and Opposition'):
        ['Hobbes'],
    ('Poetry and the Voice of Michael Oakeshott', '', 1975, 'British Journal of Aesthetics'):
        ['poetry'],
    ('A Rationalist Malgré Lui: The Perplexities of Being Michael Oakeshott', '', 1976, 'Political Theory'):
        ['rationalism'],
    ('Michael Oakeshott and Historical Particularism', '', 1981, 'Politics'):
        ['philosophy of history'],
    ("Oakeshott's Conception of Civil Association: Notes for a Critical Analysis", '', 1981, 'Political Studies'):
        ['civil association', 'enterprise association'],
    ('Conservative Thinkers: Michael Oakeshott: The Poet of Practice', '', 1983, 'Salisbury Review'):
        ['poetry'],
    ("The Creation of the Past: British Idealism and Michael Oakeshott's Philosophy of History", '', 1984, 'History and Theory'):
        ['idealism', 'philosophy of history'],
    ('Michael Oakeshott as Liberal Theorist', '', 1985, 'Canadian Journal of Political Science'):
        ['civil association'],
    ("The Legend of Oakeshott's Conservatism: Sceptical Philosophy and Limited Politics", '', 1985, 'Canadian Journal of Political Science'):
        ['politics of scepticism'],
    ('Authority and the Individual in Civil Association: Oakeshott, Flathman and Yves Simon', '', 1987, 'in: Authority Revisited'):
        ['civil association'],
    ('Science and the Voice of Michael Oakeshott', '', 1987, 'Rostrum: A Journal of Education and the Arts'):
        ['philosophy of science'],
    ('Oakeshott on Law, Liberty and Civil Association', '', 1988, 'The World and I'):
        ['civil association'],
    ('Learning to be Virtuous and Learning to Converse: The Treatment of the Theme of Moral Education in the Writings of Michael Oakeshott', '', 1989, 'Oideas'):
        ['morality'],
    ("Michael Oakeshott's Critique of Rationalism in Politics", '', 1989, 'in: The Activity of Politics and Related Essays'):
        ['rationalism'],
    ('Oakeshott on the Authority of Law', '', 1989, 'Ratio Juris'):
        ['civil association', 'enterprise association'],
    ("Oakeshott's Hobbesian Myth: Pride, Character and the Limits of Reason", '', 1990, 'Western Political Quarterly'):
        ['Hobbes'],
    ('The Political Philosophy of Michael Oakeshott', '', 1990, 'Yale University Press'):
        ['civil association'],
    ('Criticism and Tradition in Popper, Oakeshott and Hayek', '', 1992, 'Journal of Applied Philosophy'):
        ['rationalism'],
    ("Oakeshott's Critique of Rationalism Revisited", '', 1992, 'Political Science Reviewer'):
        ['rationalism'],
    ("Proud Men / Just Men: An Analysis of Michael Oakeshott's Account of Hobbesian Morality", '', 1992, 'Hobbes Studies'):
        ['morality', 'Hobbes'],
    ('Human Conduct, History, and Social Science in the Works of R. G. Collingwood and Michael Oakeshott', '', 1993, 'New Literary History'):
        ['philosophy of history'],
    ('Adventures of Self-Understanding: Gadamer, Oakeshott and the Question of Education', '', 1996, 'Journal of the British Society for Phenomenology'):
        ['rationalism'],
    ('Michael Oakeshott on History, Practice and Political Theory', '', 1996, 'History of Political Thought'):
        ['philosophy of history'],
    ('Michael Oakeshott: Rationalism in Politics', '', 1996, 'in: The Political Classics: Green to Dworkin'):
        ['rationalism'],
    ("Oakeshott's Claims of Politics", '', 1997, 'Political Studies'):
        ['civil association'],
    ('The Life of Hobbes in the Writings of Michael Oakeshott', '', 1997, 'History of Political Thought'):
        ['Hobbes'],
    ('Art, History and Science: The Contrasting Worlds of Collingwood and Oakeshott', '', 1998, 'Collingwood Studies'):
        ['aesthetics', 'philosophy of science', 'philosophy of history'],
    ('A Democratic Oakeshott?', '', 1999, 'Political Research Quarterly'):
        ['civil association', 'enterprise association'],
    ('Michael Oakeshott: Rationalism and Civil Association', '', 1999, 'in: Political Philosophers of the Twentieth Century'):
        ['rationalism', 'civil association'],
    ('Michael Oakeshott and the City of God', '', 2000, 'Political Theory'):
        ['religion'],
    ("A Preface to an Unpublished MS by Michael Oakeshott on Hobbes's Leviathan", '', 2001, 'Political Theory'):
        ['Hobbes'],
    ("Oakeshott's Hobbes and the Fear of Political Rationalism", '', 2001, 'Political Theory'):
        ['rationalism', 'Hobbes'],
    ('The Idealism of Michael Oakeshott', '', 2001, 'Collingwood and British Idealism Studies'):
        ['idealism'],
    ('The University Programme: Arts Philosophy of History', '', 2001, 'Collingwood and British Idealism Studies'):
        ['philosophy of history'],
    ('Leviathan as Myth: Michael Oakeshott and Carl Schmitt on Hobbes and the Critique of Rationalism', '', 2002, 'Contemporary Political Theory'):
        ['rationalism', 'politics of faith', 'politics of scepticism', 'Hobbes'],
    ("The Voice of Poetry in Oakeshott's Moral Philosophy", '', 2002, 'Review of Politics'):
        ['poetry', 'aesthetics', 'morality'],
    ('The Voice of Poetry in the Thought of Michael Oakeshott', '', 2002, 'Journal of the History of Ideas'):
        ['poetry', 'aesthetics'],
    ('The Shapes of Liberal Thought: Oakeshott, Berlin, and Liberalism', '', 2003, 'Political Theory'):
        ['rationalism'],
    ("Michael Oakeshott as a Critic of Hobbes's Theory of the Will", '', 2004, 'Rivista di Storia Della Filosofia'):
        ['Hobbes'],
    ('Michael Oakeshott on Civility, Civil Society and Civil Association', '', 2004, 'Political Studies'):
        ['civil association', 'enterprise association'],
    ('Michael Oakeshott: Rationalism and Self-Serving in Politics', '', 2004, 'Contemporary Review'):
        ['rationalism'],
    ('The Scientific Positivism of Michael Oakeshott', '', 2004, 'British Journal for the History of Philosophy'):
        ['philosophy of science'],
    ("A Qualified Defence of Oakeshott's Politics of Scepticism", '', 2005, 'European Journal of Political Theory'):
        ['politics of faith', 'politics of scepticism'],
    ("Contingency and Judgement in Oakeshott's Political Thought", '', 2005, 'European Journal of Political Theory'):
        ['rationalism'],
    ('How Oakeshott Became an Oakeshottean', '', 2005, 'European Journal of Political Theory'):
        ['idealism', 'civil association'],
    ('Michael Oakeshott and the Poetic Character of Human Activity', '', 2005, 'in: The Intellectual Legacy of Michael Oakeshott'):
        ['poetry'],
    ('Oakeshott and the Nature and Place of Aesthetic Experience: A Critique', '', 2005, 'in: The Intellectual Legacy of Michael Oakeshott'):
        ['aesthetics'],
    ('Oakeshott: Rationalism Revisited', '', 2005, 'in: The Intellectual Legacy of Michael Oakeshott'):
        ['rationalism'],
    ('Poetic Experience and the Good Life in the Writings of Michael Oakeshott', '', 2005, 'European Journal of Political Theory'):
        ['poetry', 'morality'],
    ('Political Theory and the Conduct of Faith: Oakeshott on Religion in Public Life', '', 2005, 'Contemporary Political Theory'):
        ['religion'],
    ('Collingwood, Oakeshott and Webb on the “Historical Element” in Religion', '', 2007, 'Collingwood and British Idealism Studies'):
        ['religion'],
    ('Ethics and the Conduct of Life in the old Georg Simmel and the young Michael Oakeshott', '', 2007, 'Simmel Studies'):
        ['morality'],
    ('Intimations Pursued: The Voice of Practice in the Conversation of Michael Oakeshott', '', 2007, 'Imprint Academic'):
        ['civil association', 'poetry'],
    ("Michael Oakeshott's Critique of Rationalism in Politics as Basis for His Theory of Civil Association", '', 2008, 'Synthesis Philosophica'):
        ['rationalism', 'civil association'],
    ("The Lion and the Ox: Oakeshott's Engagement with Leo Strauss on Hobbes", '', 2008, 'History of Political Thought'):
        ['Hobbes'],
    ('Oakeshott on Science as a Mode of Experience', '', 2009, 'Zygon: Journal of Religion & Science'):
        ['philosophy of science'],
    ('Oakeshott on the Character of Religious Experience: Need There Be a Conflict Between Science and Religion?', '', 2009, 'Zygon: Journal of Religion & Science'):
        ['religion', 'philosophy of science'],
    ('Oakeshottian Modes at the Crossroads of the Evolution Debates', '', 2009, 'Zygon: Journal of Religion & Science'):
        ['religion', 'philosophy of science'],
    ('Reflecting on Michael Oakeshott: Introduction to the Symposium', '', 2009, 'Zygon: Journal of Religion & Science'):
        ['religion', 'philosophy of science'],
    ('Religion and the Mode of Practice in Michael Oakeshott', '', 2009, 'Zygon: Journal of Religion & Science'):
        ['religion'],
    ("'What's Gone and What's Past Help…': Oakeshott and Strauss on Historical Explanation", '', 2010, 'Journal of the Philosophy of History'):
        ['philosophy of history'],
    ('Hayek and Oakeshott: Situating the Mind', '', 2012, 'in: A Companion to Michael Oakeshott'):
        ['rationalism'],
    ("Homo Ludens and Civil Association: The Sublime Nature of Michael Oakeshott's Civil Condition", '', 2014, 'Cosmos + Taxis'):
        ['civil association', 'enterprise association'],
    ("Jane Jacobs' Critique of Rationalism in Urban Planning", '', 2014, 'Cosmos + Taxis'):
        ['rationalism'],
    ('Oakeshott and the Complex Ecology of the Moral Life', '', 2014, 'Cosmos + Taxis'):
        ['morality'],
    ('Oakeshott on Modernity and the Crisis of Political Legitimacy in Contemporary Western Liberal Democracy', '', 2014, 'Cosmos + Taxis'):
        ['civil association'],
    ('The Critique of Rationalism and the Defense of Individuality: Oakeshott and Hayek', '', 2014, 'Cosmos + Taxis'):
        ['rationalism'],
    ("The Instrumental Idiom in American Politics: The 'City on the Hill' as a Spontaneous Order", '', 2014, 'Cosmos + Taxis'):
        ['civil association'],
    ('Michael Oakeshott and John Grote: On the Nature of Self-Realization and Idealist Philosophy', '', 2016, 'Collingwood and British Idealism Studies'):
        ['idealism'],
    ("Rationalism in Law: Constitutional Originalism and the 'Sovereignty of Technique'", '', 2016, 'Collingwood and British Idealism Studies'):
        ['rationalism'],
    ('The Critique of Rationalism: Ryle and Oakeshott on Tacit Knowledge', '', 2018, 'in: Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, and Others'):
        ['rationalism'],
    ('Michael Oakeshott on Authority, Governance, and the State', '', 2019, 'Palgrave Macmillan'):
        ['civil association'],
    ('Critics of Enlightenment Rationalism', '', 2020, 'Palgrave Macmillan'):
        ['rationalism'],
    ("Michael Oakeshott's Critique of Modern Rationalism", '', 2020, 'in: Critics of Enlightenment Rationalism'):
        ['rationalism'],
    ('Apologia for Poetry and the Art of Conversation', '', 2022, 'Cosmos + Taxis'):
        ['poetry', 'aesthetics'],
    ('Interview with Robert Grant', '', 2022, 'Cosmos + Taxis'):
        ['rationalism'],
    ('Living in the Past: Oakeshott and Strauss on Historical Knowing', '', 2022, 'Cosmos + Taxis'):
        ['philosophy of history'],
    ('Michael Oakeshott and Leo Strauss on the Individual, Christianity, and Creativity in Thought and Action', '', 2022, 'Cosmos + Taxis'):
        ['religion'],
    ('Michael Oakeshott on Libertarianism, Conservatism, and the Freedom of the English', '', 2022, 'Cosmos + Taxis'):
        ['rationalism'],
    ('Michael Oakeshott: 21st Century Radical?', '', 2022, 'Cosmos + Taxis'):
        ['rationalism'],
    ('Oakeshott-22', '', 2022, 'Cosmos + Taxis'):
        ['rationalism'],
    ('Paradoxes of the Modern Moral Imagination: Reflections on Contemplation and Action', '', 2022, 'Cosmos + Taxis'):
        ['morality'],
    ("Political Philosophy versus Poetic Individuality: A Response to David McIlwain's Michael Oakeshott and Leo Strauss: The Politics of Renaissance and Enlightenment", '', 2022, 'Cosmos + Taxis'):
        ['poetry'],
    ('Rationalism in Ideal Theory: Michael Oakeshott on John Rawls', '', 2022, 'Cosmos + Taxis'):
        ['rationalism'],
    ('Reason and Unreason in Politics', '', 2022, 'Cosmos + Taxis'):
        ['rationalism'],
    ("An Oakeshottian Analysis of Stephen Wolfe's Christian Nationalism: Civil Associations vs. The Complete Good", '', 2025, 'Cosmos + Taxis'):
        ['civil association', 'enterprise association'],
}


# THE SECOND SET (2026-11-20)

BOOK_KEYWORDS_2 = {
    'The Concept of a Philosophical Jurisprudence: Essays and Reviews 1926–51':
        ['jurisprudence'],
    'On History and Other Essays':
        ['jurisprudence'],
    'The Defence of Natural Law: A Study of the Ideas of Law and Justice in the Writings of Lon L. Fuller, Michael Oakeshott, F. A. Hayek, Ronald Dworkin and John Finnis':
        ['jurisprudence'],
    'Michael Oakeshott':
        ['pluralism'],
    'In Defence of Modernity: Vision and Philosophy in Michael Oakeshott':
        ['pluralism'],
    'On World Politics: R. G. Collingwood, Michael Oakeshott and Neotraditionalism in International Relations':
        ['Collingwood'],
    'Experience and Its Modes':
        ['Bradley', 'Hegel'],
    'The Politics and Philosophy of Michael Oakeshott':
        ['Bradley'],
    'Oakeshott and His Contemporaries: Montaigne, St. Augustine, Hegel, et al.':
        ['Hegel'],
    'Religion, Politics and the Moral Life':
        ['moral philosophy', 'political philosophy'],
    'Religious and Poetic Experience in the Thought of Michael Oakeshott':
        ['moral philosophy'],
    'Morality and Politics in Modern Europe: The Harvard Lectures':
        ['moral philosophy'],
    'The Political Philosophy of Michael Oakeshott':
        ['political philosophy'],
    "The Limits of Political Theory: Oakeshott's Philosophy of Civil Association":
        ['political philosophy'],
    "The Skeptic's Oakeshott":
        ['political philosophy'],
    'Michael Oakeshott and Liberalism Revisited':
        ['political philosophy'],
    "Michael Oakeshott's Political Philosophy of International Relations: Civil Association and International Society":
        ['political philosophy'],
    'Political Education: An Inaugural Lecture':
        ['political philosophy'],
    'Lectures in the History of Political Thought':
        ['political philosophy'],
    'Early Political Writings 1925–30: A Discussion of Some Matters Preliminary to the Study of Political Philosophy':
        ['political philosophy'],
}

ENTRY_KEYWORDS_2 = {
    ('Law, Legislation and Liberty', '', 1973, 'Routledge and Kegan Paul'):
        ['nomocracy', 'teleocracy', 'jurisprudence'],
    ('', 'Natural Law and the Theory of Society, 1500 to 1800 (trans. E. Barker)', 1934, 'Cambridge Review'):
        ['jurisprudence'],
    ('Legal Intimations: Michael Oakeshott and the Rule of Law', '', 1993, 'Wisconsin Law Journal'):
        ['jurisprudence'],
    ('Michael Oakeshott and the Elusive Identity of the Rule of Law', '', 2005, 'in: The Intellectual Legacy of Michael Oakeshott'):
        ['jurisprudence'],
    ('Oakeshott on Law, Liberty and Civil Association', '', 1988, 'The World and I'):
        ['jurisprudence'],
    ('Oakeshott on the Authority of Law', '', 1989, 'Ratio Juris'):
        ['jurisprudence'],
    ('Oakeshott on the Rule of Law: A Defense', '', 2014, 'Cosmos + Taxis'):
        ['jurisprudence'],
    ('The Rule of Law in the Modern European State: Oakeshott and the Enlargement of Europe', '', 2005, 'European Journal of Political Theory'):
        ['jurisprudence'],
    ('What Is a Non-Instrumental Law?', '', 1992, 'Political Science Reviewer'):
        ['jurisprudence'],
    ('Law and Contingency: Michael Oakeshott and The German Historical School', '', 2016, 'Collingwood and British Idealism Studies'):
        ['jurisprudence'],
    ("Rationalism in Law: Constitutional Originalism and the 'Sovereignty of Technique'", '', 2016, 'Collingwood and British Idealism Studies'):
        ['jurisprudence'],
    ('Law, Morality, and the Relations of States', '', 1983, 'Princeton University Press'):
        ['jurisprudence'],
    ('The Anglo-American Conception of the Rule of Law', '', 2019, 'Palgrave Macmillan'):
        ['jurisprudence'],
    ('Pluralism in the Thought of Oakeshott, Shils and Weber', '', 2002, 'Journal of Classical Sociology'):
        ['pluralism'],
    ('Dimensions of Radical Democracy: Pluralism, Citizenship, Community', '', 1992, 'Verso'):
        ['pluralism'],
    ('How Oakeshott Became an Oakeshottean', '', 2005, 'European Journal of Political Theory'):
        ['pluralism'],
    ('The Shapes of Liberal Thought: Oakeshott, Berlin, and Liberalism', '', 2003, 'Political Theory'):
        ['pluralism'],
    ('Art, History and Science: The Contrasting Worlds of Collingwood and Oakeshott', '', 1998, 'Collingwood Studies'):
        ['Collingwood'],
    ('Collingwood, Oakeshott and Webb on the “Historical Element” in Religion', '', 2007, 'Collingwood and British Idealism Studies'):
        ['Collingwood'],
    ('Collingwood, Oakeshott, and the Social Contract', '', 1996, 'Collingwood Studies'):
        ['Collingwood'],
    ('Human Conduct, History, and Social Science in the Works of R. G. Collingwood and Michael Oakeshott', '', 1993, 'New Literary History'):
        ['Collingwood'],
    ('Overlap and Autonomy: The Different Worlds of Collingwood and Oakeshott', '', 1989, 'Storia Antropologia e Scienza del Linguaggio'):
        ['Collingwood'],
    ('The English Idea of History from Coleridge to Collingwood', '', 2000, 'Ashgate'):
        ['Collingwood'],
    ('The Idea of History', '', 1946, 'Clarendon Press'):
        ['Collingwood'],
    ('', '', 1933, 'Cambridge Review'):
        ['Collingwood'],
    ('Apologia for Poetry and the Art of Conversation', '', 2022, 'Cosmos + Taxis'):
        ['Collingwood'],
    ('Scepticism and Historical Knowledge', '', 1965, 'Random House'):
        ['Collingwood'],
    ('', 'The Political Philosophies of Plato and Hegel', 1935, 'Cambridge Review'):
        ['Hegel', 'political philosophy'],
    ('', 'Critique of Hegel’s Philosophy of Right (ed. J. O’Malley)', 1971, 'Spectator'):
        ['Hegel'],
    ('', 'Hegel’s Theory of the Modern State', 1975, 'European Studies Review'):
        ['Hegel'],
    ("Oakeshott's Relationship to Hegel", '', 2005, 'in: The Intellectual Legacy of Michael Oakeshott'):
        ['Hegel'],
    ('', 'Ethical Principles in Theory and Practice', 1931, 'Journal of Theological Studies'):
        ['ethics'],
    ('', 'Socialism and Ethics', 1949, 'Cambridge Journal'):
        ['ethics'],
    ('', 'The Ethics of Redistribution', 1952, 'Clare Market Review'):
        ['ethics'],
    ('Ethics and the Conduct of Life in the old Georg Simmel and the young Michael Oakeshott', '', 2007, 'Simmel Studies'):
        ['ethics'],
    ('The Moral Life in the Writings of Thomas Hobbes', '', 1962, 'in: Rationalism in Politics and Other Essays'):
        ['moral philosophy'],
    ("The Voice of Poetry in Oakeshott's Moral Philosophy", '', 2002, 'Review of Politics'):
        ['moral philosophy'],
    ('Oakeshott and the Complex Ecology of the Moral Life', '', 2014, 'Cosmos + Taxis'):
        ['moral philosophy'],
    ("Proud Men / Just Men: An Analysis of Michael Oakeshott's Account of Hobbesian Morality", '', 1992, 'Hobbes Studies'):
        ['moral philosophy'],
    ('The Minefields of Moral Philosophy', '', 1976, 'Encounter'):
        ['moral philosophy'],
    ('Poetic Experience and the Good Life in the Writings of Michael Oakeshott', '', 2005, 'European Journal of Political Theory'):
        ['moral philosophy'],
    ('Habit and Discovery: The Political Philosophy of Michael Oakeshott', '', 1977, 'Political Science Reviewer'):
        ['political philosophy'],
    ('Michael Oakeshott as a Political Philosopher', '', 1975, 'Indian Journal of Political Science'):
        ['political philosophy'],
    ('Michael Oakeshott, Political Philosopher', '', 1991, 'Cambridge Review'):
        ['political philosophy'],
    ('Review Article: The Political Philosophy of Michael Oakeshott', '', 1979, 'British Journal of Political Science'):
        ['political philosophy'],
    ("The Dilemma of Michael Oakeshott: Oakeshott's Treatment of Equality of Opportunity in Education and His Political Philosophy", '', 1989, 'Journal of Philosophy of Education'):
        ['political philosophy'],
    ("Political Philosophy versus Poetic Individuality: A Response to David McIlwain's Michael Oakeshott and Leo Strauss: The Politics of Renaissance and Enlightenment", '', 2022, 'Cosmos + Taxis'):
        ['political philosophy'],
    ("Contingency and Judgement in Oakeshott's Political Thought", '', 2005, 'European Journal of Political Theory'):
        ['political philosophy'],
    ("What Can We Learn from Michael Oakeshott's Effort to Understand Our World?", '', 2020, 'Cosmos + Taxis'):
        ['political philosophy'],
    ('Rationalism in Ideal Theory: Michael Oakeshott on John Rawls', '', 2022, 'Cosmos + Taxis'):
        ['political philosophy'],
    ("Liberalism and the Prospect of Rational Order in Hobbes's Political Philosophy and the Responses of Oakeshott, Strauss and Voegelin", '', 2018, 'in: Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, and Others'):
        ['political philosophy'],
    ('', 'The Political Philosophy of Hobbes', 1936, 'Cambridge Review'):
        ['political philosophy'],
    ('', 'The Political Philosophy of Hobbes', 1937, 'Philosophy'):
        ['political philosophy'],
    ('', 'The Political Philosophy of Thomas Hobbes', 1957, 'Spectator'):
        ['political philosophy'],
    ('', 'John Locke’s Political Philosophy', 1950, 'English Historical Review'):
        ['political philosophy'],
    ('Conceptions of Liberty in Political Philosophy', '', 1984, 'Athlone Press'):
        ['political philosophy'],
    ('Contemporary Political Philosophers', '', 1976, 'Methuen'):
        ['political philosophy'],
    ('Political Philosophers of the Twentieth Century', '', 1999, 'Blackwell'):
        ['political philosophy'],
}

# Possible tags, for the editors to decide: (question title) ->
# (details, entries as BOOK_KEYWORDS titles or ENTRY_KEYWORDS keys)
POSSIBLE = {
    "Keywords: tag these 'nomocracy' and 'teleocracy'?": (
        "Hayek took the terms from Oakeshott's LSE lectures, which may be "
        "these (not checked); 'Michael Oakeshott Goes Fishing' lists the "
        "pair among his distinctions.",
        ['Lectures in the History of Political Thought',
         ('Michael Oakeshott Goes Fishing', '', 2025, 'Cosmos + Taxis')]),
    "Keywords: tag these 'pluralism'?": (
        "One is on plurality in liberal education; the other reads his "
        "1930s writings as defending a pluralist order.",
        [('The Meaning of Plurality in Liberal Education', '', 2025,
          'Cosmos + Taxis'),
         ("Oakeshott's Politics for Gentlemen", '', 2007,
          'Review of Politics')]),
    "Keywords: tag these 'Collingwood'?": (
        "Each sets Oakeshott beside Collingwood in part: Dray presents "
        "both as idealist philosophers of history; Boucher notes "
        "Collingwood's praise; Jackson compares their accounts of "
        "conduct.",
        [('Philosophy of History', '', 1964, 'Prentice-Hall'),
         ("The Creation of the Past: British Idealism and Michael "
          "Oakeshott's Philosophy of History", '', 1984,
          'History and Theory'),
         ('The Global Covenant: Human Conduct in a World of States', '',
          2000, 'Oxford University Press')]),
    "Keywords: tag these 'Hegel'?": (
        "Franco places Oakeshott in a liberal line from Hobbes through "
        "Hegel; the 2025 essay says he used parts of Hegel. Tagging "
        "Franco's book would tag its 14 reviews too.",
        ['The Political Philosophy of Michael Oakeshott',
         ('Oakeshott Turned Conservatism into a Creed of Liberty', '', 2025,
          'Cosmos + Taxis')]),
    "Keywords: tag these 'moral philosophy'?": (
        "On Human Conduct sets out his theory of moral conduct, but "
        "tagging it would tag its 38 reviews too; Nardin's book is on "
        "law and morality among states.",
        ['On Human Conduct',
         ('Law, Morality, and the Relations of States', '', 1983,
          'Princeton University Press')]),
}
