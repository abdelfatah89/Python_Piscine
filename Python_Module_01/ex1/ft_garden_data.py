class Plant:
    """Represent a plant with a name, height,
    and age in a digital registry."""
    def __init__(self, name, height, age):
        """Initialize a new plant instance with specific attributes."""
        self.name = name
        self.height = height
        self.age = age

    def display_plant(self):
        """Prints the plant's current attributes in a formatted string."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    # Instantiate three distinct objects
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")

    Rose.display_plant()
    Sunflower.display_plant()
    Cactus.display_plant()
