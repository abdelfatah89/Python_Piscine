from typing import Any


def mage_counter() -> callable:
    i = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str) -> None:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault.update({key: value})

    def recall(key: str) -> Any:
        if vault.get(key):
            return vault.get(key)
        return "Memory not found"

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i+1}: {counter()}")

    print("\nTesting spell accumulator...")
    initial_power = 8
    accumulator = spell_accumulator(initial_power)
    print(f"Initial power: {initial_power}"
          f"\nAfter Accumulation: {accumulator(5)}")

    print("\nTesting enchantment factory...")
    enchant = enchantment_factory("Flaming")
    print(enchant("Sword"))
    enchant2 = enchantment_factory("Frozen")
    print(enchant2("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    store = vault.get("store")
    recall = vault.get("recall")
    print("  - Storing data in vault...")
    store('name', 'Abdelfatah')
    print("  - Recall data from vault...")
    print(f"   -- Recall value of 'name': {recall('name')}")


if __name__ == "__main__":
    main()
