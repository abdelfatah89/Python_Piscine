from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard (Card, Combatable, Magical):
    """A high-tier card that integrates physical
    combat prowess with magical spell casting."""
    def __init__(self, name, cost, rarity,
                 attack, defend, health, mana_pool):
        """Initialize elite card with both combat and magic attributes."""
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.defend_power = defend
        self.health = health
        self.mana_pool = mana_pool

    def play(self, game_state: dict = None) -> dict:
        """Trigger elite card deployment with dual-threat capabilities."""
        return {
            'card': self.name,
            'status': 'Elite unit deployed',
            'capabilities': ['Combat', 'Magic']
        }

    def attack(self, target) -> dict:
        """Execute an attack against a target and return the combat results."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        """Process incoming damage and update the card's health status."""
        actual_damage = max(0, incoming_damage - self.defend_power)
        self.health -= actual_damage
        return {
            'defender': self.name,
            'damage_taken': actual_damage,
            'damage_blocked': incoming_damage - actual_damage,
            'still_alive': self.health > 0
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Channel mana to cast a powerful spell on selected targets."""
        return {
            'caster': self.name,
            'spell': spell_name,
            'mana_used': self.cost,
            'targets': targets
        }

    def channel_mana(self, amount: int) -> dict:
        """Adjust the card's internal mana pool and return the status."""

        self.mana_pool = max(0, self.mana_pool + amount)
        return {
            'channeled': amount,
            'total_mana': self.mana_pool
        }

    def get_combat_stats(self) -> dict:
        """Return specialized combat statistics for this elite unit."""
        return {
            'power': self.attack_power,
            'defense': self.defend_power,
            'health': self.health
        }

    def get_magic_stats(self) -> dict:
        """Return specialized magic statistics including mana pool size."""
        return {
            'mana_pool': self.mana_pool,
            'spell_affinity': 'High'
        }
