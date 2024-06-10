def dynamic_prompt(categories: list[str]) -> str:
    prompt = f"""As an AI image tagging expert, analyze the given image containing explicit content. 
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
    return prompt
