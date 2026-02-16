import sys


def inventory_analysis(inventory: dict) -> None:
    """Calculates and displays total items
    and count of unique item types."""
    print("=== Inventory System Analysis ===")
    total_item = sum(inventory.values())
    item_count = 0
    for key in inventory.keys():
        item_count += 1
    print(f"Total items in inventory: {total_item}")
    print(f"Unique item types: {item_count}")


def current_inventory(inventory: dict) -> None:
    """Displays each item with its quantity and
    its percentage of the total inventory."""
    print("\n=== Current Inventory ===")
    total_item = sum(inventory.values())
    for key, value in inventory.items():
        percent = (value * 100 / total_item) if total_item > 0 else 0
        print(f"{key}: {value} units ({percent:.1f}%)")


def inventory_statistics(inventory: dict) -> None:
    """Identifies and prints the most and
    least abundant items in the inventory."""
    print("\n=== Inventory Statistics ===")
    min_value = min(inventory.values())
    max_value = max(inventory.values())
    for key, value in inventory.items():
        if value == max_value:
            print(f"Most abundant: {key} ({value} unit)")
            break
    for key, value in inventory.items():
        if value == min_value:
            print(f"Least abundant: {key} ({value} unit)")
            return


def item_category(inventory: dict) -> None:
    """Classifies items into 'Moderate' or 'Scarce'
    categories based on their quantities."""
    moderate = dict()
    scarce = dict()
    for key, value in inventory.items():
        if value > 3:
            moderate.update({key: value})
        else:
            scarce.update({key: value})

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def management_suggestions(inventory: dict) -> None:
    """Identifies items with quantities
    below 2 that require restocking."""
    restock = list()
    for key, value in inventory.items():
        if value < 2:
            restock.append(key)

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock}")


def dict_demo(inventory: dict) -> None:
    """Demonstrates dictionary methods including keys,
    values, and safe lookup using get()."""
    keys = list()
    values = list()
    item = "sword"
    for key, value in inventory.items():
        keys.append(key)
        values.append(value)

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print("Sample lookup - '{}' in inventory: {}".format(
        item, True if inventory.get(item) else False))


def main() -> None:
    """Parses command-line arguments into a dictionary
    and executes the inventory analysis suite."""
    inventory = dict()
    errors_arg = list()

    if len(sys.argv) < 2:
        print("=== Inventory System Analysis ===")
        print("No inventory data provided.")
        return

    for arg in sys.argv[1:]:
        try:
            key, value = arg.split(":")
            inventory.update({key: int(value)})
        except (ValueError, IndexError):
            errors_arg.append(arg)

    if errors_arg:
        print("=== Dictionary Check Error ===")
        for err in errors_arg:
            print(f"[Error] Invalid format for: {err}")
        print("Required format: \"name:value\" (e.g., sword:10)\n")

    if inventory:
        inventory_analysis(inventory)
        current_inventory(inventory)
        inventory_statistics(inventory)
        item_category(inventory)
        management_suggestions(inventory)
        dict_demo(inventory)
    else:
        print("=== Inventory System Analysis ===")
        print("No inventory data provided.")


if __name__ == "__main__":
    main()
