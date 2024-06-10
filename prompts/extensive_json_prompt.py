# As an AI image tagging expert, analyze the given image containing explicit content and complete the provided template.
# Return the filled template as a JSON object.Ensure that you select the most appropriate words from the provided lists
# in the template.You may select multiple words from the list if applicable.If an item visible in the image is not
# mentioned in the list, you may add it to your response. If['*'], please provide precise tag / tags to enhance the BLIP
# model 's understanding of the content. Employ succinct keywords or phrases, steering clear of elaborate sentences and
# extraneous conjunctions.
#
# JSON_TEMPLATES:
# flags_template = {
#     'partial-nudity': bool,
#     'full-nudity': bool,
#     'intercourse': bool,
#     'masturbation': bool,
#     'genitals-close-up': bool,
#     'left-breast-visible': bool,
#     'right-breast-visible': bool,
#     'underboob-visible': bool,
#     'visible-vagina': bool,
#     'visible-penis': bool,
#     'visible-asshole': bool,
#     'visible-dildo': bool
# }
# woman_template = {
#     'age-category': [
#         'young_adult', 'adult', 'mature', 'granny'
#     ],
#     'hair': {
#         'style': [
#             'straight', 'curly', 'wavy', 'afro', 'braided', 'cornrows', 'bun',
#             'ponytail', 'dreadlocks', 'shaved', 'updo'
#         ],
#         'color': [
#             'black', 'brown', 'blonde', 'red', 'platinum blonde', 'gray', 'balayage', 'auburn'
#         ],
#     },
#     'face': {
#         'makeup': ['no', 'light', 'medium', 'heavy', 'smudged'],
#         'expressions': [
#             'happy', 'sad', 'angry', 'surprised', 'disgusted', 'neutral', 'excited', 'confident',
#             'sensual', 'seductive'
#         ],
#     },
#     'skin': {
#         'color': [
#             'fair', 'white', 'light brown', 'olive', 'black'
#         ],
#         'details': [
#             'freckles', 'moles', 'birthmarks', 'wrinkles', 'scars', 'age spots', 'skin folds', 'cellulite',
#         ],
#     },
#     'body': {
#         'visibility': [
#             'full_body', 'upper_body', 'mid_shot', 'lower_body', 'portrait', 'close_up', 'knee_up', 'waist_up'
#         ],
#         'type': [
#             'slim', 'fit', 'average', 'curvy', 'plus-size', 'fat'
#         ],
#         'position': [
#             'on all fours', 'standing', 'sitting', 'lying down', 'crouching', 'kneeling', 'leaning forward',
#             'bending over', 'reclining', 'masturbation', 'intercourse'
#         ]
#     },
#     'sex-positions': [
#         'missionary', 'doggy style', 'cowgirl', 'reverse cowgirl', 'spooning', 'standing', 'lotus',
#         'legs on shoulders', 'butterfly', '69', 'side-by-side', 'face-to-face', 'lap dance', 'bridge',
#         'scissors', 'kneeling', 'crab walk', 'prone bone', 'blowjob', 'cunnilingus'
#     ],
#     'upper_body': {
#         'activity': [
#             'arms crossed', 'hands on breast', 'hands on hips', 'hands behind back', 'hands clasped',
#             'hands in pockets', 'hands on head', 'hands on ass',
#         ],
#         'breasts': {
#             'size': [
#                 'small', 'medium', 'large', 'extra large'
#             ],
#             'type': [
#                 'saggy', 'perky', 'teardrop', 'asymmetric', 'flat', 'round', 'bell'
#             ]
#         },
#         'clothing': [
#             'blouse', 'tank top', 'sweater', 'cardigan', 't-shirt', 'crop top', 'tube top', 'hoodie',
#             'blazer', 'vest', 'shirt', 'polo shirt', 'bra-only', 'lace bra', 'naked', 'bikini', 'gown', 'pyjama'
#         ],
#         'accessories': [
#             "necklace", "scarf", "tie", "bow tie", "pendant", "choker", "badge", "collar pin",
#         ]
#     },
#     'lower_body': {
#         'activity': [
#             'cross-legged', 'legs apart', 'sprawled', 'spread-eagled', 'legs raised',
#             'legs crossed', 'legs straight', 'legs bent'
#         ],
#         'clothing': [
#             "jeans", "trousers", "shorts", "mini skirt", "short skirt", "long skirt", "leggings",
#             "capri pants", "joggers", "pencil skirt", "denim shorts", 'naked', 'panties', 'lingerie',
#             'bikini', 'thongs', 'pyjama', 'stockings', 'lace panties'
#         ],
#         'shoes': [
#             'sneakers', 'platform shoes', 'heels', 'boots', 'bare feet'
#         ],
#     },
#     'sexual-position': [
#         'missionary', 'doggy style', 'cowgirl', 'reverse cowgirl', 'spooning', 'standing', 'lotus',
#         'legs on shoulders', 'butterfly', '69', 'side-by-side', 'face-to-face', 'lap dance', 'bridge',
#         'scissors', 'kneeling', 'crab walk', 'prone bone', 'blowjob', 'cunnilingus'
#     ],
# }
# photo_descriptions = {
#     'context': ['*'],
#     'style': ['*'],
#     'composition': ['*'],
#     'lighting': ['*'],
#     'location': ['*'],
#     'background': ['*'],
#     'mood': ['*'],
#     'person-count': ['*'],
#     'photo_theme': ['*'],
#     'sex-gadgets-types': [
#         'vibrator', 'dildo', 'butt plug', 'anal beads', 'strap-on', 'bondage kit'
#     ],
# },
# camera = {
#     'shot-size': ['*'],
#     'angle': ['*'],
#     'distance': ['*'],
#     'focus': ['*'],
#     'blur': ['*']
# }

# ======================================================================================================================
