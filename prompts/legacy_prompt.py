# As an AI image tagging expert, please provide precise for this image to enhance the SDXL model's understanding of the content.
# Employ succinct keywords or phrases, steering clear of elaborate sentences and extraneous conjunctions.
# Your tags should capture key categories and elements such as the:
#
# 1. Woman's attributes:
# - gender, age-category, hair-style, hair-color, face-expressions (if visible), skin-color,
# body-type, body-language, skin-type, breast-size, breast-type, body-position, position-description,
# upper-body-clothing, lower-body-clothing, accessories-types, sex-gadgets-types, sexual-position-name (if recognizable)
#
# 2. Photo attributes:
# - context, style, composition, lighting, location, background, mood, person-count
#
# 3. Camera attributes:
# - shot-size, angle, distance, focus, blur
#
# 4. Flags (yes/no questions):
# - face-visible-flag, nudity-flag, intercourse-flag, masturbation-flag, breasts-visible-flag, natural-breasts-flag, vagina-flag, penis-flag, dildo_flag
#
# Your tags should be accurate and non-duplicative.
# These tags will be used for image re-creation, so the closer the resemblance to the original image, the better the tag quality.
# Tags should be structured for easy parsing as JSON. If more than one tag can fit the image context, output them as a list.
#
# Exceptional tagging will be rewarded with $10 per mage.
#
# Fill this JSON template:
# {
#    "flags": {
#       "visible-face-flag: "",
#       "nudity-flag": "",
#       "intercourse-flag": "",
#       "masturbation-flag": "",
#       "genitals-close-up-flag": "",
#       "breasts-visible-flag": "",
#       "visible-vagina-flag": "",
#       "visible-penis-flag": "",
#       "visible-asshole-flag": "",
#       "visible-dildo-flag": ""
#   },
#   "person": {
#     "gender": "",
#     "age-category": "",
#     "hair-style": "",
#     "hair-color": "",
#     "face-expressions": "",
#     "skin-color": "",
#     "skin-details": "".
#     "body-type": "",
#     "body-language": "",
#     "skin-type": "",
#     "breast-size": "",
#     "breast-type": "",
#     "body-position": "",
#     "upper-body-clothing": "",
#     "lower-body-clothing": "",
#     "accessories-types": "",
#     "sexual-position-name": ""
#   },
#   "photo": {
#     "context": "",
#     "style": "",
#     "composition": "",
#     "lighting": "",
#     "location": "",
#     "background": "",
#     "mood": "",
#     "person-count": "",
#     "sex-gadgets-types": ""
#   },
#   "camera": {
#     "shot-size": "",
#     "angle": "",
#     "distance": "",
#     "focus": "",
#     "blur": ""
#   },
# }
#
# ======================================================================================================================================================================================================
#
# Generate a detailed and accurate description for the given IMAGE. This description will be used to fine-tune a Stable Diffusion model, requiring comprehensive and precise textual data.
#
# Input:
# You are given one IMAGE (from the gallery of pictures) and TAGS that were extracted from the image.
# The task is to use given TAGS and IMAGE to write a descriptive paragraph that includes information about the people, objects, their actions, the setting, colors, and any other relevant details.
# When describing the image by focus only on observable details. Avoid making assumptions about what objects might be or the actions taking place. Use factual and verifiable language.
#
# Instructions:
# 1.	Extract Information from the Image and Tags:
# 	•	Carefully observe all elements in the image, including the background, foreground, people, their actions, dynamics, and objects.
# 	•	Identify key tags that describe the main aspects of the image.
# 	•	Describe the woman, her posture and her actions extensively. Use given tags to provide accurate details. Make sure to mention her skin-color, age-group, body-type, clothing, and accessories.
#
# 2.	Write a Detailed Description Using Extracted Tags:
# 	•	Objects: Identify and describe the main objects in the image, noting their shapes, sizes, and relative positions.
# 	•	Actions: Describe any actions or interactions between objects. Specify what each object is doing or how they are interacting.
# 	•	Setting: Provide details about the environment or setting, such as location, time of day, weather conditions, and relevant background elements.
# 	•	Colors and Styles: Note the prominent colors, textures, and any stylistic elements present in the image.
# 	•	Additional Features: Mention any other notable features or details that contribute to the overall context or story of the image.
#
# 3.	Notes:
# 	•	Ensure the description is unique and captures the essence of the image.
# 	•	The description should be vivid and detailed enough to create a mental image for someone who hasn’t seen the picture.
# 	•	Maintain a consistent style and tone throughout the description.
# 	•	Focus on providing a comprehensive narrative that encompasses all visible elements and their interactions within the image.
