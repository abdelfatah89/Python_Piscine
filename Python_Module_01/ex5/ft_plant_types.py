class Plant:
    """Base class representing common features
    for all vegetation in the garden."""
    def __init__(self, name, height, age):
        """Initialize the fundamental attributes of a plant."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represent flowers with color attributes and blooming capabilities."""
    def __init__(self, name, height, age, color):
        """Initialize flower using parent setup plus a specific color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Prints the flower's details and a blooming message."""
        print("{} (Flower): {}cm, {} days, {} color".format(
            self.name, self.height, self.age, self.color))
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Represent trees with trunk diameter and shade production features."""
    def __init__(self, name, height, age, trunk_diameter):
        """Initialize tree with a specific trunk diameter using inheritance."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Calculate and display the shade area based on trunk diameter."""
        r = self.trunk_diameter / 100
        shade_area = 312 * r**2
        print("{} (Tree): {}cm, {} days, {}cm diameter".format(
            self.name, self.height, self.age, self.trunk_diameter))
        print("{} provides {:.0f} square meters of shade".format(
            self.name, shade_area))


class Vegetable(Plant):
    """Represent edible plants with seasonal and nutritional data."""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initialize vegetable with harvest and nutrition
        details via parent class.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutritional_value(self):
        """Print the vegetable's attributes and its nutritional profile."""
        print("{} (Vegetable): {}cm, {} days, {} harvest".format(
            self.name, self.height, self.age, self.harvest_season))
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    rose.bloom()
    print()
    oak.produce_shade()
    print()
    tomato.get_nutritional_value()
