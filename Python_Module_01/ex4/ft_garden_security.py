class SecurePlant:
    """Represent a plant with encapsulated data
    and validation to ensure integrity."""
    def __init__(self, name, height, age):
        """Initialize plant and use setters to validate initial
        height and age values."""
        self.name = name
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_age(self, age):
        """Update age if non-negative,
        otherwise print a security rejection message."""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected.")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def set_height(self, height):
        """Update height if non-negative,
        otherwise print a security rejection message."""
        if height < 0:
            print(f"\n\
Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected.\n")
            return
        self.__height = height
        print(f"Height updated: {height} days [OK]")

    def get_age(self):
        """Return the current private age of the plant."""
        return self.__age

    def get_height(self):
        """Return the current private height of the plant."""
        return self.__height

    def get_info(self):
        """Print a summary of the plant's current name, height, and age."""
        print("Current plant: {} ({}cm, {} days)".format(
            self.name, self.__height, self.__age))


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    rose.get_info()
