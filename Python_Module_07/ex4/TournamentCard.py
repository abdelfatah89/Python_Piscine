from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Enhanced card class combining core, combat, and ranking capabilities."""
    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, attack_power: int) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.rating = 1200
        self.attack_power = attack_power
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        """Implement Card interface."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Entered tournament battlefield"
        }

    def attack(self, target: str) -> dict:
        """Implement Combatable interface."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'alive': self.health > 0
        }

    def defend(self, incoming_damage: int) -> dict:
        """Implement Combatable interface"""
        self.health -= incoming_damage
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'alive': self.health > 0
        }

    def calculate_rating(self) -> int:
        """Calculate rating based on win/loss ratio."""
        return self.rating + (self.wins * 25) - (self.losses * 10)

    def update_wins(self, wins: int) -> None:
        """Update total wins."""
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """Update total losses."""
        self.losses += losses

    def get_combat_stats(self) -> dict:
        """Implement Combatable interface"""
        return {
            'attack': self.attack_power,
            'health': self.health
        }

    def get_rank_info(self) -> dict:
        """Return ranking metadata."""
        return {
            'rating': self.calculate_rating(),
            'record': f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        """Comprehensive tournament performance report."""
        stats = {'name': self.name}
        stats.update(self.get_rank_info())
        return stats
