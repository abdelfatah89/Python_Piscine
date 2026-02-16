from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self.match_count = 0
        self.cards_registered = {}

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its unique ID."""
        card_id = "{}_{}".format(
            card.name.split(' ')[-1].lower(), len(self.cards_registered))
        self.cards_registered.update({card_id: card})
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two cards and update rankings."""
        card_1 = self.cards_registered.get(card1_id)
        card_2 = self.cards_registered.get(card2_id)

        if card_1.attack_power >= card_2.attack_power:
            winner, loser = card_1, card_2
        else:
            winner, loser = card_2, card_1

        winner.update_wins(1)
        loser.update_losses(1)
        self.match_count += 1
        return {
            'winner': winner.name,
            'loser': loser.name,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        """Return cards sorted by rating."""
        sorted_cards = sorted(self.cards_registered.values(),
                              key=lambda card: card.calculate_rating(),
                              reverse=True)
        return [f"{c.name}: - Rating: {c.calculate_rating()}"
                f" ({c.get_rank_info().get('record')})"
                for c in sorted_cards]

    def generate_tournament_report(self) -> dict:
        """Generate platform-wide statistics"""
        return {
            'total_cards': len(self.cards_registered),
            'match_played': self.match_count,
            'status': "active"
        }
