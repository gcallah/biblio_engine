"""Abstracts for Voegelin entries, used by load_abstracts_voegelin.

Keyed by (title, year, where): "where" is the journal name, "in: <book
title>" for a chapter, or the publisher name for a book. Each abstract
paraphrases the source at its URL: "basis" says whether that is the
publisher's description or abstract, a catalogue note, the volume's
introduction, or the piece's own open text. Keep them under 1024
characters.
"""

ABSTRACTS = {
    ('Rasse und Staat', 1933, 'J. C. B. Mohr (Paul Siebeck)'): dict(
        source='https://cdn.mohrsiebeck.com/8a,20554b2fb94e8d9fa4bb7aef72f022.pdf',
        basis='volume introduction',
        abstract=(
            "Voegelin's introduction explains that the book grew out of his "
            'work on a system of political theory (Staatslehre). In that '
            'system the ideas of the body (Leibideen) were to be treated, '
            'among the ideas of the state, as co-creators of political '
            'communities. Because the subject needed fuller treatment, he '
            'lifted out its most important modern case, the idea of race. His '
            'starting thesis is that the roots of the state lie in human '
            'nature, so political theory must rest on philosophical '
            'anthropology. Against the German theory of the state since 1871, '
            'and Kelsen above all, he argues that reducing it to the study of '
            'legal norms leaves out the ideas of the state. The book has two '
            "parts. The first examines race theory's claim to be a science, "
            'through the relation of body, soul and spirit, and criticises '
            'the dogmas of nineteenth-century scientism. The second traces '
            'the idea of race as a political idea that builds community.'
        )),
    ('The New Science of Politics: An Introduction', 1952, 'University of Chicago Press'): dict(
        source='https://press.uchicago.edu/ucp/books/book/chicago/N/bo3622811.html',
        basis='publisher description',
        abstract=(
            "Voegelin's Walgreen Foundation lectures, in which he sets out a "
            'theory of humanity, society and history. Drawing on material '
            'from many periods, including the Mongol Orders of Submission, '
            'the Behistun Inscription and a controversy over an altar to the '
            'goddess Victoria in the Roman Forum, he examines the access to '
            'truth offered by myth, revelation and philosophy and contrasts '
            'each with gnosticism. The chapters treat representation and '
            'existence, representation and truth, the struggle for '
            'representation in the Roman Empire, gnosticism as the nature of '
            'modernity, the Puritan case as a gnostic revolution, and the end '
            'of modernity, tracing European political development within the '
            'Western tradition and the place of the inner search for '
            'transcendent reality.'
        )),
    ('Plato', 1966, 'Louisiana State University Press'): dict(
        source='https://books.google.com/books?id=uGfxAQAACAAJ',
        basis='publisher description',
        abstract=(
            'A separate edition of the first part of Plato and Aristotle, the '
            'third volume of Order and History, in which Voegelin completes '
            'his study of Greek culture from its pre-Hellenic origins to the '
            "time of Athenian dominance. Through an analysis of Plato's "
            'vision of soul, polis and cosmos, Voegelin shows how the symbols '
            'of the older myth were superseded by the more differentiated '
            'symbols of philosophy. He makes this the basis of a conception '
            "of history in which societies' imperfect attempts to symbolize "
            'the truth of the order of being form an intelligible sequence of '
            'advances and recessions, so that history gains unity in a common '
            'effort toward meaning and order rather than having an evident '
            'meaning of its own.'
        )),
    ('Science, Politics and Gnosticism: Two Essays', 1968, 'Henry Regnery Company'): dict(
        source='https://books.google.com/books?id=RIvmAgAAQBAJ',
        basis='publisher description',
        abstract=(
            'Two essays in which Voegelin argues that several modern '
            'movements, among them positivism, Hegelianism, Marxism and the '
            '"God is dead" movement, are variants of the ancient gnostic '
            'tradition he had identified in The New Science of Politics. He '
            'seeks to clear up the intellectual confusion that he attributes '
            'to the dominance of gnostic thinking by drawing a clear '
            'distinction between political gnosticism and the philosophy of '
            'politics.'
        )),
    ('Anamnesis', 1978, 'University of Notre Dame Press'): dict(
        source='https://upress.missouri.edu/9780826207371/anamnesis/',
        basis='publisher description',
        abstract=(
            "English translation, first published in 1978, of Voegelin's "
            'Anamnesis, which appeared in German in 1966. Rather than '
            'rendering the whole German book, the translated edition gathers '
            'the materials that bear most directly on the development of '
            "Voegelin's philosophy of consciousness. It also adds his essay "
            '"Reason: The Classic Experience" and a new opening chapter that '
            'Voegelin wrote specially for this translation.'
        )),
    ('Political Religions', 1986, 'Edwin Mellen Press'): dict(
        source='https://edwinmellen.com/book/ES-Easterly-III/1736/',
        basis='publisher description',
        abstract=(
            "An English translation of Voegelin's Die politischen Religionen, "
            'prepared by E. S. Easterly III and T. J. DiNapoli. The volume '
            "opens with a translator's preface that recounts the history of "
            'the text, followed by an introduction offering a short '
            'intellectual biography of the young Voegelin. The English text '
            'of the translation is cross-referenced throughout to the '
            'original German.'
        )),
    ('Published Essays, 1966–1985 (The Collected Works of Eric Voegelin, Volume 12)', 1990, 'Louisiana State University Press'): dict(
        source='https://upress.missouri.edu/9780807115954/published-essays-1966-1985-cw12/',
        basis='publisher description',
        abstract=(
            "Essays from the last two decades of Voegelin's life, written "
            'alongside Anamnesis and the fourth and fifth volumes of Order '
            'and History. They range from a critique of the German '
            'universities during the Hitler period and a satire on '
            'contemporary culture to studies of immortality, reason and '
            'consciousness. The collection also contains his elaboration of '
            'the theory of equivalent experiences and symbols across history '
            'and his reflection on the "lure of extremes" in modern revolts '
            'of magic against reason, and ends with a meditation on God '
            'written shortly before his death. Throughout runs his view that '
            'the philosophical life is ordered as faith seeking '
            'understanding, a search for the divine ground indebted to Plato, '
            'Anselm, Bodin and Bergson.'
        )),
    ('What Is History? And Other Late Unpublished Writings (The Collected Works of Eric Voegelin, Volume 28)', 1990, 'Louisiana State University Press'): dict(
        source='https://upress.missouri.edu/9780807116036/what-is-history-and-other-late-unpublished-writings-cw28/',
        basis='publisher description',
        abstract=(
            'Five previously unpublished texts written between the early '
            '1960s and the late 1970s, after the first three volumes of Order '
            'and History: "What Is History?", on a transcendent structure of '
            'history without a universal meaning; "Anxiety and Reason," on '
            'his theory of historiogenesis; "The Eclipse of Reality," a '
            'critique of modernity through Sartre, Schiller, Comte and '
            'others; "The Moving Soul," a thought experiment on physics and '
            'myth prompted by Henry Margenau; and "The Beginning and the '
            'Beyond," a meditation on the experience of existence under God. '
            'The editors, Thomas A. Hollweck and Paul Caringella, introduce '
            'the texts and show what they reveal about the changing '
            'conception of his main work.'
        )),
    ('The Nature of the Law and Related Legal Writings (The Collected Works of Eric Voegelin, Volume 27)', 1991, 'Louisiana State University Press'): dict(
        source='https://upress.missouri.edu/9780807116739/nature-of-the-law-and-related-legal-writings-cw27/',
        basis='publisher description',
        abstract=(
            "Voegelin's writings on law, centred on the previously "
            'unpublished The Nature of the Law, completed in 1957 while he '
            'taught jurisprudence at the Louisiana State University law '
            'school. In it he argues that law is not a discrete entity, '
            'neither the command of a sovereign nor a social compact nor the '
            'will of a majority, but the structure of a society: part of the '
            'order a society discovers and specifies for itself in pursuit of '
            'the common good. The volume also contains the detailed outline '
            'of his LSU jurisprudence course (1954-1957), concerned with the '
            'criteria of legal order, the supplementary notes he prepared for '
            'it, and four reviews from 1941 and 1942 of books on legal '
            'science and legal philosophy.'
        )),
    ('Briefwechsel über „Die Neue Wissenschaft der Politik“', 1993, 'Karl Alber'): dict(
        source='https://doi.org/10.5771/9783495993927',
        basis='publisher abstract',
        abstract=(
            "This book is about another book: Voegelin's The New Science of "
            'Politics, published in the United States in 1952 and reissued in '
            'German by Alber in 1991 as Die Neue Wissenschaft der Politik. '
            'That work offered an interpretation of modernity. It also '
            'challenged the positivist conception of science that dominated '
            'the social sciences, and it tried to renew the rational '
            'foundations of political philosophy. Even before it appeared, '
            'the New Science was the subject of extensive correspondence '
            'between Voegelin and friends among his fellow scholars, above '
            'all Alfred Schütz, Leo Strauss and Aron Gurwitsch. The volume, '
            'edited with an introduction by Peter J. Opitz, collects the most '
            'important of these letters, some previously unpublished. In them '
            'Voegelin develops central parts of his approach in more detail '
            "than in the book itself. His correspondents' questions and "
            'objections pick out its sensitive points and shed light on their '
            'own positions. Karl Alber, 1993, 158 pages.'
        )),
    ('Faith and Political Philosophy: The Correspondence between Leo Strauss and Eric Voegelin, 1934–1964', 1993, 'Pennsylvania State University Press'): dict(
        source='https://books.google.com/books?id=ZGUNAQAAMAAJ',
        basis='publisher description',
        abstract=(
            'Fifty-three letters exchanged between Leo Strauss and Eric '
            'Voegelin between 1934 and 1964, in which the two political '
            'theorists discuss their agreements and differences, comment on '
            "each other's work and on the state of their discipline, and "
            'reflect on the influences acting on them. The letters make '
            'explicit many assumptions behind their published writings. The '
            'volume also reprints four essays: Strauss\'s "Jerusalem and '
            'Athens: Some Preliminary Reflections" and "The Mutual Influence '
            'of Theology and Philosophy," and Voegelin\'s "The Gospel and '
            'Culture" and "Immortality: Experience and Symbol," with '
            'commentaries by James L. Wiser, Hans-Georg Gadamer, Stanley '
            'Rosen, Thomas J. J. Altizer, Timothy Fuller, Ellis Sandoz, '
            'Thomas L. Pangle and David Walsh.'
        )),
    ('On the Form of the American Mind (The Collected Works of Eric Voegelin, Volume 1)', 1995, 'Louisiana State University Press'): dict(
        source='https://upress.missouri.edu/9780807118269/on-the-form-of-the-american-mind-cw1/',
        basis='publisher description',
        abstract=(
            "Collected Works edition of Voegelin's first major book, "
            'published in German in 1928 after his two years in the United '
            'States (1924-1926) as a Laura Spelman Rockefeller Memorial '
            'Fellow. It opens with a discussion of time and existence in '
            'European and American philosophy, then offers an interpretation '
            'of George Santayana, a study of the Puritan Jonathan Edwards, a '
            'treatment of Anglo-American jurisprudence, and an account of '
            'John R. Commons, especially his views on democracy in modern '
            'urban and industrial America. Voegelin argues that these themes '
            'are united as linguistic expressions of a theoretical kind. A '
            'two-part introduction by Jürgen Gebhardt and Barry Cooper places '
            'the book in German methodological debates of the time and in the '
            "context of Voegelin's American experience."
        )),
    ('History of Political Ideas, Volume I: Hellenism, Rome, and Early Christianity (The Collected Works of Eric Voegelin, Volume 19)', 1997, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826211262/history-of-political-ideas-volume-1-cw19/',
        basis='publisher description',
        abstract=(
            "First volume of Voegelin's History of Political Ideas, covering "
            'the span from the decline of the Greek polis to Saint Augustine '
            'and so filling the gap between volumes 3 and 4 of Order and '
            'History. Its centre is an account of the political implications '
            'of apostolic Christianity and the work of the early church '
            'fathers, together with the political philosophy of Rome and '
            'Greek and early Roman law. Begun as a textbook for Macmillan, '
            'the History grew into an interpretation built on primary sources '
            'and specialist scholarship and remained unpublished in '
            "Voegelin's lifetime, as he turned to Order and History. Here he "
            'argues that the spiritual disintegration of the Hellenic world '
            'began a long transition in the self-understanding of '
            'Mediterranean and European man.'
        )),
    ('History of Political Ideas, Volume II: The Middle Ages to Aquinas (The Collected Works of Eric Voegelin, Volume 20)', 1997, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826211422/history-of-political-ideas-volume-2-cw20/',
        basis='publisher description',
        abstract=(
            'Second volume of the History of Political Ideas, on medieval '
            'political thought. It opens with a survey of the structure of '
            'the period and analyzes the Germanic invasions, the fall of '
            'Rome, and the rise of empire and monastic Christianity. Chapters '
            'on John of Salisbury, Joachim of Fiore, Frederick II, Siger de '
            'Brabant, Francis of Assisi and Roman law lead to a study of '
            "Thomas Aquinas's thirteenth-century synthesis. Begun as a "
            "textbook for Macmillan and left unpublished in Voegelin's "
            'lifetime, the History became the body of material from which '
            'much of his later theory grew; this volume takes a revisionist '
            'approach that looks for the experiences underlying medieval '
            'thought.'
        )),
    ('Race and State (The Collected Works of Eric Voegelin, Volume 2)', 1997, 'Louisiana State University Press'): dict(
        source='https://upress.missouri.edu/9780807118429/race-and-state-cw2/',
        basis='publisher description',
        abstract=(
            "English translation of Voegelin's Rasse und Staat, first "
            'published in Germany in 1933 and prompted partly by the rise of '
            'National Socialism. Part I analyzes contemporary race theories '
            'by setting the question of race within the larger philosophical '
            'problem of how body, mind and soul are related, exposing the '
            'theoretical fallacies of the theories and contributing to a '
            'philosophical anthropology of the human being as a many-layered '
            'whole. Part II treats race ideas, distinguished from race '
            'theories as political ideas that form part of political reality '
            'and help constitute communities. Voegelin presents the modern '
            'race idea as one "body ideal" among others, traces its rise and '
            'function, and asks why it succeeded in Germany.'
        )),
    ('History of Political Ideas, Volume III: The Later Middle Ages (The Collected Works of Eric Voegelin, Volume 21)', 1998, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826211545/history-of-political-ideas-volume-3-cw21/',
        basis='publisher description',
        abstract=(
            'Third volume of the History of Political Ideas, on the later '
            'Middle Ages. Voegelin traces the symbols that held medieval '
            'civilization together, centred on the sacrum imperium uniting '
            'spiritual and temporal, and follows the "civilizational schism" '
            'in which both its reality and the aspiration to it faded and the '
            'union of faith and reason dissolved. William of Ockham, Dante, '
            'Giles of Rome and Marsilius of Padua appear as forerunners of '
            'modern thought; the mysticism of Piers Plowman and the revolt of '
            'Cola di Rienzo are read as responses to disintegration. He also '
            'treats the rise of the constitutional tradition, the English '
            'political pattern and the German imperial zone, ending with '
            'Nicholas of Cusa.'
        )),
    ('History of Political Ideas, Volume IV: Renaissance and Reformation (The Collected Works of Eric Voegelin, Volume 22)', 1998, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826211552/history-of-political-ideas-volume-4-cw22/',
        basis='publisher description',
        abstract=(
            'Fourth volume of the History of Political Ideas, examining the '
            'Renaissance and the Reformation as two distinct beginnings of '
            'modern political consciousness. The Renaissance is represented '
            'by Machiavelli, Erasmus and Thomas More: Machiavelli and Erasmus '
            'both look to a virtuous prince for order, by force or by '
            "Christian spirituality, while the themes of More's Utopia are "
            'linked to later colonization, imperialism, national socialism '
            'and communism. A chapter on "The People of God" studies the '
            "sectarian movements and supplies background for Voegelin's later "
            'work on Gnosticism. The volume then treats the Reformation and '
            'the situation preceding it, assessing Martin Luther, whose '
            'personality drove the revolt, and John Calvin, with his attempt '
            'at a new universal church and his theory of an elite.'
        )),
    ('History of Political Ideas, Volume V: Religion and the Rise of Modernity (The Collected Works of Eric Voegelin, Volume 23)', 1998, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826211941/history-of-political-ideas-volume-5-cw23/',
        basis='publisher description',
        abstract=(
            'Fifth volume of the History of Political Ideas, continuing the '
            'analysis of the sixteenth-century "great confusion" that '
            "followed Luther's Ninety-Five Theses. Voegelin argues that in "
            'this period the medieval Christian picture of a divinely created '
            'closed cosmos was giving way to a modern consciousness that '
            'takes man as the source of meaning. Figures discussed include '
            'Calvin, Althusius, Hooker, Bracciolini, Savonarola, Copernicus, '
            'Tycho Brahe and Giordano Bruno, with extended attention to Jean '
            'Bodin, presented as a prophet of a new religion amid '
            'post-Christian disorder. Alongside monarchy, just war theory and '
            'the philosophy of law, the volume also takes up astrology, '
            'cosmology and mathematics.'
        )),
    ('History of Political Ideas, Volume VI: Revolution and the New Science (The Collected Works of Eric Voegelin, Volume 24)', 1998, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212009/history-of-political-ideas-volume-6-cw24/',
        basis='publisher description',
        abstract=(
            'Sixth volume of the History of Political Ideas, continuing from '
            'Jean Bodin. It begins with the dispute between Bossuet and '
            'Voltaire over sacred and profane history: Bossuet held the '
            'Augustinian position, while Voltaire pointed to facts, such as '
            'Chinese civilization and the New World, that it could not easily '
            'absorb. Here the historicity of the symbols of political order '
            "becomes Voegelin's central theoretical problem, which found a "
            "provisional answer in Vico's New Science. He traces a growing "
            'closure toward the world-transcendent ground of reality and the '
            'resulting disorientation in personal, social and political life '
            'and in accounts of history and nature. A long chapter on Vico is '
            'the main exception to this decline.'
        )),
    ('The History of the Race Idea: From Ray to Carus (The Collected Works of Eric Voegelin, Volume 3)', 1998, 'Louisiana State University Press'): dict(
        source='https://upress.missouri.edu/9780807118436/the-history-of-the-race-idea-cw3/',
        basis='publisher description',
        abstract=(
            "English translation of Voegelin's 1933 study placing the rise of "
            'the race idea within the development of modern philosophy. He '
            'dates its beginning to the post-Christian turn toward a natural '
            'system of living forms and to the eighteenth-century effort to '
            'place man, in all his physical variety, within a systematic '
            'order of nature. Part I follows race theory from the English '
            'naturalist John Ray to Blumenbach and Kant, holding that '
            'humanity is one species. Part II treats the evolving concepts of '
            'body, organism and person, culminating in Carl Gustav Carus, '
            'whose theory Voegelin takes as the first significant racial '
            'ideology. The book includes a sharp critique of contemporary '
            'Nazi race theory as a decline from its classical form.'
        )),
    ('History of Political Ideas, Volume VII: The New Order and Last Orientation (The Collected Works of Eric Voegelin, Volume 25)', 1999, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212146/history-of-political-ideas-volume-7-cw25/',
        basis='publisher description',
        abstract=(
            'Seventh volume of the History of Political Ideas, in two parts. '
            '"The New Order" describes seventeenth-century Europe after the '
            'decline of church and empire and the responses to its disorder: '
            "Grotius on natural right, Hobbes's Leviathan, the Fronde and the "
            "French national state, Spinoza's Tractatus Theologico-Politicus, "
            "and Locke's Second Treatise, along with Montesquieu and Hume. "
            '"Last Orientation" opens with a chapter on "Phenomenalism," '
            "Voegelin's criticism of the scientistic phenomenalism of the "
            'modern project, followed by a chapter on Schelling as a '
            'spiritual realist and a concluding chapter, "Nietzsche and '
            'Pascal," which uses Nietzsche\'s affinity with Pascal to analyze '
            'the strengths and weaknesses of his thought.'
        )),
    ('History of Political Ideas, Volume VIII: Crisis and the Apocalypse of Man (The Collected Works of Eric Voegelin, Volume 26)', 1999, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212337/history-of-political-ideas-volume-8-cw26/',
        basis='publisher description',
        abstract=(
            'Final volume of the History of Political Ideas, reaching the '
            'modern period. It treats the breakdown of traditional sources of '
            'meaning and the attempt to generate order from within the self, '
            'which Voegelin calls the apocalypse of man replacing the '
            'apocalypse of God, and sees the totalitarian upheavals of his '
            'time as the outward sign of this spiritual crisis, whose '
            'emergence he dates to the Enlightenment. He examines thinkers '
            'such as Comte, Bakunin and Marx, who sought to supply a new '
            'spiritual order themselves, and the more moderate Enlightenment '
            'faith in progress through scientific method and instrumental '
            "reason held by Voltaire, Helvétius, Diderot, D'Alembert and "
            'Condorcet.'
        )),
    ('Hitler and the Germans (The Collected Works of Eric Voegelin, Volume 31)', 1999, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212160/hitler-and-the-germans-cw31/',
        basis='publisher description',
        abstract=(
            'Lectures Voegelin gave in Munich in 1964, first published in '
            "this volume, on Hitler's rise to power, its causes and its "
            'consequences for post-Nazi Germany, which he called the central '
            'German experiential problem of his time. He examines the '
            'mentality of individual Germans and the order of German society '
            'during and after the Nazi period, drawing on Plato and '
            'Aristotle, the Judeo-Christian tradition and writers such as '
            'Doderer, Karl Kraus, Thomas Mann and Musil. Discussing Percy '
            'Schramm\'s "Anatomy of a Dictator" and studies of the churches '
            'and the legal profession, he criticizes German historiography, '
            'the Evangelical and Catholic churches and the legal process of '
            'the period. A lecture on Max Weber points toward a recovery of '
            'order.'
        )),
    ('The Authoritarian State: An Essay on the Problem of the Austrian State (The Collected Works of Eric Voegelin, Volume 4)', 1999, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212351/the-authoritarian-state-cw4/',
        basis='publisher description',
        abstract=(
            "First English translation of Voegelin's book published in Vienna "
            'in 1936, whose sales stopped after the Nazi annexation of '
            'Austria and whose stock was later destroyed by wartime bombing. '
            'It examines the leading European theories of the state and '
            'constitutional law and analyzes the Austrian situation: the '
            'dismissal of Parliament in 1933, the civil war, the murder of '
            'Chancellor Dollfuss, the authoritarian constitution of 1934, and '
            "Austria's position between Hitler and Mussolini. At its centre "
            "is a critique of Hans Kelsen's pure theory of law, marking "
            "Voegelin's break with Neo-Kantian epistemology, and a first "
            'statement of the distinction between theoretical concepts and '
            'political symbols, by which "total" and "authoritarian" are '
            'treated as ideological self-interpretations.'
        )),
    ('Modernity without Restraint: The Political Religions, The New Science of Politics, and Science, Politics, and Gnosticism (The Collected Works of Eric Voegelin, Volume 5)', 2000, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212450/modernity-without-restraint-cw5/',
        basis='publisher description',
        abstract=(
            'Brings together in one volume three works: The Political '
            'Religions (Vienna, 1938, the year Voegelin emigrated), The New '
            'Science of Politics (1952), and Science, Politics, and '
            'Gnosticism, his 1958 inaugural lecture at the University of '
            'Munich. Written in very different circumstances, all three '
            'analyze a modern Western civilization that has lost its '
            'spiritual foundations and faces ideological movements, a '
            '"modernity without restraint" with Hegelian, Marxian, '
            'Nietzschean, Heideggerian, positivist and Fascist features, '
            'which Voegelin sets against the meaning that emerged in Greece, '
            "Rome, Israel and Christianity. Editor Manfred Henningsen's "
            'introduction discusses the experiences behind the analyses and '
            'their relevance after the collapse of state socialism in Eastern '
            'Europe and the Soviet Union.'
        )),
    ('Order and History, Volume III: Plato and Aristotle (The Collected Works of Eric Voegelin, Volume 16)', 2000, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212504/order-and-history-volume-3-cw16/',
        basis='publisher description',
        abstract=(
            'Collected Works edition of the third volume of Order and '
            "History, which completes Voegelin's study of Greek culture from "
            'its pre-Hellenic origins to the age of Athenian dominance and is '
            'devoted mainly to Plato and Aristotle. Analyzing their vision of '
            'soul, polis and cosmos, Voegelin shows the older symbols of myth '
            'being superseded by the more differentiated symbols of '
            "philosophy, and argues that the succession of societies' "
            'attempts to symbolize order forms an intelligible sequence of '
            'advances and recessions rather than a series of failures. This '
            'edition has a new introduction by Dante Germino, which guides '
            "the reader through Voegelin's reading of Plato, and secondarily "
            'Aristotle, and argues for its relevance to the modern world.'
        )),
    ('Order and History, Volume IV: The Ecumenic Age (The Collected Works of Eric Voegelin, Volume 17)', 2000, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826213013/order-and-history-volume-4-cw17/',
        basis='publisher description',
        abstract=(
            'Collected Works edition of the fourth volume of Order and '
            'History. In The Ecumenic Age Voegelin departs from the plan of '
            'the series, which was to present types of order and their '
            'symbols in historical succession, because the original '
            'conception had not allowed for lines of meaning in history that '
            'do not run along lines of time. History is treated instead as '
            "man's participation in a flux of divine presence with an "
            'eschatological direction. The volume applies this to the period '
            'from the rise of the Persian Empire to the fall of Rome, when '
            'ecumenic empires were built at great destructive cost, while '
            'spiritual movements arose that produced the ecumenic religions.'
        )),
    ('Order and History, Volume V: In Search of Order (The Collected Works of Eric Voegelin, Volume 18)', 2000, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212610/order-and-history-volume-5-cw18/',
        basis='publisher description',
        abstract=(
            'The fifth and last volume of Order and History, which Voegelin '
            'planned as a philosophical inquiry into the main types of order '
            'of human existence in society and history and their symbolic '
            'forms. After the earlier volumes on the cosmological empires of '
            "the ancient Near East, Israel's revelation, the Greek polis and "
            'philosophy, and the ecumenic religions, this volume turns to '
            'clarifying the experience of transcendence itself. Voegelin '
            'reflects on the meditative movement he sees at work throughout '
            'his own search, and the volume includes analyses of Hegel, '
            'Hesiod and Plato. Left shorter than intended by his death in '
            'January 1985, it nonetheless essentially completes the '
            'theoretical presentation he had set himself.'
        )),
    ('Published Essays, 1940–1952 (The Collected Works of Eric Voegelin, Volume 10)', 2000, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826213044/published-essays-1940-1952-cw10/',
        basis='publisher description',
        abstract=(
            "Essays from Voegelin's first years in the United States after he "
            'fled Vienna, including commentary on National Socialism from the '
            'opening of the Second World War. Among them are "Growth of the '
            'Race Idea," which summarizes his two race books of 1933, and '
            '"Nietzsche, the Crisis, and the War." Other studies analyze the '
            'diplomatic correspondence between the Western powers, the papacy '
            'and the Mongol Great Khans, and trace "The Origins of Scientism" '
            'as a ground of modern philosophy and political ideology. The '
            'volume also has surveys of political theory in the late 1940s, '
            'essays on utopian thought in Thomas More and Goethe, and a '
            'closing essay on "Gnostic Politics," a theme of The New Science '
            'of Politics.'
        )),
    ('Published Essays, 1953–1965 (The Collected Works of Eric Voegelin, Volume 11)', 2000, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826212825/published-essays-1953-1965-cw11/',
        basis='publisher description',
        abstract=(
            'Fourteen essays from the years in which Voegelin moved from '
            'Louisiana State University to Munich, where in 1958 he took up '
            'the political science chair at Ludwig Maximilian University once '
            'held by Max Weber. The pieces reflect that transition and the '
            'shifts in world politics around it, as well as his developing '
            'account of the stratification of reality and of what a science '
            'of human affairs requires in the face of the continuing crisis '
            'of the West. Several began as talks to particular organizations '
            'on German democratization and the building of a market economy '
            'after the war, and so give a central place to practical '
            'questions, above all how Germany could pass from an ideological '
            'order to a liberal democratic one.'
        )),
    ('Ordnung und Geschichte, Band 7: Aristoteles', 2001, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/2772890-9783770535866-aristoteles',
        basis='publisher description',
        abstract=(
            'Volume 7 of the German edition of Order and History, edited by '
            'Dietmar Herz and Peter J. Opitz. With Aristotle, a process that '
            'had taken centuries in the Aegean world came to an end: '
            'philosophy had emerged as a new symbolic form out of the '
            'symbolic form of myth. Voegelin shows that a process of '
            "splitting, already present in Plato's late work, continued in "
            'Aristotle. The political and religious will to found, which had '
            "marked Plato's work, receded further. Two new independent "
            'disciplines took shape. One was an ethics grounded in '
            'anthropology, together with a general theory of action. The '
            'other was a differentiated nomothetic political science, whose '
            "reach was much wider than Plato's politics because it opened "
            'pragmatically to the variety of practical political problems. '
            "Plato's enchantment gave way to an accommodation with reality "
            'and a scientific sobriety. Fink, 2001.'
        )),
    ('Published Essays, 1934–1939 (The Collected Works of Eric Voegelin, Volume 9)', 2001, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826213372/published-essays-1934-1939-cw9/',
        basis='publisher description',
        abstract=(
            'Essays from 1934 to 1939, written while Voegelin was a scholar '
            'and public intellectual in Vienna until his flight from the Nazi '
            'takeover of Austria in 1938. Their subjects include Austrian '
            'politics and constitutional history, European racism, the '
            'formation and expression of public opinion, theories of '
            'administrative law, and the place of political science in '
            'university education. Several serve as commentaries on or '
            'summaries of arguments from the five books he published between '
            '1928 and 1938. Thirteen are short pieces from trade journals and '
            'newspapers, nine of them from the Wiener Zeitung in 1934 and the '
            'Neue Freie Presse in 1937.'
        )),
    ('Selected Book Reviews (The Collected Works of Eric Voegelin, Volume 13)', 2001, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826213655/selected-book-reviews-cw13/',
        basis='publisher description',
        abstract=(
            "A collection of Voegelin's book reviews, written for scholarly "
            'journals and the popular press from the 1920s until the 1950s, '
            'when he began to decline such requests. The books he reviewed '
            'follow his changing interests: questions of method, legal '
            'philosophy and jurisprudence, race, war and its aftermath, as '
            'well as standard texts, new editions and monographs across '
            'political science. Some reviews are brief summaries, others '
            'analytic essays or extended engagements with a text or problem; '
            'the later ones, often written in English, sometimes show his wit '
            'and impatience with inadequate approaches. Together they mirror '
            'many of the problems Voegelin took up in his essays and books.'
        )),
    ('Anamnesis: On the Theory of History and Politics (The Collected Works of Eric Voegelin, Volume 6)', 2002, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826213501/anamnesis-cw6/',
        basis='publisher description',
        abstract=(
            'The first English translation of the complete German text of '
            "Anamnesis (1966). Gerhart Niemeyer's earlier English version "
            'concentrated on the philosophy of consciousness and left out '
            'several of the historical studies on which it rested; this '
            'volume restores them. In Anamnesis Voegelin looks back on his '
            'own development, including early childhood memories, and applies '
            'the anamnetic method to a range of historical materials, working '
            'out the reconception of Order and History. Part I contains '
            'reflections written in 1943 on recovering consciousness from '
            'current theories of it; Part III, from 1965, begins as a '
            "rethinking of Aristotle's account of consciousness and moves "
            'beyond it. Between them stand eight studies of historical '
            'phenomena of order.'
        )),
    ('Ordnung und Geschichte, Band 1: Die kosmologischen Reiche des Alten Orients – Mesopotamien und Ägypten', 2002, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/naturwissenschaften/2772886-9783770535842-die-kosmologischen-reiche-des-alten-orients-mesopotamien-und-aegypten',
        basis='publisher description',
        abstract=(
            'Volume 1 of the German edition of Order and History, on the '
            'cosmological empires of Mesopotamia and Egypt, edited by Jan '
            'Assmann, Dietmar Herz and Peter J. Opitz and translated by '
            'Reinhard W. Sonnenschmidt. Cosmological cultures are marked by a '
            "principle of 'early tolerance', the interchangeability of "
            'different symbolisations. They know no orthodoxy and no heresy, '
            'and the distinction between true and false does not yet matter. '
            'That changes dramatically with the arrival of Jewish monotheism '
            'and Greek philosophy. The volume attempts to do justice to the '
            'thought forms of the early high civilisations within a '
            'comprehensive theory of evolution. The publisher notes that the '
            'specialist disciplines concerned have not yet taken up '
            "Voegelin's questions, and presents his attempt as a step toward "
            'the kind of cultural-scientific analysis now being called for, '
            'especially in Germany. Fink, 2002, 286 pages.'
        )),
    ('Ordnung und Geschichte, Band 4: Die Welt der Polis: Gesellschaft, Mythos und Geschichte', 2002, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/4706240-9783770537372-die-welt-der-polis',
        basis='publisher description',
        abstract=(
            'Volume 4 of the German edition of Order and History, edited by '
            'Jürgen Gebhardt, Dietmar Herz and Peter J. Opitz. Voegelin '
            'reconstructs how Greek thought and its social context developed '
            'their symbols, from Minoan-Mycenaean prehistory, as preserved in '
            'Greek cultural memory, to the political philosophy of Plato and '
            'Aristotle. The historical frame is Greek civilisation in its '
            'Minoan, Mycenaean and Hellenic phases, the last shaped by the '
            'political culture of the polis. Voegelin sees the '
            'Minoan-Mycenaean period as a cosmological form of society '
            'comparable to the ancient Near East, present to later Greek '
            'historians and philosophers as a mythical past. Each epoch was '
            'marked by crises of order, so that a cycle of rise and decline '
            'became a central motif of Hellenic self-understanding. It runs '
            "from Homer's mythopoetic poetry and Hesiod's speculation on myth "
            'to the Presocratics, who prepared the way for political '
            'philosophy within the polis.'
        )),
    ('Jean Bodin', 2003, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/5424783-9783770538393-jean-bodin',
        basis='publisher description',
        abstract=(
            'Two essays by Eric Voegelin on Jean Bodin (1529/30-1596), '
            'published here in German for the first time and edited by Peter '
            'J. Opitz. Bodin is widely known as one of the major political '
            'philosophers of the early modern period, and his theory of '
            'sovereignty as a contribution to modern political thought. Much '
            'less known are the theoretical and religious foundations of his '
            "thinking, which reveal the unity of his work. Voegelin's essays "
            "concentrate on the religious foundations of Bodin's thought. "
            "They show how the unity of the French philosopher and mystic's "
            'work unfolds from them. They also show how strongly Bodin '
            "influenced Voegelin's own political philosophy: for Voegelin, "
            "Bodin was one of the great 'representative figures in the "
            "understanding of order in times of spiritual disorder'. Fink, "
            '2003, Periagoge series, 147 pages.'
        )),
    ('Ordnung und Geschichte, Band 5: Die Welt der Polis: Vom Mythos zur Philosophie', 2003, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/5424791-9783770538416-die-welt-der-polis',
        basis='publisher description',
        abstract=(
            'Volume 5 of the German edition of Order and History, edited by '
            'Jürgen Gebhardt, Dietmar Herz and Peter J. Opitz. It is the '
            "second part of Voegelin's study of the world of the polis, which "
            'traces spiritual development in Hellas up to the philosophy of '
            'Plato and Aristotle. After a first part on the cosmological '
            'order of Homer and Hesiod, this part follows the transition from '
            'archaic to classical Hellas: over centuries, philosophy replaced '
            'the traditional myth of the polis as a new symbolic form. In '
            'this process the human soul, its depth and its order were '
            'discovered, along with the radical transcendence of the divine. '
            'Voegelin follows its steps in Anaximander, Heraclitus and '
            "Parmenides. The book ends with a study of the 'Athenian "
            "century': the political meaning of Greek tragedy, the spiritual "
            'crisis of the Sophists, and the rise and fall of Athens and the '
            'problem of power and history in Herodotus and Thucydides.'
        )),
    ('Published Essays, 1922–1928 (The Collected Works of Eric Voegelin, Volume 7)', 2003, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826214423/published-essays-1922-1928-cw7/',
        basis='publisher description',
        abstract=(
            'Essays Voegelin published from 1922 to 1928, after his doctorate '
            'and including his two-year study trip to the United States. They '
            'trace his formation in the 1920s: a critique of political '
            'science understood purely in legal terms, and a turn toward the '
            'ideas and structures underlying a political society, with '
            'growing distance from his teacher Hans Kelsen. Topics range from '
            "theories of state form, Max Weber's science, the sociology of "
            "knowledge, Hume's sociology, time and economy, and Kelsen's pure "
            'theory of law, to practical matters such as amending the '
            'American Constitution, the U.S. Federal Reserve Board, class '
            'conflict in the United States, and the French National '
            "Assembly's debates on the 1789 Declaration of the Rights of Man."
        )),
    ('Published Essays, 1929–1933 (The Collected Works of Eric Voegelin, Volume 8)', 2003, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826214829/published-essays-1929-1933-cw8/',
        basis='publisher description',
        abstract=(
            'Essays Voegelin published between 1929 and 1933, between his '
            "first book, On the Form of the American Mind, and Hitler's rise "
            'to power and his own two books on race. They show him moving '
            "away from positivism and Kelsen's pure theory of law toward "
            'philosophical anthropology and the moral substance of political '
            'communities. Grouped around sociological theory, political '
            'science and legal theory, they engage French and German theories '
            'of the state and treat American theories of property, economic '
            'transactions, due process, Austrian constitutional reform, '
            "sovereignty and law, Max Weber's science, the spiritual form of "
            "Europe, Kant's idea of moral duty, and solidarity as the "
            'substance of democratic society.'
        )),
    ('The Theory of Governance and Other Miscellaneous Papers, 1921–1938 (The Collected Works of Eric Voegelin, Volume 32)', 2003, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826214881/theory-of-governance-and-other-miscellaneous-papers-1921-1938-cw32/',
        basis='publisher description',
        abstract=(
            "The first of two volumes of Voegelin's miscellaneous papers, "
            'publishing for the first time writings from his formative '
            'period. It opens with his 1922 University of Vienna dissertation '
            'on sociological method, written under Othmar Spann and Hans '
            'Kelsen and drawing on Simmel and Husserl. These early texts take '
            'up the relation of insight to language, the structure of the '
            'human being and its spiritual centre, with reference to Bergson, '
            'Spann, Simmel and Husserl. The volume also contains his extended '
            'study on the "theory of governance" (1930-1932), which traces '
            'political problems to the soul and its relation to the ground of '
            'being and includes meditative readings of Augustine, Descartes '
            'and Husserl, along with essays such as "Theory of Law" and '
            '"Political Theory as Human Science."'
        )),
    ('Eine Freundschaft, die ein Leben ausgehalten hat: Briefwechsel 1938–1959', 2004, 'UVK Verlagsgesellschaft'): dict(
        source='https://www.lehmanns.de/shop/sozialwissenschaften/5976549-9783896696991-eine-freundschaft-die-ein-leben-ausgehalten-hat',
        basis='publisher description',
        abstract=(
            'The correspondence between Alfred Schütz and Eric Voegelin, '
            'edited by Gerhard Wagner and Gilbert Weiss. The two had '
            'developed their work in dialogue since their student years in '
            'Vienna in the 1920s. After the Anschluss of 1938 forced them '
            'into exile in the United States, Schütz in New York and Voegelin '
            'in Baton Rouge, they carried the dialogue on by letter. The '
            'letters document the years of exile. They also record the '
            'tentative emergence of the theories with which the two are now '
            "associated: Schütz's theory of the life-world and Voegelin's "
            'theory of gnosis. The volume is the first complete edition of '
            'the correspondence, based on current textual criticism and '
            'editing technique and furnished with commentary.'
        )),
    ('Ordnung und Geschichte, Band 10: Auf der Suche nach Ordnung', 2004, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/6007044-9783770538461-auf-der-suche-nach-ordnung',
        basis='publisher description',
        abstract=(
            "The German translation of 'In Search of Order', the last volume "
            'of Order and History, published posthumously in 1987. Voegelin '
            'worked on the text intensively from 1980 until his death in '
            '1985. In her preface Lissy Voegelin reports that her husband saw '
            'in these pages the key to all his other works. In a highly '
            'condensed and direct form, Voegelin speaks once more of the '
            'foundations of order in human existence, located in the complex '
            'of consciousness, reality and language, and of their '
            'deformation. His main theoretical points of reference are '
            "Plato's Timaeus and Hegel. In his approach to the experience of "
            'the metaxy, the existential tension between immanence and '
            'transcendence, the anamnetic character of his thinking again '
            "comes clearly into view. The volume can be read as Voegelin's "
            'philosophical testament. Fink, 2004.'
        )),
    ('Ordnung und Geschichte, Band 8: Das Ökumenische Zeitalter: Die Legitimität der Antike', 2004, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/5864072-9783770538447-das-oekumenische-zeitalter-die-legitimitaet-der-antike',
        basis='publisher description',
        abstract=(
            'Volume 8 of the German edition of Order and History, edited by '
            'Thomas Hollweck, Dietmar Herz and Peter J. Opitz. It is the '
            "first part of 'The Ecumenic Age'. It deals with the problems of "
            'a philosophy of history that is not Eurocentric, and with the '
            'symbolisms such a philosophy must draw on. These new symbolisms '
            'first appear in the centuries between the rise of the Persian '
            'empire and the fall of the Roman. The introduction gives the '
            "philosophical grounds for Voegelin's reordering of this age. It "
            'presents it as a process between a cosmological beginning and a '
            'transcosmic beyond, in which mankind forms the field shaped by '
            'the tension of that process. For Voegelin, the legitimacy of the '
            'ecumenic age of antiquity lies in this: it marks out in '
            'principle the possibilities of what can be called history, and '
            'it shows the tension of the historical process to be the essence '
            'of being human.'
        )),
    ('Ordnung und Geschichte, Band 9: Das Ökumenische Zeitalter: Weltherrschaft und Philosophie', 2004, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/5864073-9783770538454-das-oekumenische-zeitalter-weltherrschaft-und-philosophie',
        basis='publisher description',
        abstract=(
            'Volume 9 of the German edition of Order and History, edited by '
            'Dietmar Herz, Manfred Henningsen and Peter J. Opitz. It is the '
            "second part of 'The Ecumenic Age'. Voegelin continues his study "
            'of history as a process in which human consciousness '
            'differentiates and comes to recognise history as a dimension of '
            'its humanity. The compact myth with which the cosmological '
            'empires had answered the question of the ground of existence '
            'became doubtful once many ecumenic empires entered a bloody '
            'struggle for supremacy. The ecumenic age thus created both the '
            "need and the conditions for the spiritual outbursts of Hegel's "
            "'absolute epoch' or Jaspers's 'axial age'. In that period "
            'philosophers and prophets overcame the plurality of ecumenic '
            'empires in the symbol of a universal mankind. For Voegelin this '
            'is a generally valid structure of history, not confined to the '
            'Western ecumene, as he shows at length through the example of '
            'China.'
        )),
    ('Robert B. Heilman and Eric Voegelin: A Friendship in Letters, 1944–1984', 2004, 'University of Missouri Press'): dict(
        source='https://books.google.com/books?id=15eDAAAAMAAJ',
        basis='publisher description',
        abstract=(
            'Letters exchanged over more than forty years between Eric '
            'Voegelin and the literary scholar Robert B. Heilman, who met '
            'around 1941 when Voegelin lectured at Louisiana State '
            'University, where Heilman taught English alongside Robert Penn '
            'Warren and Cleanth Brooks. The correspondence begins with an '
            "eight-page letter by Voegelin on Heilman's manuscript on King "
            "Lear and runs until four months before Voegelin's death in 1985. "
            "It is Voegelin's longest correspondence with an American-born "
            'scholar and shows him as a literary critic, with the background '
            "to his reading of Henry James's The Turn of the Screw and "
            'comments on Mann, Eliot, Shakespeare, Homer, Proust and '
            "Flaubert, alongside Heilman's questions about Voegelin's "
            'philosophy and his own theories of tragedy and melodrama.'
        )),
    ('The Drama of Humanity and Other Miscellaneous Papers, 1939–1985 (The Collected Works of Eric Voegelin, Volume 33)', 2004, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826215451/the-drama-of-humanity-and-other-miscellaneous-papers-1939-1985-cw33/',
        basis='publisher description',
        abstract=(
            "The second volume of Voegelin's miscellaneous papers, with "
            'unpublished writings from his emigration in 1938 to his death in '
            '1985, centred on Voegelin as lecturer and discussant. "The Drama '
            'of Humanity" gives his 1967 Candler Lectures at Emory University '
            'in four parts. Also included are the "Conversations with Eric '
            'Voegelin" at the Thomas More Institute in Montreal (1967-1976); '
            'the full foreword to the second edition of The Political '
            "Religions; notes on T. S. Eliot's Four Quartets; pieces such as "
            '"What Is Political Theory?", "Structures of Consciousness" and '
            '"The Beyond and Its Parousia"; excerpts from conference '
            'dialogues on industrial society, natural law and political '
            'institutions; and his "Autobiographical Statement at the Age of '
            'Eighty-Two."'
        )),
    ('Ordnung und Geschichte, Band 2: Israel und die Offenbarung: Die Geburt der Geschichte', 2005, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/6007038-9783770537020-israel-und-die-offenbarung-die-geburt-der-geschichte',
        basis='publisher description',
        abstract=(
            'Volume 2 of the German edition of Order and History, edited by '
            'Jörg Jeremias, Dietmar Herz and Peter J. Opitz. Its thesis is '
            'that without Israel there would have been no history, at least '
            'not as a conscious retrospective interpretation of past events. '
            'The symbolisms of the ancient Near Eastern cultures followed a '
            'model of correspondence between cosmos and society. They aimed '
            'to keep the social order in harmony with the great rhythms of '
            'heaven and earth. In ancient Israel, as in a different way in '
            "Greece, a decisive 'leap in being' took place. Moses' encounter "
            'with God at the burning bush and the exodus from Egypt gave the '
            'relation between order and history a new quality. For the first '
            'time human existence was consciously placed before a God who '
            'transcends the world. This transition divided time into before '
            "and after, and gave birth to history as the form of a society's "
            'existence. Fink, 2005, 318 pages.'
        )),
    ('Ordnung und Geschichte, Band 3: Israel und die Offenbarung: Mose und die Propheten', 2005, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/6007040-9783770537037-israel-und-die-offenbarung-mose-und-die-propheten',
        basis='publisher description',
        abstract=(
            'Volume 3 of the German edition of Order and History, edited by '
            'Jörg Jeremias, Dietmar Herz and Peter J. Opitz. Whatever the '
            'historicity of Moses and the exodus, the revelation at work '
            'throughout the biblical texts is of the highest importance for '
            'the sequence of cultural ideas of order. The former compactness '
            'of being is broken open for a direct partnership with God, '
            'mediated by the gift of the Decalogue at Sinai: human action '
            'must correspond to nearness to God. Because the Decalogue orders '
            "the people's social existence, it is also ambiguous. The social "
            'existence it founds repeatedly blocks a reflective relation to '
            'transcendence. This is where the message of the prophets begins. '
            "They point to the contradiction between God's revealed order and "
            'the real disorder of society, and they increasingly develop the '
            'universal, all-human dimension of the image of God. Fink, 2005, '
            '217 pages.'
        )),
    ('Autobiographical Reflections: Revised Edition, with a Voegelin Glossary and Cumulative Index (The Collected Works of Eric Voegelin, Volume 34)', 2006, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826215895/autobiographical-reflections-cw34/',
        basis='publisher description',
        abstract=(
            "The final volume of the Collected Works. It reprints Voegelin's "
            'Autobiographical Reflections from the 1989 edition with '
            'additional annotations, and adds a glossary of terms used in his '
            'writings, a volume index, and a cumulative index to the whole '
            'edition, excluding the History of Political Ideas, which has its '
            'own index, and the two volumes of Selected Correspondence, then '
            'unpublished. The glossary defines key terms, with particular '
            'attention to Greek ones, and illustrates them with examples '
            'drawn from throughout the Collected Works.'
        )),
    ('Hitler und die Deutschen', 2006, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/7187676-9783770538652-hitler-und-die-deutschen',
        basis='publisher description',
        abstract=(
            "Voegelin's lectures on Hitler and the Germans, delivered at the "
            'University of Munich in the summer semester of 1964 and edited '
            'by Manfred Henningsen. The lectures are an unsparing reckoning '
            'with a society that, in the early 1960s, had sunk into a great '
            "silence about its past. Voegelin's concern was less the "
            'murderous details of the Nazi state than the failure of the '
            'German political and intellectual elites who had supported the '
            'regime or at least tolerated it. Having returned from American '
            'exile, the political philosopher offers a critical analysis of '
            'Germany, both historical and contemporary.'
        )),
    ('Mysterium, Mythos und Magie: Bewußtseinsphilosophische Meditationen', 2006, 'Passagen'): dict(
        source='https://www.passagen.at/gesamtverzeichnis/unkategorisiert/mysterium-mythos-und-magie/',
        basis='publisher description',
        abstract=(
            "Two essays from Voegelin's late work, translated into German by "
            'Nils Winkler. From the early 1960s on, in trying to lay '
            'theoretical foundations for politics and history, Voegelin '
            'worked more and more on a philosophy of consciousness. His '
            'research centred on two sets of problems. One was the structures '
            'of healthy consciousness and the meditative processes that bring '
            "them to light. The other was the forms of 'diseased "
            "consciousness', what he sometimes called the psychopathology of "
            'the modern age. Topics include Plato, Hegel, gnosis, religion '
            'and politics. The book is a 152-page paperback in the series '
            'Passagen Religion und Politik, published in October 2006.'
        )),
    ('Das Drama des Menschseins: Die Walter Turner Candler Lectures', 2007, 'Passagen'): dict(
        source='https://www.passagen.at/gesamtverzeichnis/unkategorisiert/das-drama-des-menschseins/',
        basis='publisher description',
        abstract=(
            "The first German translation of the original version of 'The "
            "Drama of Humanity'. In 1967 Voegelin began work on a new book "
            'with that title, based on a lecture series he had just given at '
            'Emory University in Atlanta, Georgia, the Walter Turner Candler '
            'Lectures. The book was never finished and is considered lost. '
            'This volume presents the original lecture text. Its subjects are '
            'the philosophy of history and political science. It is a '
            '120-page paperback in the series Passagen Religion und Politik, '
            'published in November 2007.'
        )),
    ('Das Jüngste Gericht: Friedrich Nietzsche', 2007, 'Matthes & Seitz'): dict(
        source='https://www.matthes-seitz-berlin.de/buch/das-juengste-gericht-friedrich-nietzsche.html',
        basis='publisher description',
        abstract=(
            'Two essays on Friedrich Nietzsche, published here in German for '
            'the first time. Voegelin wrote them in the mid-1940s, while in '
            'exile in the United States, as part of his planned History of '
            'Political Ideas. For Voegelin, Nietzsche was the most powerful '
            "symptom of the West's spiritual crisis. He was also its most "
            'sensitive diagnostician and its tragic hero. The essays come out '
            "of Voegelin's lifelong engagement with Nietzsche's work and its "
            "influence. The volume appeared in the publisher's series "
            'Fröhliche Wissenschaft.'
        )),
    ('Die Krise: Zur Pathologie des modernen Geistes', 2007, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/7933960-9783770543908-die-krise',
        basis='publisher description',
        abstract=(
            "The 'spiritual crisis' of Western modernity was the centre "
            "around which Voegelin's thinking turned. One great theme of his "
            'work was to reconstruct the processes that led to this crisis '
            'and to identify its spiritual roots. The other was the search '
            'for ways out of it and the outline of a philosophy of order. In '
            '1938, still in Vienna, he had given a first interpretation of '
            'the crisis in his study of the political religions. A decade '
            'later, still in exile, the closing part of his History of '
            'Political Ideas offered a second, much more precise diagnosis '
            "under the title 'The Crisis'. The volume presents that "
            'diagnosis, which traces the intellectual and political currents '
            'since the Enlightenment that destroyed the spiritual foundations '
            'of Western civilisation and culminated in the totalitarian '
            'regimes of the twentieth century.'
        )),
    ('Selected Correspondence, 1950–1984 (The Collected Works of Eric Voegelin, Volume 30)', 2007, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826216724/selected-correspondence-1950-1984-cw30/',
        basis='publisher description',
        abstract=(
            "The second volume of Voegelin's selected letters, covering 1950 "
            'to 1984, mostly from originals in the Hoover Institution '
            'Archives. Correspondents include Leo Strauss, Karl Löwith, '
            'Alfred Schütz, Aron Gurwitsch, Hans Kelsen, Marshall McLuhan, '
            'Bertrand de Jouvenel, Arnold Toynbee and Marie König. The '
            'letters run from the period of the Walgreen Lectures and The New '
            'Science of Politics through the publication of the first four '
            'volumes of Order and History, his move to Munich and founding of '
            'the Institut für Politische Wissenschaft, and his years as '
            'Salvatori Fellow at the Hoover Institution (1969-1974). Letters '
            'to directors of LSU Press trace the changing plan of Order and '
            'History. Many are translated from German and published here for '
            'the first time.'
        )),
    ('Selected Correspondence, 1924–1949 (The Collected Works of Eric Voegelin, Volume 29)', 2009, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826218421/the-selected-correspondence-1924-1949-cw29/',
        basis='publisher description',
        abstract=(
            "The first of two volumes of Voegelin's selected letters, "
            'covering 1924 to 1949, from his early academic years in Vienna '
            'through emigration and his first decade in the United States. '
            'The editorial board of the Collected Works chose the letters to '
            'illuminate his intellectual life and the formative experiences '
            "behind it, following Voegelin's own principle that the study of "
            'a thinker should uncover the biographical roots of his '
            'philosophizing. The letters show the development of his thought, '
            'including his effort from the 1930s onward to explicate a '
            'contemplative understanding of human reality grounded in the '
            'experience of reason. Because of the very large number of later '
            'letters, both volumes print only letters written by Voegelin, '
            'not those of his correspondents.'
        )),
    ('Glaube und Wissen: Der Briefwechsel zwischen Eric Voegelin und Leo Strauss von 1934 bis 1964', 2010, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/11998871-9783770549672-glaube-und-wissen',
        basis='publisher description',
        abstract=(
            'The correspondence between Eric Voegelin and Leo Strauss, two '
            'German émigrés, conducted over more than two decades, from 1934 '
            'to 1964. It is edited by Peter J. Opitz. Both men are known for '
            'sharp criticism of a social science that had flattened into '
            'positivism, and for their efforts to revive Greek political '
            'philosophy. Beyond these shared concerns, the letters show that '
            'the two thinkers held very different philosophical positions. '
            'The correspondence had already appeared in English and French '
            'translation. This volume publishes it for the first time in its '
            'original form. Wilhelm Fink, 2010, 208 pages.'
        )),
    ('Realitätsfinsternis', 2010, 'Matthes & Seitz'): dict(
        source='https://www.matthes-seitz-berlin.de/buch/realitaetsfinsternis.html',
        basis='publisher description',
        abstract=(
            'A German translation, by Dora Fischer-Barnicol, of a late text '
            'by Eric Voegelin that remained a fragment. Its subject is the '
            'blindness of the modern age toward metaphysics: the way modern '
            'thought closes itself off from the reality that metaphysical '
            'questioning addresses. One line the publisher quotes says that '
            'by an act of imagination a person can shrink himself into a self '
            "that is 'condemned to be free'. Peter J. Opitz, editor of "
            "Voegelin's writings, adds an afterword on how the text came to "
            'be written and on where it stands, both in its themes and in the '
            "history of Voegelin's work. The volume appeared in 2010 in the "
            "publisher's series Fröhliche Wissenschaft."
        )),
    ('A Friendship That Lasted a Lifetime: The Correspondence between Alfred Schütz and Eric Voegelin', 2011, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826219114/a-friendship-that-lasted-a-lifetime/',
        basis='publisher description',
        abstract=(
            'An English selection from the correspondence between Alfred '
            'Schütz (1899-1959) and Eric Voegelin (1901-1985), who met as '
            'students in Vienna in the 1920s, were driven out of Europe by '
            'Nazi pressure, and taught at separate American universities. For '
            'some twenty years they wrote to each other, developing their '
            'scholarly work in that exchange; the letters record their '
            'friendship in exile and their early attempts to formulate the '
            'ideas of the "lifeworld" and of "gnosis" now associated with '
            'them. The full set of 238 letters appeared in German in 2004; '
            'editors Gerhard Wagner and Gilbert Weiss chose the letters most '
            "important to the two men's theoretical discussions, presenting "
            "them without interpreting the authors' works in their light."
        )),
    ('Luther und Calvin: Die große Verwirrung', 2011, 'Wilhelm Fink'): dict(
        source='https://www.lehmanns.de/shop/geisteswissenschaften/17611770-9783770551590-luther-und-calvin',
        basis='publisher description',
        abstract=(
            "Voegelin's study of Luther and Calvin, edited by Peter J. Opitz. "
            "The publisher's text starts from Luther's stay in Rome in 1511. "
            'There, the sale of indulgences, corruption and moral decay '
            'prepared his conversion experience: the insight that justice is '
            'purely a gift of grace, given through faith in Christ alone. For '
            'Voegelin, Luther with this sola fide principle represents the '
            'great confusion. He was concerned with spreading his personal '
            'experience and imposing it on mankind as an order of existence, '
            'and the shadow of egoistic obscurantism began to spread. '
            "Voegelin also draws a line from Luther's 'heart' to Kant's "
            "'conscience'. The chapters cover the press and the public "
            'sphere, the schism and the Leipzig Disputation, the historicity '
            'of symbols (church and transubstantiation), the 95 Theses, the '
            'address to the Christian nobility, justification by faith, and '
            'Calvin and predestination. Fink, 2011, 114 pages.'
        )),
    ('Die Natur des Rechts', 2012, 'Matthes & Seitz'): dict(
        source='https://www.matthes-seitz-berlin.de/buch/die-natur-des-rechts.html',
        basis='publisher description',
        abstract=(
            "A German translation, by Thomas Nawrath, of Voegelin's essay on "
            'the nature of law, with an afterword by the translator. The '
            'essay opens provocatively: an inquiry into the nature of law, '
            'Voegelin says, is burdened from the start by doubt that it can '
            'be done, since the classical philosophers had no philosophy of '
            'law at all. He then asks whether, and under what conditions, law '
            'can be said to have an essence, that is, whether law is a thing '
            'with an ontological status of its own. The volume appeared in '
            "2012 as volume 10 of the publisher's series Batterien."
        )),
    ('Disput über den Totalitarismus: Texte und Briefe', 2015, 'V&R unipress'): dict(
        source='https://eichendorff21.de/buch/9783847104926',
        basis='publisher description',
        abstract=(
            "A short volume tracing the origins of Hannah Arendt's analysis "
            'of totalitarianism through her exchange with Eric Voegelin. It '
            'brings together passages that Arendt cut from the first English '
            "edition of her book on totalitarianism, her reply to Voegelin's "
            'review of that book, and her 1951 correspondence with Voegelin. '
            'Accompanying texts by Ursula Ludz, Ingeborg Nordmann and Michael '
            'Henkel set the documents in context. Together they help clarify '
            "Arendt's idea of totalitarianism as a form of rule without "
            'precedent, an idea the publisher says is still misunderstood in '
            'the German debate. It was edited by the Hannah-Arendt-Institut '
            'in cooperation with the Voegelin-Zentrum für Politik, Kultur und '
            'Religion at LMU Munich, and published by V&R unipress in 2015 as '
            'a 110-page paperback.'
        )),
    ('Was ist Geschichte?', 2015, 'Matthes & Seitz'): dict(
        source='https://www.matthes-seitz-berlin.de/buch/was-ist-geschichte.html',
        basis='publisher description',
        abstract=(
            'A German translation, by Dora Fischer-Barnicol and edited by '
            "Peter J. Opitz, of Voegelin's study 'What Is History?' Alongside "
            'it the volume prints, also for the first time, his 1962 lecture '
            "'Ewiges Sein in der Zeit' (Eternal Being in Time). Together the "
            "two texts set out, in a short space, Voegelin's basic thinking "
            'about the philosophy of history, and they open a new view of his '
            'late work. Opitz supplies a preface. The book appeared in 2015 '
            'as volume 56 of the series Fröhliche Wissenschaft.'
        )),
    ('The Eric Voegelin Reader: Politics, History, Consciousness', 2017, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826222893/the-eric-voegelin-reader/',
        basis='publisher description',
        abstract=(
            "A one-volume selection of Voegelin's writings, drawn by Charles "
            "Embry and Glenn Hughes from the University of Missouri Press's "
            'thirty-four-volume Collected Works and meant as a general '
            'introduction to his philosophy of politics, history and '
            'consciousness. It begins with excerpts from Autobiographical '
            "Reflections, then turns to Voegelin's call to re-ground "
            'political science on a non-positivist basis, with his survey of '
            'science and scientism and the introduction to The New Science of '
            'Politics, and continues with his introductions to volumes 1, 2 '
            'and 4 of Order and History and his accounts of what a philosophy '
            'of history requires. The editors provide a short introduction '
            "and place each selection within Voegelin's overall work."
        )),
    ('Angst und Vernunft', 2018, 'Matthes & Seitz'): dict(
        source='https://www.matthes-seitz-berlin.de/buch/angst-und-vernunft.html',
        basis='publisher description',
        abstract=(
            "Two self-contained studies from Voegelin's late work, edited by "
            'Peter J. Opitz and translated by Dora Fischer-Barnicol and '
            "Helmut Winterholler: 'Angst und Vernunft' (1967) and 'Vernunft: "
            "Die Erfahrung der Philosophen' (1973). They offer a new account "
            'of historiogenesis, that is, how historicity arose and how the '
            'linear Jewish-Christian sense of time replaced cosmologically '
            'ordered societies. They also take up the equivalence of myth and '
            'philosophy. That idea let Voegelin relate problems that stay the '
            'same across civilisations and periods, though they are expressed '
            'in different symbolic forms. The essays belong to his effort to '
            'understand modernity and touch on basic problems of philosophy. '
            'The book is volume 97 of the series Fröhliche Wissenschaft.'
        )),
    ('Unsterblichkeit: Erfahrung und Symbol', 2020, 'Matthes & Seitz'): dict(
        source='https://www.matthes-seitz-berlin.de/buch/unsterblichkeit.html',
        basis='publisher description',
        abstract=(
            'A German translation, by Dora Fischer-Barnicol with a preface by '
            'Peter J. Opitz, of an essay by Voegelin on immortality. The '
            "essay tries to recover what the symbol 'immortality' originally "
            'meant within experienced reality. It traces the symbolism of '
            'immortality back to its source in experience, to show that life '
            "is more than mortal life alone. Like Voegelin's work as a whole, "
            'the text responds to what he saw as the spiritual crisis of the '
            'West. It sketches a sequence of historical phases in which '
            'living existential tension declined. Christianity hardened into '
            "doctrine, and so did metaphysics, leaving a 'secondary mode of "
            "truth'. Enlightenment thinkers revolted against this surrogate "
            'but obscured reality further. A radical revolt against every '
            'kind of doctrine then followed, and with it a return to life '
            'lived in existential tension. The book is volume 166 of the '
            'series Fröhliche Wissenschaft.'
        )),
    ('Voegelin, Schelling, and the Philosophy of Historical Existence', 2003, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826214935/voegelin-schelling-and-the-philosophy-of-historical-existence/',
        basis='publisher description',
        abstract=(
            "Jerry Day argues that Eric Voegelin's mature philosophy needs "
            'substantial reinterpretation in light of his published and '
            'unpublished regard for F. W. J. Schelling, whom Day treats as '
            "one of the main guides to Voegelin's philosophy of consciousness "
            'and of history. Against the common picture of Schelling as a '
            'scattered thinker who fathered idealism and existentialism, '
            'Voegelin held that Schelling founded no school and recovered the '
            "perennial concerns of philosophy as a 'spiritual realist'. Day "
            'maintains that Voegelin read Schelling well, especially in the '
            'years when the History of Political Ideas was being transformed '
            'into Order and History, and he assembles evidence for this while '
            'summarising much untranslated German literature. Partly agreeing '
            "with Voegelin's assessment, Day suggests how philosophical "
            'realists might accept insights of recent continental philosophy '
            'without its drift toward nihilism or fideistic historicism.'
        )),
    ('Eric Voegelin and the Problem of Christian Political Order', 2007, 'University of Missouri Press'): dict(
        source='https://books.google.com/books?vid=ISBN9780826217370',
        basis='publisher description',
        abstract=(
            "Some critics of Eric Voegelin's later work faulted him for "
            'neglecting the historical Jesus and the implications of '
            'Christianity for social and political life. Using the recently '
            'published History of Political Ideas, Jeffrey C. Herndon answers '
            "that criticism by tracing how Voegelin's early work treated the "
            'origins of Christianity in Jesus, the formation of the church '
            'through Paul, and the relation between an institutional order '
            'representing divine presence and the struggle for social and '
            'political order. Centring on the tension between Pauline faith '
            'and its institutionalisation in the church, the study follows '
            "Voegelin's account of Christian political order from its "
            'beginnings to the Reformation. It clarifies his theory of '
            'civilisational foundation and his philosophy of history, '
            "discusses the 'Pauline compromises with the world', and shows "
            'how his reading of the Reformation bears on his later account of '
            'Christian symbols in ideological disorder.'
        )),
    ('The Philosopher and the Storyteller: Eric Voegelin and Twentieth-Century Literature', 2008, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826221520/the-philosopher-and-the-storyteller/',
        basis='publisher description',
        abstract=(
            "A book-length study of the literary side of Eric Voegelin's "
            'philosophy that also applies that philosophy to particular '
            "novels. Drawing on Voegelin's published remarks on literature "
            'and especially his correspondence with the critic Robert '
            'Heilman, Charles R. Embry argues that novels, like myth, '
            'philosophy and religious texts, take part in the search for the '
            'truth of existence. He singles out two Voegelinian notions as '
            'central to the reading of literature: metaxy, consciousness as '
            'existing in the in-between, and metalepsis, human sharing in the '
            "community of being, shows how Voegelin's thought rests on the "
            'interpretation of symbols, and discusses his view that sound '
            "criticism depends on the reader's consciousness. The second part "
            "offers readings of Graham Swift's Waterland, Heimito von "
            "Doderer's The Demons, and Flannery O'Connor's The Violent Bear "
            'It Away, the last read in terms of what Voegelin called the Time '
            'of the Tale.'
        )),
    ('Voegelin Recollected: Conversations on a Life', 2008, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826217653/voegelin-recollected/',
        basis='publisher description',
        abstract=(
            'A collection of personal recollections of Eric Voegelin, '
            'gathered by Barry Cooper and Jodi Bruhn through extended '
            'interviews with his wife, close friends and first-generation '
            'students. Contributors such as Paul Caringella, Bruno '
            'Schlesinger and Heinz Barazon describe both his strengths and '
            'his failings. The book moves progressively back in time, from '
            'his years in America to Munich, where German colleagues recall '
            'him, and to Vienna, where former students speak of him, '
            'including memories of Gestapo intimidation and his emigration. '
            'The accounts touch on his difficulties in communication and '
            'impatience with administration, his respect for prudent '
            'statesmen and public servants, and his affection for colleagues, '
            'students, secretaries and nurses, and they repeatedly return to '
            'his intelligence, optimism and integrity and his sense of the '
            'importance of his own work.'
        )),
    ('Beginning the Quest: Law and Politics in the Early Work of Eric Voegelin', 2009, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826218544/beginning-the-quest/',
        basis='publisher description',
        abstract=(
            "Barry Cooper analyses Eric Voegelin's legal and political "
            'writings of the 1920s and 1930s, stressing that Voegelin, a '
            'pupil of Hans Kelsen, began as a legal scholar, unlike his '
            'contemporaries Leo Strauss and Hannah Arendt. The book opens '
            "with Voegelin's postwar attempts to relate law and Staatslehre "
            "to 'sociohistorical reality', largely through methodological "
            'criticism of neo-Kantian foundations for social science. It then '
            'treats his first systematic effort to combine philosophical '
            'anthropology and philosophy of history with comparative social '
            "science and a theory of law broader than Kelsen's, in which he "
            "came to see the centrality of 'political ideas'. Cooper "
            'discusses The Authoritarian State (1936), which argued that '
            'Austria was an administrative entity rather than a true body '
            "politic, the race books, and the concept of 'political religion' "
            'developed in 1938 to describe National Socialism, marking a '
            'shift from legal structure to spiritual order.'
        )),
    ('Eric Voegelin and the Continental Tradition: Explorations in Modern Political Thought', 2011, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826219107/eric-voegelin-and-the-continental-tradition/',
        basis='publisher description',
        abstract=(
            'An edited collection, by Lee Trepanier and Steven F. McGuire, on '
            "Eric Voegelin's relation to modern continental philosophy from "
            'Kant to Derrida. Voegelin is known as a critic of modernity, '
            'which he described as a Gnostic revolt against the structure of '
            'reality, and he held the modern continental philosophers '
            'complicit in it; yet his work also shows their influence. The '
            "editors' introduction reviews the course of his thought and his "
            'critique of modernity, then points to affinities between '
            'Voegelin and continental thinkers. The chapters, by established '
            'and newer Voegelin scholars, take up his intellectual '
            'relationship to individual figures including Hegel, Schelling, '
            "Kierkegaard, Heidegger and Gadamer, going beyond Voegelin's own "
            'readings of them to reassess how his response to the crisis of '
            'modernity stands within that tradition.'
        )),
    ('Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, and Others', 2018, 'Lexington Books'): dict(
        source='https://books.google.com/books?vid=ISBN9781498571722',
        basis='publisher description',
        abstract=(
            'An edited collection, by Lee Trepanier and Eugene Callahan, '
            'comparing leading twentieth-century critics of rationalism: '
            'Hans-Georg Gadamer, F. A. Hayek, Aurel Kolnai, Alasdair '
            'MacIntyre, Michael Oakeshott, Michael Polanyi, Gilbert Ryle, '
            'Eric Voegelin and Ludwig Wittgenstein. Starting from the '
            'observation that the practical failures of rationalism, such as '
            'the Holocaust and the Gulag, gained force from a theoretical '
            'diagnosis of it, the book asks whether these thinkers were '
            'attacking the same thing, and where their analyses overlap and '
            'differ. It argues that they shared the view that tradition keeps '
            'a place in the world as a store of wisdom, and it uses them as a '
            'starting point for asking whether a life increasingly shaped by '
            'political, technological, economic and cultural rationalisms is '
            'desirable, and what alternatives might be proposed.'
        )),
    ('Gesellschaft, Staat und Recht: Festschrift gewidmet Hans Kelsen zum 50. Geburtstage', 1931, 'Springer'): dict(
        source='https://digitale-objekte.hbz-nrw.de/storage2/2015/02/21/file_2/6021607.pdf',
        basis='catalogue',
        abstract=(
            "A Festschrift for Hans Kelsen's fiftieth birthday, edited by "
            'Alfred Verdross with the collaboration of Josef Dobretsberger '
            "and subtitled 'Untersuchungen zur reinen Rechtslehre' (studies "
            'in the Pure Theory of Law). Its philosophical-sociological part '
            'contains essays by Dobretsberger (epistemology and natural law), '
            'Felix Kaufmann (juristic and sociological concepts of law), '
            'Julius Kraft (pure and applied sociology), Julius Moór (the Pure '
            'Theory, natural law and legal positivism), Tomoo Otaka (future '
            "tasks of the Pure Theory) and Erich Voegelin ('Das Sollen im "
            "System Kants'). The juristic part has contributions by Walter "
            'Henrich, Josef L. Kunz, Adolf Merkl, Leonidas Pitamic, Fritz '
            'Schreier, Verdross (general principles of law as a source of '
            'international law), Franz Weyr and Kisaburo Yokota, on '
            'constitutional, international, private and administrative law '
            'and the theory of the hierarchical structure of law. An appendix '
            "by Rudolf Aladár Métall lists Kelsen's writings chronologically."
        )),
    ('Goethe after Two Centuries', 1952, 'Louisiana State University Press'): dict(
        source='https://openlibrary.org/books/OL5617738M',
        basis='catalogue',
        abstract=(
            'A collection of lectures given in the WLSU radio series of March '
            "1949 to January 1950, part of Louisiana State University's "
            'commemoration of the Goethe bicentennial, with a foreword by C. '
            "Hammer, Jr. The contributions cover several sides of Goethe's "
            'work and reputation: L. A. Willoughby on Goethe as natural '
            "philosopher, H. Rehder on 'the eternal Goethe', J. T. "
            'Krumpelmann on Goethe himself and on the Goethe bicentennial in '
            'Frankfurt am Main, C. L. Shaver on Goethe as theatre director, '
            "E. W. Voegelin on 'Goethe's Utopia', R. Heberle on sociological "
            'aspects of his works, G. C. Jaffe on his theory of colour, E. H. '
            'Behre on Goethe and anatomy, J. H. Uhler on Goethe and '
            'Shakespeare, and L. A. Lenel on Goethe and Albert Schweitzer.'
        )),
    ('Erziehung zur Freiheit', 1959, 'Eugen Rentsch'): dict(
        source='https://digitale-objekte.hbz-nrw.de/storage2/2019/07/02/file_1/8488815.pdf',
        basis='catalogue',
        abstract=(
            'A collection of essays on freedom, with a foreword by Albert '
            "Hunold. The contributors and topics are: Carlo Antoni on Croce's "
            'philosophy of freedom, Hannah Arendt on freedom and politics, '
            'Hans Barth on the nature and origin of thought hostile to '
            'freedom, Louis Baudin on freedom through history, Goetz Briefs '
            'on trade unions and freedom, Wilhelm Flitner on the educational '
            'problem of freedom, F. A. Hayek on responsibility and freedom, '
            'Werner Kägi on federalism and freedom, Theodor Litt on the '
            'freedom of the person and the orders of life, Karl R. Popper on '
            'what the West believes in, Hermann Priebe on the peasantry and '
            'freedom, Wilhelm Röpke on education for economic freedom, Helmut '
            'Schoeck on intellectualism and political impotence, Emil Staiger '
            'on Goethe and human freedom, and Eric Voegelin on readiness for '
            "discussion ('Diskussionsbereitschaft'). An index and "
            'biographical notes are appended.'
        )),
    ('Christentum und Liberalismus', 1960, 'Zink'): dict(
        source='https://digitale-objekte.hbz-nrw.de/storage2/2019/05/20/file_3/8466881.pdf',
        basis='catalogue',
        abstract=(
            'A collection of essays on the relation between Christianity, '
            'especially Catholic social and political thought, and '
            'liberalism. Eric Voegelin opens the volume with an essay on '
            'liberalism and its history. Erich Mende then outlines the '
            'conception of the state in political liberalism, and Paul Mikat '
            'the basic elements of the Catholic conception of the state. '
            'Gustav Gundlach, S.J., discusses Catholic social teaching and '
            'the liberal economic order, and Alexander Rüstow treats '
            'palaeoliberalism, collectivism and neoliberalism in the economic '
            'and social order. The last two essays concern cultural policy: '
            'Paul Luchtenberg on the nature and aims of liberal cultural '
            'policy, and Wilhelm Geiger on state and culture.'
        )),
    ("L'histoire et ses interprétations: Entretiens autour de Arnold Toynbee", 1961, 'Mouton'): dict(
        source='https://books.google.com/books?vid=ISBN9782705683726',
        basis='publisher description',
        abstract=(
            "The proceedings of a colloquium on Arnold Toynbee's "
            'interpretation of history, held at the Centre culturel '
            'international de Cerisy-la-Salle in July 1958 under the auspices '
            'of the École pratique des hautes études and directed by Raymond '
            "Aron; the volume appeared in the school's 'Congrès et colloques' "
            'series and was reissued by Hermann in 2012. It contains papers '
            'by Aron, Jean Daniélou, Lucien Goldmann and Paul Ricoeur among '
            'others, a statement by Toynbee himself, and records of the '
            'discussions, with interventions by participants including Othmar '
            'Anderle, François Bourricaud, François Châtelet, Jacques '
            'Madaule, Henri Marrou, Clémence Ramnoux and Maxime Rodinson. The '
            'exchanges address the broader problem of history and how it is '
            'to be interpreted.'
        )),
    ('The Old Testament and Christian Faith: A Theological Discussion', 1963, 'Harper & Row'): dict(
        source='https://books.google.com/books?vid=ISBN9781608996865',
        basis='catalogue',
        abstract=(
            'A theological symposium, edited by Bernhard W. Anderson, on the '
            'place of the Old Testament in Christian faith, first published '
            'by Harper & Row in 1963 and later reissued by Wipf and Stock. It '
            "opens with Rudolf Bultmann's essay 'The Significance of the Old "
            "Testament for the Christian Faith', followed by contributions "
            "from Alan Richardson, Carl Michalson, Eric Voegelin ('History "
            "and Gnosis'), Wilhelm Vischer, John L. McKenzie, Oscar Cullmann, "
            'James M. Robinson, John Dillenberger, G. Ernest Wright, Claus '
            'Westermann, Anderson and Emil Brunner. Chapter titles include '
            "'Is the Old Testament the Propaedeutic to Christian Faith?', "
            "'Bultmann against Marcion', 'Everywhere the Scripture Is about "
            "Christ Alone', 'The Way of the Promise through the Old "
            "Testament', 'The New Covenant and the Old' and 'The Significance "
            "of the Old Testament for Our Faith'."
        )),
    ('Die unternehmerische Verantwortung in unserer Gesellschaftsordnung (Veröffentlichungen der Walter-Raymond-Stiftung, Bd. 4)', 1964, 'Westdeutscher Verlag'): dict(
        source='https://digitale-objekte.hbz-nrw.de/storage2/2023/10/10/file_8/9444758.pdf',
        basis='catalogue',
        abstract=(
            'The proceedings of a series of three colloquia held by the '
            'Walter-Raymond-Stiftung on the responsibility of entrepreneurs '
            'in the present social order, introduced by Ludwig Vaubel. The '
            'first colloquium sets out the theme in general terms, with '
            'papers by Hans Freyer on the social order from the French '
            'Revolution to the present, Alwin Münchmeyer on freedom and '
            'obligation in the social market economy, Arnold Gehlen on the '
            'social order amid conflicting interest groups, and Eric Voegelin '
            'on democracy and industrial society, summarised by Gustav '
            'Gundlach. The second treats the theme from the standpoint of the '
            'firm, including Ludwig von Friedeburg on works constitution and '
            'co-determination with discussion. The third looks beyond the '
            'firm, with Gerhard Leibholz on associations and the state and '
            "papers on employers' associations, chambers of commerce and "
            'other organisations, summarised by Günter Schmölders.'
        )),
    ('Zeit und Geschichte: Dankesgabe an Rudolf Bultmann zum 80. Geburtstag', 1964, 'J. C. B. Mohr (Paul Siebeck)'): dict(
        source='https://digitale-objekte.hbz-nrw.de/storage2/2020/10/17/file_1/8940926.pdf',
        basis='catalogue',
        abstract=(
            "A tribute volume for Rudolf Bultmann's eightieth birthday, "
            'edited by Erich Dinkler, with about forty-five contributions in '
            'German and English. The first, exegetical part treats '
            "eschatology, Jesus' expectation of the end, Q, Mark, Luke-Acts "
            'and the Pauline letters, with essays by Nils A. Dahl, Amos '
            'Wilder, W. G. Kümmel, Ernst Käsemann, Helmut Koester, James M. '
            'Robinson, Philipp Vielhauer, Günther Bornkamm, Hans Conzelmann, '
            'Ernst Haenchen and others. The systematic part covers theology '
            '(Gerhard Ebeling, Ernst Fuchs, Heinrich Ott, Schubert Ogden, '
            'Herbert Braun, Friedrich Gogarten and others) and philosophy, '
            'including Hans-Georg Gadamer on Heidegger and Marburg theology, '
            "a passage from Heidegger's last Marburg lectures, and Hans Jonas "
            'on Romans 7. A final part, on concrete applications and '
            "contemporary history, contains Eric Voegelin's 'Ewiges Sein in "
            "der Zeit' and essays on Faulkner, Francis Bacon, Hamann and "
            'Kierkegaard, euthanasia and religious education.'
        )),
    ('Historica: Studien zum geschichtlichen Denken und Forschen. Festschrift für Friedrich Engel-Janosi', 1965, 'Herder'): dict(
        source='https://digitale-objekte.hbz-nrw.de/storage2/2022/04/04/file_1/9141814.pdf',
        basis='catalogue',
        abstract=(
            'A Festschrift for the historian Friedrich Engel-Janosi, edited '
            'by Hugo Hantsch and offered by friends and colleagues, subtitled '
            "'Studien zum geschichtlichen Denken und Forschen' (studies in "
            "historical thought and research). After Hantsch's foreword, the "
            'contents open with essays on the philosophy of history: Eric '
            "Voegelin's 'Was ist Natur?', Frederic C. Lane on human history "
            'and natural history, and Robert A. Kann on Hermann Broch and the '
            'philosophy of history. Further contributions treat the '
            'historiography of the Second World War (Kent Roberts Greenfield) '
            'and Austrian and Habsburg history: Erich Zöllner on concepts of '
            'Austria, Hans Sturmberger on the Habsburg ideal of the prince, '
            'Max Braubach on Prince Eugene and Jansenism, Adam Wandruszka on '
            "the background of Josephinism, Franco Valsecchi on Joseph II's "
            'reforms in Lombardy, and Hantsch on Archduke Franz Ferdinand and '
            'Count Berchtold.'
        )),
    ('Die deutsche Universität im Dritten Reich: Eine Vortragsreihe der Universität München', 1966, 'R. Piper'): dict(
        source='https://digitale-objekte.hbz-nrw.de/storage2/2015/03/27/file_2/6075187.pdf',
        basis='catalogue',
        abstract=(
            'Eight lectures from a series held at the University of Munich on '
            'the German university under National Socialism. Helmut Kuhn '
            'describes the German university on the eve of the Nazi seizure '
            'of power; Joseph Pascher recounts the Third Reich as experienced '
            'at three German universities; Hans Maier examines National '
            'Socialist higher-education policy; Wolfgang Kunkel writes on the '
            'professor in the Third Reich and Otto B. Roegele on the student; '
            'Fritz Leist considers the possibilities and limits of resistance '
            'within the university; and Friedrich G. Friedmann reflects on '
            "emigration and return. The series closes with Eric Voegelin's "
            'lecture on the German university and the order of German '
            'society.'
        )),
    ('Aufklärung und Materialismus im Frankreich des 18. Jahrhunderts', 1968, 'Paul List Verlag'): dict(
        source='https://digitale-objekte.hbz-nrw.de/storage/2009/05/01/file_17/2980736.pdf',
        basis='catalogue',
        abstract=(
            "A volume in the series 'Geschichte des politischen Denkens', "
            'edited by Arno Baruzzi, on the materialist thinkers of the '
            'French Enlightenment. After an introduction, Baruzzi contributes '
            'a general essay on the French materialists of the eighteenth '
            'century and chapters on La Mettrie and on Sade; the chapter on '
            'Helvétius is by Eric Voegelin and Peter Leuschner, and that on '
            'Diderot by Tilo Schabert. The book closes with notes, '
            'bibliographical and biographical guides, an index of persons and '
            'subjects, and notes on the authors.'
        )),
    ('Phenomenology and Social Reality: Essays in Memory of Alfred Schutz', 1970, 'Martinus Nijhoff'): dict(
        source='https://link.springer.com/book/10.1007/978-94-011-7523-4',
        basis='publisher description',
        abstract=(
            'A memorial volume for the phenomenologist and social theorist '
            'Alfred Schutz (Vienna 1899 - New York 1959), edited by Maurice '
            'Natanson for the seventieth anniversary of his birth and the '
            'tenth of his death. The essays are offered by friends, '
            "colleagues and former students as a tribute; the editor's "
            'introduction gives biographical information and a brief memoir, '
            'covering his Viennese upbringing, wartime service in the '
            'Austrian army and law doctorate from the University of Vienna. '
            'The fourteen contributions are by Marvin Farber, Richard M. '
            'Zaner, Aron Gurwitsch, Werner Marx, Thomas Luckmann, Natanson, '
            "Fritz Machlup, Adolph Lowe, Arvid Brodersen, Eric Voegelin ('The "
            "Eclipse of Reality'), Philip Merlan, Peter L. Berger, Fred "
            'Kersten and Emanuel Winternitz, on topics including '
            'epistemology, the life-world and its sub-worlds, the boundaries '
            'of the social world, economics, alienation in Marx, multiple '
            'realities in Musil, myth and history, and music in Leonardo.'
        )),
    ('Transcendence and History: The Search for Ultimacy from Ancient Societies to Postmodernity', 2003, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826222190/transcendence-and-history/',
        basis='publisher description',
        abstract=(
            "Glenn Hughes examines what Eric Voegelin called 'the decisive "
            "problem of philosophy': the discovery of transcendent meaning "
            'and its effect on human self-understanding. The major religious '
            'and wisdom traditions rest on that recognition, yet over the '
            'past three centuries Western thought has increasingly resisted '
            'it, and contemporary and postmodern accounts of the human '
            'situation show a loss of confidence in it. Drawing chiefly on '
            'Voegelin and Bernard Lonergan, Hughes traces the historical '
            'discovery of transcendence and what it implies for the structure '
            'of history, concentrating on transcendence in relation to '
            'historical existence. Chapters treat experiences and symbols of '
            "transcendence, the 'terror of history', apocalypse, Gnosticism "
            'and historiogenesis, Ezra Pound, divine presence in the cosmos '
            'and in consciousness, and close with Ernest Becker and the drama '
            'of universal humanity.'
        )),
    ('New Political Religions, or An Analysis of Modern Terrorism', 2004, 'University of Missouri Press'): dict(
        source='https://upress.missouri.edu/9780826216212/new-political-religions-or-an-analysis-of-modern-terrorism/',
        basis='publisher description',
        abstract=(
            "Barry Cooper applies Eric Voegelin's political science to modern "
            'terrorism, arguing that most studies neglect the spiritual '
            "motivation of today's terrorists, which they file under the "
            "vague heading of religion. In its place he uses Voegelin's "
            'Schellingian notion of pneumopathology, a disease of the spirit, '
            'to separate groups pursuing more or less rational political ends '
            'from those with apocalyptic aims, for whom killing matters more '
            "than exploiting grievances. Using Voegelin's distinction between "
            'first reality (common-sense reality, including legitimate '
            'grievances) and second reality (an imaginary objective pursued '
            'by those whose reason is obscured), he analyses two groups '
            'showing a pneumopathological consciousness: Aum Shinrikyo, '
            'responsible for the 1995 Tokyo subway poisoning, and Al-Qaeda, '
            'responsible for the 11 September 2001 attacks. A closing chapter '
            'considers what is distinctive about terrorist networks, their '
            'limits, and how they might be countered.'
        )),
    ('Etty Hillesum and the Flow of Presence: A Voegelinian Analysis', 2008, 'University of Missouri Press'): dict(
        source='https://books.google.com/books?vid=ISBN9780826217974',
        basis='publisher description',
        abstract=(
            'Meins G. S. Coetsier reads the life and writings of Etty '
            'Hillesum, the young Dutch Jewish diarist who died at Auschwitz '
            "aged twenty-nine, through Eric Voegelin's philosophy of "
            'consciousness, especially his account of luminous participation '
            'in the transcendent ground of being. Working from her letters '
            'and diaries in the Dutch originals, Coetsier follows how her '
            'inward, mystically rooted resistance to Nazism developed and '
            'follows the symbolism of her spiritual journey with the help of '
            "Voegelin's analysis of experience and symbolisation. He argues "
            "that attunement to the 'flow of presence', Voegelin's term for "
            'human responsiveness to the divine, is the key to her life and '
            'writing, and he gives particular attention to the transformation '
            'she underwent near the end of her life and her understanding of '
            "each person's contribution to sustaining the human spirit."
        )),
    ('Teaching in an Age of Ideology', 2012, 'Lexington Books'): dict(
        source='https://books.google.com/books?vid=ISBN9780739173596',
        basis='publisher description',
        abstract=(
            'An edited collection, by John von Heyking and Lee Trepanier, on '
            'prominent twentieth-century philosophers and political thinkers '
            'in their role as teachers, and on how they conveyed truth to '
            'students in the face of ideological pressures in the university '
            'and society. Its subjects include philosophers (Edmund Husserl, '
            'Hannah Arendt), political thinkers (Eric Voegelin, Leo Strauss) '
            'and students of theirs, including Ellis Sandoz, Stanley Rosen '
            'and Harvey Mansfield, considered as teachers who analysed, '
            'denounced and tried to move beyond ideology toward a more '
            'genuine way of thinking. The volume presents teaching not merely '
            'as conveying concepts but as a way of living in the world, the '
            'philosophical search for truth amid ideological deformation. Its '
            "sections include 'The Teacher's Search for Order' and 'The "
            "Teaching of Natural Rights Today'."
        )),
    ('The Growth of the Race Idea', 1940, 'The Review of Politics'): dict(
        source='https://www.cambridge.org/core/journals/review-of-politics/article/abs/growth-of-the-race-idea/623E7171D220F69F7BDDAE2B2F34B1F2',
        basis='opening page',
        abstract=(
            'Voegelin traces the growth of the race idea, taken not as the '
            'natural-science concept of race but as a political idea. He sets '
            'aside several questions at the outset: how the human races are '
            'classified, eugenic improvement of populations, and relations '
            'between white and coloured races. His subject is the race idea '
            'as modern creeds of the National Socialist type use it to '
            'integrate a community spiritually and politically.'
        )),
    ('Nietzsche, the Crisis and the War', 1944, 'The Journal of Politics'): dict(
        source='https://doi.org/10.4324/9781315254968-4',
        basis='publisher abstract',
        note='Paraphrased from the abstract shown for the 2017 Routledge reprint of the 1944 article.',
        abstract=(
            "The essay discusses whether Nietzsche's critique of Western "
            'civilisation should be set aside as merely expressive, or even '
            'causative, of a specifically German view of politics. It cites '
            "H. L. Stewart's study, which counted Nietzsche among the causes "
            'of the German state of mind behind the First World War. It then '
            "turns to George Santayana's Egotism in German Philosophy, which "
            'Voegelin counts among the great interpretations of Nietzsche '
            'occasioned by the war of 1914-1918. Taking egotism as his '
            "criterion, Santayana could partly agree with Nietzsche's "
            'diagnosis of the crisis. Voegelin judges the category of egotism '
            'an excellent instrument for interpreting both the crisis, German '
            'and general, and Nietzsche, but only up to a certain point.'
        )),
    ("The Philosophy of Existence: Plato's Gorgias", 1949, 'The Review of Politics'): dict(
        source='https://www.cambridge.org/core/journals/review-of-politics/article/abs/philosophy-of-existence-platos-gorgias/D95DC9133C18841CD065C020957D1B2E',
        basis='opening page',
        abstract=(
            "This is a study of Plato's Gorgias as a philosophy of existence. "
            'Voegelin reads the dialogue, which opens with the words "war and '
            'battle", as a declaration of war on a corrupt society. He looks '
            "at its dramatic setting: Gorgias visits Callicles' house, and "
            'Polus and Chaerephon open the exchange. He argues that Plato '
            'signals the deeper motive through the form of the dialogue '
            'rather than stating it. At stake is a struggle for the soul of '
            "the younger generation, over who will form the polity's future "
            'leaders: the rhetor who teaches the techniques of political '
            'success, or the philosopher who creates spiritual substance in '
            'soul and society.'
        )),
    ('The Formation of the Marxian Revolutionary Idea', 1950, 'The Review of Politics'): dict(
        source='https://www.cambridge.org/core/journals/review-of-politics/article/abs/formation-of-the-marxian-revolutionary-idea/786B5C16D5E489E4129C94538C766359',
        basis='opening page',
        abstract=(
            "This article studies how Marx's idea of the great proletarian "
            'revolution was formed. In that idea the revolution ends the '
            'pre-history of mankind and opens its true history. Voegelin '
            "notes that the idea's public career after the Communist "
            'Manifesto of 1848 is well known, but its formation in the '
            'preceding decade is not. One reason is that the source materials '
            'have been fully available only since 1932. Monographs have '
            "clarified details, but a comprehensive study of the idea's "
            'genesis is still lacking, and this article addresses that gap.'
        )),
    ("Machiavelli's Prince: Background and Formation", 1951, 'The Review of Politics'): dict(
        source='https://www.cambridge.org/core/journals/review-of-politics/article/abs/machiavellis-prince-background-and-formation/5D1610BC1F59A79091D1D4768C845B3B',
        basis='opening page',
        abstract=(
            "Voegelin sets out to move the study of Machiavelli's Prince "
            'beyond the moralistic condemnation that Counter-Reformation '
            'propaganda fixed on it. He grants that the caricature records '
            'something real: a sharp break with traditional ways of treating '
            'politics, and the threshold of a modern era. But he rejects the '
            "picture of Machiavelli as a solitary moral freak. Machiavelli's "
            'ideas had a long pre-history and were shared by his '
            'contemporaries. The article reconstructs that background and the '
            'circumstances that led Machiavelli to crystallise the ideas of '
            'his age in the symbol of a Prince who, through fortuna and '
            'virtu, would save and restore Italy.'
        )),
    ('The World of Homer', 1953, 'The Review of Politics'): dict(
        source='https://www.cambridge.org/core/journals/review-of-politics/article/abs/world-of-homer/CB2CDDB54D69E09E1C121A67FC8867C3',
        basis='opening page',
        abstract=(
            'Voegelin examines the political and spiritual world of the '
            'Homeric epics. He finds that in the Iliad the constitutional '
            'order of the Achaean army still works, but under strain, which '
            'points to a general malaise and impending disaster. He rejects '
            'the eighteenth-century picture of Homer as the naive, fresh '
            'voice of a young people. Instead he argues that Hellenic culture '
            'was a recovery after a catastrophic dark age, and that Homer was '
            "a pre-Hellenic poet and thinker of a dying civilisation. Homer's "
            'freshness is that of a great observer and artist, not of the '
            'culture he describes. Like Plato, he distilled the essence of a '
            'fading grandeur for posterity.'
        )),
    ('Demokratie und Industriegesellschaft', 1964, 'in: Die unternehmerische Verantwortung in unserer Gesellschaftsordnung (Veröffentlichungen der Walter-Raymond-Stiftung, Bd. 4)'): dict(
        source='https://doi.org/10.1007/978-3-663-02256-5_6',
        basis='publisher abstract',
        abstract=(
            'Voegelin addresses a gathering of entrepreneurs as a newcomer to '
            'the circle. He says he is surprised that they let themselves be '
            'pushed onto the defensive by an image of the entrepreneur drawn '
            "from labour's attacks and intellectuals' cliches. He would have "
            'expected confident anger, given the achievement of building a '
            'flourishing economy from the post-war ruins. He argues that the '
            'traditional image grew out of past situations and is now '
            'obsolete in light of trends in Western, especially American, '
            'economy and society, and he points to phenomena that contradict '
            'it. He also questions the taken-for-granted identification of '
            'the entrepreneur with the industrial entrepreneur. That '
            'identification, he argues, rests on a common worldview of an '
            'industrial society whose great social problem is the conflict of '
            'interest and power between employers and workers.'
        )),
    ('Immortality: Experience and Symbol', 1967, 'Harvard Theological Review'): dict(
        source='https://www.cambridge.org/core/journals/harvard-theological-review/article/abs/immortality-experience-and-symbol/8E08CCB4709F38EF10188942257365A7',
        basis='opening page',
        abstract=(
            'This lecture was delivered at Harvard. In it Voegelin treats '
            'immortality as one of the language symbols engendered by a class '
            'of experiences, which he calls, after an established precedent, '
            'the varieties of religious experience. He adopts the term so '
            'that he and his audience share an immediate understanding of the '
            'subject. His inquiry concerns immortality as a symbol and the '
            'experiences that engender it.'
        )),
    ('Equivalences of Experience and Symbolization in History', 1970, 'in: Eternità e storia: I valori permanenti nel divenire storico'): dict(
        source='https://doi.org/10.3917/leph.092.0255',
        basis='publisher abstract',
        note='Paraphrased from the abstract of the first French translation, Les Etudes philosophiques, 2009.',
        abstract=(
            'In this 1970 essay Voegelin sets out explicitly the principles '
            'of his approach to history. He interprets the history of mankind '
            'as a sequence, discontinuous in time, of differing degrees to '
            'which the human soul opens to the mystery of the ground of '
            'being, or closes itself to it in periods when reality is '
            'deformed. In doing so he breaks with the unilinear visions of '
            'history that have marked Western thought since the eighteenth '
            'century, visions the abstract describes as a disastrous form of '
            'spiritual imperialism.'
        )),
    ('The Eclipse of Reality', 1970, 'in: Phenomenology and Social Reality: Essays in Memory of Alfred Schutz'): dict(
        source='https://link.springer.com/chapter/10.1007/978-94-011-7523-4_10',
        basis='publisher abstract',
        abstract=(
            'Voegelin analyses how a person can, by an act of imagination, '
            'contract himself into a self that is "condemned to be free". For '
            'this contracted self, traditional faith and the past have lost '
            'their meaning. The present becomes a movement away from the '
            "self's inessential givens, the future becomes a field of "
            'options, and freedom becomes the inescapable task of choosing '
            "what one's existence is to be. The essay presents this freedom "
            'as a curse, since the contracted self cannot escape being free.'
        )),
    ('On Hegel: A Study in Sorcery', 1971, 'Studium Generale'): dict(
        source='https://link.springer.com/chapter/10.1007/978-3-642-65387-2_30',
        basis='publisher abstract',
        abstract=(
            'Voegelin begins from the observation that once the gods have '
            'been driven from the cosmos, the world that remains is a dull '
            'place. In the seventeenth century Pascal described this ennui as '
            'a private condition: the plight of a man who has lost his faith '
            'and seeks distractions to keep anxiety at bay. After the French '
            'Revolution, Hegel diagnosed the same ennui as the symptom of an '
            'entire historical epoch. In about a century and a half, the '
            'sense of being lost in a godless world had grown from a personal '
            'unease into a collective illness. (Abstract from the 1972 '
            'reprint in The Study of Time, ed. J. T. Fraser et al.)'
        )),
    ('On Classical Studies', 1973, 'Modern Age'): dict(
        source='https://modernagejournal.com/?p=228163',
        basis='full text',
        abstract=(
            "Voegelin starts from F. A. Wolf's definition of classical "
            "philology as the study of man's nature as it became manifest in "
            'the Greeks. He argues that this ideal has been overtaken by the '
            'fragmentation of scholarship into specialties and by the '
            'deculturation of Western society. Classical studies have been '
            'reduced to enclaves within the universities, and public interest '
            'has moved from the nature of man to the mastery of nature. He '
            'sets the classical understanding of human nature, of the '
            'movement from opinion to knowledge, and of society as man writ '
            'large against a modern climate of opinion hostile to the life of '
            'reason. He traces this climate through modern thinkers. He finds '
            'signs of a recovery of reason, and he calls for noetic analysis '
            'of the historical materials on myth, religion and empire, and '
            'for renewed study of the Greek analysis of existential '
            'deformation.'
        )),
}
