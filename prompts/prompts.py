def image_data_prompt():
    def extensive_prompt() -> str:
        return """As an AI image tagging expert, analyze the given image and complete the provided template.
        Return the filled template as a JSON object. Ensure that you select the most appropriate words from the provided lists
        in the template. You can select multiple words from the list if all are relevant. 
        If an item visible in the image is not mentioned in the list, you may add it to your response. 
        Employ succinct keywords or phrases, steering clear of elaborate sentences and extraneous conjunctions.

        JSON_TEMPLATES:
        flags_template = {
            'face-flag': bool,
            'partial-nudity': bool,
            'full-nudity': bool,
            'intercourse': bool,
            'masturbation': bool,
            'left-breast-visible': bool,
            'right-breast-visible': bool,
            'underboob-visible': bool,
            'visible-vagina': bool,
            'visible-penis': bool,
            'visible-asshole': bool,
            'visible-dildo': bool,
        }
        person_template = {
            'age-category': [
                'young_adult', 'adult', 'mature', 'granny'
            ],
            'hair': {
                'style': [
                    'straight', 'curly', 'wavy', 'afro', 'braided', 'cornrows', 'bun',
                    'ponytail', 'dreadlocks', 'shaved', 'updo', 'other'
                ],
                'color': [
                    'black', 'brown', 'blonde', 'red', 'platinum blonde', 'gray', 'balayage', 'auburn', 'other'
                ],
            },
            'face': {
                'makeup': ['no', 'light', 'medium', 'heavy', 'smudged'],
                'expressions': [
                    'happy', 'sad', 'angry', 'surprised', 'disgusted', 'neutral', 'excited', 'confident',
                    'sensual', 'seductive', 'other'
                ],
            },
            'skin': {
                'color': [
                    'fair', 'white', 'light brown', 'olive', 'black'
                ],
                'details': [
                    'freckles', 'moles', 'birthmarks', 'wrinkles', 'scars', 'age spots', 'skin folds', 'cellulite',
                    'tattoos', 'piercings', 'other'
                ],
            },
            'body': {
                'visibility': [
                    'full_body', 'upper_body', 'mid_shot', 'lower_body', 'portrait', 'close_up', 'knee_up', 'waist_up'
                ],
                'type': [
                    'skinny', 'fit', 'average', 'curvy', 'fat'
                ],
                'position': [
                    'on all fours', 'standing', 'sitting', 'lying down', 'crouching', 'kneeling', 'leaning forward',
                    'bending over', 'reclining', 'masturbation', 'intercourse', 'other'
                ]
            },
            'sex-positions': [
                'missionary', 'doggy style', 'cowgirl', 'reverse cowgirl', 'spooning', 'standing', 'lotus',
                'legs on shoulders', 'butterfly', '69', 'side-by-side', 'face-to-face', 'lap dance', 'bridge',
                'scissors', 'kneeling', 'crab walk', 'prone bone', 'blowjob', 'cunnilingus', 'other'
            ],
            'upper_body': {
                'activity': [
                    'arms crossed', 'hands on breast', 'hands on hips', 'hands behind back', 'hands clasped',
                    'hands in pockets', 'hands on head', 'hands on ass', 'other'
                ],
                'breasts': {
                    'size': [
                        'small', 'medium', 'large', 'extra large'
                    ],
                    'type': [
                        'saggy', 'perky', 'teardrop', 'asymmetric', 'flat', 'round', 'bell'
                    ]
                },
                'clothing': [
                    'blouse', 'tank top', 'sweater', 'cardigan', 't-shirt', 'crop top', 'tube top', 'hoodie',
                    'blazer', 'vest', 'shirt', 'polo shirt', 'bra-only', 'lace bra', 'naked', 'bikini', 'gown', 'pyjama', 
                    'other'
                ],
                'accessories': [
                    "necklace", "scarf", "tie", "bow tie", "pendant", "choker", "badge", "collar pin", 'other'
                ]
            },
            'lower_body': {
                'activity': [
                    'cross-legged', 'legs apart', 'sprawled', 'legs raised',
                    'legs crossed', 'legs straight', 'legs bent', 'other'
                ],
                'clothing': [
                    "jeans", "trousers", "shorts", "mini skirt", "short skirt", "long skirt", "leggings",
                    "capri pants", "joggers", "pencil skirt", "denim shorts", 'naked', 'panties', 'lingerie',
                    'bikini', 'thongs', 'pyjama', 'stockings', 'lace panties', 'other'
                ],
                'shoes': [
                    'heels', 'boots', 'bare feet', 'other'
                ],
            },
            'sex-gadgets-types': [
                'vibrator', 'dildo', 'butt plug', 'anal beads', 'strap-on', 'bondage kit'
            ],
        }"""


