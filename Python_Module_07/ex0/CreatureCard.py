from ex0.Card import Card


class CreatureCard(Card):
    """A concrete implementation of Card representing
    a creature with combat stats."""
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        """Initialize creature with name, cost, rarity,
        attack, and health points."""
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        """Return basic card info updated with creature-specific stats."""
        info = super().get_card_info()
        info.update({
            'type': "Creature",
            'attack': self.attack,
            'health': self.health
        })
        return info

    def play(self, game_state: dict = None) -> dict:
        """Return a summary of the creature being summoned to the field."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        """Execute an attack against a target and return the combat results."""
        return {
            'Card played': self.name,
            "target": target,
            'damage_dealt': self.attack,
            "combat_resolved": True
        }
