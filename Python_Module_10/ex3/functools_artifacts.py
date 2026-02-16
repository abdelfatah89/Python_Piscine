from functools import reduce, partial, lru_cache, singledispatch
from typing import Any
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    if operation == "multiply":
        return reduce(mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)
    return 0.0


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Casting {element} enchantment (Power: {power}) on {target}"


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire_enchant = partial(base_enchantment, power=50, element="fire_enchant")
    ice_enchant = partial(base_enchantment, power=50, element="ice_enchant")
    lightning_enchant = partial(base_enchantment, power=50,
                                element="lightning_enchant")
    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': lightning_enchant
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch
    def spell(arg: Any) -> str:
        return f"Unknown essence: {type(arg).__name__}. Spell fizzled!"

    @spell.register
    def _(arg: int):
        return f"Damage spell cast with power: {arg}"

    @spell.register
    def _(arg: str):
        return f"Incantation spoken: {arg.upper()}!"

    @spell.register
    def _(arg: list):
        return f"Casting ritual chain: {arg}"

    return spell


def main() -> None:
    print("\nTesting spell reducer...")
    print("Sum:", spell_reducer([1, 2, 3, 4, 5], "add"))
    print("Multiply:", spell_reducer([1, 2, 3, 4, 5], "multiply"))
    print("Max:", spell_reducer([1, 2, 3, 4, 5], "max"))
    print("Min:", spell_reducer([1, 2, 3, 4, 5], "min"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting partial enchanter...")
    funcs = partial_enchanter(base_enchantment)
    fire_enchant = funcs.get('fire_enchant')
    ice_enchant = funcs.get('ice_enchant')
    lightning_enchant = funcs.get('lightning_enchant')
    print(fire_enchant(target="Dragon Scale"))
    print(ice_enchant(target="Dragon Scale"))
    print(lightning_enchant(target="Dragon Scale"))

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(100))
    print(spell("fireball"))
    print(spell([10, "Heal", 20]))
    print(spell(42.5))


if __name__ == "__main__":
    main()
