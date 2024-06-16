def json_data_prompt() -> str:
    return """As an AI image tagging expert, analyze the given image and complete the provided template.
        Return the filled template as a JSON object. Ensure that you select the most appropriate words from the provided lists
        in the template. You can select multiple words from the list if all are relevant. 

        JSON_TEMPLATES:
        flags_template = {
            'face-visible-flag': bool,
            'partial-nudity': bool,
            'full-nudity': bool,
            'intercourse': bool,
            'masturbation': bool,
            'visible-breasts': bool,
            'visible-vagina': bool,
            'visible-penis': bool,
            'visible-asshole': bool,
            'visible-dildo': bool,
        }
        
        person_template = {
            'age': [
                'teen', 'adult', 'mature', 'granny'
            ],
            'hair': {
                'style': [
                    'straight', 'curly', 'wavy', 'afro', 'braided', 'cornrows', 'bun',
                    'ponytail', 'dreadlocks', 'short', 'updo', 'None'
                ],
                'color': [
                    'black', 'brown', 'blonde', 'red', 'platinum blonde', 'gray', 'balayage', 'auburn', 'None'
                ],
            },
            'face': {
                'expressions': [
                    'happy', 'sad', 'angry', 'surprised', 'disgusted', 'neutral', 'excited', 'confident',
                    'sensual', 'seductive', 'None'
                ],
                'details': [
                    'freckles', 'moles', 'wrinkles', 'piercing', 'makeup', 'None'
                ],
            },
            'body': {
                'visibility': [
                    'full_body', 'upper_body', 'mid_shot', 'lower_body', 'portrait', 'close_up'
                ],
                'type': [
                    'skinny', 'fit', 'average', 'curvy', 'fat'
                ],
                'skin_color': [
                    'fair', 'white', 'light brown', 'olive', 'black'
                ],
                'skin_details': [
                    'birthmarks', 'wrinkles', 'scars', 'skin folds', 'cellulite', 'tattoos', 'piercings', 'None'
                ],
            },
            'sex-positions': [
                'missionary', 'doggy style', 'cowgirl', 'reverse cowgirl', 'spooning', 'standing', 'lotus',
                'legs on shoulders', 'butterfly', '69', 'side-by-side', 'face-to-face', 'lap dance', 'bridge',
                'scissors', 'kneeling', 'crab walk', 'prone bone', 'blowjob', 'cunnilingus', 'None'
            ],
            'upper_body': {
                'breasts': {
                    'size': [
                        'small', 'medium', 'large'
                    ],
                    'type': [
                        'saggy', 'perky', 'teardrop', 'asymmetric', 'flat', 'round', 'bell'
                    ]
                },
                'clothing': [
                    'blouse', 'tank top', 'sweater', 'cardigan', 't-shirt', 'crop top', 'tube top', 'hoodie',
                    'blazer', 'vest', 'shirt', 'polo shirt', 'bra-only', 'lace bra', 'naked', 'bikini', 'gown', 
                    'pyjama'
                ],
            },
            'lower_body': {
                'clothing': [
                    "jeans", "pants", "shorts", "short skirt", "long skirt", "leggings",
                    "joggers", "denim shorts", 'naked', 'panties', 'lingerie',
                    'bikini', 'thongs', 'pyjama', 'stockings', 'lace panties'
                ],
                'shoes': [
                    'heels', 'boots', 'bare feet', 'None'
                ],
            },
            'sex-gadgets-types': [
                'vibrator', 'dildo', 'butt plug', 'anal beads', 'strap-on', 'bondage kit', 'None'
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


""" SIMPLE PROMPTS """


def simple_original(categories: list[str]):
    return f"""Reduce this list only to the ones that fit the image context:
{categories}
Your output should be a non repeatable list with categories names that apply to the image. Output only the list."""


def simple_0(categories: list[str]):
    return f"""Review the given tags and identify which ones apply to the provided image:
{categories}
Output a Python list of applicable tags without duplicates."""


def simple_1(categories: list[str]):
    return f"""Examine the provided tags and determine which ones are relevant to the image:
{categories}
Return a Python list of applicable tags with no duplicates."""


def simple_2(categories: list[str]):
    return f"""Analyze the tags and select only those that are suitable for the image:
{categories}
Provide a Python list of fitting tags without repetition."""


def simple_3(categories: list[str]):
    return f"""Look at the image and identify the tags that are appropriate:
{categories}
Your output should be a Python list of applicable tags, ensuring no duplicates."""


def simple_4(categories: list[str]):
    return f"""Assess the image and determine which of the given tags are applicable:
{categories}
Return a non-repeating Python list of relevant tags."""


""" MEDIUM PROMPTS """


def medium_original(categories: list[str]):
    return f"""Your task is to return is to generate a list of tags that will use given tags as basis.
