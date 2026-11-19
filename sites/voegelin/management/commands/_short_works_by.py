"""Short works by Eric Voegelin: his essays, articles, published
lectures and chapters, in their first publication (1922-1985), for
load_short_works_by_voegelin. Book reviews are a separate load.

Compiled 2026-11-19 from the Collected Works (vols 6-12, 27, 28, 32, 33:
their contents and editors' notes on first publication), the Eric
Voegelin Institute's list of articles and essays, the Voegelin papers
register (Hoover Institution), Crossref, K10plus and Open Library;
"source" is the record used. Doubts the sources left open are in
QUESTIONS, which the loader puts on the editors' to-do page.

ARTICLES are in a journal or newspaper, CHAPTERS in a book (a key into
HOSTS, stored as Works Mentioning Voegelin). authors: "V" is Voegelin.
reprinted: keys (in _books_by.py) of the books of his that reprint the
piece, usually a Collected Works volume.
"""

PUBLISHERS = {}

HOSTS = {'gesellschaft_staat_und_recht_f': {'title': 'Gesellschaft, Staat und Recht: '
                                             'Festschrift gewidmet Hans '
                                             'Kelsen zum 50. Geburtstage',
                                    'year': 1931,
                                    'publisher': 'Springer',
                                    'city': 'Wien',
                                    'editors': [('Alfred', '', 'Verdross')],
                                    'subject': 'Philosophy'},
 'die_kunst_des_denkens': {'title': 'Die Kunst des Denkens',
                           'year': 1932,
                           'publisher': 'Herder',
                           'city': 'Freiburg im Breisgau',
                           'editors': [],
                           'subject': 'Philosophy'},
 'psychologie_des_gemeinschaftsl': {'title': 'Psychologie des '
                                             'Gemeinschaftslebens: Bericht '
                                             'über den 14. Kongreß der '
                                             'Deutschen Gesellschaft für '
                                             'Psychologie in Tübingen vom '
                                             '22.-26. Mai 1934',
                                    'year': 1935,
                                    'publisher': 'Gustav Fischer',
                                    'city': 'Jena',
                                    'editors': [('Otto', '', 'Klemm')],
                                    'subject': 'Politics'},
 'actorum_academiae_universalis': {'title': 'Actorum Academiae Universalis '
                                            'Jurisprudentiae Comparativae / '
                                            "Mémoires de l'Académie "
                                            'Internationale de Droit '
                                            'Comparé, vol. 2, pt. 3',
                                   'year': 1935,
                                   'publisher': 'Sirey',
                                   'city': 'Paris',
                                   'editors': [('Elemér', '', 'Balogh')],
                                   'subject': 'Law'},
 'memoranda_prepared_by_a_study': {'title': 'Memoranda. Prepared by a Study '
                                            'Group on Ideological Questions. '
                                            'Austrian Coordinating Committee '
                                            'for International Studies. '
                                            'General Study Conference on '
                                            'Peaceful Change. International '
                                            'Studies Conference, 10th '
                                            'Session, June 28-July 3, 1937',
                                   'year': 1937,
                                   'publisher': 'League of Nations, '
                                                'Institute for International '
                                                'Intellectual Cooperation',
                                   'city': 'Paris',
                                   'editors': [],
                                   'subject': 'Politics'},
 'goethe_after_two_centuries': {'title': 'Goethe after Two Centuries',
                                'year': 1952,
                                'publisher': 'Louisiana State University '
                                             'Press',
                                'city': 'Baton Rouge',
                                'editors': [('Carl', '', 'Hammer')],
                                'subject': 'Literature'},
 'problems_of_communication_in_a': {'title': 'Problems of Communication in a '
                                             'Pluralistic Society',
                                    'year': 1956,
                                    'publisher': 'Marquette University Press',
                                    'city': 'Milwaukee',
                                    'editors': [],
                                    'subject': 'Politics'},
 'erziehung_zur_freiheit': {'title': 'Erziehung zur Freiheit',
                            'year': 1959,
                            'publisher': 'Eugen Rentsch',
                            'city': 'Erlenbach-Zürich and Stuttgart',
                            'editors': [('Albert', '', 'Hunold')],
                            'subject': 'Politics'},
 'colloques_de_rheinfelden': {'title': 'Colloques de Rheinfelden',
                              'year': 1960,
                              'publisher': 'Calmann-Lévy',
                              'city': 'Paris',
                              'editors': [('Raymond', '', 'Aron'),
                                          ('George', 'F.', 'Kennan')],
                              'subject': 'Sociology'},
 'christentum_und_liberalismus': {'title': 'Christentum und Liberalismus',
                                  'year': 1960,
                                  'publisher': 'Zink',
                                  'city': 'München',
                                  'editors': [('Karl', '', 'Forster')],
                                  'subject': 'Politics'},
 'the_intent_of_toynbee_s_histor': {'title': "The Intent of Toynbee's "
                                             'History',
                                    'year': 1961,
                                    'publisher': 'Loyola University Press',
                                    'city': 'Chicago',
                                    'editors': [('Edward', 'T.', 'Gargan')],
                                    'subject': 'History'},
 'l_histoire_et_ses_interprétati': {'title': "L'histoire et ses "
                                             'interprétations: Entretiens '
                                             'autour de Arnold Toynbee',
                                    'year': 1961,
                                    'publisher': 'Mouton',
                                    'city': 'Paris and The Hague',
                                    'editors': [('Raymond', '', 'Aron')],
                                    'subject': 'History'},
 'the_old_testament_and_christia': {'title': 'The Old Testament and '
                                             'Christian Faith: A Theological '
                                             'Discussion',
                                    'year': 1963,
                                    'publisher': 'Harper & Row',
                                    'city': 'New York',
                                    'editors': [('Bernhard',
                                                 'W.',
                                                 'Anderson')],
                                    'subject': 'Religion'},
 'zeit_und_geschichte_dankesgabe': {'title': 'Zeit und Geschichte: '
                                             'Dankesgabe an Rudolf Bultmann '
                                             'zum 80. Geburtstag',
                                    'year': 1964,
                                    'publisher': 'J. C. B. Mohr (Paul '
                                                 'Siebeck)',
                                    'city': 'Tübingen',
                                    'editors': [('Erich', '', 'Dinkler')],
                                    'subject': 'Philosophy'},
 'die_unternehmerische_verantwor': {'title': 'Die unternehmerische '
                                             'Verantwortung in unserer '
                                             'Gesellschaftsordnung '
                                             '(Veröffentlichungen der '
                                             'Walter-Raymond-Stiftung, Bd. '
                                             '4)',
                                    'year': 1964,
                                    'publisher': 'Westdeutscher Verlag',
                                    'city': 'Köln and Opladen',
                                    'editors': [],
                                    'subject': 'Sociology'},
 'historica_studien_zum_geschich': {'title': 'Historica: Studien zum '
                                             'geschichtlichen Denken und '
                                             'Forschen. Festschrift für '
                                             'Friedrich Engel-Janosi',
                                    'year': 1965,
                                    'publisher': 'Herder',
                                    'city': 'Wien',
                                    'editors': [('Hugo', '', 'Hantsch'),
                                                ('Eric', '', 'Voegelin'),
                                                ('Franco', '', 'Valsecchi')],
                                    'subject': 'Philosophy'},
 'die_deutsche_universität_im_dr': {'title': 'Die deutsche Universität im '
                                             'Dritten Reich: Eine '
                                             'Vortragsreihe der Universität '
                                             'München',
                                    'year': 1966,
                                    'publisher': 'R. Piper',
                                    'city': 'München',
                                    'editors': [],
                                    'subject': 'Politics'},
 'the_concept_of_order': {'title': 'The Concept of Order',
                          'year': 1968,
                          'publisher': 'University of Washington Press',
                          'city': 'Seattle',
                          'editors': [('Paul', 'G.', 'Kuntz')],
                          'subject': 'History'},
 'zwischen_revolution_und_restau': {'title': 'Zwischen Revolution und '
                                             'Restauration: Politisches '
                                             'Denken in England im 17. '
                                             'Jahrhundert',
                                    'year': 1968,
                                    'publisher': 'Paul List Verlag',
                                    'city': 'München',
                                    'editors': [],
                                    'subject': 'Politics'},
 'aufklärung_und_materialismus_i': {'title': 'Aufklärung und Materialismus '
                                             'im Frankreich des 18. '
                                             'Jahrhunderts',
                                    'year': 1968,
                                    'publisher': 'Paul List Verlag',
                                    'city': 'München',
                                    'editors': [('Arno', '', 'Baruzzi')],
                                    'subject': 'Philosophy'},
 'eternità_e_storia_i_valori_per': {'title': 'Eternità e storia: I valori '
                                             'permanenti nel divenire '
                                             'storico',
                                    'year': 1970,
                                    'publisher': 'Vallecchi',
                                    'city': 'Firenze',
                                    'editors': [],
                                    'subject': 'Philosophy'},
 'phenomenology_and_social_reali': {'title': 'Phenomenology and Social '
                                             'Reality: Essays in Memory of '
                                             'Alfred Schutz',
                                    'year': 1970,
                                    'publisher': 'Martinus Nijhoff',
                                    'city': 'The Hague',
                                    'editors': [('Maurice', '', 'Natanson')],
                                    'subject': 'Philosophy'},
 'jesus_and_man_s_hope_vol_2': {'title': "Jesus and Man's Hope, vol. 2",
                                'year': 1971,
                                'publisher': 'Pittsburgh Theological '
                                             'Seminary Press',
                                'city': 'Pittsburgh',
                                'editors': [('Donald', 'G.', 'Miller'),
                                            ('Dikran', 'Y.', 'Hadidian')],
                                'subject': 'Religion'}}

