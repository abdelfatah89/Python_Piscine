from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")

    tournament = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendry", 8, 5)
    wizard = TournamentCard("Ice Wizard", 3, "Legendry", 10, 2)

    print("\nRegistering Tournament Cards...")
    cards = [dragon, wizard]
    for card in cards:
        tournament.register_card(card)

    for card_id, card in tournament.cards_registered.items():
        rank_info = card.get_rank_info()
        print(f"{card.name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {rank_info.get("rating")}")
        print(f"- Record: {rank_info.get("record")}")

    ids = [k for k in tournament.cards_registered.keys()]
    if len(ids) > 1:
        match = tournament.create_match(ids[0], ids[1])
        print("\nCreating tournament match...")
        print(f"Match result: {match}")

    print("\nTournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    for i, card in enumerate(leaderboard):
        print(f"{i+1}. {card})")

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
