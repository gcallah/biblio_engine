"""Abstracts for entries in the database, used by load_abstracts.

Keyed by (title, year, where): "where" is the journal name, "in: <book
title>" for a chapter, or the publisher name for a book. Each abstract
paraphrases the online description at its source URL. Keep them under
1024 characters.
"""

ABSTRACTS = {
    ("Reason, Revolution and Political Theory: Notes on Oakeshott's 'Rationalism in Politics'", 1967, "People's Publishing House"): dict(
        source='https://mainstreamweekly.net/article7021.html',
        abstract=(
            "This book is the Indian Marxist political theorist Randhir Singh's"
            " response to Michael Oakeshott's Rationalism in Politics. Framed "
            "as notes on Oakeshott's collection, it offers a Marxist critique "
            "of the conservative theorist's attack on rationalism and was "
            'widely reviewed when it appeared. Later commentators, among them '
            "the editor of Singh's selected writings, treat it as more than a "
            'rebuttal: it is read as a theoretical statement in its own right '
            'on the nature of social enquiry, addressing the relations between '
            'science and philosophy, facts and values, and ideology and '
            'practice. Extracts from the book were reprinted in Selected '
            'Writings of Randhir Singh (2017).'
        )),
    ('Politics and Experience: Essays Presented to Professor Michael Oakeshott on the Occasion of His Retirement', 1968, 'Cambridge University Press'): dict(
        source='https://tuklas.up.edu.ph/Record/UP-99796217608823682',
        abstract=(
            'This volume is a Festschrift honouring Michael Oakeshott on his '
            'retirement from the London School of Economics, edited by Preston '
            'King and B. C. Parekh. It gathers essays by philosophers, '
            'historians and political theorists, including W. H. Walsh, William'
            ' Dray, R. S. Peters, Sheldon Wolin, J. G. A. Pocock, K. R. '
            'Minogue, Dorothea Krook and Donald Davie, on themes connected with'
            " Oakeshott's interests, such as the relation between the practical"
            ' and the historical past, paradigms in political theory, and '
            'revolution, tradition and political continuity. One essay examines'
            ' rationalism in the Israeli kibbutz movement. The book closes with'
            " W. H. Greenleaf's bibliography of Oakeshott's writings. It was "
            'reissued in paperback in 2011.'
        )),
    ('A Rationalist Malgré Lui: The Perplexities of Being Michael Oakeshott', 1976, 'Political Theory'): dict(
        source='https://doi.org/10.1177/009059177600400307',
        abstract=(
            'This essay, part of a 1976 symposium on On Human Conduct, contends'
            " that apart from his Hobbes scholarship, Oakeshott's importance as"
            ' a political philosopher before that book rests largely on his '
            'inaugural lecture "Political Education," with much of his other '
            'writing, including Rationalism in Politics, elaborating its theme.'
            ' Spitz argues that this theme matters both philosophically, as a '
            'challenge to received views of political theory, and doctrinally, '
            'as a rival to ordinary conservatism, one that he insists cannot be'
            ' harmonised with the conservatism some Americans have tried to '
            'align it with.'
        )),
    ('Contemporary Political Philosophers', 1976, 'Methuen'): dict(
        source='https://www.routledge.com/Contemporary-Political-Philosophers-Routledge-Revivals/Crespigny-Minogue/p/book/9780415614375',
        abstract=(
            'This collection surveys major developments in twentieth-century '
            'political philosophy through chapters on individual thinkers, '
            'written by scholars from Europe and North America. The figures '
            'covered are Herbert Marcuse, F. A. Hayek, Leo Strauss, Eric '
            'Voegelin, Michael Oakeshott, Karl Popper, Bertrand de Jouvenel, '
            'Raymond Aron, Jean-Paul Sartre, Hannah Arendt, C. B. Macpherson '
            'and John Rawls. It was written to introduce newcomers to these '
            'thinkers while offering critical discussion for readers already '
            'familiar with them, and was later reissued in the Routledge '
            'Revivals series.'
        )),
    ('Review Article: The Political Philosophy of Michael Oakeshott', 1979, 'British Journal of Political Science'): dict(
        source='https://doi.org/10.1017/S0007123400001940',
        abstract=(
            "This review essay concentrates on Oakeshott's political "
            'philosophy, leaving aside his writings on other subjects such as '
            'religion, law and aesthetics. Parekh identifies two central '
            'concerns in that work: an account of what philosophy, and '
            'political philosophy specifically, is; and a positive theory of '
            'political life. The first three sections of the essay set out how '
            'Oakeshott handles these two themes, and the final section '
            'evaluates how adequate his positions are.'
        )),
    ("Oakeshott's Conception of Civil Association: Notes for a Critical Analysis", 1981, 'Political Studies'): dict(
        source='https://doi.org/10.1111/j.1467-9248.1981.tb01325.x',
        abstract=(
            "Berki argues that Oakeshott's notion of civil association runs "
            'together two things that do not fit: a moral ideal of civility and'
            ' the actual state as an institution. He attributes this to the '
            'idealist habit of abstracting one aspect of reality from the rest.'
            ' Taken abstractly, civil association looks like an entirely moral '
            'bond set against purpose-driven enterprise associations; yet on '
            'closer analysis its premises presuppose such enterprises, and it '
            'only makes sense against a background of real inequality and '
            'conflict that Oakeshott leaves out. The article concludes that the'
            ' concept is hard to distinguish from utopian ideals.'
        )),
    ('Oakeshott and the Impossibility of Philosophical Politics', 1982, 'Political Studies'): dict(
        source='https://doi.org/10.1111/j.1467-9248.1982.tb00529.x',
        abstract=(
            "Hall and Modood examine Oakeshott's radical claim that philosophy "
            'can neither appraise nor recommend political ideas. Working '
            'through his reasoning stage by stage, they dispute the view that '
            'practical life, being made of changing, inconsistent and '
            "unreflective actions, shuts out philosophy's pursuit of final "
            'truth and calls for its own style of thinking. In their account '
            'Oakeshott overdraws the contrast between theory and practice and '
            'wrongly denies philosophy any practical bearing. The authors grant'
            ' that the two are distinct, but argue that distinctness does not '
            'mean separation: any reasoned assessment of political concepts '
            'needs philosophy.'
        )),
    ('Conceptions of Liberty in Political Philosophy', 1984, 'Athlone Press'): dict(
        source='https://stafforini.com/works/pelczynski-1984-conceptions-liberty-political-philosophy/',
        abstract=(
            'This collection of essays examines how liberty has been understood'
            ' by political philosophers from ancient Greece to the present, '
            "using Isaiah Berlin's distinction between negative and positive "
            'liberty as a recurring frame. Chapters address Hobbes, Locke, '
            'Rousseau, Kant, Hegel, Mill, Marx, Hayek and Oakeshott, among '
            'others. John Gray contributes an introduction and a closing essay '
            'on negative and positive liberty.'
        )),
    ("The Creation of the Past: British Idealism and Michael Oakeshott's Philosophy of History", 1984, 'History and Theory'): dict(
        source='https://doi.org/10.2307/2505006',
        abstract=(
            "The article situates Oakeshott's philosophy of history, a "
            "relatively neglected part of his work despite Collingwood's high "
            'praise for it, within the concerns of British idealism. Boucher '
            "argues that Oakeshott shared the idealists' central preoccupations"
            " and drew heavily on their conclusions. On Oakeshott's view, "
            'history, like other modes of understanding, constitutes its own '
            'object on its own postulates; the historical past is reached by '
            'reading present evidence as traces of vanished activity, and a '
            'practical past that speaks to present concerns lies outside '
            "history. The article also contrasts Oakeshott's ideas of "
            'coherence, continuity and identity in difference with '
            "Collingwood's notion of re-enactment."
        )),
    ('Michael Oakeshott as Liberal Theorist', 1985, 'Canadian Journal of Political Science'): dict(
        source='https://doi.org/10.1017/S0008423900059576',
        abstract=(
            'The article first resists two easy classifications of Oakeshott: '
            'as a Kantian liberal, on the strength of his formal account of '
            'civil association, and as a Burkean liberal, on the strength of '
            'his regard for inherited practice. Coats then surveys the main '
            "themes of Oakeshott's work to bring out its originality. He reads "
            "Oakeshott's theory of civil association as a coherent blend of "
            "three sources: Aristotle's idea of politics as concern for the "
            'common arrangements of a community, the liberal and Christian '
            'valuation of the individual, and the Roman conception of civil '
            'obligation owed to authority, which allows the first two to be '
            'reconciled.'
        )),
    ("The Legend of Oakeshott's Conservatism: Sceptical Philosophy and Limited Politics", 1985, 'Canadian Journal of Political Science'): dict(
        source='https://doi.org/10.1017/S0008423900030274',
        abstract=(
            'Rayner holds that Oakeshott has been widely misread as a spokesman'
            ' for modern conservatism, and that this label has hidden the real '
            "nature of his contribution. The article traces Oakeshott's "
            'treatment of politics as a limited, particular activity back to a '
            'more general scepticism about how what we believe bears on what we'
            " do. That scepticism, Rayner argues, owes more to Hume's call for "
            "moderation in theorising than to Burke's distrust of general "
            "ideas. Far from lacking political relevance, Oakeshott's work is "
            'read here as offering a sharp critique of conservatism as '
            'practised in Europe and America.'
        )),
    ('The Blackwell Encyclopaedia of Political Thought', 1987, 'Basil Blackwell'): dict(
        source='https://www.altpress.org/apc_library/display/1051',
        abstract=(
            'This reference work covers the history and theory of political '
            'thought from ancient to modern times, from Socrates to Rawls. Its '
            'roughly 350 entries, written by about 120 international '
            'specialists, mix longer survey articles with shorter definitions '
            'of concepts, thinkers and doctrines. It was edited by David Miller'
            ' with Janet Coleman, William Connolly and Alan Ryan as advisory '
            'editors.'
        )),
    ('Oakeshott on the Authority of Law', 1989, 'Ratio Juris'): dict(
        source='https://doi.org/10.1111/j.1467-9337.1989.tb00024.x',
        abstract=(
            "Friedman approaches Oakeshott's theory of law through his account "
            "of authority. He sets out Oakeshott's claim that the modern state "
            'is ambiguous, part civil association and part enterprise '
            'association. For Oakeshott, authority is not a matter of how '
            'subjects feel about rulers; it obtains when an act of government '
            'is itself taken as a reason to obey without conditions. Such '
            'authority is impossible in an enterprise association, where '
            'loyalty hinges on common purposes, and no rational-choice theory '
            'can justify it. Since political obligation therefore has no '
            'general solution, philosophy is left to give an abstract '
            'description of a law-governed state in which authority and liberty'
            ' coexist.'
        )),
    ("Oakeshott's Hobbesian Myth: Pride, Character and the Limits of Reason", 1990, 'Western Political Quarterly'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/oakeshotts-hobbesian-myth-pride-character-and-the-limits-of-reason/',
        abstract=(
            "The article argues that Oakeshott's radical philosophical "
            'scepticism, which doubts both thought detached from context and '
            "reason's primacy in understanding the world, carries a moral "
            'teaching that commentators have overlooked. That teaching, drawn '
            'from his reading of Hobbes, is embodied in the character of the '
            'self-respecting man of proper pride, who accepts the inherited '
            'myth of his civilization and pursues his own ends, not all of '
            'which can be rationally justified, in preference to communal ties.'
            " Frohnen presents this as Oakeshott's alternative both to utopian "
            'planning and to the disorder that follows when such myths are '
            'destroyed in the name of an illusory freedom.'
        )),
    ('The Political Philosophy of Michael Oakeshott', 1990, 'Yale University Press'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/the-political-philosophy-of-michael-oakeshott/',
        abstract=(
            "This book was the first full-length study of Michael Oakeshott's "
            'thought. Drawing on the whole of his published work, Franco '
            "situates Oakeshott's political philosophy within his wider "
            'philosophy. He begins with a close reading of Experience and its '
            "Modes, which he treats as a defence of philosophy's independence "
            'from the partial standpoints of science, history and practice and '
            "as the basis of Oakeshott's politics, and he examines the logic of"
            " experience underlying Oakeshott's account of the forms of "
            'knowledge. Franco places Oakeshott in a liberal tradition running '
            'from Hobbes through Hegel and Bosanquet, and argues that the '
            'theory of civil association in On Human Conduct is among the most '
            'sophisticated contemporary formulations of liberalism.'
        )),
    ('The Work of Michael Oakeshott', 1991, 'Political Theory'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/the-work-of-michael-oakeshott/',
        abstract=(
            'This short memorial essay, part of a Political Theory tribute '
            "following Oakeshott's death, reflects on his intellectual "
            'character and manner of writing. Fuller presents the essay as '
            "Oakeshott's favoured form, written as an invitation to "
            'conversation rather than as an attempt to settle debate, and '
            'places him in an English essayistic line running from Bacon and '
            'Hume to Macaulay and Mill. He also recalls Oakeshott as a '
            'perceptive but generous judge of people, with a romantic side.'
        )),
    ('Criticism and Tradition in Popper, Oakeshott and Hayek', 1992, 'Journal of Applied Philosophy'): dict(
        source='https://doi.org/10.1111/j.1468-5930.1992.tb00296.x',
        abstract=(
            'The article compares how three thinkers understand tradition. '
            'Popper is said to judge traditions rationalistically, by how well '
            'they serve aims that can be stated apart from them, while Hayek '
            'values traditions for helping a culture survive, in ways that may '
            "be hidden even from its members. O'Hear finds both views deficient"
            " beside Oakeshott's claim that traditions do not exist to serve "
            'goals and that ends cannot be defined apart from the ways of life '
            'of those who pursue them. Oakeshott is thus presented as occupying'
            " a middle position between Popper's rationalism and Hayek's anti-"
            'rationalism.'
        )),
    ('In Appreciation: Michael Oakeshott, Philosopher of Individuality', 1992, 'Review of Politics'): dict(
        source='https://doi.org/10.1017/S0034670500016090',
        abstract=(
            'This appreciation, published in a Review of Politics section '
            'honouring Oakeshott after his death, sets out to correct the '
            'picture given by most obituaries. Riley objects that the press '
            'portrayed Oakeshott either as a right-wing guru commenting on '
            'current affairs or as the philosophical source of Margaret '
            "Thatcher's policies, and he offers instead an account of Oakeshott"
            ' as a philosopher whose central concern was individuality.'
        )),
    ('Oakeshott and the Practice of Politics', 1992, 'Journal of Philosophical Research'): dict(
        source='https://doi.org/10.5840/jpr_1992_23',
        abstract=(
            "The article challenges Oakeshott's claim that political knowledge "
            'is purely practical, meaning that it cannot be stated in '
            'propositions or applied deliberately and is instead shown in '
            'conduct and passed on through example. Katzoff contends that this '
            'description fits mainly bodily skills that rest on unconscious '
            'physiological processes. Political activity, she argues, is '
            'largely governed by rules, many of which we can bring to mind by '
            'introspection, and there is good reason to think we can '
            'consciously and reflectively choose to apply them.'
        )),
    ('Cambridge Minds', 1994, 'Cambridge University Press'): dict(
        source='https://www.cambridge.org/core/journals/history-of-education-quarterly/article/richard-mason-ed-cambridge-minds-cambridge-eng-cambridge-university-press-1994-pp-xiii-237-cloth-3995-paper-1595/7B97292BD1E485F6C0F0D265BC621F9D',
        abstract=(
            'This collection of essays, written for a general readership, '
            'surveys the intellectual achievements associated with the '
            'University of Cambridge over roughly a century and a half. Each '
            'essay focuses on a notable Cambridge figure or field; examples '
            'include Ray Monk on Bertrand Russell, Ernest Gellner on James '
            'Frazer and Max Perutz on molecular biology.'
        )),
    ('Michael Oakeshott', 1994, 'in: Cambridge Minds'): dict(
        source='https://doi.org/10.1017/CBO9780511523007.017',
        abstract=(
            'This chapter, in a collection on notable Cambridge figures, '
            'introduces Oakeshott and his reputation. Grant notes that '
            'Oakeshott, who died in 1990, was respected but controversial among'
            ' colleagues and never achieved the public fame of contemporaries '
            'such as Hayek or his LSE predecessor Harold Laski, though his '
            'death and the warm obituaries that followed triggered a surge of '
            'interest in his work. The chapter considers why his public profile'
            ' stayed low, pointing first to his modest, retiring temperament, '
            'his small published output, and his repeated refusal of public '
            'honours.'
        )),
    ('Recasting Conservatism: Oakeshott, Strauss, and the Response to Postmodernism', 1994, 'Yale University Press'): dict(
        source='https://yalebooks.yale.edu/9780300068689/recasting-conservatism',
        abstract=(
            'This book examines the new conservative political theory that '
            'emerged in Britain and the United States, focusing on Michael '
            'Oakeshott, Leo Strauss and their followers. Devigne reads both as '
            'responses to postmodernism and to the erosion of civil traditions,'
            ' moral norms and authority in contemporary societies. He argues '
            'that these theories are not simply variants of economic liberalism'
            ' but attempts to establish new forms of political and civil '
            'authority, and that their different philosophical roots yield '
            'distinct constitutional doctrines and political aims. The book '
            "traces these differences through the two schools' views of "
            'morality, authority, democracy, liberty, justice, community and '
            'religion, and their policy preferences, and compares them with '
            'earlier dominant British and American political outlooks.'
        )),
    ('Voices in Conversation: Philosophy and Politics in the Work of Michael Oakeshott', 1995, 'Journal of Politics'): dict(
        source='https://doi.org/10.2307/2960190',
        abstract=(
            'This article disputes the widely held view that Oakeshott kept '
            'philosophy rigidly apart from politics throughout his career. '
            'Gerencser contends that the strict separation rested on '
            "Oakeshott's early idealism, which he later left behind, and that "
            'from the 1940s he allowed for a looser, more contingent relation '
            'between theory and practice. That relation is best captured by '
            "Oakeshott's image of different voices in conversation. The article"
            " closes by suggesting that this reading of Oakeshott's sceptical, "
            "ironic temperament gives some support to Richard Rorty's treatment"
            ' of him as a fellow liberal ironist.'
        )),
    ('Adventures of Self-Understanding: Gadamer, Oakeshott and the Question of Education', 1996, 'Journal of the British Society for Phenomenology'): dict(
        source='https://doi.org/10.1080/00071773.1996.11007167',
        abstract=(
            'This article compares the educational thought of Hans-Georg '
            'Gadamer and Michael Oakeshott. Lawn argues that both work from a '
            'non-epistemological understanding of knowledge rooted in a shared '
            "reading of Aristotle's idea of phronesis, or practical wisdom. "
            'Drawing on the themes of self-understanding, dialogue and '
            "tradition, the article shows how Gadamer's hermeneutics and "
            "Oakeshott's critique of rationalism in politics converge in a "
            'common defence of liberal education.'
        )),
    ('The Political Classics: Green to Dworkin', 1996, 'Oxford University Press'): dict(
        source='https://www.schweitzer-online.de/en/buch/Forsyth/Political-Classics/9780198780953/A28044802/',
        abstract=(
            'This collection, intended mainly for undergraduate students of '
            'political theory, offers twelve chapters, each by a different '
            'author, analysing a key text by a major political thinker from T. '
            'H. Green to Ronald Dworkin. The thinkers include Sorel, Gramsci, '
            'Schmitt, Oakeshott, Berlin, Arendt, Hayek, Hart, Rawls and Nozick.'
            ' The chapters concentrate on the ideas in each text rather than on'
            " the authors' lives, and each provides suggestions for further "
            'reading.'
        )),
    ("Oakeshott's Claims of Politics", 1997, 'Political Studies'): dict(
        source='https://doi.org/10.1111/1467-9248.00108',
        abstract=(
            'The article argues that reading Oakeshott chiefly as a political '
            'philosopher can obscure his central account of civil association, '
            'a far wider idea than politics. Worthington nonetheless insists '
            "that Oakeshott's positive view of politics should not be lost when"
            ' attention shifts to civil association, since politics is an '
            "activity civil association cannot do without. On Oakeshott's "
            'account, politics treats civil rules not as authoritative '
            'conditions or as matters for adjudication or command, but as '
            'proposals to be argued over in terms of their desirability. The '
            'article examines this conception of politics and its positive and '
            'negative relations to the practice of civil association.'
        )),
    ('Oakeshott, Wittgenstein and the Practice of Social Science', 1998, 'Journal for the Theory of Social Behaviour'): dict(
        source='https://doi.org/10.1111/1468-5914.00079',
        abstract=(
            'This article considers what sociology is and the logical limits '
            'that its subject matter sets on its practice. It starts from '
            "Oakeshott's distinction between technical and practical knowledge "
            'and his notion of abridgment, and applies the resulting view of '
            'human action to show that sociology involves its own kind of '
            "abridgment. Using Wittgenstein's conception of philosophy, "
            'Costelloe argues that sociological inquiry is best understood as '
            "description. He then critically assesses Harvey Sacks's idea of a "
            "'primitive, natural science', claiming its shortcomings come from "
            "neglecting Oakeshott's insights into human action, and ends by "
            'drawing out implications of the argument.'
        )),
    ("Sartre's Radicalism and Oakeshott's Conservatism: The Duplicity of Freedom", 1998, 'Macmillan'): dict(
        source='https://doi.org/10.1057/9780230380264',
        abstract=(
            'This book compares the political thought of Jean-Paul Sartre and '
            'Michael Oakeshott around the question of human freedom: if human '
            'beings have no fixed nature, can they remake themselves? Farr '
            'takes Sartre as the representative of a radical answer and '
            'Oakeshott of a conservative one, and uses the contrast to set out '
            'how radical and conservative thought understand social order and '
            'the human self. After an introductory discussion of freedom, the '
            'book devotes separate chapters to each thinker. A review in '
            'Redescriptions noted that the analysis relies on sharp dichotomies'
            ' and questioned its relative neglect of Aristotle and Hobbes as '
            'sources for Oakeshott.'
        )),
    ('A Democratic Oakeshott?', 1999, 'Political Research Quarterly'): dict(
        source='https://doi.org/10.1177/106591299905200409',
        abstract=(
            'This article asks why some radical democratic theorists have taken'
            " an interest in Oakeshott's political thought. Gerencser examines "
            "Oakeshott's distinction between civil and enterprise association "
            'and his preference for the former, locating the key difference in '
            'how each relates power to freedom in the modern state: enterprise '
            'association, conceived as the state, cannot preserve the freedom '
            'it promises, while civil association can. He argues that '
            'Oakeshott, though doubtful that a common good could ground the '
            'state, is not equally doubtful about the consensus needed to '
            'recognise civil authority. Even so, by taking questions of '
            'authority out of politics, Oakeshott ironically points to a space '
            'for democratic citizenship.'
        )),
    ('Political Philosophers of the Twentieth Century', 1999, 'Blackwell'): dict(
        source='https://www.wiley-vch.de/en/areas-interest/humanities-social-sciences/political-philosophers-of-the-twentieth-century-978-0-631-20261-5',
        abstract=(
            'This book surveys the work of leading twentieth-century political '
            'philosophers: Max Weber, Herbert Marcuse of the Frankfurt School, '
            'Hannah Arendt, C. B. Macpherson, Michael Oakeshott, Friedrich '
            'Hayek, Karl Popper, Isaiah Berlin, John Rawls, Robert Nozick and '
            'Jürgen Habermas. It concludes by asking whether we have reached '
            "'the end of history'. A later review described it as more "
            'accessible than larger reference histories of twentieth-century '
            'political thought.'
        )),
    ('A Skeptical Conservative – Michael Oakeshott, Former Chair of Political Science at London School of Economics', 2000, 'National Interest'): dict(
        source='https://law-journals-books.vlex.com/vid/skeptical-conservative-52822818',
        abstract=(
            "Written about a decade after Oakeshott's death, this essay "
            'reassesses his reputation and influence. McInnes notes that '
            'Oakeshott left no school of followers and discusses his '
            'appointment at the London School of Economics. He rejects the idea'
            ' that Margaret Thatcher drew her philosophy from Oakeshott, '
            'arguing that her free-market programme was the kind of rationalist'
            ' politics Oakeshott opposed and owed more to Hayek. The essay '
            "presents Oakeshott's conservatism as scepticism about political "
            'activism itself: politics for him was a limited, largely custodial'
            ' activity ranking below art, literature and philosophy, and '
            'political science offered little insight into human conduct.'
        )),
    ('Michael Oakeshott and the City of God', 2000, 'Political Theory'): dict(
        source='https://doi.org/10.1177/0090591700028003004',
        abstract=(
            "This article examines Oakeshott's treatment of religious "
            'experience. Worthington shows that Oakeshott addresses religion '
            'directly, setting out a post-moralist understanding of salvation, '
            'and argues that religious experience has a part to play both in '
            "Oakeshott's own civil philosophy and in present-day conceptions of"
            ' individuality.'
        )),
    ('Michael Oakeshott and the Idea of Liberal Education', 2000, 'Social Theory and Practice'): dict(
        source='https://doi.org/10.5840/soctheorpract200026312',
        abstract=(
            'This article takes up the debates and sense of crisis surrounding '
            'liberal education in the United States and approaches them through'
            " Oakeshott's philosophy. McCabe considers the place of the "
            "university within a liberal society and defends Oakeshott's ideal "
            'of liberal learning against objections raised from both '
            'conservative and multiculturalist positions.'
        )),
    ('Oakeshott and His Contemporaries: Montaigne, St. Augustine, Hegel, et al.', 2000, 'Susquehanna University Press'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/oakeshott-and-his-contemporaries/',
        abstract=(
            "This short book studies Michael Oakeshott's ideas by setting them "
            'beside related themes in seven European thinkers: Montaigne, St. '
            'Augustine, Hegel, Hobbes, Benjamin Constant, Rousseau and Hume. By'
            ' showing where Oakeshott modifies, extends or departs from these '
            'writers, Coats aims to bring out the significance and internal '
            "coherence of Oakeshott's own concerns. It was reviewed by Timothy "
            'Fuller in the American Political Science Review.'
        )),
    ("The Skeptic's Oakeshott", 2000, "St. Martin's Press"): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/the-skeptics-oakeshott/',
        abstract=(
            "This book argues that Michael Oakeshott's political philosophy is "
            'best understood through his scepticism and his kinship with Thomas'
            ' Hobbes, rather than through the British idealist tradition with '
            'which he is often associated. Gerencser contends that Oakeshott '
            "adopts Hobbes's view of consent as the ground of political "
            'authority but softens it, locating authority in acknowledgement '
            'and recognition, and that this move leaves room for democratic '
            'politics. Chapters treat idealist and Hobbesian readings of '
            'Oakeshott, conversation, civil association and authority, and '
            'dissent and democracy; the author argues that civil disobedience '
            "is compatible with, and even required by, Oakeshott's "
            'understanding of politics. The book also notes how Thatcherism '
            'drew on Oakeshott while misreading him, and ends with a critical '
            'assessment.'
        )),
    ('Jacques Maritain and Michael Oakeshott on the Modern State', 2001, "in: Reassessing the Liberal State: Reading Maritain's Man and the State"): dict(
        source='https://www3.nd.edu/~maritain/ama/Fuller/Fuller02.pdf',
        abstract=(
            "This chapter, from a volume revisiting Maritain's Man and the "
            "State, compares Jacques Maritain's and Michael Oakeshott's "
            'accounts of the modern state. Fuller presents Oakeshott as '
            'describing the modern European state as it has historically '
            'developed, without speculating about its future, whereas Maritain '
            'also contemplates the possibility of a world political society. '
            'Both thinkers treat the emergence of the individual as central to '
            'modern life, but only Maritain places natural rights at the centre'
            ' of that idea.'
        )),
    ("Michael Oakeshott, Philosopher: A Commemoration of the Centenary of Oakeshott's Birth", 2001, 'Michael Oakeshott Association'): dict(
        source='https://manwithoutqualities.com/2007/05/06/a-commemoration-of-the-centenary-of-oakeshotts-birth%C2%A02001/',
        abstract=(
            'This booklet was produced for the inaugural conference of the '
            'Michael Oakeshott Association, held in 2001 to mark the centenary '
            "of Oakeshott's birth under the theme 'Michael Oakeshott, "
            "philosopher'. Compiled by Leslie Marsh as a lasting record of the "
            "conference, it opens with his convenor's message, which argues for"
            ' reading Oakeshott as a philosopher in the broad sense and not '
            'only as a political thinker, and touches on friendship, tacit '
            "knowledge and practice, Oakeshott's idealism, his qualified (non-"
            'libertarian) conservatism, and liberal education as the '
            "'conversation of mankind', while warning against uncritical "
            'admiration. It also contains pieces by speakers including Kenneth '
            "Minogue, Timothy Fuller, Noël O'Sullivan, Anthony Quinton and "
            'Josiah Lee Auspitz.'
        )),
    ('Michael Polanyi and Michael Oakeshott: Common Ground, Uncommon Foundations', 2001, 'Tradition and Discovery'): dict(
        source='https://www.polanyisociety.org/TAD%20WEB%20ARCHIVE/TAD28-2/TAD28-2-pg23-34-pdf.pdf',
        abstract=(
            "This article compares Oakeshott's thought with that of Michael "
            'Polanyi. Both were concerned with philosophy and political theory,'
            " and both held that a society's approach to knowledge helps "
            'explain its politics; Oakeshott himself believed he and Polanyi '
            'agreed on key points in the theory of knowledge. After outlining '
            "Oakeshott's philosophical project, Mitchell sets out their "
            'agreements and disagreements, arguing that despite real '
            'philosophical and political common ground they part ways at the '
            'foundations: Oakeshott is an idealist and Polanyi a realist, and '
            'the most significant differences between them follow from this.'
        )),
    ("Reassessing the Liberal State: Reading Maritain's Man and the State", 2001, 'Catholic University of America Press'): dict(
        source='https://www.americanmaritainassociation.com/reassessing-the-liberal-state',
        abstract=(
            'This collection of essays, issued by the American Maritain '
            "Association, revisits Jacques Maritain's Man and the State, based "
            'on his 1949 Walgreen Lectures at the University of Chicago. The '
            "contributors consider whether Maritain's reworking of the theory "
            'of the modern state holds up philosophically, examining the state '
            'and its relation to the body politic, the natural-law foundations '
            'of political order, and relations between Church and state. '
            'Contributors include Timothy Fuller, Russell Hittinger, James '
            'Hanink and J. Budziszewski.'
        )),
    ('The Philosophy of Michael Oakeshott', 2001, 'Pennsylvania State University Press'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/the-philosophy-of-michael-oakeshott/',
        abstract=(
            'This book presents Michael Oakeshott primarily as a philosopher '
            'rather than a political theorist, drawing on both published and '
            "unpublished writings. Nardin argues that Oakeshott's central "
            'project was a critical philosophy of human activity and of the '
            'disciplines that interpret it. While covering his views of '
            'morality, law and government, the book focuses on knowledge, '
            'especially knowledge of intelligent conduct, organised around '
            "modality, contingency and civility. It examines Oakeshott's anti-"
            'foundationalist positions on epistemology, metaphysics, the '
            'philosophy of history and the human sciences, including criteria '
            'of truth, theory and practice, interpretation and historical '
            'explanation, and argues that his critique of scientism supports '
            'history as the proper way of understanding human action. It also '
            'relates Oakeshott to phenomenology, hermeneutics and other '
            'Continental movements.'
        )),
    ('Leviathan as Myth: Michael Oakeshott and Carl Schmitt on Hobbes and the Critique of Rationalism', 2002, 'Contemporary Political Theory'): dict(
        source='https://doi.org/10.1057/palgrave.cpt.9300042',
        abstract=(
            'The article compares Michael Oakeshott and Carl Schmitt, two '
            'prominent critics of political rationalism who both drew heavily '
            'on Hobbes. Tregenza shows how their worries about rationalism '
            'shape their readings of Hobbes, especially their use of the idea '
            'of myth, and argues that this comparison clarifies the deeper '
            'differences between their political theories despite shared views '
            "of modern rationalism. Borrowing Oakeshott's own terms, he "
            "characterises Schmitt's position as a politics of faith, seeking "
            'in Hobbes a political theology to ground authority against liberal'
            " scepticism, and Oakeshott's as a politics of scepticism, in which"
            ' authority arises from doubt that any such ground exists. He '
            'concludes that the politics of faith is the more dangerous, as '
            "Schmitt's career shows."
        )),
    ('Pluralism in the Thought of Oakeshott, Shils and Weber', 2002, 'Journal of Classical Sociology'): dict(
        source='https://doi.org/10.1177/1468795X02002001676',
        abstract=(
            'This article traces a shared pluralism in Michael Oakeshott, '
            'Edward Shils and Max Weber. Oakeshott held that there are '
            'categorially distinct modes of understanding that coexist but '
            'cannot be reduced to one another; Shils likewise wrote of the '
            'incommensurable plurality of orientations of the mind, and Weber '
            'of distinct types of social action and different directions of '
            'religious world-rejection. Grosby argues that this convergence '
            'matters above all for what it reveals about the nature of human '
            'cognition and action.'
        )),
    ('Skepticism, Individuality, and Freedom: The Reluctant Liberalism of Richard Flathman', 2002, 'University of Minnesota Press'): dict(
        source='https://mitpressbookstore.mit.edu/book/9780816639700',
        abstract=(
            'This collection of essays responds to the political theory of '
            'Richard Flathman, in particular his argument that liberal theory '
            'has helped justify a politics of governance that has moved away '
            "from liberalism's central commitments to individuality and "
            "freedom. The contributors examine Flathman's skeptical, "
            'individualist liberalism and its place in contemporary liberal '
            'debate. They include Ronald Beiner, Jane Bennett, William E. '
            'Connolly, George Kateb, Nancy J. Hirschmann, Patrick Neal, Richard'
            ' Tuck, Jeremy Waldron and Linda Zerilli.'
        )),
    ('The Grace and the Severity of the Ideal: John Dewey and the Transcendent', 2002, 'University of Chicago Press'): dict(
        source='https://chicagoreference.com/ucp/books/book/chicago/G/bo3615797.html',
        abstract=(
            "This book challenges the common view that John Dewey's pragmatism "
            'leaves no place for the transcendent. Kestenbaum argues that '
            "Dewey's writings on education, ethics, art and religion are shaped"
            ' by a tension between the natural and the transcendent ideal. He '
            'does not claim that Dewey endorsed a supernatural transcendence, '
            'but traces the forms of transcendence that appear within ongoing '
            'experience itself. Chapters include discussions of faith and the '
            'unseen, and comparisons of Dewey with Gadamer, Oakeshott and '
            'Wallace Stevens.'
        )),
    ("The Voice of Poetry in Oakeshott's Moral Philosophy", 2002, 'Review of Politics'): dict(
        source='https://doi.org/10.1017/S0034670500038109',
        abstract=(
            "This article offers an extended treatment of Oakeshott's "
            'aesthetics, a topic largely neglected despite growing interest in '
            "his work. Worthington surveys Oakeshott's writings on the nature "
            'of art and gives a critical account of how this aesthetics '
            'complements his moral philosophy by supplying it with an idea of '
            'authenticity. He argues that individuals and societies that fail '
            'to recognise the poetic dimension of moral life suffer a '
            'corruption of consciousness, and that, contrary to critics who '
            'link it with nihilism or aestheticism, acknowledging this '
            'dimension actually prevents moral life from collapsing into the '
            'pursuit of arbitrary preferences.'
        )),
    ('The Voice of Poetry in the Thought of Michael Oakeshott', 2002, 'Journal of the History of Ideas'): dict(
        source='https://doi.org/10.1353/jhi.2003.0010',
        abstract=(
            "This article examines Oakeshott's aesthetic theory, set out mainly"
            ' in his 1959 essay on the voice of poetry in the conversation of '
            'mankind. Podoksik notes that Oakeshott is usually read as a '
            'conservative political thinker concerned with practice, tradition '
            'and rationalism, while his philosophies of history, science and '
            'art receive less attention. He argues that aesthetics, in which '
            'poetry figures as one of several independent modes of '
            "understanding, holds a central place in Oakeshott's mature "
            'philosophy, and that close study of it reveals a more radical '
            'Oakeshott, attuned to and shaped by the intellectual currents of '
            'his time.'
        )),
    ('Freedom and Normalisation: Poststructuralism and the Liberalism of Michael Oakeshott', 2003, 'American Political Science Review'): dict(
        source='https://doi.org/10.1017/S0003055403000790',
        abstract=(
            'This article treats normalization, a central poststructuralist '
            'concern, as a problem for liberal orders and examines it through '
            "Oakeshott's political theory. Segal argues that Oakeshott connects"
            ' normalization to the existential fact of human finitude: when '
            'people answer finitude by overvaluing instrumentality and treat '
            'freedom as a means to external ends, they become disciplined and '
            'normalized. Oakeshott recasts liberalism around an alternative '
            'response that values experience and freedom for their own sake, '
            "easing normalizing pressure. The article claims Hayek's liberalism"
            ' illustrates the danger Oakeshott warned of, and that Oakeshott '
            'helps restate the public-private distinction and exposes the '
            'limits of contemporary liberal theories that ignore normalization.'
        )),
    ('In Defence of Modernity: Vision and Philosophy in Michael Oakeshott', 2003, 'Imprint Academic'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/in-defense-of-modernity-vision-and-philosophy-in-michael-oakeshott/',
        abstract=(
            "This book argues that, although Michael Oakeshott's philosophy has"
            ' been widely studied, the underlying vision that ties his ideas '
            'together has been neglected. Podoksik locates that vision in the '
            "intellectual debates of Oakeshott's time and reads it as a defence"
            ' of modernity, whose defining feature is radical plurality arising'
            ' from the fragmentation of experience and society. In experience, '
            'modernity abandons the hierarchical medieval picture and treats '
            'modes such as science and history as independent and irreducible; '
            'in society, it takes a liberal form in which individuals pursue '
            'their own choices. Since Oakeshott held that modernity could not '
            'be given a comprehensive philosophical justification, its '
            'preservation depended on sentiment, which led him to champion '
            "liberal education and the 'conversation of mankind'."
        )),
    ('Michael Oakeshott on Hobbes: A Study in the Renewal of Philosophical Ideas', 2003, 'Imprint Academic'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/michael-oakeshott-on-hobbes-a-study-in-the-renewal-of-philosophical-ideas/',
        abstract=(
            "This book is a systematic study of Michael Oakeshott's "
            'interpretation of Thomas Hobbes. Although Oakeshott, an idealist '
            'and critic of rationalism in politics, appears to have little in '
            'common with Hobbes, often read as a materialist and rationalist, '
            'Tregenza argues that the two share fundamental affinities and that'
            ' Oakeshott brought out aspects of Hobbes overlooked by other '
            "scholars. The book follows how Oakeshott's own theory developed "
            'alongside his reading of Hobbes, with attention to his modal and '
            "sceptical theory of knowledge, the 'morality of individuality', "
            'civil association and the critique of rationalism. It also '
            "considers parallels between Oakeshott's religious ideas and "
            "Hobbes's philosophy of religion, and places Oakeshott's reading "
            'among other twentieth-century interpretations of Hobbes.'
        )),
    ('Oakeshott and the New Crime Prevention', 2003, 'Australian and New Zealand Journal of Criminology'): dict(
        source='https://doi.org/10.1375/acri.36.3.338',
        abstract=(
            "The article uses Oakeshott's philosophy to examine the 'new crime "
            "prevention', which moves responsibility for preventing crime "
            'beyond the criminal justice system to households, neighbourhoods '
            'and families and is now organised nationally in many countries. '
            'Knepper surveys recent developments in Australia, Canada, New '
            'Zealand, the United Kingdom and the United States. He brings four '
            'Oakeshottian themes, his view of social science, his idea of the '
            'person, his theory of human association and his account of the '
            'rule of law, to bear on four emerging rationales: evidence-based '
            'policy, situational crime prevention, social crime prevention, and'
            ' the marketing of prosocial values.'
        )),
    ('Oakeshott on History', 2003, 'Imprint Academic'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/oakeshott-on-history/',
        abstract=(
            "This book is a comprehensive study of Michael Oakeshott's ideas "
            'about history, challenging the usual view that his importance lies'
            " mainly in political philosophy. O'Sullivan argues that "
            "Oakeshott's philosophy of history makes him the twentieth-century "
            'philosopher who did most to establish historical inquiry as an '
            "autonomous form of understanding. The book also places Oakeshott's"
            ' work on the history of political thought in the context of '
            'debates about the origins of the liberal state. Drawing on '
            'unpublished material in the Oakeshott papers at the LSE, it is '
            'organised as an intellectual biography covering his career from '
            '1901 to 1983 and is aimed at both newcomers and specialists.'
        )),
    ("Oakeshott's Theory of Freedom as Recognized Contingency", 2003, 'European Journal of Political Theory'): dict(
        source='https://doi.org/10.1177/1474885103002001279',
        abstract=(
            "This article argues that Oakeshott's account of freedom is more "
            'coherent than commonly supposed. Podoksik defines Oakeshottian '
            "freedom as 'recognized contingency', joining genuine choice of "
            "action with the agent's awareness of having that choice. He "
            'identifies two contexts in which Oakeshott uses the notion: one '
            'marking off what is human from what is not, and one concerning '
            'membership in societies, which may be characterised by the '
            "presence or absence of freedom. Although Oakeshott's view can seem"
            ' counter-intuitive, the article contends that at a deeper level it'
            ' resembles the understanding of freedom common in modern liberal '
            'societies.'
        )),
    ('The Shapes of Liberal Thought: Oakeshott, Berlin, and Liberalism', 2003, 'Political Theory'): dict(
        source='https://doi.org/10.1177/0090591703254385',
        abstract=(
            'This article compares Michael Oakeshott and Isaiah Berlin, '
            'arguably the two leading British political philosophers of the '
            "postwar period, who nonetheless engaged little with each other's "
            'work. Franco concentrates on their respective critiques of '
            'rationalism and their theories of liberal pluralism, treating both'
            " thinkers as pluralists, and suggests that Oakeshott's theory of "
            "civil association answers a difficulty in Berlin's account of "
            'negative liberty. He concludes that on both counts Oakeshott '
            'offers the more consistent and philosophically satisfying '
            'position.'
        )),
    ('Political Thinkers: From Socrates to the Present', 2003, 'Oxford University Press'): dict(
        source='https://wholesale.awesomebooks.com/book/9780198781943/political-thinkers-from-socrates-to-the-present',
        abstract=(
            'This collection provides an overview of the Western tradition of '
            'political thought, with chapters by different contributors on the '
            'major theorists from Socrates and the Sophists to recent figures '
            "such as Habermas and Foucault. The editors' introduction sets out "
            'the context of the history of political thought for students, and '
            'each chapter examines the ideas of one thinker or group of '
            'thinkers.'
        )),
    ('The Sceptical Idealist: Michael Oakeshott as a Critic of the Enlightenment', 2003, 'Imprint Academic'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/the-skeptical-idealist-michael-oakeshott-as-critic-of-the-enlightenment/',
        abstract=(
            "This book, developed from the author's LSE doctoral thesis, offers"
            " a structured interpretation of Michael Oakeshott's critique of "
            "the Enlightenment, reading him as a 'sceptical idealist'. Tseng "
            "argues that Oakeshott's well-known critique of philosophy and "
            'rationalism expresses a sense of crisis in philosophical '
            'modernity, and that his core analysis remained stable throughout '
            'his career, including his view of philosophy as an open-ended '
            'pursuit of completeness and of the modes of experience as self-'
            'contained worlds of discourse. In ethics and politics, Oakeshott '
            'shifts the emphasis from technique and enterprise association '
            'toward traditional knowledge, conversation and civil association, '
            'making him neither a doctrinaire liberal nor a dogmatic '
            'conservative. In historiography, he distinguishes historical '
            "understanding from the naturalised 'History' of scientific "
            'history.'
        )),
    ("Tradition and Cognitive Science: Oakeshott's Undoing of the Kantian Mind", 2003, 'Philosophy of the Social Sciences'): dict(
        source='https://doi.org/10.1177/0048393102250282',
        abstract=(
            "This article asks whether Oakeshott's well-known account of "
            'practice can be understood in light of contemporary cognitive '
            'science, especially connectionism with its focus on skills and '
            'skilled knowing, and of the now-standard Anglo-American treatment '
            'of normativity. Turner reads Oakeshott as opposing practices to a '
            "'Kantian' picture of a shared tacit mental framework or set of "
            'rules. If connectionism can give his claims a naturalistic but '
            'non-reductive sense, then Oakeshott, like other theorists of '
            'tradition, extended his account into a broader metaphilosophical '
            'rethinking of theorizing, which the article relates to John '
            'McDowell and to the problem of how the normative is acquired.'
        )),
    ('Comment on “Oakeshott and the New Crime Prevention”', 2004, 'Australian and New Zealand Journal of Criminology'): dict(
        source='https://doi.org/10.1375/acri.37.1.141',
        abstract=(
            "This short comment replies to Paul Knepper's article 'Oakeshott "
            "and the New Crime Prevention', published in the same journal in "
            "2003. Grabosky takes issue with Knepper's rejection of the "
            'traditional forms of knowledge that, according to Knepper, '
            'dominate conventional criminology, and offers a critique of that '
            'position.'
        )),
    ("Michael Oakeshott as a Critic of Hobbes's Theory of the Will", 2004, 'Rivista di Storia Della Filosofia'): dict(
        source='https://francoangeli.it/riviste/articolo/21810',
        abstract=(
            'The article asks why Oakeshott, who in his early Hobbes studies '
            "had judged Hobbes's account of volition incoherent, dropped that "
            'charge after the Second World War. Riley suggests Oakeshott became'
            ' more concerned to resist the determinist readings of Hobbes '
            'current in the 1970s, which treated the will as mere natural '
            "motion. He also considers Jürgen Overhoff's claim that Hobbes's "
            'theory of the will is fully consistent and finds it unpersuasive. '
            "Riley ultimately endorses Oakeshott's earlier, less charitable "
            "verdict, because Hobbes's rejection of free will sits uneasily "
            'with the rational will that a contractarian politics needs.'
        )),
    ('Michael Oakeshott on Civility, Civil Society and Civil Association', 2004, 'Political Studies'): dict(
        source='https://ideas.repec.org/a/bla/polstu/v52y2004i3p603-622.html',
        abstract=(
            'The article starts from the difficulty that recent theorists of '
            'civil society have had in saying which associations deserve to be '
            "called genuinely civil. Boyd argues that Oakeshott's account of "
            'civility, and especially his contrast between civil and enterprise'
            ' association, can help sharpen that debate and separate healthy '
            'from unhealthy forms of associational life. At the same time, '
            'reading Oakeshott alongside the civil society literature exposes '
            'ambiguities in his own thought, which make his conception of the '
            'liberal state an uncertain guide for those hoping to revive civil '
            'society.'
        )),
    ('Michael Oakeshott: An Introduction', 2004, 'Yale University Press'): dict(
        source='https://yalebooks.yale.edu/9780300215274/michael-oakeshott',
        abstract=(
            'This book is a general introduction to the life and thought of '
            'Michael Oakeshott. After a short biographical sketch, Franco sets '
            'out his main ideas: the early idealist theory of knowledge, the '
            'critique of rationalism and of centrally planned social '
            'organisation, and the liberal theory of civil association. He also'
            " covers Oakeshott's writings on the philosophy of history, "
            'aesthetics, religion and education. The book places Oakeshott in '
            'his historical and intellectual context, relating him to his '
            'contemporaries, and considers how his thought bears on present-day'
            ' debates in political philosophy. It was reissued in paperback by '
            'Yale in 2015.'
        )),
    ("The Limits of Political Theory: Oakeshott's Philosophy of Civil Association", 2004, 'Imprint Academic'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/the-limits-of-political-theory-oakeshotts-philosophy-of-civil-association/',
        abstract=(
            "This book interprets Michael Oakeshott's political philosophy in "
            'light of his broader account of philosophical understanding, '
            'stressing the continuity of his major political writings and the '
            'idea of understanding the world in terms of modes. McIntyre argues'
            " that Oakeshott's philosophy of political activity cannot be "
            'reduced to conservatism, liberalism or postmodernism, nor to the '
            'doctrine of a school such as idealism or scepticism. Instead it '
            'challenges the presuppositions of the dominant schools of '
            'political theory and practice, exposing their apparent certainties'
            ' as ambiguous or confused. Chapters address theorising and '
            'modality, the move from practice and tradition to conduct and '
            'practices, historical understanding, morality and the state in '
            'modern Europe, and civil association, illuminating the limits of '
            'political activity and political theory.'
        )),
    ("A Qualified Defence of Oakeshott's Politics of Scepticism", 2005, 'European Journal of Political Theory'): dict(
        source='https://philarchive.org/rec/HORAQD',
        abstract=(
            'This article offers a critical but largely sympathetic assessment '
            "of Oakeshott's idea of a politics of scepticism. Horton argues "
            'that Oakeshott does not succeed in drawing a sharp line between '
            'the politics of faith and the politics of scepticism. He then '
            'sketches, in general terms, a revised version of sceptical '
            'politics and considers both what it has to recommend it and where '
            'its limits lie.'
        )),
    ('Constructivism and Relativism in Oakeshott', 2005, 'in: The Intellectual Legacy of Michael Oakeshott'): dict(
        source='https://philarchive.org/rec/MARCAR-3',
        abstract=(
            "This chapter argues that Oakeshott's relativist constructivism "
            'sits uneasily with his political views, since its logic points '
            'toward conclusions he would have rejected. Marsh traces the '
            'tension in politics, where Oakeshott would oppose rights-based '
            'social ontologies lacking moral grounding; in education, where he '
            'regretted the eclipse of disinterested liberal learning; and in '
            'science, where his relativism leaves him unable to tell good '
            'science from pseudo-science. The chapter also considers how '
            "Rorty's appropriation of Oakeshott's metaphor of conversation "
            'complicates the picture.'
        )),
    ("Contingency and Judgement in Oakeshott's Political Thought", 2005, 'European Journal of Political Theory'): dict(
        source='https://orca.cardiff.ac.uk/id/eprint/3466/',
        abstract=(
            "The article examines Oakeshott's effort to keep political "
            'philosophy strictly separate from normative recommendation. '
            "Haddock accepts the main thrust of Oakeshott's case against "
            'rationalism in politics, but argues that the normative element '
            'that remains in his thinking should not be written off as '
            'philosophically irrelevant. Concentrating on what is actually '
            "involved in 'pursuing intimations', and on what Oakeshott does "
            'rather than what he says he is doing, the article places him much '
            'nearer to the mainstream of Western political philosophy than his '
            'self-presentation suggests.'
        )),
    ("From a 'Necessary Evil' to an Art of Contingency: Michael Oakeshott's Conception of Political Activity", 2005, 'Imprint Academic'): dict(
        source='https://store.ellibs.com/fi/book/9781845400064/from-a-necessary-evil-to-the-art-of-contingency',
        abstract=(
            "This book, based on the author's doctoral dissertation at the "
            "University of Jyväskylä, studies Michael Oakeshott's conception of"
            ' political activity. Soininen first situates Oakeshott in relation'
            ' to liberal, conservative and idealist traditions and then follows'
            ' the development of his view of politics within British postwar '
            'political thought. She argues that Oakeshott moved from near '
            'contempt for politics toward valuing it as a deliberative and '
            'reflective activity, a shift traced through changes in key '
            'concepts such as authority and tradition, including his eventual '
            'replacement of tradition by the idea of practice. The book also '
            "points to less obvious connections, such as Oakeshott's relation "
            'to the linguistic turn, and concludes that his later work offers '
            'an original account of politics as an art of contingency.'
        )),
    ('How Oakeshott Became an Oakeshottean', 2005, 'European Journal of Political Theory'): dict(
        source='https://cris.huji.ac.il/en/publications/how-oakeshott-became-an-oakeshottean/',
        abstract=(
            "This article traces how Oakeshott's two most characteristic ideas,"
            ' the irreducible plurality of modern experience and the modern '
            'state understood as a civil association without a common purpose, '
            'emerged from his break with the British Idealism that shaped his '
            'thinking in his twenties. Podoksik argues that what most '
            'distinguishes Oakeshott from the other British Idealists is his '
            'thoroughgoing rejection of methodological holism, and suggests '
            'that this departure may owe something to Central European sources,'
            ' notably neo-Kantian ideas about the fragmentation of experience.'
        )),
    ('Oakeshott and Mises on Understanding Human Action', 2005, 'Independent Review'): dict(
        source='https://www.independent.org/publications/tir/article.asp?a=547',
        abstract=(
            "The article compares Michael Oakeshott's account of human conduct "
            "with Ludwig von Mises's praxeology. Although the two started from "
            'different philosophical positions and their followers rarely meet,'
            ' Callahan argues that they reached strikingly similar views about '
            'the social sciences: that the basic postulates of action are a '
            'priori, that historical understanding is distinctive, that '
            'intelligent conduct must be studied differently from mechanical '
            'processes, and that agents act on their own interpretation of '
            'their situation. He also notes where they diverge, for example on '
            'modes of experience, the relation of reason to practice, and '
            'deductive knowledge of conduct.'
        )),
    ("Oakeshott's Skepticism and the Skeptical Traditions", 2005, 'European Journal of Political Theory'): dict(
        source='https://philpapers.org/rec/LAUOSA',
        abstract=(
            'The article asks why Oakeshott, who at times described himself as '
            'a sceptic, engaged so little with the two main Hellenistic schools'
            ' of scepticism, Pyrrhonism and Academic scepticism. Laursen '
            'explores this gap, situates it in the modern reception of ancient '
            'scepticism, and suggests that Oakeshott and his commentators may '
            'have passed over these traditions through unfamiliarity, a low '
            'view of their rigour, or worry about their moral consequences. He '
            'closes by indicating what a closer engagement with them might have'
            ' offered.'
        )),
    ('On World Politics: R. G. Collingwood, Michael Oakeshott and Neotraditionalism in International Relations', 2005, 'Palgrave Macmillan'): dict(
        source='https://research.ceu.edu/en/publications/on-world-politics-rg-collingwood-michael-oakeshott-and-neotraditi/',
        abstract=(
            'This book draws on the philosophy of R. G. Collingwood and Michael'
            ' Oakeshott to rethink International Relations theory. Astrov '
            'treats world politics not as a fixed arrangement of actors but as '
            'an ongoing activity of thinking and talking about the conditions '
            'under which world order is possible, with order understood as a '
            'set of activities carried on by individuals in the many '
            'associations to which they belong. On this basis the book develops'
            " 'neotraditionalism', a reformulation of the older traditionalist "
            'approach to International Relations in the wake of rationalism and'
            ' the reflectivist critique of it.'
        )),
    ('Poetic Experience and the Good Life in the Writings of Michael Oakeshott', 2005, 'European Journal of Political Theory'): dict(
        source='https://doi.org/10.1177/1474885105048049',
        abstract=(
            "This article argues that Oakeshott's account of poetic experience "
            'sheds light on aspects of his moral philosophy that are easily '
            'overlooked. Worthington uses the discussion of poetry to bring out'
            " Oakeshott's understanding of the good life and his picture of "
            'society as a tapestry woven from many moral images.'
        )),
    ('Political Theory and the Conduct of Faith: Oakeshott on Religion in Public Life', 2005, 'Contemporary Political Theory'): dict(
        source='https://philpapers.org/rec/SWAPTA-5',
        abstract=(
            "The article examines Oakeshott's unusual understanding of religion"
            ' and its bearing on politics and public life in democratic '
            'societies. It looks at his treatment of religion as an expression '
            'of practical life and at the reconciling work he assigns to the '
            "religious imagination. Swaine argues that Oakeshott's idea of a "
            'reconciled religiosity seems meant to answer the problem of '
            'religious enthusiasm in liberal democracies, but concludes that '
            'this answer, together with the conservative disposition Oakeshott '
            'recommends to citizens, is inadequate and problematic.'
        )),
    ('Religious and Poetic Experience in the Thought of Michael Oakeshott', 2005, 'Imprint Academic'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/religious-and-poetic-experience-in-the-thought-of-michael-oakeshott/',
        abstract=(
            "This book addresses a less studied aspect of Michael Oakeshott's "
            'moral philosophy. Whereas most scholarship concentrates on his '
            'account of the relationships that constitute moral life in modern '
            'society, Worthington examines the kind of persona that such moral '
            "association calls for. Oakeshott's best-known treatment of this "
            "theme is his idea of the 'morality of the individual', but the "
            'book argues that his accounts of religious and poetic experience '
            'give a fuller picture of the persona that emerged in modern times '
            'in response to the invitation to take part in moral association.'
        )),
    ('The Dictionary of Twentieth-Century British Philosophers', 2005, 'Thoemmes Continuum'): dict(
        source='https://wellcomecollection.org/works/ugymzt6m',
        abstract=(
            'This two-volume reference work contains biographical and critical '
            'entries on people who contributed to philosophy in Britain from '
            'about 1900 to 1960 or shortly afterward. Each entry addresses the '
            "whole of an individual's philosophical output. Because 'British' "
            'is hard to define for the period, the editors included both those '
            'who were British subjects for a significant part of their lives '
            'and those who spent much of their lives in Britain, whatever their'
            ' origin.'
        )),
    ('The Enemies of Perfection: Oakeshott, Plato, and the Critique of Rationalism', 2005, 'Lexington Books'): dict(
        source='https://bookcurl.com/products/the-enemies-of-perfection-oakeshott-plato-and-the-critique-of-rationalism-9780739106624',
        abstract=(
            "This book examines Michael Oakeshott's relationship to Plato. "
            "Candreva argues that Plato's philosophy is one of the most "
            "important influences on Oakeshott's thought, and that Oakeshott's "
            'debts to Plato outweigh his explicit criticisms of him, including '
            'in his critique of rationalism. Her reading of how Oakeshott '
            'treats Plato also supports a wider argument against the view that '
            'a radical break between ancient and modern thought makes ancient '
            'philosophy inaccessible or irrelevant to contemporary thinking.'
        )),
    ('The Intellectual Legacy of Michael Oakeshott', 2005, 'Imprint Academic'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/the-intellectual-legacy-of-michael-oakeshott/',
        abstract=(
            'This collection of essays, edited by Corey Abel and Timothy '
            'Fuller, grew out of the first two international conferences of the'
            ' Michael Oakeshott Association, held in London in 2001 and '
            'Colorado Springs in 2003. Combining established Oakeshott scholars'
            ' with a newer generation of researchers, and reflecting '
            'international and multidisciplinary interest in his work, the '
            "volume contends that Oakeshott's reputation as merely a critic of "
            'social planning is too narrow and highlights the depth, '
            'originality and complexity of his writing. Contributors include '
            'Josiah Lee Auspitz, Debra Candreva, Wendell John Coats Jr., Paul '
            'Franco, Timothy Fuller, Robert Grant, Eric Kos, Leslie Marsh, '
            'Kenneth Minogue, Terry Nardin, Martyn Thompson and Gerhard '
            'Wolmarans, among others.'
        )),
    ('The Rule of Law in the Modern European State: Oakeshott and the Enlargement of Europe', 2005, 'European Journal of Political Theory'): dict(
        source='https://philpapers.org/rec/BOUTRO-25',
        abstract=(
            'The article notes that the rule of law is central to how the '
            'European Union understands itself and is one of its main political'
            ' conditions for admitting new members. Boucher argues that the '
            'core point of the idea is protection against arbitrary rule, and '
            'that if the criterion is to be more than rhetoric, the EU must '
            'face what it means for candidate states whose political cultures '
            "have not traditionally embraced it. He draws on Oakeshott's "
            'account of the rule of law to clarify its meaning in modern '
            'European history and in relation to the modern European state.'
        )),
    ('Michael Oakeshott on Religion, Aesthetics, and Politics', 2006, 'University of Missouri Press'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/michael-oakeshott-religion-aesthetics-politics/',
        abstract=(
            "This book argues that Oakeshott's political thought is grounded in"
            ' religious and aesthetic commitments to a greater extent than '
            'earlier scholarship recognized, and it treats these elements as '
            'parts of a single moral outlook. Drawing on recently published '
            "early material, including the 'Tower of Babel' essays, Corey "
            'places Oakeshott within an Augustinian tradition, starting from '
            "his 1929 essay 'Religion and the World', and then identifies the "
            'points where he departs from it. Chapters address his religious '
            'thought, his aesthetics, the politics of faith, skeptical politics'
            ' and civil association, and his understanding of past, present and'
            " future. A concluding chapter compares Oakeshott's critique of "
            "Rationalism with Eric Voegelin's account of Gnosticism and "
            'considers how each thinker read Hobbes.'
        )),
    ('The Politics and Philosophy of Michael Oakeshott', 2006, 'Routledge'): dict(
        source='https://www.routledge.com/The-Politics-and-Philosophy-of-Michael-Oakeshott/Isaacs/p/book/9780415396332',
        abstract=(
            "This book offers a critical study of Oakeshott's thought that "
            'places moral concern at the centre of his philosophical system. '
            'Organised in three parts, it first considers his philosophy and '
            'its influences, notably Bradley and British Idealism, then turns '
            'to practice, morality and religion, conversation and intimation, '
            'and history and politics. The final part sets Oakeshott alongside '
            'later currents of thought, comparing his ideas with Wittgenstein '
            'and discourse analysis, liberalism, pragmatism and deconstruction,'
            ' and relating him to contemporary political philosophers such as '
            'Arendt, Rorty and Rawls. It appeared in the Routledge Studies in '
            'Social and Political Thought series.'
        )),
    ('Collingwood, Oakeshott and Webb on the “Historical Element” in Religion', 2007, 'Collingwood and British Idealism Studies'): dict(
        source='https://philpapers.org/rec/TRECOA',
        abstract=(
            'The article explores how R. G. Collingwood, Michael Oakeshott and '
            'Clement C. J. Webb understood the relation between religion and '
            'history. Tregenza shows that all three, influenced by the growth '
            'of historical thinking in the late nineteenth and early twentieth '
            'centuries, treated history as a distinct and genuine form of '
            'understanding, unlike earlier British Idealists who met biblical '
            'criticism with speculative philosophies of history. They differ, '
            'however: Collingwood and Webb tried to integrate history with '
            'other forms of thought, whereas Oakeshott kept the modes of '
            'experience apart, which shields religion from historical criticism'
            ' but may also cut it off from ultimate truth.'
        )),
    ('Education and the Voice of Michael Oakeshott', 2007, 'Imprint Academic'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/education-and-the-voice-of-michael-oakeshott/',
        abstract=(
            "This book examines Michael Oakeshott's writings on education and "
            'their place in the philosophy of education. Williams notes that '
            "Oakeshott's ideas continue to be widely discussed in the field, a "
            "standing he connects with Oakeshott's influence on the educational"
            ' philosophers Paul Hirst and Richard Peters. The study sets out '
            "Oakeshott's conception of education and considers its relevance to"
            ' current educational debate. It was published in Imprint '
            "Academic's British Idealist Studies series of volumes on "
            'Oakeshott.'
        )),
    ('Intimations Pursued: The Voice of Practice in the Conversation of Michael Oakeshott', 2007, 'Imprint Academic'): dict(
        source='https://www.cambridge.org/core/journals/review-of-politics/article/philosophy-and-poetry-of-practice-andrew-sullivan-intimations-pursued-the-voice-of-practice-in-the-conversation-of-michael-oakeshott-exeter-imprint-academic-2007-pp-xi-219-4990/FC415E6C7C78AB036F771E8F5CB79827',
        abstract=(
            "This book traces how Oakeshott's thought moved from philosophy "
            "toward an account of practical life, focusing on the 'voice of "
            "practice' within his idea of the conversation of mankind. Sullivan"
            ' argues that poetry and practice can combine to yield a fuller '
            "kind of satisfaction, and on that basis interprets Oakeshott's "
            'account of religion as practice in its most poetic form. A further'
            " part applies this reading of practice to Oakeshott's political "
            'writings, especially his concept of civil association. The book '
            "was published in Imprint Academic's British Idealist Studies "
            'series on Oakeshott.'
        )),
    ('Michael Oakeshott, the Ancient Greeks, and the Philosophical Study of Politics', 2007, 'Imprint Academic'): dict(
        source='https://readings.com.au/product/9781845400750/michael-oakeshott-the-ancient-greeks-and-the-philosophical-study-of-politics--eric-s-kos--2008--9781845400750',
        abstract=(
            "This book studies Oakeshott's unpublished notebooks on early Greek"
            ' political philosophy, including his reading of Plato, and uses '
            'them to ask what it means to read and discuss the major texts of '
            'the history of political thought. Kos finds in the notebooks a '
            'combination of philosophical skepticism and a monism Oakeshott '
            "shared with other British Idealists, and he discusses Oakeshott's "
            'view of Socrates as conservative in social matters but radical in '
            "philosophy. The book then brings Oakeshott's approach to the "
            'history of political thought to bear on current debates over the '
            "study of 'great books', including a comparison with the methods of"
            " Quentin Skinner. It appeared in Imprint Academic's British "
            'Idealist Studies series.'
        )),
    ('Oakeshott and the History of Political Thought', 2007, 'Collingwood and British Idealism Studies'): dict(
        source='https://research.usc.edu.au/esploro/outputs/journalArticle/Oakeshott-and-the-History-of-Political/99449967402621',
        abstract=(
            'The article asks why Oakeshott, in his lectures on the history of '
            'political thought, did not follow his own methodological '
            'prescriptions. Boucher is concerned with how Oakeshott approached '
            'the subject rather than with the content of the lectures. He '
            "argues that Oakeshott's philosophical understanding of the field "
            'is shared by many historians and philosophers, including John '
            'Rawls, that the lectures range well beyond what his threefold '
            'scheme of traditions can accommodate, and he questions whether '
            'that scheme of three master traditions should be retained.'
        )),
    ("Oakeshott's Politics for Gentlemen", 2007, 'Review of Politics'): dict(
        source='https://www.cambridge.org/core/journals/review-of-politics/article/oakeshotts-politics-for-gentlemen/D5A85C291BD5C54B11C18BF772571B75',
        abstract=(
            'The article argues that Oakeshott, despite presenting himself as a'
            ' philosopher with little practical interest in politics, was led '
            'by his genteel ideal of the good life toward a political doctrine.'
            ' Wulf reads his critique of collectivism in the 1930s as the start'
            ' of a defence of a pluralist order suited to that ethical ideal, a'
            ' defence developed in his writings on the self, society and the '
            'state. Oakeshott disowned the practical purposes of this work, '
            'Wulf suggests, because political engagement seemed to him at odds '
            'with gentility.'
        )),
    ('Political Education in/as the Practice of Freedom: A Paradoxical Defence from the Perspective of Michael Oakeshott', 2007, 'Journal of Philosophy of Education'): dict(
        source='https://doi.org/10.1111/j.1467-9752.2007.00560.x',
        abstract=(
            'The article situates Oakeshott within debates over what kind of '
            'education sustains democracy, where deliberative and Schumpeterian'
            ' views of democracy yield, respectively, reconstructive and '
            'constructive models of civic education. Engel argues that '
            'Oakeshott offers a third way of linking government and education. '
            'Although Oakeshott himself regarded civic or political education '
            'as vocational and so outside liberal learning, the article '
            'contends that the weight he gives to experience as a source of '
            'learning actually supports political education within the liberal '
            'arts, and connects this to experiential civic engagement '
            'programmes in American universities.'
        )),
    ('Anti-Totalitarian Ambiguities: Jacob Talmon and Michael Oakeshott', 2008, 'History of European Ideas'): dict(
        source='https://doi.org/10.1016/j.histeuroideas.2007.12.009',
        abstract=(
            'The article compares Jacob Talmon and Michael Oakeshott as '
            'representatives of two contrasting tendencies within anti-'
            'totalitarian thought. Podoksik notes what they share, including '
            'treating the Soviet and Nazi regimes as alike, admiration for '
            'England, and rejection of utopianism, but argues that this '
            'agreement conceals important differences of attitude and '
            "temperament. Talmon's liberalism is driven by anxiety, whereas "
            'Oakeshott regarded totalitarianism as a secondary phenomenon '
            'rooted in resentment, which left him more confident about liberal '
            'modernity.'
        )),
    ("Michael Oakeshott's Critique of Rationalism in Politics as Basis for His Theory of Civil Association", 2008, 'Synthesis Philosophica'): dict(
        source='https://hrcak.srce.hr/en/30808',
        abstract=(
            "The article explains Oakeshott's objection to rationalism in "
            'politics as a rejection of the view that only what is grounded in '
            'and justified by theory counts. Mihatov presents civil '
            'association, an order based on shared recognition of general rules'
            " within which politics proceeds as conversation, as Oakeshott's "
            'way of freeing politics from technical problem-solving. He judges '
            'the critique of rationalism the more convincing part of '
            "Oakeshott's work, regards civil association as closer to a thought"
            " experiment, and uses Foucault's account of power and knowledge to"
            ' show how its institutional framework depends on relations of '
            'power.'
        )),
    ('Overcoming the Conservative Disposition: Oakeshott vs. Tönnies', 2008, 'Political Studies'): dict(
        source='https://econpapers.repec.org/RePEc:bla:polstu:v:56:y:2008:i:4:p:857-880',
        abstract=(
            'The article presents Oakeshott, usually seen as a British '
            'conservative, as a critic of conservatism, in particular of the '
            'German conservative tradition represented by Ferdinand Tönnies, '
            'which rejected modern individualist society as the product of '
            'alienating, purpose-driven rationalism. Podoksik shows that at one'
            ' stage Oakeshott was drawn to this critique and held views close '
            "to Tönnies's, but that he later abandoned its premises and "
            'developed the idea of a non-purposive form of association, which '
            'allowed him to accept modern liberal society.'
        )),
    ("The Lion and the Ox: Oakeshott's Engagement with Leo Strauss on Hobbes", 2008, 'History of Political Thought'): dict(
        source='https://centaur.reading.ac.uk/31200/',
        abstract=(
            "The article argues that Oakeshott's interpretation of Hobbes was "
            "shaped both by sympathy for Leo Strauss's reading and by treating "
            'Strauss as his principal rival. Through a close reading of '
            "Oakeshott's essay 'The Moral Life in the Writings of Thomas "
            "Hobbes', Boyd shows that Oakeshott adopted a good deal of "
            "Strauss's interpretation, including, surprisingly, his distinction"
            " between esoteric and exoteric teaching, while the essay's central"
            ' aim was nonetheless to refute Strauss.'
        )),
    ('Oakeshott on Science as a Mode of Experience', 2009, 'Zygon: Journal of Religion & Science'): dict(
        source='https://doi.org/10.1111/j.1467-9744.2009.00993.x',
        abstract=(
            "This essay offers a critical reconstruction of Oakeshott's account"
            ' of natural science as a mode of experience. Kaldis aims to '
            "strengthen Oakeshott's modal scheme by testing its internal "
            'consistency and bringing it into contact with more recent '
            'philosophy. He also examines the privileged position Oakeshott '
            'gives philosophy and the separateness of the modes, which he '
            'likens to Leibnizian monads, and asks whether ethics, as one '
            'moment of philosophical reflection, might be brought together with'
            ' science despite that separation.'
        )),
    ('Oakeshott on the Character of Religious Experience: Need There Be a Conflict Between Science and Religion?', 2009, 'Zygon: Journal of Religion & Science'): dict(
        source='https://relbib.de/Record/182796071X',
        abstract=(
            "This essay traces Oakeshott's lifelong reflection on religious "
            'experience, which he placed within the practical mode, while '
            'treating science as a distinct mode in Experience and Its Modes. '
            'Fuller shows that for Oakeshott the question whether science and '
            'religion conflict becomes the question whether the scientific and '
            'practical modes conflict. On his account the modes are voices that'
            ' may address one another but stand in no hierarchy, and neither '
            'can absorb the other without falling into contradiction.'
        )),
    ('Oakeshottian Modes at the Crossroads of the Evolution Debates', 2009, 'Zygon: Journal of Religion & Science'): dict(
        source='https://doi.org/10.1111/j.1467-9744.2009.00994.x',
        abstract=(
            "This essay brings Oakeshott's theory of modes of experience to "
            'bear on current debates over evolution, arguing that much of the '
            'controversy has science and religion either attacking each other '
            "irrelevantly or seeking each other's support in ways that miss the"
            " point. Abel's analysis of Oakeshott's idea of religion connects "
            'his early holistic theory of the state, his individualist account '
            'of religious sensibility and his theory of political, moral and '
            'religious authority, and presents civil conversation as a way of '
            'holding together diverse modal truths, religious or philosophical '
            'truth, and a free political order.'
        )),
    ('Reflecting on Michael Oakeshott: Introduction to the Symposium', 2009, 'Zygon: Journal of Religion & Science'): dict(
        source='https://doi.org/10.1111/j.1467-9744.2009.00990.x',
        abstract=(
            "This piece introduces a Zygon symposium on Oakeshott's "
            'understanding of how religion, science and politics relate, with '
            'essays by Elizabeth Corey, Timothy Fuller, Byron Kaldis and Corey '
            'Abel and a review by Efraim Podoksik. Marsh discusses the view '
            'that apparent conflicts among these fields are pseudo-problems, '
            "comparing it with Stephen Jay Gould's idea of non-overlapping "
            "magisteria, and argues that Oakeshott's appeal to ignoratio "
            "elenchi, often equated with Ryle's category mistake, is "
            'tendentious in several respects.'
        )),
    ('Religion and the Mode of Practice in Michael Oakeshott', 2009, 'Zygon: Journal of Religion & Science'): dict(
        source='https://doi.org/10.1111/j.1467-9744.2009.00991.x',
        abstract=(
            'This essay contends that a religious outlook underlies much of '
            "Oakeshott's political and philosophical writing. Corey first sets "
            'out his understanding of religion and of the practical mode in his'
            ' own terms, then draws on thinkers with similar views, such as '
            'Georg Simmel and George Santayana, to restate it more plainly. She'
            ' goes on to ask whether these ideas withstand scrutiny and whether'
            ' they remain relevant to religious reflection today.'
        )),
    ('Michael Oakeshott', 2010, 'Continuum'): dict(
        source='https://biblioteca.izt.uam.mx/vufind/Record/EBSCO_ocn676698430/Description',
        abstract=(
            "This book is a short introduction to Oakeshott's thought, "
            "published as a volume in Continuum's Major Conservative and "
            'Libertarian Thinkers series, whose volumes combine intellectual '
            'biography, critical exposition and an assessment of reception and '
            "influence. Neill presents Oakeshott's ideas in accessible form "
            'across four chapters: an account of his life, a reading of his '
            'work as a defence of pluralism and modernity, a survey of how his '
            'thought was received, and a discussion of its continuing relevance'
            ' to debates about conservatism and liberalism.'
        )),
    ('Ryle and Oakeshott on the Know-How/Know-That Distinction', 2010, "in: The Meanings of Michael Oakeshott's Conservatism"): dict(
        source='https://philpapers.org/rec/MARRAO-2',
        abstract=(
            "This chapter treats Gilbert Ryle's distinction between knowing how"
            ' and knowing that as a sharper formulation of a problem Oakeshott '
            'had long been addressing: the epistemic standing of ordinary '
            'practical life, including political practice. Marsh places this '
            'concern within a wider inquiry into the nature of rationality, and'
            ' in particular its social character.'
        )),
    ("The Meanings of Michael Oakeshott's Conservatism", 2010, 'Imprint Academic'): dict(
        source='https://biblioteca.izt.uam.mx/vufind/Record/EBSCO_ocn930490391/Description',
        abstract=(
            "This collection of essays examines what Oakeshott's conservatism "
            'amounts to, approaching it through his ideas on religion, history '
            'and tradition, and through his connections with thinkers ranging '
            'from Hume to Ryle and Cavell. The essays are grouped into parts on'
            " religion, history, currents in philosophy, and Oakeshott's essay "
            "'On Being Conservative'. Rather than settling on one definition, "
            'the volume treats conservatism as a disposition or habit of mind '
            'rather than a fixed doctrine, and leaves its meaning open. '
            'Contributors include Ian Tregenza, Corey Abel, Richard Flathman, '
            "Stephen Turner and Ivo Mosley. It appeared in Imprint Academic's "
            'British Idealist Studies series on Oakeshott.'
        )),
    ("Michael Oakeshott's Skepticism", 2011, 'Princeton University Press'): dict(
        source='https://press.princeton.edu/titles/9367.html',
        abstract=(
            'This book argues that skepticism about foundations is what unifies'
            " Oakeshott's work. Botwinick reads Oakeshott's resistance to "
            'sweeping intellectual systems as making him sympathetic to liberal'
            ' individualism and as aligning him with postmodern '
            'antifoundationalism. Building on this reading, he develops a '
            "position of 'generalized agnosticism' which, he contends, leads "
            'toward mysticism and links philosophy with religion. The chapters '
            'work through epistemology, metaphysics, religion and science, '
            'political theory, personal identity, law and history. It was '
            'published in the Princeton Monographs in Philosophy series.'
        )),
    ('A Companion to Michael Oakeshott', 2012, 'Pennsylvania State University Press'): dict(
        source='https://www.degruyterbrill.com/document/doi/10.1515/9780271060170/html',
        abstract=(
            "This collection of essays surveys the full range of Oakeshott's "
            'thought. The chapters address his theory of knowledge and his '
            'philosophies of history, religion, art, education, morality, '
            'politics and law. Contributors include Robert Grant, David '
            'Boucher, Kenneth McIntyre, Geoffrey Thomas, Elizabeth Corey, Noël '
            "O'Sullivan and Steven Gerencser. A review in Political Studies "
            'Review judged the volume useful both to established scholars and '
            'to readers coming to Oakeshott for the first time.'
        )),
    ('Hayek and Oakeshott: Situating the Mind', 2012, 'in: A Companion to Michael Oakeshott'): dict(
        source='https://manwithoutqualities.com/2008/07/01/the-essential-oakeshott/',
        abstract=(
            'This chapter reads Oakeshott and Hayek as social epistemologists '
            'whose critiques of rationalism share a common view of mind. Marsh '
            'places both within the non-Cartesian, situated-cognition strand of'
            ' cognitive science, argues that Oakeshott misread Hayek in '
            "'Rationalism in Politics', and concludes by linking their shared "
            'theory of mind to their political positions.'
        )),
    ('Oakeshott on Rome and America', 2012, 'Imprint Academic'): dict(
        source='https://kirkcenter.org/reviews/can-rationalism-make-it-in-the-long-run/',
        abstract=(
            "This book, based on Callahan's Cardiff doctoral thesis, applies "
            "Oakeshott's critique of Rationalism in politics to concrete "
            'historical cases, ancient Rome and the United States. It presents '
            'Rome as an example of a pragmatic, tradition-guided political '
            'style, and then turns to its main concern, American political '
            'self-understanding. Callahan suggests that, despite the '
            'Rationalist language of their public declarations, the American '
            'Founders in practice largely followed inherited tradition. '
            'Reviewers note that the book questions whether the United States '
            'should simply be classed as a Rationalist political project.'
        )),
    ('The Cambridge Companion to Oakeshott', 2012, 'Cambridge University Press'): dict(
        source='https://contemporarythinkers.org/michael-oakeshott/commentary/cambridge-companion-oakeshott/',
        abstract=(
            'This collection, in the Cambridge Companions to Philosophy series,'
            " offers fourteen chapters on the main areas of Oakeshott's "
            'thought. It is organised in three parts: his philosophy, including'
            ' his views on history, science, aesthetics and education; his '
            'account of morality, society and politics; and his relation to '
            'other thinkers and traditions. The editor contributes an '
            'introduction and a chapter placing Oakeshott in the context of '
            'German Idealism. Other contributors include James Alexander, '
            'Steven B. Smith, Andrew Gamble, David Boucher, Dana Villa and '
            'William A. Galston.'
        )),
    ('A Danse Macabre of Wants and Satisfactions: Hayek, Oakeshott, Liberty, and Cognition', 2014, 'in: Austrian Economic Perspectives on Individualism and Society: Moving Beyond Methodological Individualism'): dict(
        source='https://ideas.repec.org/h/pal/palchp/978-1-137-36884-3_6.html',
        abstract=(
            'This chapter seeks to reclaim the idea of liberty from those who '
            'misuse it, drawing on Hayek and Oakeshott to examine how liberty '
            'relates to human nature, culture and economic order. Abel and '
            "Marsh direct their criticism mainly at 'hard' libertarianism, "
            'arguing that it amounts to a form of absolutism and an extreme '
            'case of rationalism that yields, at best, an empty account of '
            'freedom.'
        )),
    ('Austrian Economic Perspectives on Individualism and Society: Moving Beyond Methodological Individualism', 2014, 'Palgrave Macmillan'): dict(
        source='https://ideas.repec.org/b/pal/palbok/978-1-137-36884-3.html',
        abstract=(
            'This collection brings together economists and political '
            'scientists working on evolutionary change and spontaneous order to'
            ' reconsider methodological individualism in the Austrian '
            "tradition. Chapters examine Hayek's changing view of "
            'methodological individualism, the move from Misesian to Hayekian '
            'social science, spontaneous order in relation to democracy and '
            'public choice, and the varieties of spontaneous orders. A chapter '
            'by Corey Abel and Leslie Marsh discusses Hayek, Oakeshott and '
            "cognition, and a closing chapter asks how Hayek's ideas about mind"
            ' and society bear on freedom.'
        )),
    ("Michael Oakeshott's Cold War Liberalism", 2015, 'Palgrave Macmillan'): dict(
        source='https://doi.org/10.1057/9781137507020',
        abstract=(
            'This collection of ten essays reconsiders Oakeshott in the context'
            " of the Cold War. It opens with Nardin's chapter on whether "
            'Oakeshott is better described as liberal or conservative, then '
            'turns to his responses to totalitarianism and constitutional '
            'democracy, and closes with essays on the reception and relevance '
            'of his ideas in East Asia. Reviewers note that the volume places '
            'Oakeshott in dialogue with Cold War liberals such as Isaiah '
            'Berlin, Raymond Aron, Karl Popper and Friedrich Hayek, while also '
            'showing where he diverged from them. Contributors include Andrew '
            'Gamble.'
        )),
    ("Education and Conversation: Exploring Oakeshott's Legacy", 2016, 'Bloomsbury Academic'): dict(
        source='https://edrev.asu.edu/index.php/ER/article/download/2182/670/2556',
        abstract=(
            "This collection takes as its starting point Oakeshott's idea of "
            "education as an initiation into the 'conversation of mankind'. Its"
            ' chapters examine that metaphor, the roots of his educational '
            'thinking in his early philosophy, the connection of his ideas to '
            'the concept of Bildung, and the bearing of his political '
            'conservatism. Other chapters use Oakeshott as a way into current '
            'philosophical debates about education, learning and development, '
            'including the nature of initiation, the phenomenology of listening'
            ' and the value of the liberal arts. The volume brings together '
            'analytic and continental philosophers; contributors include Paul '
            'Standish, Paul Fairfield, Shaun Gallagher, Sebastian Rödl, Babette'
            ' Babich and Christine Sypnowich.'
        )),
    ("Michael Oakeshott's Political Philosophy of International Relations: Civil Association and International Society", 2016, 'Palgrave Macmillan'): dict(
        source='https://doi.org/10.1007/978-3-319-38785-7',
        abstract=(
            "This book considers what Oakeshott's political philosophy "
            'contributes to current debates in normative international theory. '
            'Beginning from his account of experience and of political '
            'philosophy, Orsi develops the idea of civil association and '
            'relates it to international order and international society. He '
            'compares the Oakeshottian position with constructivist scholarship'
            ' in International Relations, and closes by discussing realism, '
            'universalism and an evolving international morality. It appeared '
            "in Palgrave Macmillan's International Political Theory series."
        )),
    ('The Place of Michael Oakeshott in Contemporary Western and Non-Western Thought', 2017, 'Imprint Academic'): dict(
        source='https://orca.cardiff.ac.uk/143905',
        abstract=(
            'This collection offers a critical assessment of the main aspects '
            "of Oakeshott's thought, with contributors from Britain, Canada, "
            "Hong Kong, India and the United States. The editor's introduction "
            'presents the volume as a response to the recent appearance of two '
            'Companion volumes on Oakeshott, and the essays explore why his '
            'work has attracted interest both in the West and beyond it. The '
            'book was reviewed by W. J. Morgan in Collingwood and British '
            'Idealism Studies.'
        )),
    ('Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, and Others', 2018, 'Lexington Books'): dict(
        source='https://voegelinview.com/review-of-tradition-v-rationalism-voegelin-oakeshott-hayek-and-others/',
        abstract=(
            'This collection compares twentieth-century critics of rationalism:'
            ' Eric Voegelin, Michael Oakeshott, F. A. Hayek, Ludwig '
            'Wittgenstein, Alasdair MacIntyre, Gilbert Ryle, Hans-Georg Gadamer'
            ' and Aurel Kolnai, with a brief look at Leo Strauss. Chapters '
            "include Gene Callahan's discussion of Hayek and Oakeshott on "
            "rationalism, Kenneth McIntyre's comparison of Ryle and Oakeshott "
            "on tacit knowledge, John von Heyking's question of whether Hayek "
            "was himself a rationalist, and essays on Voegelin's critique of "
            "ideology. A review in VoegelinView commended the volume's breadth "
            'within a short compass, while noting that a direct comparison of '
            'Oakeshott and Voegelin would have strengthened it.'
        )),
    ('Michael Oakeshott and Leo Strauss: The Politics of Renaissance and Enlightenment', 2019, 'Palgrave Macmillan'): dict(
        source='https://doi.org/10.1007/978-3-030-13381-8',
        abstract=(
            'This book compares Oakeshott and Leo Strauss, two thinkers usually'
            ' classed as conservatives, and argues that they are better '
            'understood as committed respectively to a politics of renaissance '
            'and a politics of enlightenment: Oakeshott to a renewal of poetic '
            'individuality, Strauss to recovering the universality of '
            'philosophy. McIlwain develops the comparison through chapters on '
            'liberal education and classical republicanism, historical '
            "interpretation, the legacy of Hobbes, each thinker's engagement "
            "with Alexandre Kojève, Strauss's Socratism after Heidegger, and "
            "Oakeshott's Augustinianism after Hobbes, framing their "
            'disagreement as a version of the quarrel between poetry and '
            'philosophy.'
        )),
    ('Michael Oakeshott and the Cambridge School on the History of Political Thought', 2019, 'Routledge'): dict(
        source='https://www.routledge.com/Michael-Oakeshott-and-the-Cambridge-School-on-the-History-of-Political/Thompson/p/book/9781032092430',
        abstract=(
            "This book offers a critique of the Cambridge School's historical "
            'contextualism, which it treats as the prevailing approach to the '
            "history of political thought, using Oakeshott's account of how "
            'historical inquiry works. Thompson accepts that the early '
            'Cambridge School writings were a real advance, but identifies '
            'problems with the approach, including its failure to do justice to'
            ' the variety of past political thinking, in particular the '
            'difference between ideology and philosophy. A reviewer credited '
            'the book with making a strong case for Oakeshott as the leading '
            'twentieth-century philosopher of history.'
        )),
    ('Michael Oakeshott as a Philosopher of the "Creative" and Other Essays', 2019, 'Imprint Academic'): dict(
        source='https://www.cambridge.org/core/journals/review-of-politics/article/abs/wendell-john-coats-jr-michael-oakeshott-as-a-philosopher-of-the-creative-and-other-essays-exeter-imprint-academic-2019-pp-viii-129/CAFD272861FD83C665F42DBF6C976DC7',
        abstract=(
            'This book collects eight essays on Oakeshott, most of them recent.'
            ' Six advance the claim that his work can be read as variations on '
            "a single idea, the 'creative' or 'poetic' character of human "
            'experience. Other essays compare Oakeshott with Leo Strauss, '
            'Friedrich Hayek and A. C. Graham, and discuss his views on '
            'education alongside those of A. N. Whitehead. A brief postscript '
            "argues for the relevance of Oakeshott's ideas in an age of "
            'artificial intelligence. A review in The Review of Politics '
            'observed that the core claims recur across the essays, often in '
            'similar wording.'
        )),
    ('Michael Oakeshott on Authority, Governance, and the State', 2019, 'Palgrave Macmillan'): dict(
        source='https://doi.org/10.1007/978-3-030-17455-2',
        abstract=(
            'This collection, in the Palgrave Studies in Classical Liberalism '
            "series, examines Oakeshott's understanding of authority, "
            'governance and the state. Its contributors, from Europe, North '
            'America and India, draw on less familiar Oakeshott material, '
            'including his lectures at Cambridge and the London School of '
            'Economics. Topics include liberal political legitimacy, '
            "Oakeshott's political realism and questions of global governance. "
            "The editor's introduction observes that Oakeshott's treatment of "
            'governance and authority varies with his object of attention, so '
            'that civil association is handled differently from the historical '
            'modern European state.'
        )),
    ('Critics of Enlightenment Rationalism', 2020, 'Palgrave Macmillan'): dict(
        source='https://www.palgrave.com/gb/book/9783030425982',
        abstract=(
            'This collection, in the Palgrave Studies in Classical Liberalism '
            'series, surveys major thinkers who opposed Enlightenment '
            'rationalism. Its chapters cover figures including Burke, '
            'Tocqueville, Kierkegaard, Nietzsche, Wittgenstein, Heidegger, '
            'Gadamer, Voegelin, Oakeshott, Berlin and Jane Jacobs. A review in '
            "the Russell Kirk Center's journal noted the range of themes across"
            " the essays and the volume's lack of a single unifying approach."
        )),
    ("Michael Oakeshott's Critique of Modern Rationalism", 2020, 'in: Critics of Enlightenment Rationalism'): dict(
        source='https://gcallah.github.io/Rationalism/AntiRats/oakeshott.html',
        abstract=(
            'This chapter explains what Oakeshott meant by modern Rationalism, '
            "an outlook he traced to an exaggerated version of Bacon's and "
            "Descartes' hopes for a universal method, stripped of Descartes' "
            "occasional scepticism. Coats summarizes Oakeshott's objections to "
            'its effects on politics and morals, shows how the charge that '
            'Rationalism ignores the poetic or creative character of experience'
            " connects with Experience and Its Modes and with Oakeshott's "
            'preference for civil association, and assesses how accurate and '
            'reasonable his analysis and proposed alternatives are.'
        )),
    ("Oakeshott's Skepticism, Politics, and Aesthetics", 2022, 'Palgrave Macmillan'): dict(
        source='https://doi.org/10.1007/978-3-030-83055-7',
        abstract=(
            'This collection of thirteen essays, in the Palgrave Studies in '
            "Classical Liberalism series, approaches Oakeshott's work chiefly "
            'through his skepticism, his politics and his aesthetics. Chapters '
            'ask whether Oakeshott as a philosopher of skepticism is best read '
            'as conservative or liberal, compare him with Popper on the crises '
            'of rationalist politics, consider Oakeshott, Strauss and the '
            'Romans, examine his theory of poetry in the light of Seamus '
            'Heaney, and ask what contemporary realists can learn from '
            'Montaigne. The contributors include a newer generation of '
            'Oakeshott scholars.'
        )),
    ('Michael Oakeshott on the Human Condition: Essays', 2024, 'Liberty Fund'): dict(
        source='https://about.libertyfund.org/?p=124759',
        abstract=(
            'This book gathers sixteen essays written by Timothy Fuller between'
            " 1976 and 2020 on Oakeshott's ideas about politics, philosophy, "
            'religion and conservatism. Some were previously published and some'
            ' appear for the first time. Fuller, a founding member of the '
            'Michael Oakeshott Association and co-editor of the Yale University'
            " Press series of Oakeshott's selected works, knew Oakeshott "
            'personally from 1974 until his death in 1990. The volume includes '
            'an introduction, a select bibliography and an index.'
        )),
    ('Michael Oakeshott and Liberalism Revisited', 2025, 'Palgrave Macmillan'): dict(
        source='https://doi.org/10.1007/978-3-032-04163-0',
        abstract=(
            'This collection, in the Palgrave Studies in Classical Liberalism '
            "series, examines how Oakeshott's political philosophy relates to "
            'liberalism in both theory and practice. Its essays read Oakeshott '
            'alongside Hobbes, Strauss, Houellebecq, Berlin and Aristotle, and '
            'consider the reception of his thought in China and Poland. Other '
            'chapters address his legal theory, questions of technology policy,'
            ' and liberal theory in its own right. The editor is a longtime '
            'officer of the Michael Oakeshott Association.'
        )),
    ('The Politics of Imperfection: The Religious and Secular Traditions of Conservative Thought in England from Hooker to Oakeshott', 1978, 'Faber & Faber'): dict(
        source='https://librarycatalog.ecu.edu/catalog/155755',
        abstract=(
            "This short book, which began as Quinton's T. S. Eliot Memorial "
            "Lectures of 1976, surveys the religious and secular traditions "
            "of conservative thought in England, from Richard Hooker in the "
            "sixteenth century to Michael Oakeshott."
        )),
    ('The Defence of Natural Law: A Study of the Ideas of Law and Justice in the Writings of Lon L. Fuller, Michael Oakeshott, F. A. Hayek, Ronald Dworkin and John Finnis', 1992, 'Macmillan'): dict(
        source='https://dx.doi.org/10.1007/978-1-349-22359-6',
        abstract=(
            "This book studies the legal philosophies of five twentieth-"
            "century theorists: Lon L. Fuller, Michael Oakeshott, F. A. Hayek, "
            "Ronald Dworkin and John Finnis. Covell argues that each of them "
            "stayed close to the standpoint of natural law, while at the same "
            "time defending the understanding of law and the state that "
            "belongs to modern liberalism. The book includes a bibliography of "
            "the five thinkers' writings."
        )),
    ('Dr. Leo Strauss on Hobbes', 1937, 'Politica'): dict(
        source='https://oll.libertyfund.org/titles/franco-hobbes-on-civil-association',
        abstract=(
            "Oakeshott's review essay on Leo Strauss's The Political Philosophy"
            ' of Hobbes (1936). He welcomes the renewed scholarly interest in '
            "Hobbes, calls Strauss's book the most original study of Hobbes for"
            ' many years and a work to be followed with profit, though with '
            'some caution, and then examines its interpretation of the basis '
            "and genesis of Hobbes's political philosophy in detail. Reprinted "
            'in Hobbes on Civil Association; the Liberty Fund edition can be '
            'read free at the Online Library of Liberty.'
        )),
    ('The "Collective Dream of Civilisation"', 1947, 'Listener'): dict(
        source='https://oll.libertyfund.org/titles/franco-hobbes-on-civil-association',
        abstract=(
            'A broadcast talk, reprinted as "Leviathan: A Myth" in Hobbes on '
            'Civil Association. Oakeshott argues that Leviathan, usually read '
            'only as a book of philosophy and politics, is a work of art and '
            'one of the masterpieces of English literature. A civilization, he '
            'suggests, is at bottom a collective dream, whose substance is a '
            'myth: an imaginative interpretation of human existence. '
            "Literature's task is to recall and recreate that dream, and "
            "Hobbes's book does so for its civilization. Free at the Online "
            'Library of Liberty.'
        )),
    ('The Definition of a University', 1967, 'Journal of Educational Thought'): dict(
        source='https://journalhosting.ucalgary.ca/index.php/jet/article/view/43498',
        abstract=(
            'The text of a lecture given at the University of Calgary on 4 '
            'April 1967. Oakeshott describes learning as the activity in which '
            'we come to know ourselves and the world, and teaching as the '
            'imparting of learning to pupils, and considers what part a '
            'university plays in both: it is the custodian of the great '
            'enterprises of human understanding and explanation. He warns '
            'against bending universities to the wants of a technological '
            'society, and holds that academic freedom can mean only the freedom'
            " to be academic. Free on the journal's site."
        )),
    ('Work and Play', 1995, 'First Things'): dict(
        source='https://firstthings.com/work-and-play/',
        abstract=(
            "A previously unpublished essay, printed after Oakeshott's death. "
            'Human beings, as creatures of wants, exploit the world through '
            'work, and Oakeshott traces how, over some four centuries, work '
            "came to be thought humanity's proper and even exclusive "
            'occupation. Against it he sets play: activities pursued for their '
            'own sake, among them philosophy, science and history as well as '
            'poetry, music and the other arts. He ends by warning that '
            'education is where the reduction of play to work is most '
            'dangerous, recalling that "school" comes from the Greek word for '
            'leisure. Free on the First Things site.'
        )),
    ('Introduction to Leviathan', 1946, 'in: Leviathan, or the Matter, Forme and Power of a Commonwealth Ecclesiasticall and Civil'): dict(
        source='https://oll.libertyfund.org/titles/franco-hobbes-on-civil-association',
        abstract=(
            "Oakeshott's introduction to his 1946 Blackwell edition of "
            'Leviathan, revised for Hobbes on Civil Association (1975). Its six'
            " sections cover Hobbes's life, the context of Leviathan, the "
            "character of Hobbes's mind and manner of writing, his "
            'philosophical system, the argument of Leviathan, and some disputed'
            ' topics. The revised version can be read free at the Online '
            'Library of Liberty.'
        )),
    ('The Moral Life in the Writings of Thomas Hobbes', 1962, 'in: Rationalism in Politics and Other Essays'): dict(
        source='https://oll.libertyfund.org/titles/franco-hobbes-on-civil-association',
        abstract=(
            'An essay that grew out of a lecture at the University of '
            'Nottingham. Beginning from the observation that the moral life is '
            'a life among human beings, an art of behaving as one ought rather '
            'than a natural necessity, Oakeshott examines how Hobbes understood'
            ' moral conduct and obligation. Reprinted in Hobbes on Civil '
            'Association; free at the Online Library of Liberty.'
        )),
    ('Michael Oakeshott and the Conversation of Modern Political Thought', 2015, 'State University of New York Press'): dict(
        source='https://www.sunypress.edu/p-5996-michael-oakeshott-and-the-conve.aspx',
        abstract=(
            "Rather than treating Oakeshott as the author of a closed "
            "system, Plotica reads his work as he himself understood it: as "
            "contributions to an ongoing conversation. The book follows that "
            "conversation through language and individual agency, "
            "individuality between tradition and contingency, the modern "
            "state, and democracy, setting Oakeshott beside thinkers such as "
            "Wittgenstein, Charles Taylor, Foucault and Arendt, and drawing "
            "from him a conversational ethos for democratic politics."
        )),
}
