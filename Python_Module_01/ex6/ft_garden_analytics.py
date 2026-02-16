class Plant:
    """Represent a basic plant and provide
    static height/age validation methods."""
    def __init__(self, name, typePlant, height, age):
        """Initialize core attributes: name, type, height, and age."""
        self.name = name
        self.typePlant = typePlant
        self.height = height
        self.age = age

    def grow(self):
        """Increment height and age by 1 and print growth confirmation."""
        self.height += 1
        self.age += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        """Print the current basic state of the plant instance."""
        print("Current plant: {} ({}cm, {} days)".format(
            self.name, self.height, self.age))

    @staticmethod
    def validate_height(height):
        """Check if height is positive and print the validation result."""
        print(f"Height validation test: {height > 0}")

    @staticmethod
    def validate_age(age):
        """Check if age is positive and print the validation result."""
        print(f"Age validation test: {age > 0}")


class FloweringPlant(Plant):
    """Specialized plant that includes flower color and blooming status."""
    def __init__(self,
                 name, typePlant, height, age, color, is_blooming):
        """Initialize flowering plant attributes using
        parent and specific data."""
        super().__init__(name, typePlant, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def get_info(self):
        """Print state including specific flower color information."""
        print("Current plant: {} ({}cm, {} days, {} color)".format(
            self.name, self.height, self.age, self.color))


class PrizeFlower(FloweringPlant):
    """High-value flower that tracks points for garden competitions."""
    def __init__(self, name, typePlant,
                 height, age, color, is_blooming, prizePoints):
        """Initialize prize flower with points using inheritance chain."""
        super().__init__(name, typePlant, height, age, color, is_blooming)
        self.prizePoints = prizePoints


class GardenManager:
    """Manage plant collections and calculate garden-wide statistics."""
    TotalManagers = 0

    def __init__(self, name):
        """Initialize manager with name, zero growth, and empty plant list."""
        self.name = name
        self.TotalGrowth = 0
        self.plants = []

    def addPlant(self, typePlant, name, height, age, color=None,
                 is_blooming=None, prizePoints=None) -> None:
        """Create and add a specific plant type to the garden inventory."""
        if (typePlant.lower() == "plant"):
            a = Plant(name, typePlant, height, age)
        elif (typePlant.lower() == "floweringplant"):
            a = FloweringPlant(name, typePlant, height,
                               age, color, is_blooming)
        elif (typePlant.lower() == "prizeflower"):
            a = PrizeFlower(name, typePlant, height,
                            age, color, is_blooming, prizePoints)
        self.plants.append(a)
        self.TotalPlant = len(self.plants)
        print("Added {} to {}'s garden".format(
            a.name, self.name))

    def growAll(self):
        """Trigger growth for every plant in the manager's collection."""
        print("Alice is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.TotalGrowth += 1

    def PlantsTypes(self):
        """Categorize and print the count of different
        plant types in the garden."""
        regular = 0
        flowering = 0
        prizeflower = 0
        for plant in self.plants:
            if plant.typePlant.lower() == "prizeflower":
                prizeflower += 1
            elif plant.typePlant.lower() == "floweringplant":
                flowering += 1
            else:
                regular += 1
        print("Plant types: {} regular, {} flowering, {} prize flowers".format(
            regular, flowering, prizeflower))

    def CalculeScore(self):
        """Calculate total garden score based on heights and prize points."""
        score = 0
        for plant in self.plants:
            score += plant.height
            if plant.typePlant.lower() == "prizeflower":
                score += plant.prizePoints
        return score

    @staticmethod
    def GardenScore(managers):
        """Print scores for multiple managers and total gardens managed."""
        combined_scores = ""
        is_first = True
        manager_count = 0

        for manager in managers:
            current_score_info = f"{manager.name}: {manager.CalculeScore()}"

            if is_first:
                combined_scores += current_score_info
                is_first = False
            else:
                combined_scores += ", " + current_score_info

            manager_count += 1
        print(f"Garden scores - {combined_scores}")
        print(f"Total gardens managed: {manager_count}")

    def displayAll(self):
        """List all plants and their specific attributes in the garden."""
        print("Plants in garden:")
        for plant in self.plants:
            bloom = "not blooming"
            if plant.typePlant.lower() == "prizeflower":
                if plant.is_blooming:
                    bloom = "blooming"
                print("- {}: {}cm, {} flowers ({}), Prize points: {}".format(
                    plant.name, plant.height,
                    plant.color, bloom, plant.prizePoints))
            elif plant.typePlant.lower() == "floweringplant":
                if plant.is_blooming:
                    bloom = "blooming"
                print("- {}: {}cm, {} flowers ({})".format(
                    plant.name, plant.height, plant.color, bloom))
            else:
                print("- {}: {}cm".format(plant.name, plant.height))

    @classmethod
    def create_garden_network(cls, nameslist):
        """Instantiate multiple GardenManagers and track total count."""
        managers = []
        for name in nameslist:
            newManager = cls(name)
            managers.append(newManager)
            cls.TotalManagers += 1
        return managers

    class GardenStats:
        """Nested helper class to generate detailed analytic reports."""
        @staticmethod
        def report(manager):
            """Print a full statistical report for a specific GardenManager."""
            print("=== {}'s Garden Report ===".format(
                manager.name))
            manager.displayAll()
            print()
            print("Plants added: {}, Total growth: {}cm".format(
                len(manager.plants), manager.TotalGrowth))
            manager.PlantsTypes()


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    managers = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = managers[0]
    bob = managers[1]

    alice.addPlant("plant", "Oak Tree", 100, 1)
    alice.addPlant("FloweringPlant", "Rose", 25, 1, "red", True)
    bob.addPlant("FloweringPlant", "Rose", 25, 1, "red", True)
    alice.addPlant("PrizeFlower", "Sunflower", 50, 1, "yellow", True, 10)
    bob.addPlant("PrizeFlower", "Sunflower", 50, 1, "yellow", True, 10)
    bob.addPlant("PrizeFlower", "Sunflower", 50, 1, "yellow", True, 10)
    print()

    alice.growAll()
    print()

    alice.GardenStats.report(managers[0])
    print()

    Plant.validate_height(5)

    GardenManager.GardenScore(managers)
