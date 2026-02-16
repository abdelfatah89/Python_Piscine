from alchemy.elements import create_fire as cf
from alchemy.elements import create_earth as ce


def lead_to_gold():
    return f"Lead transmuted to gold using {cf()}"


def stone_to_gem():
    return f"Stone transmuted to gem using {ce()}"
