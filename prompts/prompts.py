def dynamic_prompt(categories: list[str]) -> str:
    prompt = f"""
As an AI image tagging expert, analyze the given image containing explicit content and complete the task.

Task:
You are given a single image from a gallery. 
Your main objective is to categorize this image based on a given set of categories.
Not every category is applicable to the image, so choose the most relevant ones from the list provided.
There are ~120 categories to choose from make sure use the most relevant ones.

**Categories**: \n{categories}\n
If a category does not apply to the specific image, do not include it in your response for that image.

#### Instructions:
1. Review the provided image.
2. Assign relevant categories from the provided **Categories** to the image.
3. Do not include tags that do not apply to the image.
4. If you are unsure about a tag or category, feel free to skip it.
5. Do not use other categories than the ones provided.
 If a response will contain category thats not specified in the list, you will receive penalty of 10$.


### Output Template:
Tags should be structured for easy parsing as JSON. For example: """
    prompt += """
{
    'categories': ['category1', 'category2']
}
"""
    return prompt
