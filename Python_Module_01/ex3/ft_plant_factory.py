class Plant:
    """Factory class to create and track specific plant species instances."""
    plantsNumber = 0

    def __init__(self, name, height=1, age=1):
        """Initialize plant attributes with species-specific defaults
        and increment counter."""
        self.name = name

        species_data = {
            "rose":         {"height": 25, "age": 30},
            "oak":          {"height": 200, "age": 365},
            "cactus":       {"height": 5, "age": 90},
            "sunflower":    {"height": 80, "age": 45},
            "fern":         {"height": 15, "age": 120}
        }
        species_found = False
        for species, data in species_data.items():
            if self.name.lower() == species:
                self.height = data["height"]
                self.age = data["age"]
                species_found = True
                break

        if not species_found:
            self.height = height
            self.age = age

        Plant.plantsNumber += 1

    def get_info(self):
        """Print a summary of the plant's current species, height, and age."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def grow(self):
        """Increase the plant's height by 1cm."""
        self.height += 1

    def aging(self):
        """Increase the plant's age by 1 day."""
        self.age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose = Plant("Rose")
    oak = Plant("Oak")
    cactus = Plant("Cactus")
    sunflower = Plant("Sunflower")
    fern = Plant("Fern")

    rose.get_info()
    oak.get_info()
    cactus.get_info()
    sunflower.get_info()
    fern.get_info()

    # Displaying the shared class variable
    print(f"Total plants created: {Plant.plantsNumber}")
