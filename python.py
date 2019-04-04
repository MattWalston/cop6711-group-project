import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')


def term_intersection(tokens, terms):
    return list(set(tokens) & set(terms))


stop_words = set(stopwords.words("english"))

terms = {
    'economy': ['business deal', 'unemployment', 'monetary valu', 'economic', 'merchandise', 'commercial-grade', 'busi',
                'manufacture', 'consumpt', 'recognition', 'cost', 'innov', 'economist', 'business organization',
                'commercialise', 'trade in', 'economic consumpt', 'service', 'saving', 'labor mov', 'thriftiness',
                'recognit', 'business enterprise', 'eec', 'labour', 'financi', 'consum', 'toil', 'european community',
                'business d', 'business organisation', 'taxat', 'trade protect', 'trade union mov',
                'stock market index',
                'serv', 'initi', 'department of labor', 'commercial message', 'initiative', 'business', 'property',
                'belongings', 'use of goods and services', 'economic expert', 'craft', 'business enterpris', 'yield',
                'inflation, stock', 'manufactur', 'proletariat', 'tribut', 'undertaking', 'barter',
                'economic consumption',
                'task', 'gdp', 'infrastructur', 'forward-look', 'marketplac', 'downswing', 'infrastructure', 'commerci',
                'econom', 'business concern', 'assess', 'drudge', 'belonging', 'credit', 'marketplace', 'mart',
                'business organ', 'globalis', 'dol', 'properti', 'commercial enterpris', 'expenditur',
                'economic science',
                'credit rating', 'patronag', 'market plac', 'substructur', 'commercialize', 'financ', 'tax', 'europ',
                'industry', 'billionaire', 'serve', 'credit entry', 'line of work', 'political economy', 'fiscal',
                'wall street', 'save', 'billionair', 'servic', 'finance', 'british labour parti', 'capitalist economy',
                'innovational', 'occupation', 'productivity', 'swap', 'credit entri', 'labor movement', 'ec',
                'political economi', 'european economic community', 'project', 'tug', 'financial', 'distribution',
                'enterpris', 'moil', 'job', 'gross domestic product', 'socialism', 'european commun', 'travail',
                'expenditure', 'commercial enterprise', 'lien', 'revenue enhancement', 'trade union movement',
                'labor department', 'commercialis', 'exportation', 'labour parti', 'clientel', 'patronage', 'downsw',
                'tribute', 'socialist', 'substructure', 'entrepreneur', 'economic sci', 'consumption', 'innovative',
                'credit r', 'sell', 'european union', 'enterprising', 'revenue enhanc', 'merchandis', 'usance',
                'economi',
                'business sector', 'industriousness', 'trade wind', 'go-ahead', 'export', 'enterprise', 'wage',
                'forward-looking', 'production', 'enterpriser', 'taxation', 'grind', 'deal', 'product', 'downturn',
                'securities industri', 'ass', 'economic system', 'byplay', 'consumer', 'use of goods and servic',
                'productiveness', 'occup', 'economical', 'global', 'european economic commun', 'europe', 'accredit',
                'trade protection', 'common market', 'drudg', 'british labour party', 'stage busi', 'belong',
                'commercial messag', 'securities industry', 'commercial-grad', 'capitalism', 'capitalist economi',
                'economics', 'wages', 'partnership', 'market place', 'business organis', 'globalization', 'industri',
                'market', 'social', 'monetary value', 'distribut', 'economy', 'swop', 'labor depart', 'labor',
                'unemploy',
                'stage business', 'labour party', 'capit', 'working class', 'clientele', 'globalisation', 'thrifti',
                'undertak', 'trade', 'enterprisingness', 'usanc', 'commercial', 'course credit', 'eu'],
    'mobility': ['sign-language', 'taxi', 'taxicab', 'commuter train', 'signalis', 'sign-languag', 'locomotion',
                 'servicearea', 'transport', 'carri', 'truck', 'speed', 'access', 'fuel', 'acceleratorpedal',
                 'motorcoach',
                 'thoroughfares', 'sidewalk', 'sign', 'fare', 'cable car', 'jalopy', 'commute', 'carry', 'omnibus',
                 'vehicle', 'berth', 'trafficaccident', 'transportation system', 'gondola', 'skyway', 'vehicl',
                 'mapping',
                 'department of transport', 'passenger vehicl', 'drive', 'cycl', 'infrastructur', 'commuter', 'caravan',
                 'speedbump', 'traffic', 'infrastructure', 'pedestrian', 'gasstation', 'Transportation', 'wheel', 'dot',
                 'conveyance', 'convert', 'footer', 'street', 'lyft', 'motor', 'channelise', 'channelis', 'way',
                 'bus topolog', 'substructur', 'cycle', 'transpose', 'buse', 'bus', 'bridg', 'signal',
                 'charabancautobus',
                 'tape transport', 'car', 'k-turn', 'pedicab', 'highway', 'pedal', 'transportation',
                 'Department of Transportation', 'parking', 'motive', 'pavement', 'avail', 'park', 'convey',
                 'automobile',
                 'availableness', 'locomot', 'gasstat', 'flight', 'availability', 'thoroughfare', 'buses', 'DoT',
                 'transpos',
                 'exchang', 'motiv', 'double-deck', 'shipping', 'passenger vehicle', 'thoroughfar', 'ship', 'commut',
                 'signalise', 'acceleratorped', 'transmit', 'substructure', 'roadwork', 'department of transportation',
                 'speedlimit', 'trucks', 'motorcar', 'cars', 'signaling', 'channel', 'gasped', 'travel',
                 'drivers licence',
                 'railway car', 'bicycle', 'bus topology', 'elevator car', 'international flight', 'map', 'bridge',
                 'drivers lic', 'auto', 'uber', 'cycle rickshaw', 'visa', 'Speedbump', 'jalopi', 'earthbound', 'bicycl',
                 'tape dr', 'transferral', 'exchange', 'Visa', 'bike', 'plane', 'detour', 'transfer', 'gaspedal',
                 'double-decker', 'jitney', 'motorbus', 'trafficdelay', 'walker', 'trafficaccid', 'transferr', 'cab',
                 'road',
                 'signalize', 'tape drive', 'accessibility', 'transit', 'channelize', 'railroad car', 'railcar',
                 'speeding',
                 'automobil', 'van'],
    'environment': ['ash-bin', 'dumpsite', 'expelling', 'pesticid', 'waste materi', 'ozone', 'food wast', 'free energy',
                    'drainage basin', 'greenhouse', 'Energy', 'ashbin', 'natural gas', 'garbage dump', 'energy',
                    'wasteyard',
                    'disposal', 'trash can', 'surroundings', 'pm2.5', 'waste', 'ditch', 'particulatematt', 'VOC',
                    'wild',
                    'water parting', 'aura', 'greenhous', 'protective cover', 'energi', 'defil', 'recycl', 'healthful',
                    'stormwater', 'Volatileorganiccompound', 'pesticide', 'water part', 'reus', 'PM10', 'atmosphere',
                    'surround', 'sanitisation', 'solildwaste', 'environ', 'waste matt', 'DOE', 'bionomic', 'nurseri',
                    'department of energi', 'ecologic', 'scrap', 'dustbin', 'health', 'energy department', 'emiss',
                    'trash dump', 'dispos', 'natural ga', 'co2', 'vent', 'nois', 'recyclable', 'gasolin', 'gas',
                    'carbonmonoxid', 'befoul', 'sanitation', 'nursery', 'environmental sci', 'protect', 'gaseous state',
                    'pointsource', 'sustainable', 'gasolen', 'watershed', 'reprocess', 'sanitization', 'voc',
                    'volatileorganiccompound', 'expel', 'sanitis', 'aerate', 'permissive wast', 'particulatematter',
                    'plant lif', 'constitute', 'gaseous st', 'reclaim', 'basin', 'subdue', 'ash bin', 'petrol',
                    'resourc',
                    'defilement', 'garbage', 'ozon', 'flora', 'ashcan', 'trash bin', 'reuse', 'shit', 'constitut',
                    'sanit',
                    'CO', 'aerat', 'ecolog', 'dump', 'permissive waste', 'sanitari', 'resourcefulness', 'waste matter',
                    'parks', 'bionomics', 'aviat', 'drainage area', 'bionomical', 'green', 'ventilate', 'co', 'park',
                    'stormwat', 'wastewat', 'ecological', 'emission', 'Department of Energy', 'solildwast', 'CO2',
                    'breez',
                    'nitrous', 'plant life', 'protective cov', 'engraft', 'gentle wind', 'coldcock', 'recycle',
                    'carbondioxide', 'protective covering', 'landmark', 'aviation', 'plant', 'drivel',
                    'catchment basin',
                    'garbage can', 'pollutant', 'wast', 'Energy Department', 'free energi', 'litter', 'emb',
                    'wastefulness',
                    'discharg', 'resource', 'carbonmonoxide', 'waste material', 'shelter', 'befoulment',
                    'contamination',
                    'pointsourc', 'glasshous', 'subsonicwav', 'o3', 'trash barrel', 'energy depart', 'subdu',
                    'environmental science', 'pollution', 'reclaimable', 'embed', 'subsonicwave', 'wastewater',
                    'pollut',
                    'garbag', 'infrasonicwave', 'nonpointsourc', 'scraps', 'recreation', 'compost', 'carbondioxid',
                    'department of energy', 'waste-yard', 'reusabl', 'catchment area', 'wastebin', 'bionom',
                    'sustainability', 'rubbish dump', 'ventil', 'environs', 'dumpsit', 'Parks', 'O3', 'breeze',
                    'gasolene',
                    'reusable', 'environment', 'watersh', 'contamin', 'PM2.5', 'air', 'recycling', 'sustain',
                    'river basin',
                    'food waste', 'gasoline', 'atmospher', 'pm10', 'doe', 'recreat', 'sanitary', 'waste product',
                    'protection', 'ecology', 'discharge', 'infrasonicwav', 'nonpointsource', 'noise', 'glasshouse'],
    'governance': ['military servic', 'provis', 'police offic', 'police forc', 'societ', 'irreverence', 'regim',
                   'governance', 'licens', 'agenc', 'recognition', 'citycouncil', 'elect', 'body politic', 'design',
                   'licence', 'polit', 'commonwealth', 'political science', 'carry n', 'offic', 'recognit',
                   'authorities',
                   'identification', 'value', 'political sci', 'infringement', 'taxat', 'politics', 'judicature',
                   'elected',
                   'infract', 'effici', 'agit', 'nosecount', 'body polit', 'administrator', 'prescript', 'countri',
                   'decre',
                   'comptroller', 'presid', 'government agency', 'trespass', 'movement', 'valu',
                   'Carry Amelia Moore Nation',
                   'surveillance', 'authority', 'world', 'principl', 'regul', 'convention', 'rape', 'republica', 'task',
                   'usurp', 'police officer', 'policeman', 'violation', 'regulation', 'military officer', 'assess',
                   'governing body', 'office', 'carry amelia moore nation', 'police force', 'mayor', 'agency',
                   'government ag', 'city manag', 'constabulari', 'campaign', 'licenc', 'control', 'legislation',
                   'infraction', 'infring', 'financ', 'tax', 'ordin', 'intrusion', 'certify', 'permit', 'surveil',
                   'correctional', 'governing bodi', 'finance', 'census', 'societal', 'legisl', 'military offic',
                   'officeholder', 'identif', 'governing', 'federal agency', 'comptrol', 'govern', 'effect',
                   'government act', 'patrol', 'budget', 'polic', 'intrus', 'federal ag', 'misdemeanor', 'usurpation',
                   'presidency', 'crusade', 'correct', 'execut', 'irrever', 'ravishment', 'law', 'regime', 'violat',
                   'certifi', 'revenue enhancement', 'administr', 'author', 'government', 'encroach', 'permission',
                   'charge per unit', 'rule', 'convent', 'license', 'officehold', 'presidential term', 'officer',
                   'sociabl',
                   'efficient', 'revenue enhanc', 'sociable', 'controller', 'country', 'organis', 'populace',
                   'designation',
                   'populac', 'agitate', 'military service', 'dominion', 'police', 'Carry Nation', 'assault',
                   'taxation',
                   'principle', 'nose count', 'executive', 'ravish', 'ass', 'attorney', 'city manager', 'carry nation',
                   'provision', 'Nation', 'elective', 'bureau', 'political campaign', 'ordinance', 'reign',
                   'administration',
                   'ruler', 'state', 'social', 'public', 'government activity', 'organization', 'establish', 'spot',
                   'permiss', 'misdemeanour', 'crusad', 'judicatur', 'organisation', 'effective', 'establishment',
                   'decree',
                   'part', 'organ', 'nation', 'power', 'lawyer', 'constabulary', 'encroachment',
                   'carry amelia moore n'],
    'people': ['genderdiscrimin', 'learnedness', 'exemption', 'impression', 'minority', 'heathen', 'cultur',
               'affirmativeact', 'peopl', 'diverseness', 'affirmativeaction', 'memorise', 'human', 'blm',
               'minoritygroup',
               'creative think', 'genderdiscrimination', 'desegregation', 'studi', 'philosophy', 'Atheism', 'BLM',
               'Minoritygroup', 'divers', 'homo', 'school of thought', 'openminded', 'varieti', 'LGBT', 'acquisition',
               'opinion', 'faith', 'discover', 'righttoeducation', 'woman', 'erudition', 'equalityofsexes',
               'creativity',
               'religion', 'creativ', 'individu', 'ethnicity', 'freedom', 'EmploymentDiscrimination', 'feminism',
               'bisexu',
               'memor', 'learning', 'gay', 'womanhood', 'learned', 'human being', 'creativeness', 'lesbian', 'discov',
               'multifariousness', 'man', 'encyclopedism', 'instruct', 'acquisit', 'doctrine', 'impress', 'minor',
               'Affirmativeaction', 'ism', 'memoris', 'diversity', 'masses', 'openmind', 'equalityofsex',
               'employmentdiscrimination', 'multitude', 'mass', 'employmentdiscrimin', 'variety', 'study', 'femin',
               'memorize', 'multifari', 'the great unwashed', 'doctrin', 'transgender', 'bisexual', 'philosophi',
               'creative thinking', 'Feminism', 'citizenry', 'notion', 'heathenish', 'learn', 'righttoeduc',
               'individual',
               'religious belief', 'pagan', 'cultural', 'citizenri', 'philosophical system', 'desegreg', 'ethnical',
               'belief', 'the great unwash', 'ethnic', 'transgend', 'people', 'organized religion', 'lgbt', 'atheism',
               'erudit', 'Righttoeducation', 'teach', 'human b', 'exempt', 'feel', 'mortal', 'encycloped', 'multitud',
               'scholarship', 'feeling'],
    'living': ['hired gun', 'shooter', 'university', 'construction', 'well', 'indemn', 'health check', 'rampart',
               'inebri',
               'nursing home', 'college', 'secur', 'coher', 'house serv', 'alcoholic drink', 'licens', 'paries',
               'low-pric',
               'archeological site', 'cultur', 'lodging', 'facil', 'leisure', 'roleplay', 'dwelling house', 'licence',
               'incom', 'mansion', 'domiciliate', 'resident physician', 'domicile', 'security measur', 'lodg',
               'planetary hous', 'brood', 'tenant', 'security system', 'workplace', 'act as', 'hous', 'surety',
               'counten',
               'gunslinger', 'culture', 'housing', 'psycholog', 'pari', 'residency', 'domestic help', 'destruction',
               'actor',
               'medical', 'studi', 'facility', 'security measure', 'wiretap', 'allow', 'theatre', 'surround', 'home pl',
               'residence', 'dimens', 'property', 'electric', 'menage', 'dwell', 'belongings', 'cultiv', 'wall',
               'human act',
               'health', 'demolit', 'security', 'abode', 'rent', 'afford', 'habit', 'dig', 'bug', 'probation', 'house',
               'alcoholic beverag', 'build', 'occupier', 'checkup', 'structure', 'small-arm', 'hemipterous insect',
               'rest home', 'protect', 'electr', 'demolition', 'sceneri', 'house physician', 'aesculapian',
               'mental synthesis', 'belonging', 'gun for hir', 'dwelling hous', 'insurance', 'nonmigratori',
               'medical examination', 'abidance', 'properti', 'insurance polici', 'civil', 'leisur', 'offend',
               'domesticated', 'accultur', 'insur', 'licenc', 'security department', 'gun', 'construct', 'rest hom',
               'dwelling', 'security depart', 'occupi', 'countenance', 'security measures', 'welfar', 'permit',
               'wipeout',
               'excavation', 'cohesiveness', 'danc', 'affordable', 'residenti', 'famili', 'fence in', 'facilities',
               'nonmigratory', 'building', 'medical checkup', 'tourism', 'alcohol', 'deed', 'univers', 'medic',
               'mentalhealth', 'renter', 'inhabit', 'affordablecar', 'dimension', 'livingaccommod', 'electrical',
               'crop',
               'welfare', 'lie in', 'cohesion', 'offender', 'popul', 'sureti', 'income', 'low-priced', 'study',
               'civilis',
               'gunsling', 'resident', 'master', 'archeological sit', 'medical exam', 'indemnity', 'home', 'habitation',
               'permission', 'house servant', 'insurance policy', 'touristri', 'license', 'playact', 'landlord', 'live',
               'leisure time', 'affordablecare', 'abod', 'occupant', 'civilization', 'plate', 'caparison',
               'nursing hom',
               'fence', 'human activity', 'home plate', 'probat', 'theatr', 'destruct', 'civilisation', 'act a',
               'dissembl',
               'low-cost', 'psychology', 'domicil', 'intoxic', 'professional person', 'planetary house', 'toler',
               'wellness',
               'residential', 'occup', 'gunman', 'routine', 'home base', 'put up', 'household', 'menag', 'profession',
               'fenc', 'belong', 'coherency', 'leisure tim', 'domicili', 'dissemble', 'mental synthesi', 'intoxicant',
               'family', 'wrongdoer', 'scenery', 'hit man', 'populate', 'excav', 'professional', 'gun for hire',
               'coherence',
               'acculturation', 'alcoholic beverage', 'cultivation', 'colleg', 'dance', 'cohes', 'triggerman', 'pro',
               'domestic', 'permiss', 'base', 'touristry', 'tolerate', 'resid', 'structur', 'domest', 'medical examin',
               'palisad', 'dancing', 'room', 'bulwark', 'home bas', 'firearm', 'citizen', 'palisade', 'abid', 'routin',
               'protection', 'hire', 'human action', 'livingaccommodations', 'digging', 'workplac', 'inebriant']
}

text = input("Input text to analyze: ")

filtered_tokens = []
for w in word_tokenize(text):
    if w not in stop_words:
        filtered_tokens.append(PorterStemmer().stem(w))

print("Filterd tokens:", filtered_tokens)

features = [('economy', term_intersection(filtered_tokens, terms['economy'])),
            ('mobility', term_intersection(filtered_tokens, terms['mobility'])),
            ('environment', term_intersection(filtered_tokens, terms['environment'])),
            ('governance', term_intersection(filtered_tokens, terms['governance'])),
            ('people', term_intersection(filtered_tokens, terms['people'])),
            ('living', term_intersection(filtered_tokens, terms['living']))]
feature = sorted(features, key=lambda i: i[1], reverse=True)[0][0]

print('Feature is: ', feature)
