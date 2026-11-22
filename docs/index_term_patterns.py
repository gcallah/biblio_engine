"""The patterns that drafted the Oakeshott index (2026-11-22), kept as
a record and for drafting the next one (e.g. Voegelin's); nothing runs
this file. Each term was searched for in every entry's title, the title
of the book an Oakeshott review is of, and the abstract:

- a "sure" pattern found anywhere put the entry under the term, as did
  a keyword with the term's name (philosophy of science for science,
  moral philosophy for morality);
- a "maybe" pattern found only in an abstract made the entry a possible
  one, listed on the to-do page;
- reviews of books by or about Oakeshott (RVOB, RVAB) count only through
  their own abstract, not the reviewed book's title, so the index lists
  the book rather than all of its reviews; most have no abstract yet.

The result is sites/oakeshott/management/commands/_index_terms.py; terms
whose whole place in the index was in doubt went to its POSSIBLE.
"""
# term: (sure patterns, maybe patterns, case-sensitive?)
# sure: any hit in a title, Oakeshott's reviewed title, or an abstract.
# maybe: a hit in an abstract only -> a possible reference (to-do page).
T = {}
def t(name, sure, maybe=(), cs=False): T[name]=(list(sure),list(maybe),cs)
t('rationalism', [r'rationalis[mt]', r'anti-?rational'])
t('tradition', [r'\btraditional(ism|ist)\b', r'\btradition\b(?! of)', r'\btraditions\b'] , [])
t('conservatism', [r'conservatism', r'conservative disposition', r'on being conservative'], [r'\bconservatives?\b'])
t('civil association', [r'civil association'])
t('enterprise association', [r'enterprise association'])
t('nomocracy', [r'nomocra'])
t('teleocracy', [r'teleocra'])
t('modes of experience', [r'\bmodes?\b of experience', r'experience and its modes', r'\bmodes\b', r'\bmodality\b', r'\bmodal\b', r'arrest(s|ed)? of experience'])
t('experience', [r'\bexperience\b'], [])  # whole term is a possible
t('practice', [r'mode of practice', r'practical (life|activity|experience)', r'\bpractices\b'], [r'\bpractice\b'])
t('philosophy of history', [r'philosophy of history', r'historical (knowledge|understanding|explanation|past|thought|method|knowing|event|inquiry|enquiry)', r'\bon history\b', r'what is history', r'mode of history', r'history as a mode', r'historical past', r'historiograph', r'theory of history', r'historians?\b'])
t('science', [r'scientism', r'philosophy of science', r'science as a mode', r'scientific (experience|positivism|knowledge)', r'natural science'], [r'\bscien(ce|tific)\b'])
t('social science', [r'social science'])
t('poetry', [r'\bpoe(try|tic|t|tics)\b'])
t('aesthetics', [r'aesthetic', r'(?<!work of )\bart\b(?! of)', r'(the|other) arts\b'])
t('conversation', [r'conversation'])
t('idealism', [r'idealis[mt]'])
t('scepticism', [r'[ck]eptic'])
t('politics of faith', [r'politics of faith'])
t('politics of scepticism', [r'politics of s[ck]epticism'])
t('liberalism', [r'liberalism', r'liberal (theor|democra|tradition|state|thought)'], [r'\bliberals?\b(?! (learning|education|arts))'])
t('education', [r'liberal (learning|education)', r'\beducation', r'\buniversit(y|ies)\b', r'curricul', r'universit(y|ies)\b(?! (of|press))', r'idea of a university', r'schooling'])
t('authority', [r'\bauthorit(y|ative|ies)\b'])
t('law', [r'rule of law', r'\blaw\b', r'\blegal\b', r'\blegal theory', r'\blex\b', r'system of laws'])
t('jurisprudence', [r'jurisprud'])
t('natural law', [r'natural law'])
t('freedom', [r'\bfreedom\b', r'\bliberty\b', r'\bliberties\b'])
t('individuality', [r'individuality', r'individualism', r'\bthe individual\b', r'individual manqu'])
t('morality', [r'\bmorality\b', r'moral (life|conduct|practice|education|philosophy|imagination|theory)', r'\bmorals\b'], [r'\bmoral\b'])
t('ethics', [r'\bethics?\b'])
t('human conduct', [r'(?<!On )human conduct', r'theory of conduct', r'human action', r'understanding human', r'moral conduct', r'conduct of life'], [r'(?<!Human )\bconduct\b', r'\baction\b'])
t('religion', [r'religio(n|us)', r'christian', r'theolog', r'\bchurch\b', r'\bgod\b', r'salvation'])
t('state', [r'modern european state', r'vocabulary of a modern', r'modern state', r'\bthe state\b', r'(?<!United )\bstates?\b'])
t('government', [r'\bgovern(ment|ance)\b(?! and Opposition)', r'self-government', r'\brulers?\b'])
t('contingency', [r'contingen'])
t('practical knowledge', [r'practical knowledge', r'technical knowledge', r'tacit', r'know-how', r'knowing how', r'knowledge of technique', r'\btechnique\b'])
t('ideology', [r'ideolog'])
t('political education', [r'political education'])
t('pluralism', [r'plural'])
t('civility', [r'civility', r'civil condition', r'civil society', r'\bcivil life\b'])
t('democracy', [r'democra'])
t('modernity', [r'modernity', r'modern europe\b', r'\bmodern (politics|world|age)\b'])
t('Enlightenment', [r'enlightenment'])
t('myth', [r'\bmyth'])
t('play', [r'\bplay\b', r'homo ludens', r'\bgames?\b'], [])
t('international relations', [r'international (relations|society|politics|order)', r'world politics'])
t('history of political thought', [r'history of political (thought|ideas)', r'history of ideas', r'political thought seminar'])
t('political philosophy', [r'political philosoph'])
t('political economy', [r'political economy', r'(?<!school of )\beconomi(c|cs|es|y)\b', r'\bmarkets?\b', r'capitalism'])
t('self-understanding', [r'self-understanding', r'self-enactment', r'self-disclosure', r'self-realization', r'self-knowledge'])
t('postmodernism', [r'postmodern', r'poststructural'])
t('horse racing', [r'\bderby\b', r'horse'])
t('London School of Economics', [r'london school of economics', r'\bLSE\b'])
t('Cambridge', [r'cambridge (school|minds?|review|university)', r'gonville'], [])
t('intimations', [r'intimation'])
t('philosophy', [r'nature of philosophy', r'conception of philosophy', r'philosophical (inquiry|reflection|experience)', r'conceptions of philosophy', r'practice of philosophy', r'philosophy and its moods'])
t('judgement', [r'judge?ment'])
t('equality', [r'equality'])
t('socialism', [r'sociali[sz]'])
t('totalitarianism', [r'totalitarian'])
t('legitimacy', [r'legitima'])
t('power', [r'\bpower\b'], [])
t('reason', [r'rationality', r'(role|limits?|capacity|life|theory|application) of reason', r'reason in politics', r'practical reason', r'\breason and', r'reason\'s', r'rejection of reason', r'^Reason'], [r'\breason\b'])
# Oakeshott's works, as subjects of other entries
t('On Human Conduct (1975)', [r'On Human Conduct'], cs=True)
t('Experience and Its Modes (1933)', [r'Experience and [Ii]ts Modes'], cs=True)
t('Rationalism in Politics (essay and collection)', [r'Rationalism in Politics'], cs=True)
t('The Voice of Poetry in the Conversation of Mankind (1959)', [r'Voice of Poetry in the Conversation'], cs=True)
t('On History and Other Essays (1983)', [r'On History'], cs=True)
t('Political Education (1951)', [r'Political Education'], cs=True)
t('On Being Conservative (essay)', [r'On Being Conservative'], cs=True)
t('The Tower of Babel (essay)', [r'Tower of Babel'], cs=True)
# people: name -> sure pattern (case-sensitive)
P = {
 'Hobbes, Thomas': r'Hobbes', 'Hegel, G. W. F.': r'Hegel', 'Bradley, F. H.': r'Bradley', 'Collingwood, R. G.': r'Collingwood',
 'Gadamer, Hans-Georg': r'Gadamer', 'Hayek, F. A.': r'Hayek', 'Strauss, Leo': r'Strauss', 'Wittgenstein, Ludwig': r'Wittgenstein',
 'Ryle, Gilbert': r'Ryle\b', 'Polanyi, Michael': r'Polanyi', 'Popper, Karl': r'Popper', 'Schmitt, Carl': r'Schmitt',
 'Weber, Max': r'Weber\b', 'Burke, Edmund': r'Burke', 'Hume, David': r'Hume\b', 'Kant, Immanuel': r'Kant', 'Rawls, John': r'Rawls',
 'Arendt, Hannah': r'Arendt', 'Confucius': r'Confuci', 'Daoism': r'Dao(ism|ist)|Taois|Zhuangzi', 'Machiavelli, Niccolò': r'Machiavell',
 'Spinoza, Baruch': r'Spinoza', 'Bentham, Jeremy': r'Bentham', 'Mill, J. S.': r'\bMill\b', 'Dewey, John': r'Dewey', 'Newman, John Henry': r'Newman',
 'Berlin, Isaiah': r'Isaiah Berlin|Berlin, (and|Arendt)|Popper and Berlin|Oakeshott, Berlin|Berlin and|Berlin, Oakeshott|\bBerlin\b(?=,)', 'Schopenhauer, Arthur': r'Schopenhauer',
 'Montaigne, Michel de': r'Montaigne', 'Augustine of Hippo': r'Augustin', 'Aristotle': r'Aristot', 'Plato': r'Plato', 'Socrates': r'Socrat',
 'Laski, Harold': r'Laski', 'Voegelin, Eric': r'Voegelin', 'Mises, Ludwig von': r'Mises', 'Simmel, Georg': r'Simmel', 'Flathman, Richard': r'Flathman',
 'Talmon, Jacob': r'Talmon', 'Maritain, Jacques': r'Maritain', 'Kolnai, Aurel': r'Kolnai', 'Tönnies, Ferdinand': r'Tönnies', 'Godwin, William': r'Godwin',
 'Sartre, Jean-Paul': r'Sartre', 'Winch, Peter': r'Winch', 'Grote, John': r'Grote', 'Pascal, Blaise': r'Pascal', 'Locke, John': r'Locke',
 'Rousseau, Jean-Jacques': r'Rousseau', 'Marx, Karl': r'Marx', 'Nietzsche, Friedrich': r'Nietzsche', 'Heidegger, Martin': r'Heidegger',
 'Lewis, C. S.': r'C\. ?S\. Lewis', 'Orwell, George': r'Orwell', 'Powell, Anthony': r'Anthony Powell', 'Fuller, Lon L.': r'Lon (L\. )?Fuller|Leoni, Fuller',
 'Habermas, Jürgen': r'Habermas', 'Rorty, Richard': r'Rorty', 'Shils, Edward': r'Shils', 'Strawson, P. F.': r'Strawson', 'Bosanquet, Bernard': r'Bosanquet',
 'Green, T. H.': r'T\. ?H\. Green|Green to Dworkin', 'Taylor, Charles': r'Charles Taylor|Shils, Taylor', 'MacIntyre, Alasdair': r'MacIntyre', 'Croce, Benedetto': r'Croce',
 'Jacobs, Jane': r'Jane Jacobs', 'Trollope, Anthony': r'Trollope', 'Burckhardt, Jacob': r'Burckhardt', 'Bacon, Francis': r'Bacon', 'Descartes, René': r'Descartes',
 'Butterfield, Herbert': r'Butterfield', 'Vico, Giambattista': r'Vico\b', 'Smith, Adam': r'Adam Smith|Hume and Smith', 'Hart, H. L. A.': r'H\. ?L\. ?A\. Hart|Hart and Lon',
 'Bolingbroke, Viscount': r'Bolingbroke', 'Cavell, Stanley': r'Cavell', 'Foucault, Michel': r'Foucault', 'Skinner, Quentin': r'Quentin Skinner|Skinner\b',
 'Lao Tzu': r'Lao[- ]?(Tzu|Tse|zi)', 'Mouffe, Chantal': r'Mouffe', 'Valéry, Paul': r'Val[ée]ry', 'Leviathan (Hobbes)': r'Leviathan',
}