ARTICLES = [{'key': 'e01',
  'title': 'Die gesellschaftliche Bestimmtheit soziologischer Erkenntnis',
  'year': 1922,
  'language': 'German',
  'subject': 'Sociology',
  'authors': ['V'],
  'volume': 'N.F. 2',
  'issue': '4-6',
  'pages': '331-348',
  'journal': 'Zeitschrift für Volkswirtschaft und Sozialpolitik',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e02',
  'title': 'Reine Rechtslehre und Staatslehre',
  'year': 1924,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '4',
  'issue': '1/2',
  'pages': '80-131',
  'journal': 'Zeitschrift für öffentliches Recht',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e03',
  'title': 'Die Zeit in der Wirtschaft',
  'year': 1924,
  'language': 'German',
  'subject': 'Economics',
  'authors': ['V'],
  'volume': '53',
  'issue': '1',
  'pages': '186-211',
  'journal': 'Archiv für Sozialwissenschaft und Sozialpolitik',
  'reprinted': ['cw07'],
  'source': 'https://opac.k10plus.de/DB=2.1/PPNSET?PPN=493743901'},
 {'key': 'e04',
  'title': 'Über Max Weber',
  'year': 1925,
  'language': 'German',
  'subject': 'Sociology',
  'authors': ['V'],
  'volume': '3',
  'issue': '2',
  'pages': '177-193',
  'journal': 'Deutsche Vierteljahrsschrift für Literaturwissenschaft und '
             'Geistesgeschichte',
  'reprinted': ['cw07'],
  'source': 'https://opac.k10plus.de/DB=2.1/PPNSET?PPN=1133746810'},
 {'key': 'e05',
  'title': 'Die Verfassungsmäßigkeit des 18. Amendments zur United States '
           'Constitution',
  'year': 1926,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '5',
  'issue': '3',
  'pages': '445-464',
  'journal': 'Zeitschrift für öffentliches Recht',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e06',
  'title': 'Wirtschafts- und Klassengegensatz in Amerika',
  'year': 1926,
  'language': 'German',
  'subject': 'Sociology',
  'authors': ['V'],
  'volume': '5',
  'issue': '6',
  'pages': '6-11',
  'journal': 'Unterrichtsbriefe des Instituts für angewandte Soziologie',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e07',
  'title': "Kelsen's Pure Theory of Law",
  'year': 1927,
  'language': 'English',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '42',
  'issue': '2',
  'pages': '268-276',
  'journal': 'Political Science Quarterly',
  'reprinted': ['cw07'],
  'source': 'https://doi.org/10.2307/2142789'},
 {'key': 'e08',
  'title': 'La Follette und die Wisconsin-Idee',
  'year': 1927,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '17',
  'issue': '4',
  'pages': '309-321',
  'journal': 'Zeitschrift für Politik',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e09',
  'title': 'Zur Lehre von der Staatsform',
  'year': 1927,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '6',
  'issue': '4',
  'pages': '572-608',
  'journal': 'Zeitschrift für öffentliches Recht',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e10',
  'title': 'Konjunkturforschung und Stabilisation des Kapitalismus',
  'year': 1928,
  'language': 'German',
  'subject': 'Economics',
  'authors': ['V'],
  'volume': '9',
  'issue': '9/10',
  'pages': '252-259',
  'journal': 'Mitteilungen des Verbandes österreichischer Banken und '
             'Bankiers',
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e11',
  'title': 'Die ergänzende Bill zum Federal Reserve Act',
  'year': 1928,
  'language': 'German',
  'subject': 'Economics',
  'authors': ['V'],
  'volume': '2',
  'issue': '2',
  'pages': '225-229',
  'journal': 'Nationalwirtschaft',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/files/eric-voegelin-papers.pdf'},
 {'key': 'e12',
  'title': 'Die ergänzende Bill zum Federal Reserve Act und die '
           'Dollarstabilisation',
  'year': 1928,
  'language': 'German',
  'subject': 'Economics',
  'authors': ['V'],
  'volume': '10',
  'issue': '11/12',
  'journal': 'Mitteilungen des Verbandes österreichischer Banken und '
             'Bankiers',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e13',
  'title': 'Der Sinn der Erklärung der Menschen- und Bürgerrechte von 1789',
  'year': 1928,
  'language': 'German',
  'subject': 'History',
  'authors': ['V'],
  'volume': '8',
  'issue': '1',
  'pages': '82-120',
  'journal': 'Zeitschrift für öffentliches Recht',
  'reprinted': ['cw07'],
  'source': 'https://opac.k10plus.de/DB=2.1/PPNSET?PPN=627753361'},
 {'key': 'e14',
  'title': 'Zwei Grundbegriffe der Humeschen Gesellschaftslehre',
  'year': 1928,
  'language': 'German',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '1',
  'issue': '2',
  'pages': '11-16',
  'journal': 'Archiv für angewandte Soziologie',
  'reprinted': ['cw07'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e15',
  'title': 'Die Souveränitätstheorie Dickinsons und die Reine Rechtslehre',
  'year': 1929,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '8',
  'issue': '3',
  'pages': '413-434',
  'journal': 'Zeitschrift für öffentliches Recht',
  'reprinted': ['cw08'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e16',
  'title': 'Die Transaktion',
  'year': 1929,
  'language': 'German',
  'subject': 'Economics',
  'authors': ['V'],
  'volume': '1',
  'issue': '4/5',
  'pages': '14-21',
  'journal': 'Archiv für angewandte Soziologie',
  'reprinted': ['cw08'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e17',
  'title': 'Die amerikanische Theorie vom Eigentum',
  'year': 1930,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '2',
  'issue': '4',
  'pages': '165-172',
  'journal': 'Archiv für angewandte Soziologie',
  'reprinted': ['cw08'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e18',
  'title': 'Die amerikanische Theorie vom ordentlichen Rechtsverfahren und '
           'von der Freiheit',
  'year': 1930,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '3',
  'issue': '1',
  'pages': '40-57',
  'journal': 'Archiv für angewandte Soziologie',
  'reprinted': ['cw08'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e19',
  'title': 'Die österreichische Verfassungsreform von 1929',
  'year': 1930,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '19',
  'issue': '9',
  'pages': '585-615',
  'journal': 'Zeitschrift für Politik',
  'reprinted': ['cw08'],
  'source': 'https://opac.k10plus.de/DB=2.1/PPNSET?PPN=1137875240'},
 {'key': 'e20',
  'title': 'Max Weber',
  'year': 1930,
  'language': 'German',
  'subject': 'Sociology',
  'authors': ['V'],
  'volume': '9',
  'issue': '1/2',
  'pages': '1-16',
  'journal': 'Kölner Vierteljahrshefte für Soziologie',
  'reprinted': ['cw08'],
  'source': 'https://opac.k10plus.de/DB=2.1/PPNSET?PPN=1137001682'},
 {'key': 'e21',
  'title': 'Die Einheit des Rechtes und das soziale Sinngebilde Staat',
  'year': 1930,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '5',
  'issue': '1/2',
  'pages': '58-89',
  'journal': 'Internationale Zeitschrift für Theorie des Rechts',
  'reprinted': ['cw08'],
  'source': 'https://opac.k10plus.de/DB=2.1/PPNSET?PPN=113403203X'},
 {'key': 'e24',
  'title': 'Rassenidee und Wissenschaft: Ein Beitrag zur Klärung',
  'year': 1934,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '21',
  'month': 'January',
  'pages': '9',
  'journal': 'Kölnische Zeitung',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e25',
  'title': 'Nochmals, Rasse und Staat in der Staatslehre: Erwiderung',
  'year': 1934,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '55',
  'pages': '202-203',
  'journal': 'Reichsverwaltungsblatt und Preussisches Verwaltungsblatt',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e26',
  'title': 'Verfassungsgebung für Österreich',
  'year': 1934,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '27',
  'month': 'April',
  'pages': '1-2',
  'journal': 'Wiener Zeitung',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e27',
  'title': 'Neues Kammersystem im Spiegel der Geschichte',
  'year': 1934,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '5',
  'month': 'May',
  'pages': '1',
  'journal': 'Wiener Zeitung',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e28',
  'title': 'Der autoritäre Staatskern',
  'year': 1934,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '13',
  'month': 'May',
  'pages': '1-2',
  'journal': 'Wiener Zeitung',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e29',
  'title': 'Todesreigen 1934: Eine Rückschau zum Gedenktage der Toten',
  'year': 1934,
  'language': 'German',
  'subject': 'Literature',
  'authors': ['V'],
  'day': '1',
  'month': 'November',
  'pages': '3',
  'journal': 'Wiener Zeitung',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e32',
  'title': 'Volksbildung, Wissenschaft und Politik',
  'year': 1936,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '1',
  'issue': '7',
  'pages': '594-603',
  'journal': 'Monatsschrift für Kultur und Politik',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e33',
  'title': 'Josef Redlich',
  'year': 1936,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '65',
  'issue': '23',
  'pages': '485-486',
  'journal': 'Juristische Blätter',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e34',
  'title': 'Meinungsäußerung und Meinungsbildung',
  'year': 1937,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '30',
  'month': 'May',
  'pages': '1',
  'journal': 'Neue Freie Presse',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e35',
  'title': 'Österreich und die Studienkonferenz',
  'year': 1937,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '19',
  'month': 'June',
  'pages': '3-4',
  'journal': 'Neue Freie Presse',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e37',
  'title': 'Das Timurbild der Humanisten: Eine Studie zur politischen '
           'Mythenbildung',
  'year': 1937,
  'language': 'German',
  'subject': 'History',
  'authors': ['V'],
  'volume': '17',
  'issue': '5',
  'pages': '545-582',
  'journal': 'Zeitschrift für öffentliches Recht',
  'reprinted': ['anamnesis_de', 'cw06'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e38',
  'title': 'Was dürfen die Menschen wissen?',
  'year': 1937,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '7',
  'month': 'November',
  'pages': '1-2',
  'journal': 'Neue Freie Presse',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e39',
  'title': 'Der neue Stil des Krieges',
  'year': 1937,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '20',
  'month': 'November',
  'pages': '2',
  'journal': 'Neue Freie Presse',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e40',
  'title': 'Flucht in die Arbeit',
  'year': 1937,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'day': '16',
  'month': 'December',
  'pages': '1-2',
  'journal': 'Neue Freie Presse',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'l01',
  'title': 'Extended Strategy: A New Technique of Dynamic Relations',
  'year': 1940,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '2',
  'issue': '2',
  'pages': '189-200',
  'journal': 'The Journal of Politics',
  'reprinted': ['cw10'],
  'source': 'https://doi.org/10.2307/2125252'},
 {'key': 'l02',
  'title': 'The Growth of the Race Idea',
  'year': 1940,
  'language': 'English',
  'subject': 'History',
  'authors': ['V'],
  'volume': '2',
  'issue': '3',
  'pages': '283-317',
  'journal': 'The Review of Politics',
  'reprinted': ['cw10'],
  'source': 'https://doi.org/10.1017/s003467050000053x'},
 {'key': 'l03',
  'title': 'Some Problems of German Hegemony',
  'year': 1941,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '3',
  'issue': '2',
  'pages': '154-168',
  'journal': 'The Journal of Politics',
  'reprinted': ['cw10'],
  'source': 'https://doi.org/10.2307/2125429'},
 {'key': 'l04',
  'title': 'The Mongol Orders of Submission to European Powers, 1245-1255',
  'year': 1941,
  'language': 'English',
  'subject': 'History',
  'authors': ['V'],
  'volume': '15',
  'pages': '378-413',
  'journal': 'Byzantion',
  'reprinted': ['cw10', 'anamnesis_de', 'cw06'],
  'source': 'https://books.google.com/books?id=SnzKSc-Dn24C'},
 {'key': 'l05',
  'title': 'Nietzsche, the Crisis and the War',
  'year': 1944,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '6',
  'issue': '2',
  'pages': '177-212',
  'journal': 'The Journal of Politics',
  'reprinted': ['cw10'],
  'source': 'https://doi.org/10.2307/2125271'},
 {'key': 'l06',
  'title': 'Siger de Brabant',
  'year': 1944,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '4',
  'issue': '4',
  'pages': '507-526',
  'journal': 'Philosophy and Phenomenological Research',
  'reprinted': ['cw20'],
  'source': 'https://doi.org/10.2307/2103038'},
 {'key': 'l07',
  'title': 'Political Theory and the Pattern of General History',
  'year': 1944,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '38',
  'issue': '4',
  'pages': '746-754',
  'journal': 'The American Political Science Review',
  'reprinted': ['cw10'],
  'source': 'https://doi.org/10.2307/1950484'},
 {'key': 'l08',
  'title': "Bakunin's Confession",
  'year': 1946,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '8',
  'issue': '1',
  'pages': '24-43',
  'journal': 'The Journal of Politics',
  'reprinted': ['anamnesis_de', 'cw06'],
  'source': 'https://doi.org/10.2307/2125606'},
 {'key': 'l09',
  'title': 'Zu Sanders „Allgemeiner Staatslehre“',
  'year': 1947,
  'language': 'German',
  'subject': 'Law',
  'authors': ['V'],
  'volume': '1 (n.s.)',
  'issue': '1-2',
  'pages': '106-135',
  'journal': 'Österreichische Zeitschrift für öffentliches Recht',
  'source': 'https://books.google.com/books?id=SnzKSc-Dn24C'},
 {'key': 'l10',
  'title': "Plato's Egyptian Myth",
  'year': 1947,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '9',
  'issue': '3',
  'pages': '307-324',
  'journal': 'The Journal of Politics',
  'reprinted': ['oh3', 'cw16'],
  'source': 'https://doi.org/10.2307/2125794'},
 {'key': 'l11',
  'title': 'The Origins of Scientism',
  'year': 1948,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '15',
  'issue': '4',
  'pages': '462-494',
  'journal': 'Social Research',
  'reprinted': ['cw10'],
  'source': 'https://books.google.com/books?id=SnzKSc-Dn24C'},
 {'key': 'l12',
  'title': "The Philosophy of Existence: Plato's Gorgias",
  'year': 1949,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '11',
  'issue': '4',
  'pages': '477-498',
  'journal': 'The Review of Politics',
  'reprinted': ['oh3', 'cw16'],
  'source': 'https://doi.org/10.1017/s0034670500043825'},
 {'key': 'l13',
  'title': 'The Formation of the Marxian Revolutionary Idea',
  'year': 1950,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '12',
  'issue': '3',
  'pages': '275-302',
  'journal': 'The Review of Politics',
  'reprinted': ['cw26'],
  'source': 'https://doi.org/10.1017/s0034670500046982'},
 {'key': 'l14',
  'title': "Machiavelli's Prince: Background and Formation",
  'year': 1951,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '13',
  'issue': '2',
  'pages': '142-168',
  'journal': 'The Review of Politics',
  'reprinted': ['cw22'],
  'source': 'https://doi.org/10.1017/s0034670500047409'},
 {'key': 'l15',
  'title': "More's Utopia",
  'year': 1951,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '3 (n.s.)',
  'issue': '4',
  'pages': '451-468',
  'journal': 'Österreichische Zeitschrift für öffentliches Recht',
  'reprinted': ['cw10', 'cw22'],
  'source': 'https://books.google.com/books?id=SnzKSc-Dn24C'},
 {'key': 'l16',
  'title': 'Gnostische Politik',
  'year': 1952,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '6',
  'issue': '4',
  'pages': '301-317',
  'journal': 'Merkur',
  'reprinted': ['cw10'],
  'source': 'https://www.merkur-zeitschrift.de/artikel/gnostische-politik-a-mr-6-4-301/'},
 {'key': 'l18',
  'title': 'The Origins of Totalitarianism',
  'year': 1953,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '15',
  'issue': '1',
  'pages': '68-76',
  'journal': 'The Review of Politics',
  'reprinted': ['cw11'],
  'source': 'https://doi.org/10.1017/s0034670500007439'},
 {'key': 'l19',
  'title': 'The World of Homer',
  'year': 1953,
  'language': 'English',
  'subject': 'History',
  'authors': ['V'],
  'volume': '15',
  'issue': '4',
  'pages': '491-523',
  'journal': 'The Review of Politics',
  'reprinted': ['oh2', 'cw15'],
  'source': 'https://doi.org/10.1017/s0034670500001923'},
 {'key': 'l20',
  'title': 'The Oxford Political Philosophers',
  'year': 1953,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '3',
  'issue': '11',
  'pages': '97-114',
  'journal': 'The Philosophical Quarterly',
  'reprinted': ['cw11'],
  'source': 'https://doi.org/10.2307/2216880'},
 {'key': 'l22',
  'title': 'Der Prophet Elias',
  'year': 1958,
  'language': 'German',
  'subject': 'Religion',
  'authors': ['V'],
  'volume': '50',
  'issue': '4',
  'pages': '325-339',
  'journal': 'Hochland',
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l24',
  'title': 'Demokratie im neuen Europa',
  'year': 1959,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '4',
  'issue': '7',
  'pages': '293-300',
  'journal': 'Gesellschaft – Staat – Erziehung',
  'reprinted': ['cw11'],
  'source': 'https://books.google.com/books?id=0ENcH_0EpuMC'},
 {'key': 'l25',
  'title': 'El concepto de la "buena sociedad"',
  'year': 1960,
  'language': 'Spanish',
  'subject': 'Politics',
  'authors': ['V'],
  'issue': 'Supl. 40',
  'pages': '25-28',
  'journal': 'Cuadernos del Congreso por la Libertad de la Cultura',
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l26',
  'title': 'Religionsersatz: Die gnostischen Massenbewegungen unserer Zeit',
  'year': 1960,
  'language': 'German',
  'subject': 'Religion',
  'authors': ['V'],
  'volume': '15',
  'issue': '1',
  'pages': '5-18',
  'journal': 'Wort und Wahrheit',
  'reprinted': ['spg_1968', 'cw05'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l28',
  'title': 'Verantwortung und Freiheit in Wirtschaft und Demokratie',
  'year': 1960,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '10',
  'issue': '6',
  'pages': '207-213',
  'journal': 'Die Aussprache',
  'reprinted': ['cw11'],
  'source': 'https://books.google.com/books?id=0ENcH_0EpuMC'},
 {'key': 'l30',
  'title': 'Historiogenesis',
  'year': 1960,
  'language': 'German',
  'subject': 'History',
  'authors': ['V'],
  'volume': '68',
  'pages': '419-446',
  'journal': 'Philosophisches Jahrbuch',
  'reprinted': ['anamnesis_de', 'cw06'],
  'source': 'https://books.google.com/books?id=3NSfsKgWcbkC'},
 {'key': 'l33',
  'title': 'World-Empire and the Unity of Mankind',
  'year': 1962,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '38',
  'issue': '2',
  'pages': '170-188',
  'journal': 'International Affairs',
  'reprinted': ['cw11'],
  'source': 'https://doi.org/10.2307/2610376'},
 {'key': 'l34',
  'title': 'Das Rechte von Natur',
  'year': 1963,
  'language': 'German',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '13',
  'issue': '1-2',
  'pages': '38-51',
  'journal': 'Österreichische Zeitschrift für öffentliches Recht',
  'reprinted': ['anamnesis_de', 'cw06', 'anamnesis_en'],
  'source': 'https://books.google.com/books?id=3NSfsKgWcbkC'},
 {'key': 'l35',
  'title': 'Hacia una nueva ciencia del orden social',
  'year': 1963,
  'language': 'Spanish',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '1',
  'issue': '2',
  'pages': '121-137',
  'journal': 'Atlántida: Revista del pensamiento actual',
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l38',
  'title': 'Der Mensch in Gesellschaft und Geschichte',
  'year': 1964,
  'language': 'German',
  'subject': 'Sociology',
  'authors': ['V'],
  'volume': '14',
  'issue': '1-2',
  'pages': '1-13',
  'journal': 'Österreichische Zeitschrift für öffentliches Recht',
  'reprinted': ['cw11'],
  'source': 'https://books.google.com/books?id=0ENcH_0EpuMC'},
 {'key': 'l42',
  'title': 'Was ist politische Realität?',
  'year': 1966,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'volume': '7',
  'issue': '1',
  'pages': '2-54',
  'journal': 'Politische Vierteljahresschrift',
  'reprinted': ['anamnesis_de', 'cw06', 'anamnesis_en'],
  'source': 'https://books.google.com/books?id=3NSfsKgWcbkC'},
 {'key': 'l43',
  'title': 'On Debate and Existence',
  'year': 1967,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '3',
  'issue': '4-5',
  'pages': '143-152',
  'journal': 'The Intercollegiate Review',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l44',
  'title': 'Immortality: Experience and Symbol',
  'year': 1967,
  'language': 'English',
  'subject': 'Religion',
  'authors': ['V'],
  'volume': '60',
  'issue': '3',
  'pages': '235-279',
  'journal': 'Harvard Theological Review',
  'reprinted': ['cw12'],
  'source': 'https://doi.org/10.1017/s001781600000376x'},
 {'key': 'l50',
  'title': "On Henry James's Turn of the Screw",
  'year': 1971,
  'language': 'English',
  'subject': 'Literature',
  'authors': ['V'],
  'volume': '7 (n.s.)',
  'issue': '1',
  'pages': '3-48',
  'journal': 'The Southern Review',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l52',
  'title': 'On Hegel: A Study in Sorcery',
  'year': 1971,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '24',
  'pages': '335-368',
  'journal': 'Studium Generale',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l53',
  'title': 'On Classical Studies',
  'year': 1973,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '17',
  'issue': '1',
  'pages': '2-8',
  'journal': 'Modern Age',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l54',
  'title': 'Reason: The Classic Experience',
  'year': 1974,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '10 (n.s.)',
  'issue': '2',
  'pages': '237-264',
  'journal': 'The Southern Review',
  'reprinted': ['cw12', 'anamnesis_en'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l55',
  'title': 'Response to Professor Altizer\'s "A New History and a New But '
           'Ancient God?"',
  'year': 1975,
  'language': 'English',
  'subject': 'Religion',
  'authors': ['V'],
  'volume': '43',
  'issue': '4',
  'pages': '765-772',
  'journal': 'Journal of the American Academy of Religion',
  'reprinted': ['cw12'],
  'source': 'https://doi.org/10.1093/jaarel/xliii.4.765'},
 {'key': 'l56',
  'title': 'Philosophy of History: An Interview',
  'year': 1977,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'issue': '2',
  'pages': '135-139',
  'journal': 'New Orleans Review',
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l57',
  'title': 'Wisdom and the Magic of the Extreme: A Meditation',
  'year': 1981,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '17 (n.s.)',
  'issue': '2',
  'pages': '235-287',
  'journal': 'The Southern Review',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l58',
  'title': 'Der meditative Ursprung philosophischen Ordnungswissens',
  'year': 1981,
  'language': 'German',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '28',
  'pages': '130-137',
  'journal': 'Zeitschrift für Politik',
  'reprinted': ['obg', 'cw33'],
  'source': 'https://books.google.com/books?id=55mZCPhTtGoC'},
 {'key': 'l59',
  'title': 'Responses at the Panel Discussion of "The Beginning of the '
           'Beginning"',
  'year': 1984,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '4',
  'pages': '97-110',
  'journal': 'Lonergan Workshop',
  'reprinted': ['cw33'],
  'source': 'https://doi.org/10.5840/lw19844supplement9'},
 {'key': 'l60',
  'title': 'Autobiographical Statement at Age Eighty-Two',
  'year': 1984,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'volume': '4',
  'pages': '111-131',
  'journal': 'Lonergan Workshop',
  'reprinted': ['cw33'],
  'source': 'https://doi.org/10.5840/lw19844supplement10'},
 {'key': 'l61',
  'title': 'Quod Deus Dicitur',
  'year': 1985,
  'language': 'English',
  'subject': 'Religion',
  'authors': ['V'],
  'volume': '53',
  'issue': '4',
  'pages': '569-584',
  'journal': 'Journal of the American Academy of Religion',
  'reprinted': ['cw12'],
  'source': 'https://doi.org/10.1093/jaarel/liii.4.569'}]

CHAPTERS = [{'key': 'e22',
  'title': 'Das Sollen im System Kants',
  'year': 1931,
  'language': 'German',
  'subject': 'Philosophy',
  'authors': ['V'],
  'pages': '136-173',
  'book': 'gesellschaft_staat_und_recht_f',
  'reprinted': ['cw08'],
  'source': 'https://doi.org/10.1007/978-3-7091-5991-0_6'},
 {'key': 'e23',
  'title': 'Nachwort',
  'year': 1932,
  'language': 'German',
  'subject': 'Philosophy',
  'authors': ['V'],
  'pages': '279-296',
  'book': 'die_kunst_des_denkens',
  'reprinted': ['cw08'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'e30',
  'title': 'Rasse und Staat',
  'year': 1935,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'pages': '91-104',
  'book': 'psychologie_des_gemeinschaftsl',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e31',
  'title': 'Le régime administratif: Avantages et inconvénients',
  'year': 1935,
  'language': 'French',
  'subject': 'Law',
  'authors': ['V', ('Adolf', '', 'Merkl')],
  'pages': '126-149',
  'book': 'actorum_academiae_universalis',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'e36',
  'title': 'Changes in the Ideas of Government and Constitution in Austria '
           'since 1918',
  'year': 1937,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'pages': '1-16',
  'book': 'memoranda_prepared_by_a_study',
  'reprinted': ['cw09'],
  'source': 'The Collected Works of Eric Voegelin, vol. 9 (University of '
            "Missouri Press, 2001), editor's notes"},
 {'key': 'l17',
  'title': "Goethe's Utopia",
  'year': 1952,
  'language': 'English',
  'subject': 'Literature',
  'authors': ['V'],
  'pages': '55-62',
  'book': 'goethe_after_two_centuries',
  'reprinted': ['cw10'],
  'source': 'https://books.google.com/books?id=SnzKSc-Dn24C'},
 {'key': 'l21',
  'title': 'Necessary Moral Bases for Communication in a Democracy',
  'year': 1956,
  'language': 'English',
  'subject': 'Politics',
  'authors': ['V'],
  'book': 'problems_of_communication_in_a',
  'reprinted': ['cw11'],
  'source': 'https://books.google.com/books?id=0ENcH_0EpuMC'},
 {'key': 'l23',
  'title': 'Diskussionsbereitschaft',
  'year': 1959,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'pages': '355-372',
  'book': 'erziehung_zur_freiheit',
  'reprinted': ['anamnesis_de', 'cw06'],
  'source': 'https://books.google.com/books?id=3NSfsKgWcbkC'},
 {'key': 'l27',
  'title': 'La société industrielle à la recherche de la raison',
  'year': 1960,
  'language': 'French',
  'subject': 'Sociology',
  'authors': ['V'],
  'pages': '44-64',
  'book': 'colloques_de_rheinfelden',
  'reprinted': ['cw11'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l29',
  'title': 'Der Liberalismus und seine Geschichte',
  'year': 1960,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'pages': '13-42',
  'book': 'christentum_und_liberalismus',
  'reprinted': ['cw11'],
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l31',
  'title': "Toynbee's History as a Search for Truth",
  'year': 1961,
  'language': 'English',
  'subject': 'History',
  'authors': ['V'],
  'pages': '181-198',
  'book': 'the_intent_of_toynbee_s_histor',
  'reprinted': ['cw11'],
  'source': 'https://books.google.com/books?id=0ENcH_0EpuMC'},
 {'key': 'l32',
  'title': "Les perspectives d'avenir de la civilisation occidentale",
  'year': 1961,
  'language': 'French',
  'subject': 'History',
  'authors': ['V'],
  'pages': '133-151',
  'book': 'l_histoire_et_ses_interprétati',
  'reprinted': ['cw11'],
  'source': 'https://books.google.com/books?id=0ENcH_0EpuMC'},
 {'key': 'l36',
  'title': 'History and Gnosis',
  'year': 1963,
  'language': 'English',
  'subject': 'Religion',
  'authors': ['V'],
  'pages': '64-89',
  'book': 'the_old_testament_and_christia',
  'reprinted': ['cw11'],
  'source': 'https://books.google.com/books?id=0ENcH_0EpuMC'},
 {'key': 'l37',
  'title': 'Ewiges Sein in der Zeit',
  'year': 1964,
  'language': 'German',
  'subject': 'Philosophy',
  'authors': ['V'],
  'pages': '591-614',
  'book': 'zeit_und_geschichte_dankesgabe',
  'reprinted': ['anamnesis_de', 'cw06', 'anamnesis_en'],
  'source': 'https://books.google.com/books?id=3NSfsKgWcbkC'},
 {'key': 'l39',
  'title': 'Demokratie und Industriegesellschaft',
  'year': 1964,
  'language': 'German',
  'subject': 'Sociology',
  'authors': ['V'],
  'pages': '96-114',
  'book': 'die_unternehmerische_verantwor',
  'reprinted': ['cw11'],
  'source': 'https://doi.org/10.1007/978-3-663-02256-5_6'},
 {'key': 'l40',
  'title': 'Was ist Natur?',
  'year': 1965,
  'language': 'German',
  'subject': 'Philosophy',
  'authors': ['V'],
  'pages': '1-18',
  'book': 'historica_studien_zum_geschich',
  'reprinted': ['anamnesis_de', 'cw06', 'anamnesis_en'],
  'source': 'https://books.google.com/books?id=3NSfsKgWcbkC'},
 {'key': 'l41',
  'title': 'Die deutsche Universität und die Ordnung der deutschen '
           'Gesellschaft',
  'year': 1966,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'pages': '241-282',
  'book': 'die_deutsche_universität_im_dr',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l45',
  'title': 'Configurations of History',
  'year': 1968,
  'language': 'English',
  'subject': 'History',
  'authors': ['V'],
  'pages': '23-42',
  'book': 'the_concept_of_order',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l46',
  'title': 'Zur Geschichte des politischen Denkens',
  'year': 1968,
  'language': 'German',
  'subject': 'Politics',
  'authors': ['V'],
  'pages': '181',
  'book': 'zwischen_revolution_und_restau',
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l47',
  'title': 'Helvétius',
  'year': 1968,
  'language': 'German',
  'subject': 'Philosophy',
  'authors': ['V'],
  'pages': '63-97',
  'book': 'aufklärung_und_materialismus_i',
  'source': 'https://faculty.lsu.edu/voegelin/voegelins-works/articles-essays-by-eric-voegelin.php'},
 {'key': 'l48',
  'title': 'Equivalences of Experience and Symbolization in History',
  'year': 1970,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'pages': '215-234',
  'book': 'eternità_e_storia_i_valori_per',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'},
 {'key': 'l49',
  'title': 'The Eclipse of Reality',
  'year': 1970,
  'language': 'English',
  'subject': 'Philosophy',
  'authors': ['V'],
  'pages': '185-194',
  'book': 'phenomenology_and_social_reali',
  'reprinted': ['cw28'],
  'source': 'https://doi.org/10.1007/978-94-011-7523-4_10'},
 {'key': 'l51',
  'title': 'The Gospel and Culture',
  'year': 1971,
  'language': 'English',
  'subject': 'Religion',
  'authors': ['V'],
  'pages': '59-101',
  'book': 'jesus_and_man_s_hope_vol_2',
  'reprinted': ['cw12'],
  'source': 'https://books.google.com/books?id=5qebtKOVjJUC'}]

QUESTIONS = {'Voegelin short works 1922–1937: details to check': ('Doubts the sources '
                                                      'left open, one per '
                                                      'entry:\n'
                                                      '- Die '
                                                      'gesellschaftliche '
                                                      'Bestimmtheit '
                                                      'soziologischer '
                                                      'Erkenntnis (1922): '
                                                      "LSU list: 'New "
                                                      'series, 11, 4-6, pp. '
                                                      "331-48' - the '11' is "
                                                      "read as OCR for 'II' "
                                                      '(Neue Folge Bd. 2, '
                                                      '1922); volume not '
                                                      'confirmed elsewhere. '
                                                      'Hoover register (Box '
                                                      '51) confirms journal '
                                                      'and 1922. CW7 '
                                                      'contents (Google '
                                                      "Books) list 'The "
                                                      'Social Determination '
                                                      'of Sociological '
                                                      "[Knowledge]'.\n"
                                                      '- Über Max Weber '
                                                      '(1925): Pages: LSU '
                                                      'list 177-93; K10plus '
                                                      "offprint record 'S. "
                                                      "178 - 193' (Bd. 3, H. "
                                                      '2, 1925) - first page '
                                                      'uncertain (177 or '
                                                      '178). CW7 contents: '
                                                      "'On Max Weber'.\n"
                                                      '- Wirtschafts- und '
                                                      'Klassengegensatz in '
                                                      'Amerika (1926): Known '
                                                      'only from the LSU '
                                                      'list (which spells '
                                                      "'America'); not in "
                                                      'the Hoover register. '
                                                      'CW7 contents: '
                                                      "'Economic and Class "
                                                      "Conflict in America'. "
                                                      'Journal name '
                                                      'normalised from the '
                                                      'LSU transcription.\n'
                                                      '- Konjunkturforschung '
                                                      'und Stabilisation des '
                                                      'Kapitalismus (1928): '
                                                      "LSU list: 'IX 9/10, "
                                                      "pp. 252-59'; Hoover "
                                                      'register: printed '
                                                      'copy dated 15 January '
                                                      '1928. LSU gives the '
                                                      'same pages (252-59) '
                                                      'for the Federal '
                                                      'Reserve piece in the '
                                                      'same journal, so the '
                                                      'pages here are '
                                                      'uncertain. Probably '
                                                      'in CW7 (its index '
                                                      'terms include '
                                                      "'business cycles'), "
                                                      'but not visible in '
                                                      'the partial Google '
                                                      'Books contents list, '
                                                      'so no reprint key '
                                                      'given.\n'
                                                      '- Die ergänzende Bill '
                                                      'zum Federal Reserve '
                                                      'Act (1928): Hoover '
                                                      "register: 'Die "
                                                      'ergänzende Bill zum '
                                                      "Federal Reserve Act', "
                                                      'Nationalwirtschaft, '
                                                      '1928 (typescript and '
                                                      'printed copy). '
                                                      'Volume/issue/pages '
                                                      "from LSU list ('11, "
                                                      "2, pp. 225-29', '11' "
                                                      'read as OCR for '
                                                      "'II'). CW7 contents "
                                                      '(Google Books, '
                                                      "truncated) show 'The "
                                                      'Supplementary Bill to '
                                                      "the Federal ...' at "
                                                      'p. 255; the reprint '
                                                      'attribution between '
                                                      'this and the next '
                                                      'entry is inferred.\n'
                                                      '- Die ergänzende Bill '
                                                      'zum Federal Reserve '
                                                      'Act und die '
                                                      'Dollarstabilisation '
                                                      '(1928): Known only '
                                                      'from the LSU list '
                                                      "('X, 11/12, pp. "
                                                      "252-59'); the pages "
                                                      'duplicate those given '
                                                      'for '
                                                      "'Konjunkturforschung', "
                                                      'so left empty. Not in '
                                                      'the Hoover register. '
                                                      'May be a second '
                                                      'version of the '
                                                      'Nationalwirtschaft '
                                                      'piece rather than a '
                                                      'separate essay. CW7 '
                                                      'contents (Google '
                                                      "Books) show '... Act "
                                                      'and the Stabilization '
                                                      "of the Dollar' at p. "
                                                      '262.\n'
                                                      '- Die amerikanische '
                                                      'Theorie vom '
                                                      'ordentlichen '
                                                      'Rechtsverfahren und '
                                                      'von der Freiheit '
                                                      '(1930): LSU list: '
                                                      "'III, 1'; Hoover "
                                                      'register: 1930. '
                                                      'Volume 3 of this '
                                                      'journal may be dated '
                                                      '1931 - year not '
                                                      'independently '
                                                      'confirmed. CW8 '
                                                      "contents: 'The "
                                                      'American Theory of '
                                                      'Due Process of Law '
                                                      "and Freedom'.\n"
                                                      '- Die Einheit des '
                                                      'Rechtes und das '
                                                      'soziale Sinngebilde '
                                                      'Staat (1930): K10plus '
                                                      'offprint record: aus '
                                                      'Internationale '
                                                      'Zeitschrift für '
                                                      'Theorie des Rechts '
                                                      '1930/31, H. 1/2, S. '
                                                      '58-89 (LSU list '
                                                      "misprints '58-59'). "
                                                      'Volume 5 per E. '
                                                      'Arnold (who cites the '
                                                      "French title 'Revue "
                                                      'internationale de la '
                                                      "théorie du droit'). "
                                                      'Year 1930 vs 1930/31 '
                                                      '(Hoover: 1930/1931). '
                                                      "CW8 contents: 'The "
                                                      'Unity of the Law and '
                                                      'the Social Structure '
                                                      'of Meaning Called '
                                                      "State'.\n"
                                                      '- Todesreigen 1934: '
                                                      'Eine Rückschau zum '
                                                      'Gedenktage der Toten '
                                                      '(1934): CW9 note to '
                                                      'ch. 6. Hoover '
                                                      'register: printed '
                                                      "copy signed 'Dr. "
                                                      "E.V.'. Subject "
                                                      "'Literature' is a "
                                                      'judgement call (a '
                                                      'feuilleton).\n'
                                                      '- Le régime '
                                                      'administratif: '
                                                      'Avantages et '
                                                      'inconvénients (1935): '
                                                      'General report '
                                                      "('Rapport général de "
                                                      'M. Adolf Merkl ... et '
                                                      "M. Erich Voegelin'). "
                                                      'CW9 note to ch. 8 '
                                                      'gives the host '
                                                      'publication as a '
                                                      'volume ed. Elemer '
                                                      'Balogh (Paris: Sirey, '
                                                      '1935), vol. 2, pt. 3, '
                                                      'pp. 126-49; it could '
                                                      'equally be treated as '
                                                      'a serial article in '
                                                      "the Académie's "
                                                      'Mémoires.\n'
                                                      '- Changes in the '
                                                      'Ideas of Government '
                                                      'and Constitution in '
                                                      'Austria since 1918 '
                                                      '(1937): CW9 note to '
                                                      'ch. 12. Austrian '
                                                      'Memorandum No. 3 (LSU '
                                                      'list); Hoover '
                                                      'register calls it '
                                                      "'The Change in the "
                                                      "Ideas ...' and "
                                                      'describes a '
                                                      'mimeographed copy '
                                                      'dated April 1937 - '
                                                      'may be a mimeographed '
                                                      'conference paper '
                                                      'rather than a printed '
                                                      'book.\n'
                                                      '- Was dürfen die '
                                                      'Menschen wissen? '
                                                      '(1937): CW9 note to '
                                                      'ch. 14; Hoover '
                                                      'register agrees.',
                                                      ['e01',
                                                       'e04',
                                                       'e06',
                                                       'e10',
                                                       'e11',
                                                       'e12',
                                                       'e18',
                                                       'e21',
                                                       'e29',
                                                       'e31',
                                                       'e36',
                                                       'e38']),
 'Voegelin short works 1940–1985: details to check': ('Doubts the sources '
                                                      'left open, one per '
                                                      'entry:\n'
                                                      '- Political Theory '
                                                      'and the Pattern of '
                                                      'General History '
                                                      '(1944): Crossref '
                                                      'title is prefixed '
                                                      "'IV.' (a numbered "
                                                      'part of a symposium '
                                                      'in that issue). LSU '
                                                      "also lists 'Political "
                                                      "Theory' in E. S. "
                                                      'Griffith (ed.), '
                                                      'Research in Political '
                                                      'Science (Chapel Hill: '
                                                      'UNC Press, 1948), pp. '
                                                      '190-201; CW10 '
                                                      'contains no separate '
                                                      'piece, so it is '
                                                      'probably a reprint '
                                                      'and is not entered '
                                                      'separately (not '
                                                      'verified).\n'
                                                      '- Zu Sanders '
                                                      '„Allgemeiner '
                                                      'Staatslehre“ (1947): '
                                                      'A critical essay on '
                                                      "Fritz Sander's book "
                                                      '(review-essay). '
                                                      'Written c. 1938: '
                                                      "CW10's editor says it "
                                                      'was in galley proof '
                                                      'when Voegelin fled '
                                                      'Austria, was '
                                                      'suppressed by the '
                                                      'Nazis, and was first '
                                                      'published in 1947, so '
                                                      'it is in this range '
                                                      'by publication date. '
                                                      'CW10 excludes it and '
                                                      'says it belongs to '
                                                      'CW9; that is not '
                                                      'confirmed, so '
                                                      "'reprinted' is left "
                                                      'empty. It may overlap '
                                                      'with the 1922-1938 '
                                                      "researcher's list. "
                                                      'The quotation marks '
                                                      'in the title follow '
                                                      'German usage; exact '
                                                      'original typography '
                                                      'not seen.\n'
                                                      "- Goethe's Utopia "
                                                      '(1952): The editor is '
                                                      "'Carl Hammer' in LSU "
                                                      'and CW10 (possibly '
                                                      'Carl Hammer Jr.).\n'
                                                      '- Necessary Moral '
                                                      'Bases for '
                                                      'Communication in a '
                                                      'Democracy (1956): '
                                                      'Pages unknown. The '
                                                      'host volume is the '
                                                      'papers of a Marquette '
                                                      'University '
                                                      'anniversary '
                                                      'conference on '
                                                      'communication, March '
                                                      '20-23, 1956 (Open '
                                                      'Library); editors are '
                                                      'unknown.\n'
                                                      '- Der Prophet Elias '
                                                      '(1958): Source: LSU '
                                                      'list only, which '
                                                      'gives the volume as '
                                                      "'I'. Hochland's "
                                                      'volume for 1957/58 is '
                                                      '50, which is assumed '
                                                      'here but not '
                                                      'verified. Probably '
                                                      'related to the Elijah '
                                                      'material in Order and '
                                                      'History I; no reprint '
                                                      'confirmed.\n'
                                                      '- El concepto de la '
                                                      '"buena sociedad" '
                                                      '(1960): Source: LSU '
                                                      'list only (it prints '
                                                      'the title garbled). '
                                                      'The original language '
                                                      'and whether this is a '
                                                      'translation are '
                                                      'unverified; exact '
                                                      'title punctuation '
                                                      'unverified.\n'
                                                      '- La société '
                                                      'industrielle à la '
                                                      'recherche de la '
                                                      'raison (1960): Pages '
                                                      'from LSU; CW33 cites '
                                                      'the same volume '
                                                      '(discussion excerpts '
                                                      'at 213-26 etc.). '
                                                      'Whether Voegelin '
                                                      'wrote it in French or '
                                                      'it was translated is '
                                                      'unverified. Later '
                                                      'versions: German '
                                                      '1961; English '
                                                      "'Industrial Society "
                                                      "in Search of Reason' "
                                                      'in R. Aron (ed.), '
                                                      'World Technology and '
                                                      'Human Destiny (Ann '
                                                      'Arbor, 1963), 31-46, '
                                                      'which is the CW11 '
                                                      'text. Editors beyond '
                                                      "Aron and Kennan ('et "
                                                      "al.') not recorded.\n"
                                                      '- Les perspectives '
                                                      "d'avenir de la "
                                                      'civilisation '
                                                      'occidentale (1961): '
                                                      'Roundtable at Cerisy, '
                                                      'July 1958 (CW11 '
                                                      'note). In CW11 as '
                                                      "'Prospects of Western "
                                                      "Civilization'. The "
                                                      'French title is from '
                                                      'LSU, and the original '
                                                      'language of '
                                                      "Voegelin's "
                                                      'contribution is '
                                                      'unverified.\n'
                                                      '- Das Rechte von '
                                                      'Natur (1963): '
                                                      'Published in the '
                                                      "special issue 'Das "
                                                      'Naturrecht in der '
                                                      "politischen Theorie', "
                                                      'ed. F.-M. Schmölz '
                                                      '(Vienna, 1963), which '
                                                      'was also issued as a '
                                                      'Springer book '
                                                      '(Crossref DOI '
                                                      '10.1007/978-3-7091-7918-5_2, '
                                                      'pp. 38-51). In '
                                                      "English as 'What Is "
                                                      "Right by Nature?' in "
                                                      'Anamnesis (1978) and '
                                                      "'Right by Nature' in "
                                                      'CW6.\n'
                                                      '- Hacia una nueva '
                                                      'ciencia del orden '
                                                      'social (1963): '
                                                      'Source: LSU list '
                                                      'only. Possibly a '
                                                      'translation of '
                                                      'another piece; '
                                                      'unverified.\n'
                                                      '- History and Gnosis '
                                                      '(1963): Date '
                                                      'conflict: CW11 dates '
                                                      'it 1965 and LSU cites '
                                                      'the 1969 Herder and '
                                                      'Herder edition; Open '
                                                      'Library shows the '
                                                      'book first published '
                                                      'by Harper & Row in '
                                                      '1963, which is used '
                                                      'here. Pages are from '
                                                      'LSU (they may follow '
                                                      'the 1969 printing).\n'
                                                      '- Was ist Natur? '
                                                      '(1965): The host '
                                                      "book's exact subtitle "
                                                      'and dedication '
                                                      'wording are partly '
                                                      'from LSU.\n'
                                                      '- Die deutsche '
                                                      'Universität und die '
                                                      'Ordnung der deutschen '
                                                      'Gesellschaft (1966): '
                                                      'Reprinted as '
                                                      "'Universität und "
                                                      'Öffentlichkeit: Zur '
                                                      'Pneumopathologie der '
                                                      "Gesellschaft' in Wort "
                                                      'und Wahrheit 21 '
                                                      '(1966), 497-518. '
                                                      'English translation '
                                                      'in Intercollegiate '
                                                      'Review 20 (1985), '
                                                      '7-27, and in CW12 as '
                                                      "'The German "
                                                      'University and the '
                                                      'Order of German '
                                                      'Society: A '
                                                      'Reconsideration of '
                                                      "the Nazi Era'. The "
                                                      "host book's subtitle "
                                                      'is unverified.\n'
                                                      '- Was ist politische '
                                                      'Realität? (1966): '
                                                      'Pages 2-54 per CW6; '
                                                      'LSU gives 1-54. '
                                                      'Published the same '
                                                      'year as Part III of '
                                                      'Anamnesis (1966).\n'
                                                      '- Zur Geschichte des '
                                                      'politischen Denkens '
                                                      '(1968): Source: LSU '
                                                      "list only ('p. 181'). "
                                                      'A single page, '
                                                      "possibly an editor's "
                                                      'note for the List '
                                                      "series 'Geschichte "
                                                      'des politischen '
                                                      "Denkens' rather than "
                                                      'an essay. Host book '
                                                      'editors unknown. '
                                                      'Doubtful as a '
                                                      'separate entry.\n'
                                                      '- Helvétius (1968): '
                                                      'Source: LSU list '
                                                      'only, which lists it '
                                                      "'with Peter "
                                                      "Leuschner'. "
                                                      "Leuschner's role "
                                                      '(co-author or '
                                                      'translator) is '
                                                      'unverified; probably '
                                                      'derived from '
                                                      "Voegelin's History of "
                                                      'Political Ideas '
                                                      'material.\n'
                                                      '- Equivalences of '
                                                      'Experience and '
                                                      'Symbolization in '
                                                      'History (1970): Host '
                                                      'book editors unknown; '
                                                      'the language of the '
                                                      'original printing is '
                                                      'assumed to be English '
                                                      '(CW12 prints it in '
                                                      'English). Reprinted '
                                                      'in Philosophical '
                                                      'Studies (Ireland) 28 '
                                                      '(1981), 88-103.\n'
                                                      "- On Henry James's "
                                                      'Turn of the Screw '
                                                      '(1971): The original '
                                                      'title is unverified; '
                                                      'the CW12 title is '
                                                      'used. Pages: LSU '
                                                      'gives 3-48 (including '
                                                      "Robert Heilman's "
                                                      'prefatory note, '
                                                      "Voegelin's 1947 "
                                                      'letter and the '
                                                      "postscript 'On "
                                                      'Paradise and '
                                                      "Revolution'); CW12 "
                                                      'cites 9-48.\n'
                                                      '- On Classical '
                                                      'Studies (1973): Issue '
                                                      'no. 1 is assumed from '
                                                      'pp. 2-8 at the start '
                                                      'of the volume, not '
                                                      'verified.\n'
                                                      '- Philosophy of '
                                                      'History: An Interview '
                                                      '(1977): Source: LSU '
                                                      "list only ('No. 2 "
                                                      "(1977)'). This is an "
                                                      'interview, not an '
                                                      'essay; it is doubtful '
                                                      'as an entry and may '
                                                      'be excluded.',
                                                      ['l07',
                                                       'l09',
                                                       'l17',
                                                       'l21',
                                                       'l22',
                                                       'l25',
                                                       'l27',
                                                       'l32',
                                                       'l34',
                                                       'l35',
                                                       'l36',
                                                       'l40',
                                                       'l41',
                                                       'l42',
                                                       'l46',
                                                       'l47',
                                                       'l48',
                                                       'l50',
                                                       'l53',
                                                       'l56'])}
