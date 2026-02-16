from .basic import lead_to_gold as ltg
from ..potions import healing_potion as hp


def philosophers_stone():
    return f"Philosopher’s stone created using {ltg()} and {hp()}"


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
