def dynamic_prompt(categories: list[str]) -> str:
    prompt = f"""
As an AI image tagging expert, analyze the given image containing explicit content and complete the provided template.
You are given a single image from a gallery. 
Your task is to tag and categorize this image based on a given set of categories and tags. 
The tags may apply to the entire gallery but not necessarily to every individual image.

**Categories**: {categories}

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


def prompt_all_categories(categories: list[str], tags: list[str]) -> str:
    categories = [
        'African', 'Amateur', 'Anal', 'Arab', 'Argentina', 'Armpit', 'Asian', 'Ass', 'Ass Fucking', 'Ass Licking',
        'Asshole', 'Australian', 'BBC', 'BBW', 'BDSM', 'Babe', 'Babysitter', 'Ball Licking', 'Bath', 'Beach',
        'Beautiful', 'Big Cock', 'Big Tits', 'Bikini', 'Bisexual', 'Blindfold', 'Blonde', 'Blowbang', 'Blowjob',
        'Bondage', 'Brazilian', 'British', 'Brunette', 'Butt Plug', 'CFNM', 'Cameltoe', 'Canadian', 'Centerfold',
        'Cheerleader', 'Chinese', 'Christmas', 'Chubby', 'Clothed', 'College', 'Colombian', 'Cosplay', 'Cougar',
        'Couple', 'Cowgirl', 'Cuban', 'Cum In Mouth', 'Cum In Pussy', 'Cum Swapping', 'Cumshot', 'Curly', 'Curvy',
        'Cute', 'Czech', 'Deepthroat', 'Dildo', 'Doctor', 'Doggy Style', 'Double Penetration', 'Dress', 'Dutch',
        'Ebony', 'Erotic', 'European', 'Facesitting', 'Facial', 'Fake Tits', 'Filipina', 'Fingering', 'Flexible',
        'Footjob', 'French', 'German', 'Girlfriend', 'Glamour', 'Glasses', 'Gloryhole', 'Groupsex', 'Gym', 'Hairy',
        'Halloween', 'Handjob', 'Hardcore', 'High Heels', 'Homemade', 'Housewife', 'Humping', 'Hungarian', 'Indian',
        'Interracial', 'Italian', 'Japanese', 'Jeans', 'Kissing', 'Kitchen', 'Korean', 'Latex', 'Latina', 'Leather',
        'Legs', 'Lesbian', 'Lingerie', 'MILF', 'MMF', 'Maid', 'Masturbation', 'Mature', 'Mexican', 'Missionary',
        'Model', 'Mom', 'Natural Tits', 'Nipples', 'Non Nude', 'Nun', 'Nurse', 'Office', 'Oiled', 'Old Young',
        'Orgasm', 'Outdoor', 'PAWG', 'POV', 'Pale', 'Panties', 'Pantyhose', 'Petite', 'Pigtails', 'Police', 'Polish',
        'Pool', 'Pornstar', 'Pretty', 'Public', 'Pussy', 'Pussy Licking', 'Reality', 'Redhead', 'Russian', 'Sandals',
        'Schoolgirl', 'Secretary', 'Seduction', 'Selfie', 'Sexy', 'Shaved', 'Short Hair', 'Shorts', 'Shower', 'Skinny',
        'Skirt', 'Smoking', 'Socks', 'Solo', 'Spanish', 'Spanking', 'Sports', 'Spreading', 'Squirting', 'Step Brother',
        'Step Sister', 'Stepmom', 'Stockings', 'Tall', 'Tattoo', 'Teacher', 'Teen', 'Thai', 'Thick', 'Thong',
        'Threesome', 'Tiny Tits', 'Titjob', 'Twins', 'Ukrainian', 'Undressing', 'Uniform', 'Upskirt', 'Venezuela',
        'Wet', 'White', 'Wife', 'Yoga', 'Yoga Pants'
    ]
    return



