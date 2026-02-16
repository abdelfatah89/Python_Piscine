def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified_spell(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditional_spell(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


def main():
    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def basic_damage(power_val=10):
        return power_val

    def is_mana_full(mana_level):
        return mana_level > 50

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(basic_damage, 3)
    original = basic_damage()
    amplified = mega_fireball()
    print(f"Original: {original}, Amplified: {amplified}")

    print("\nTesting conditional caster...")
    secure_cast = conditional_caster(is_mana_full, fireball)
    print(f"High Mana (80): {secure_cast(80)}")
    print(f"Low Mana (20): {secure_cast(20)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lambda x: f"Shields {x}"])
    results = sequence("Warrior")
    print(f"Sequence results: {results}")


if __name__ == "__main__":
    main()
