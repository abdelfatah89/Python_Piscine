from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===")

    Arcane = EliteCard("Arcane Warrior", 4, "Legendary", 5, 3, 10, 4)
    print(f"\nPlaying {Arcane.name} (Elite Card):")

    print("\nCombat phase:")
    print("Attack result:", Arcane.attack("Enemy"))
    print("Defend result:", Arcane.defend(5))

    print("\nMagic phase:")
    print("Spell cast:", Arcane.cast_spell('Fireball', ['Enemy1', 'Enemy2']))
    print("Mana channel:", Arcane.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
