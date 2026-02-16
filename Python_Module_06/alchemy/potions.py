from .elements import create_water
from .elements import create_air
from .elements import create_earth
from .elements import create_fire


def healing_potion():
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion():
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    return f"Invisibility potion brewed with {create_air()} \
and {create_water()}"


def wisdom_potion():
    return "Wisdom potion brewed with all elements: {}, {}, {},{}".format(
        create_air(), create_fire(), create_earth(), create_water())
