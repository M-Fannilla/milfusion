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