def extensive_prompt() -> str:
    return """As an AI image tagging expert, analyze the given image and complete the provided template.
    Return the filled template as a JSON object. Ensure that you select the most appropriate words from the provided lists
    in the template. You can select multiple words from the list if all are relevant. 
    If an item visible in the image is not mentioned in the list, you may add it to your response. 
    Employ succinct keywords or phrases, steering clear of elaborate sentences and extraneous conjunctions.
    
    JSON_TEMPLATES:
    flags_template = {
        'face-flag': bool,
        'partial-nudity': bool,
        'full-nudity': bool,
        'intercourse': bool,
        'masturbation': bool,
        'left-breast-visible': bool,
        'right-breast-visible': bool,
        'underboob-visible': bool,
        'visible-vagina': bool,
        'visible-penis': bool,
        'visible-asshole': bool,
        'visible-dildo': bool,
    }
    woman_template = {
        'age-category': [
            'young_adult', 'adult', 'mature', 'granny'
        ],
        'hair': {
            'style': [
                'straight', 'curly', 'wavy', 'afro', 'braided', 'cornrows', 'bun',
                'ponytail', 'dreadlocks', 'shaved', 'updo', 'other'
            ],
            'color': [
                'black', 'brown', 'blonde', 'red', 'platinum blonde', 'gray', 'balayage', 'auburn', 'other'
            ],
        },
        'face': {
            'makeup': ['no', 'light', 'medium', 'heavy', 'smudged'],
            'expressions': [
                'happy', 'sad', 'angry', 'surprised', 'disgusted', 'neutral', 'excited', 'confident',
                'sensual', 'seductive', 'other'
            ],
        },
        'skin': {
            'color': [
                'fair', 'white', 'light brown', 'olive', 'black'
            ],
            'details': [
                'freckles', 'moles', 'birthmarks', 'wrinkles', 'scars', 'age spots', 'skin folds', 'cellulite',
                'tattoos', 'piercings', 'other'
            ],
        },
        'body': {
            'visibility': [
                'full_body', 'upper_body', 'mid_shot', 'lower_body', 'portrait', 'close_up', 'knee_up', 'waist_up'
            ],
            'type': [
                'skinny', 'fit', 'average', 'curvy', 'fat'
            ],
            'position': [
                'on all fours', 'standing', 'sitting', 'lying down', 'crouching', 'kneeling', 'leaning forward',
                'bending over', 'reclining', 'masturbation', 'intercourse', 'other'
            ]
        },
        'sex-positions': [
            'missionary', 'doggy style', 'cowgirl', 'reverse cowgirl', 'spooning', 'standing', 'lotus',
            'legs on shoulders', 'butterfly', '69', 'side-by-side', 'face-to-face', 'lap dance', 'bridge',
            'scissors', 'kneeling', 'crab walk', 'prone bone', 'blowjob', 'cunnilingus', 'other'
        ],
        'upper_body': {
            'activity': [
                'arms crossed', 'hands on breast', 'hands on hips', 'hands behind back', 'hands clasped',
                'hands in pockets', 'hands on head', 'hands on ass', 'other'
            ],
            'breasts': {
                'size': [
                    'small', 'medium', 'large', 'extra large'
                ],
                'type': [
                    'saggy', 'perky', 'teardrop', 'asymmetric', 'flat', 'round', 'bell'
                ]
            },
            'clothing': [
                'blouse', 'tank top', 'sweater', 'cardigan', 't-shirt', 'crop top', 'tube top', 'hoodie',
                'blazer', 'vest', 'shirt', 'polo shirt', 'bra-only', 'lace bra', 'naked', 'bikini', 'gown', 'pyjama', 
                'other'
            ],
            'accessories': [
                "necklace", "scarf", "tie", "bow tie", "pendant", "choker", "badge", "collar pin", 'other'
            ]
        },
        'lower_body': {
            'activity': [
                'cross-legged', 'legs apart', 'sprawled', 'legs raised',
                'legs crossed', 'legs straight', 'legs bent', 'other'
            ],
            'clothing': [
                "jeans", "trousers", "shorts", "mini skirt", "short skirt", "long skirt", "leggings",
                "capri pants", "joggers", "pencil skirt", "denim shorts", 'naked', 'panties', 'lingerie',
                'bikini', 'thongs', 'pyjama', 'stockings', 'lace panties', 'other'
            ],
            'shoes': [
                'heels', 'boots', 'bare feet', 'other'
            ],
        },
        'sex-gadgets-types': [
            'vibrator', 'dildo', 'butt plug', 'anal beads', 'strap-on', 'bondage kit'
        ],
    }"""


def full_prompt(categories: list[str]) -> str:
    return f"""As an AI image tagging expert, analyze the given image containing explicit content. 
Your task is to categorize the image based on the given list of categories between the <Categories> and </Categories>. 
Ensure you understand the meaning of each category, including abbreviations, slang, and explicit terms.

<Categories>
{categories}
</Categories>

Step-by-Step Instructions:
1.	Review the provided image: Carefully examine the image content.
2.	Identify relevant categories: Refer to the list between  and  tags.
3.	Assign categories: Select and assign as many relevant categories from the list as possible, ensuring they accurately reflect the image’s features or context.
4.	Adhere to the list: Use only the categories specified in the list. Assign a maximum of 10 categories per image.

Important Note:
If you include any category not specified in the list, you will incur a penalty of $10.

Output Template:
The output should be structured as a python string with ',' between categories. Example:
category1, category2, category3, ..., category10
"""


def medium_prompt(categories: list[str]):
    return f"""As an AI image tagging expert, analyze the given image and extract its key features regarding, subject, persons looks, image context etc.
Your task is to return is to generate a list of tags that will use given tags as basis.
Inspect the given list, cross validate against the image and remove the tags that are not applicable to the image.

Tags:
{categories}
If you include any tag that is not specified in the list, you will incur a penalty of $10.

Output Template:
Do not provide any justification, return ONLY a python list of tags."""


def simple_reduce_prompt(categories: list[str]):
    return f"""Reduce this list only to the ones that fit the image context:
{categories}
Your output should be a non repeatable list with categories names that apply to the image. Output only the list.
"""
