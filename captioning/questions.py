import enum


class Question:
    def __init__(
            self,
            question: str,
            options: list[str] | None = None,
            options_suffix: str | None = None,
            options_prefix: str | None = None,
            else_option: str = "no_info"
    ):
        self.question = question
        self.options_suffix = options_suffix
        self.options_prefix = options_prefix
        self.options = self._build_options(options)
        self.else_option = else_option

    def _build_options(self, options: list[str] | None):
        if options:
            if self.options_prefix:
                return [f"{self.options_prefix} {option}" for option in options]
            elif self.options_suffix:
                return [f"{option} {self.options_suffix}" for option in options]
            else:
                return options
        return None

    def __str__(self):
        if self.options:
            return " ".join(
                [
                    self.question,
                    "Choose from: ",
                    ", ".join(self.options),
                    "or", self.else_option,
                    "if can't determine or not visible.",
                    "If option is not on the list generate one that shortly answers the question.",
                ]
            )
        else:
            return " ".join(
                [
                    self.question,
                    "If can't determine output:",
                    f"{self.else_option}."
                ]
            )


class ImageQuestions(enum.Enum):
    PhotoDescription = Question(
        question="Shortly describe the image."
    )
    ActionsDescription = Question(
        question="What is the person in the image doing?"
    )
    HairColor = Question(
        question="What is the hair color of the person?",
        options=["black", "brown", "blonde", "red", "gray", "white"]
    )
    HairStyle = Question(
        question="What hairstyle does this person have?",
        options=["straight", "curly", "wavy", "updo", "ponytail", "braid"]
    )
    Physique = Question(
        question="What is the person’s physique?",
        options=["slim", "athletic", "curvy", "plus size"]
    )
    BustSize = Question(
        question="What is the bust size of the person?",
        options=["small", "medium", "large", "very large"]
    )
    AgeGroup = Question(
        question="What age group does the person belong to?",
        options=["teenager", "young adult", "middle-aged", "senior"]
    )
    FacialExpression = Question(
        question="What facial expression is the person showing?",
        options=["smiling", "frowning", "neutral", "surprised", "suggestive", "playful", "neutral", "laughing"]
    )
    ClothingCategory = Question(
        question="What type of clothing is the person wearing?",
        options=[
            "casual", "formal", "sportswear", "swimwear", "evening wear", "bra only",
            "panties only", "topless", "bottomless", "fully nude"
        ]
    )
    WornAccessories = Question(
        question="What accessories is the person wearing?",
        options=["hat", "glasses", "earrings", "necklace", "bracelet", "watch", "handbag"]
    )
    SkinTone = Question(
        question="What is the person's skin tone?",
        options=["light", "medium", "dark", "olive", "tan", "pale", "fair", "brown"]
    )
    BodyPosture = Question(
        question="What is the person’s body posture?",
        options=[
            "standing", "sitting", "lying down", "kneeling",
            "bent over", "sexy pose", "exposing", "relaxed"
        ]
    )
    GeneralLocation = Question(
        question="Where is the person located?",
        options=["indoors", "outdoors", "kitchen", "bedroom", "bathroom", "living room", "work place", "beach"]
    )
    PersonOrientation = Question(
        "What is the orientation of the person to towards camera?",
        options=["front", "back", "side", "three-quarters", "overhead", "underneath", "close-up", "full body"]
    )
    ShotContextFocus = Question(
        "What part of the body is the primary focus of the image?",
        options=[
            "face", "chest", "hips", "legs", "feet", "back", "butt",
            "genitals", "breasts", "torso", "arms", "neck",
            "hair", "eyes", "mouth"
        ]
    )
    ImageType = Question(
        question="What type of image is this?",
        options=[
            "portrait", "full body", "candid", "fashion", "close-up",
            "professional", "selfie", "posed", "suggestive", "erotic"
        ]
    )


if __name__ == "__main__":
    print(f"Questions to ask about an image: {len(ImageQuestions)}")
    for question in ImageQuestions:
        print(question.value)
        print()
