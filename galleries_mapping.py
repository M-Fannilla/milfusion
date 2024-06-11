import pandas as pd
from typing import TypeAlias

remove_tag: TypeAlias = False
remove_gallery: TypeAlias = None
keep_tag: TypeAlias = True

GALLERIES_MAP = {
    'ai': remove_gallery,
    'amateur': remove_tag,
    'anal': keep_tag,
    'anal gape': remove_gallery,
    'armpit': keep_tag,
    'asian': keep_tag,
    'ass': keep_tag,
    'ass fucking': ['ass', 'anal', 'sex'],
    'ass licking': ['rimming', 'ass licking'],
    'asshole': ['asshole', 'ass'],
    'babe': remove_tag,
    'babysitter': remove_tag,
    'ball licking': ['blowjob', ],
    'ballerina': remove_gallery,
    'bath': keep_tag,
    'bbc': ['bbc', 'big dick'],
    'bbw': ['bbw', ],
    'bdsm': keep_tag,
    'beach': ['beach', 'outdoor', 'public'],
    'beautiful': remove_tag,
    'big clit': ['pussy', ],
    'big dick': keep_tag,
    'big tits': keep_tag,
    'bikini': keep_tag,
    'bisexual': remove_tag,
    'blindfold': ['bdsm', ],
    'blonde': keep_tag,
    'blowbang': ['blowjob', 'group sex'],
    'blowjob': keep_tag,
    'bodysuit': remove_tag,
    'bondage': ['bondage', 'bdsm'],
    'boots': keep_tag,
    'braces': remove_tag,
    'brunette': keep_tag,
    'bukkake': ['masturbation', 'cumshot', 'group sex'],
    'butt plug': ['butt plug', 'toys'],
    'cameltoe': ['pants', 'cameltoe'],
    'casting': remove_gallery,
    'caught': remove_gallery,
    'centerfold': remove_tag,
    'cfnm': remove_tag,
    'cheating': remove_gallery,
    'cheerleader': remove_tag,
    'christmas': remove_gallery,
    'chubby': keep_tag,
    'close up': keep_tag,
    'clothed': ['non nude', ],
    'college': remove_gallery,
    'cosplay': keep_tag,
    'cougar': ['milf', ],
    'couple': remove_tag,
    'cowgirl': ['cowgirl', 'sex'],
    'creampie': ['creampie', 'pussy'],
    'cuckold': remove_gallery,
    'cum in mouth': keep_tag,
    'cum in pussy': ['creampie', ],
    'cum swapping': remove_gallery,
    'cumshot': keep_tag,
    'curly': keep_tag,
    'curvy': keep_tag,
    'cute': remove_tag,
    'deepthroat': ['deepthroat', 'blowjob', ],
    'dildo': ['dildo', 'sex toys'],
    'doctor': remove_tag,
    'doggy style': ['doggy style', 'sex'],
    'double penetration': ['double penetration', 'sex'],
    'dress': ['dress', 'clothed'],
    'ebony': keep_tag,
    'emo': remove_gallery,
    'erotic': remove_tag,
    'face': remove_tag,
    'facesitting': remove_tag,
    'facial': keep_tag,
    'fake tits': remove_tag,
    'family': remove_tag,
    'farm': ['outdoor', ],
    'feet': keep_tag,
    'femdom': ['bdsm', ],
    'fetish': remove_tag,
    'ffm': ['threesome', 'group sex'],
    'fingering': ['fingering', 'pussy', ],
    'fisting': keep_tag,
    'flexible': remove_tag,
    'footjob': keep_tag,
    'gangbang': ['group sex', ],
    'gay': remove_gallery,
    'girlfriend': remove_tag,
    'glamour': remove_tag,
    'glasses': keep_tag,
    'gloryhole': remove_tag,
    'goth': remove_tag,
    'granny': keep_tag,
    'group sex': keep_tag,
    'gym': keep_tag,
    'gyno': remove_gallery,
    'hairy': ['hairy pussy', ],
    'halloween': remove_gallery,
    'handjob': keep_tag,
    'hardcore': ['rough sex', ],
    'hentai': remove_gallery,
    'high heels': ['heels', ],
    'homemade': remove_tag,
    'hotwife': remove_tag,
    'housewife': remove_tag,
    'humping': ['sex', ],
    'interracial': keep_tag,
    'jeans': keep_tag,
    'kissing': keep_tag,
    'kitchen': remove_tag,
    'ladyboy': remove_gallery,
    'latex': ['leather', ],
    'latina': keep_tag,
    'leather': keep_tag,
    'legs': keep_tag,
    'lesbian': keep_tag,
    'lingerie': keep_tag,
    'maid': keep_tag,
    'massage': keep_tag,
    'masturbation': keep_tag,
    'mature': keep_tag,
    'milf': keep_tag,
    'missionary': keep_tag,
    'mmf': ['group sex', 'threesome', 'double penetration'],
    'model': remove_tag,
    'mom': ['milf', ],
    'natural tits': remove_tag,
    'nipples': keep_tag,
    'non nude': keep_tag,
    'nun': remove_gallery,
    'nurse': keep_tag,
    'office': keep_tag,
    'oiled': keep_tag,
    'old man': remove_tag,
    'old/young': remove_tag,
    'orgasm': keep_tag,
    'orgy': ['group sex', ],
    'outdoor': keep_tag,
    'pale': remove_tag,
    'panties': keep_tag,
    'pantyhose': keep_tag,
    'party': remove_gallery,
    'pawg': remove_tag,
    'pegging': remove_tag,
    'petite': keep_tag,
    'piercing': remove_tag,
    'pigtails': keep_tag,
    'pissing': keep_tag,
    'police': remove_tag,
    'pool': keep_tag,
    'pornstar': remove_tag,
    'pov': remove_tag,
    'pregnant': remove_gallery,
    'pretty': remove_tag,
    'prison': remove_tag,
    'public': keep_tag,
    'pussy': keep_tag,
    'pussy licking': keep_tag,
    'reality': remove_tag,
    'redhead': keep_tag,
    'rough sex': keep_tag,
    'saggy tits': remove_tag,
    'sandals': keep_tag,
    'schoolgirl': remove_tag,
    'secretary': remove_tag,
    'seduction': remove_tag,
    'selfie': keep_tag,
    'sex doll': remove_gallery,
    'sexy': remove_tag,
    'shaved': ['shaved pussy', ],
    'shemale': remove_tag,
    'short hair': remove_tag,
    'shorts': keep_tag,
    'shower': keep_tag,
    'skinny': keep_tag,
    'skirt': keep_tag,
    'small dick': remove_gallery,
    'smoking': keep_tag,
    'socks': keep_tag,
    'solo': keep_tag,
    'spanking': remove_gallery,
    'sports': keep_tag,
    'spreading': ['spreading legs', ],
    'squirting': keep_tag,
    'ssbbw': keep_tag,
    'step brother': remove_tag,
    'step sister': remove_tag,
    'stepmom': ['milf', ],
    'stockings': keep_tag,
    'strap on': ['strap on', 'toys'],
    'stripper': remove_gallery,
    'swingers': ['group sex', ],
    'tall': remove_tag,
    'tattoo': keep_tag,
    'teacher': keep_tag,
    'teen': keep_tag,
    'thick': keep_tag,
    'thong': keep_tag,
    'threesome': ['threesome', 'group sex', ],
    'tiny tits': ['small tits', ],
    'titjob': keep_tag,
    'tribbing': remove_gallery,
    'twink': remove_gallery,
    'twins': remove_tag,
    'underwater': remove_gallery,
    'undressing': keep_tag,
    'uniform': keep_tag,
    'upskirt': keep_tag,
    'vintage': remove_gallery,
    'voyeur': remove_gallery,
    'wedding': remove_gallery,
    'wet': remove_tag,
    'white': remove_tag,
    'wife': remove_tag,
    'yoga': remove_tag,
    'yoga pants': keep_tag,
}

""" AI GEN TAGS """

FILTERED_PORNHUB_CATEGORIES = [
    'anal',
    'bbw',
    'big ass',
    'big dick',
    'big tits',
    'blonde',
    'blowjob',
    'bondage',
    'brunette',
    'cosplay',
    'creampie',
    'cumshot',
    'double penetration',
    'ebony',
    'feet',
    'fingering',
    'fisting',
    'handjob',
    'hardcore',
    'lesbian',
    'massage',
    'masturbation',
    'milf',
    'old/young',
    'pissing',
    'public',
    'pussy licking',
    'red head',
    'rough sex',
    'small tits',
    'smoking',
    'solo',
    'squirt',
    'strap on',
    'striptease',
    'tattooed women',
    'teen',
    'threesome',
    'toys',
    'transgender'
]

AI_GEN_TAGS = pd.read_excel(
    "datasets/ai_gen_tags.xlsx", index_col=0
)
