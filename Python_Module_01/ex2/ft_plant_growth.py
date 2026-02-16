class Plant:
    """Represent a basic plant with name, height, and age attributes."""
    def __init__(self, name, height, age):
        """Initialize the plant with its name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """Print a summary of the plant's current name, height, and age."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        """Increase the plant's height by 1cm."""
        self.height += 1

    def aging(self):
        """Increase the plant's age by 1 day."""
        self.age += 1


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)

    day_counter = 1
    initial_height = Rose.height

    print("=== Day 1 ===")
    Rose.get_info()

    while (day_counter < 7):
        Rose.grow()
        Rose.aging()
        day_counter += 1

    print("=== Day 7 ===")
    Rose.get_info()

    print(f"Growth this week: +{Rose.height - initial_height}cm")
