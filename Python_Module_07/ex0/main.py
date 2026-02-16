from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\nCreatureCard Info:")
    print(dragon_card.get_card_info(), '\n')
    mana = 5
    if dragon_card.is_playable(mana):
        print(f"Playing {dragon_card.name} with {mana} mana available:")
        print("Playable:", dragon_card.is_playable(mana))
    else:
        print(f"insufficient mana ({mana} available)")
        print("Playable:", dragon_card.is_playable(mana))

    print("Play result:", dragon_card.play())

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", dragon_card.attack_target("Goblin Warrior"))

    mana = 3
    print("\nTesting insufficient mana (3 available):")
    print("Playable:", dragon_card.is_playable(mana))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