Inspect the given list, cross validate against the image and remove the tags that are not applicable to the image.

Tags:
{categories}
If you include any tag that is not specified in the list, you will incur a penalty of $10.

Output Template:
Do not provide any justification, return ONLY a python list of tags."""


def medium_0(categories: list[str]):
    return f"""Your task is to generate a list of tags based on the provided tags. Carefully inspect the given list, cross-check against the image, and remove any tags that do not apply to the image.
Tags:
{categories}
Including any tag not specified in the list will incur a penalty of $10.

Output Template:
Do not provide any explanation, return ONLY a Python list of applicable tags."""


def medium_1(categories: list[str]):
    return f"""You need to create a list of tags using the provided tags as a basis. Examine the list, validate each tag against the image, and eliminate those that do not fit the image context.
Tags:
{categories}
Including any tag not in the given list will result in a $10 penalty.

Output Template:
Provide ONLY a Python list of relevant tags, without any justification."""


def medium_2(categories: list[str]):
    return f""""Generate a list of tags by using the provided tags. Inspect the tags, compare them with the image, and discard any that are not applicable.
Tags:
{categories}
A penalty of $10 will be imposed for including any tag not specified in the list.

Output Template:
Return ONLY a Python list of tags that apply, without any additional comments."""


def medium_3(categories: list[str]):
    return f"""Your task is to produce a list of tags derived from the given tags. Scrutinize the provided list, validate each tag against the image, and remove those that do not correspond to the image.
Tags:
{categories}
Including any unlisted tag will result in a $10 penalty.

Output Template:
Supply ONLY a Python list of suitable tags, without any explanation."""


def medium_4(categories: list[str]):
    return f"""Create a list of tags by utilizing the provided tags. Examine the list carefully, cross-check with the image, and eliminate any tags that are not applicable.
Tags:
{categories}
Any tag included that is not in the given list will incur a $10 penalty.

Output Template:
Return ONLY a Python list of relevant tags, with no justification."""


""" CHAT PROMPTS """


def chat_original(categories: list[str]):
    return f"""Your task is to return is to generate a list of tags that will use given tags as basis.
Inspect the given list, cross validate against the image and remove the tags that are not applicable to the image.

Tags:
{categories}
If you include any tag that is not specified in the list, you will incur a penalty of $10.

Output Template:
Do not provide any justification, return ONLY a python list of tags."""


def chat_0(categories: list[str]):
    return f"""Examine the provided tags and image, then generate a list of tags that are applicable to the image. Use only the tags from the provided list and remove any that don't fit the image context.
Tags:
{categories}
Including any tag not on the list will incur a $10 penalty.

Output:
Return ONLY a Python list of relevant tags, without any additional explanation."""


def chat_1(categories: list[str]):
    return f"""Your task is to filter the given tags to match the context of the image. Check each tag against the image and discard those that are not relevant.
Tags:
{categories}
You will incur a $10 penalty for including any tag not listed.

Output:
Provide ONLY a Python list of applicable tags, with no justification."""


def chat_2(categories: list[str]):
    return f"""Generate a list of tags that accurately describe the image by using the provided tags. Cross-check each tag with the image and exclude any that do not apply.
Tags:
{categories}
A $10 penalty will be imposed for any tag not in the provided list.

Output:
Return ONLY a Python list of relevant tags, without additional comments."""


def chat_3(categories: list[str]):
    return f"""Review the image and provided tags, then create a list of tags that fit the image. Only use the tags from the provided list and remove those that do not match the image context.
Tags:
{categories}
Including any unlisted tag will result in a $10 penalty.

Output:
Supply ONLY a Python list of suitable tags, with no further explanation."""


def chat_4(categories: list[str]):
    return f"""Analyze the image and provided tags, then produce a list of tags that are applicable. Validate each tag against the image and exclude those that do not apply.
Tags:
{categories}
A penalty of $10 will be charged for including any tag not on the list.

Output:
Provide ONLY a Python list of relevant tags, without any justification."""

