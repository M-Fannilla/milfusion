image_description_labels = {
    "appearance": {
        "hair_color": [
            "blonde", "brunette", "red", "black", "grey", "white"
        ],
        "hairstyle": [
            "short", "long", "curly", "straight", "ponytail", "bun", "braided"
        ],
        "physique": [
            "slim", "athletic", "muscular", "stout", "plump", "curvy"
        ],
        "breast_size": [
            "small", "medium", "large", "very large"
        ],
        "age": [
            "30s", "40s", "50s", "60s"
        ],
        "expression": [
            "smiling", "frowning", "neutral", "laughing", "surprised", "suggestive"
        ],
        "clothing": [
            "casual", "formal", "sportswear", "nude", "underwear", "swimwear"
        ],
        "accessories": [
            "glasses", "hat", "jewelry", "watch", "scarf", "holding a phone", "other accessories"
        ],
        "skin_tone": [
            "light", "medium", "dark", "olive"
        ]
    },
    "pose": {
        "posture": [
            "suggestive", "dancing", "kneeling", "sitting", "lying down", "taking a selfie", "standing",
            "bending over", "posing", "drinking", "smoking", "relaxing", "smiling", "legs spread"
        ],
        "location": [
            "on a bed", "on a couch", "on the floor", "on a chair", "in a car", "in front of a mirror"
        ],
        "orientation": [
            "facing camera", "side profile", "back to camera"
        ],
    },
    "environment": {
        "setting": [
            "bedroom", "outdoors", "workplace", "indoors",
        ],
    },
    "shot_context": {
        "frame": [
            "close-up", "mid-shot", "long shot", "extreme close-up", "wide shot"
        ],
        "focus": [
            "full body", "upper body", "face only", "lower body", "legs",
            "feet", "hands", "back", "buttocks", "chest", "genital area"
        ],
        "lighting": [
            "bright", "dim", "natural light"
        ]
    }
}

"""
Generate a caption for an image, considering diverse attributes. The subject may feature various 
hair colors (blonde to white) and styles (short to braided), physique types (slim to curvy), and 
breast sizes (small to very large). Age ranges from the 30s to 60s with expressions like smiling to suggestive. 
They could wear anything from casual to swimwear, with accessories like glasses or a watch. 
Skin tones range from light to dark. The pose may include actions like dancing or relaxing, with possible 
locations like a bed or a car, facing towards or away from the camera. The setting might be indoors or outdoors, 
with framing from close-ups to wide shots and focus areas like full body to specific parts, under various lighting 
conditions (bright to natural). Use these details to accurately and inclusively caption the image.
"""

"""
1. Hair Color: “What color is the person’s hair? Choose from ‘blonde’, ‘brunette’, ‘red’, ‘black’, ‘grey’, or ‘white’.”
2. Hairstyle: “What hairstyle does the person have? Options include ‘short’, ‘long’, ‘curly’, ‘straight’, ‘ponytail’, ‘bun’, or ‘braided’.”
3. Physique: “What is the person’s physique? Select from ‘slim’, ‘athletic’, ‘muscular’, ‘stout’, ‘plump’, or ‘curvy’.”
4. Breast Size: “What is the breast size of the person? Choose from ‘small’, ‘medium’, ‘large’, or ‘very large’.”
5. Age: “In which age group does the person fall? Options are ‘30s’, ‘40s’, ‘50s’, or ‘60s’.”
6. Expression: “What expression is the person showing? Options are ‘smiling’, ‘frowning’, ‘neutral’, ‘laughing’, ‘surprised’, or ‘suggestive’.”
7. Clothing: “What kind of clothing is the person wearing? Choose from ‘casual’, ‘formal’, ‘sportswear’, ‘nude’, ‘underwear’, or ‘swimwear’.”
8. Accessories: “What accessories is the person wearing or holding? Options include ‘glasses’, ‘hat’, ‘jewelry’, ‘watch’, ‘scarf’, ‘holding a phone’, or ‘other accessories’.”
9. Skin Tone: “What is the person’s skin tone? Select from ‘light’, ‘medium’, ‘dark’, or ‘olive’.”

Pose

1. Posture: “What is the person’s posture? Choose from ‘suggestive’, ‘dancing’, ‘kneeling’, ‘sitting’, ‘lying down’, ‘taking a selfie’, ‘standing’, ‘bending over’, ‘posing’, ‘drinking’, ‘smoking’, or ‘relaxing’.”
2. Location: “Where is the person located? Options include ‘on a bed’, ‘on a couch’, ‘on the floor’, ‘on a chair’, ‘in a car’, or ‘in front of a mirror’.”
3. Orientation: “What is the orientation of the person in the image? Choose from ‘facing camera’, ‘side profile’, or ‘back to camera’.”

Environment

1. Setting: “Where is the scene set? Options are ‘bedroom’, ‘outdoors’, ‘workplace’, or ‘indoors’.”

Shot Context

1. Frame: “What type of shot frame is being used? Choose from ‘close-up’, ‘mid-shot’, ‘long shot’, ‘extreme close-up’, or ‘wide shot’.”
2. Focus: “What part of the body is the primary focus of the image? Options include ‘full body’, ‘upper body’, ‘face only’, ‘lower body’, ‘legs’, ‘feet’, ‘hands’, ‘back’, ‘buttocks’, ‘chest’, or ‘genital area’.”
3. Lighting: “What is the lighting like in the image? Choose from ‘bright’, ‘dim’, or ‘natural light’.”
"""

if __name__ == "__main__":
    for category, labels in image_description_labels.items():
        print(f"{category}:")
        for label, options in labels.items():
            print(f"  {label}: {', '.join(options)}")
        print()
