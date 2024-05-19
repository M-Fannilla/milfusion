import enum


class ImageQuestion:
    def __init__(
            self,
            question: str,
            options: list[str] | None = None,
            else_option: str = "no_info"
    ):
        self.question = question
        self.options = options
        self.else_option = else_option

    def __str__(self):
        if self.options:
            return " ".join(
                [
                    self.question,
                    "Choose from: ",
                    ", ".join(self.options),
                    "or", self.else_option,
                    "if can't determine."
                ]
            )
        else:
            return " ".join(
                [
                    self.question,
                    "If can't determine:",
                    f"{self.else_option}."
                ]
            )


class Questions(enum.Enum):
    HairColor = ImageQuestion("What hairstyle and color does this person have?")
    Physique = ImageQuestion(
        "What is the person’s physique?",
        ["slim", "athletic", "muscular", "stout", "plump", "curvy"]
    )
    BreastSize = ImageQuestion(
        "What is the breast size of the person?",
        ["small", "medium", "large", "very large"]
    )
    Age = ImageQuestion(
        "In which age group does the person fall?",
        ["30s", "40s", "50s", "60s"]
    )
    Expression = ImageQuestion("What expression is the person showing?")
    Clothing = ImageQuestion("What kind of clothing is the person wearing?")
    ClothingDistinction = ImageQuestion("Can you distinct what this woman is wearing?")
    Accessories = ImageQuestion("What accessories is the person wearing or holding?")
    SkinTone = ImageQuestion("What is the person’s skin tone?")
    Posture = ImageQuestion("What is the person’s posture?")
    Location = ImageQuestion("Where is the person located?")
    Orientation = ImageQuestion("What is the orientation of the person in the image?")
    Setting = ImageQuestion("Where is the scene set?")
    EnvironmentSetting = ImageQuestion("Where is the scene set?")
    ShotContextFrame = ImageQuestion("What type of shot frame is being used?")
    ShotContextFocus = ImageQuestion("What part of the body is the primary focus of the image?")


if __name__ == "__main__":
    print(f"Questions to ask about an image: {len(Questions)}")
    for question in Questions:
        print(question.value)
