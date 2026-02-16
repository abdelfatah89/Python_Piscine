from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Factory for creating high-fantasy
    cards like Dragons and Fireballs."""
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Instantiate a fantasy Creature card
        with defined or default attributes."""
        if isinstance(name_or_power, str):
            return CreatureCard(name_or_power, 4, "Legendary", 5, 7)
        power = name_or_power if name_or_power is not None else 5
        return CreatureCard("Dragon", 4, "Legendary", power, 7)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Instantiate a fantasy Spell card with a magic effect."""
        if isinstance(name_or_power, str):
            return SpellCard(name_or_power,
                             5, "Rare", "Deal 3 damage to target")
        if name_or_power is not None:
            effect = name_or_power
        else:
            effect = "Deal 3 damage to target"
        return SpellCard("Fireball", 5, "Rare", effect)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Instantiate a fantasy Artifact card for utility or mana boost."""
        if isinstance(name_or_power, str):
            return ArtifactCard(name_or_power,
                                5, 7, 5, "Permanent: +1 mana per turn")
        if name_or_power is not None:
            effect = name_or_power
        else:
            effect = "Permanent: +1 mana per turn"
        return ArtifactCard("mana_ring", 5, 7, 5, effect)

    def create_themed_deck(self, size: int) -> dict:
        """Generate a balanced deck dictionary following a 60/20/20 ratio."""
        spell_count = int(size * 0.2)
        creature_count = int(size * 0.6)
        artifact_count = size - (spell_count + creature_count)
        spells = [self.create_spell() for i in range(spell_count)]
        creatures = [self.create_creature() for i in range(creature_count)]
        artifacts = [self.create_artifact() for i in range(artifact_count)]
        return {
            'deck_name': "Fantasy Theme Pack",
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'total_size': size
        }

    def get_supported_types(self) -> dict:
        """Return the categories of cards this factory supports."""
        return {
            "Creature": True,
            "Spell": True,
            "Artifact": True
        }
