def display_players_achievements(players_achievements: dict) -> None:
    """Lists each player alongside their current set of earned achievements."""
    print("=== Achievement Tracker System ===\n")
    for key, value in players_achievements.items():
        player_achievements = set(value)
        print(f"Player {key} achievements:", player_achievements)
    print()


def unique_achievements(players_achievements: dict) -> None:
    """Identifies and counts every distinct achievement
    earned across the entire player base."""
    print("=== Achievement Analytics ===\n")

    list_achievements = []
    achievements_unique = set()

    for value in players_achievements.values():
        list_achievements.append(set(value))

    for item in list_achievements:
        achievements_unique = achievements_unique.union(item)

    print("All unique achievements: ", achievements_unique)
    print("Total unique achievements: ", len(achievements_unique))


def common_achievements(players_achievements: dict) -> None:
    """Finds and displays achievements that have been unlocked
    by every single player."""
    list_achievements = []
    for v in players_achievements.values():
        list_achievements.append(set(v))
    if not list_achievements:
        print("No players found.")
        return

    common = list_achievements[0]
    for player in list_achievements[1:]:
        common = common.intersection(player)

    if not common:
        print("No common Achievement!")
    else:
        print("Common to all players: ", common)


def rare_achievements(players_achievements: dict) -> None:
    """Extracts achievements held by only one individual
    player in the system."""
    total_rare = set()
    for player, player_achs in players_achievements.items():
        achievements = set()
        for key, value in players_achievements.items():
            if key != player:
                achievements = achievements.union(set(value))
        total_rare = total_rare.union(set(
            player_achs).difference(achievements))

    print("Rare achievements (1 player): ", total_rare)


def unique_achievements4player(players_achievements: dict, player_key) -> None:
    """Checks if a specific player possesses any
    achievements that no one else has."""
    target_set = set(players_achievements[player_key])
    other_set = set()

    for key, value in players_achievements.items():
        if key != player_key:
            other_set.update(value)

    unique = target_set.difference(other_set)
    if not unique:
        print(f"{player_key.capitalize()} don't have unique Achievement")
    else:
        print(f"{player_key.capitalize()} unique:", unique)


def common_between2(players_achievements, player_1, player_2) -> None:
    """Compares two players to find the shared achievements between them."""
    player_1achievements = set(players_achievements[player_1])
    player_2achievements = set(players_achievements[player_2])
    common = player_1achievements.intersection(player_2achievements)
    if not common:
        print("No common achievement between {} and {}".format(
            player_1.capitalize(), player_2.capitalize()))
    print("{} vs {} common: {}".format(
        player_1.capitalize(), player_2.capitalize(), common))


def ft_achievement_tracker(players_achievements) -> None:
    """Executes a full suite of achievement analysis and comparison reports."""
    display_players_achievements(players_achievements)
    print()
    unique_achievements(players_achievements)
    print()
    common_achievements(players_achievements)
    rare_achievements(players_achievements)
    print()
    common_between2(players_achievements, "alice", "bob")
    unique_achievements4player(players_achievements, "alice")
    unique_achievements4player(players_achievements, "bob")


if __name__ == "__main__":
    players_achievements = {
        'alice': ['level_10', 'first_blood', 'pixel_perfect', 'speed_runner',
                  'first_blood', 'first_blood'],
        'bob': ['level_10', 'level_master', 'boss_hunter', 'treasure_seeker',
                'level_master', 'level_master'],
        'charlie': ['level_10', 'treasure_seeker', 'boss_hunter', 'combo_king',
                    'first_blood', 'boss_hunter', 'first_blood',
                    'boss_hunter', 'first_blood'],
        'diana': ['level_10', 'first_blood', 'combo_king', 'level_master',
                  'treasure_seeker', 'speed_runner', 'combo_king',
                  'combo_king', 'level_master'],
        'eve': ['level_10', 'level_master', 'treasure_seeker', 'first_blood',
                'treasure_seeker', 'first_blood', 'treasure_seeker'],
        'frank': ['level_10', 'explorer', 'boss_hunter', 'first_blood',
                  'explorer', 'first_blood', 'boss_hunter']
    }
    ft_achievement_tracker(players_achievements)
