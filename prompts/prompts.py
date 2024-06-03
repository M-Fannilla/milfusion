def dynamic_prompt(categories: list[str], tags: list[str]) -> str:
    prompt = f"""
As an AI image tagging expert, analyze the given image containing explicit content and complete the provided template.
You are given a single image from a gallery. Your task is to tag and categorize this image based on a given set of categories and tags. 
The tags may apply to the entire gallery but not necessarily to every individual image.

**Categories**: {categories}
**Tags**: {tags}

For the given image, identify the relevant tags from the list above. If a tag does not apply to the specific image, do not include it in your response for that image.

#### Instructions:
1. Review the provided image.
2. Assign relevant tags from the provided **Tags** to the image.
3. Assign relevant categories from the provided **Categories** to the image.
4. Do not include tags that do not apply to the image.
5. If you are unsure about a tag or category, feel free to skip it.
6. Do not use more tags or categories than provided.

### Output:
Tags should be structured for easy parsing as JSON. For example: """
    prompt += """
{
    'tags': ['tag1', 'tag2', 'tag3'],
    'categories': ['category1', 'category2']
}
"""
    return prompt
