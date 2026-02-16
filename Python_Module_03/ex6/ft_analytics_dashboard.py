def list_Comprehension(game_data: dict) -> None:
    """Uses list comprehensions to filter
    and transform gaming data"""
    print("\n=== List Comprehension Example ===")

    scores_doubled = list()

    high_scorers = [p for p, ts in game_data.get("players").items()
                    if ts.get("total_score") > 2000]

    all_session_scores = [s.get("score")
                          for s in game_data.get("sessions", [])]

    game_modes = [mode for mode in game_data.get("game_modes", [])]
    scores_doubled = {s for s in all_session_scores
                      if all_session_scores.count(s) > 1}

    print(f"High scores (>2000): {high_scorers}")
    if scores_doubled:
        print(f"Scores doubled: {list(scores_doubled)}")
    else:
        print("Scores doubled: No double score")
    print(f"Active players: {game_modes}")


def dict_Comprehension(game_data: dict) -> None:
    """Uses dict comprehensions for elegant data mapping"""
    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p: d.get("total_score")
                     for p, d in game_data.get("players", {}).items()}

    fav_modes = {p: d.get("favorite_mode")
                 for p, d in game_data.get("players", {}).items()}

    achievement_counts = {p: d.get("achievements_count")
                          for p, d in game_data.get("players", {}).items()}

    print(f"Player scores: {player_scores}")
    print(f"Players favorite mode: {fav_modes}")
    print(f"Achievement counts: {achievement_counts}")


def set_Comprehension(game_data: dict) -> None:
    """Uses set comprehensions to ensure unique data collection"""
    print("\n=== Set Comprehension Example ===")

    unique_players = {s.get("player") for s in game_data.get("sessions")}
    unique_achievements = {ach for ach in game_data.get("achievements")}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")


def combined_analysis(game_data: dict) -> None:
    """Combines all collection types for final aggregate insights"""
    print("\n=== Combined Analysis ===")

    total_players = 0

    scores = [game_data.get("players").get(p).get("total_score")
              for p in game_data.get("players")]

    players_scores = {p: game_data.get("players").get(p).get("total_score")
                      for p in game_data.get("players")}

    unique_achievement = {ach for ach in game_data.get("achievements")}

    for player in game_data.get("players"):
        total_players += 1

    ranked_list = sorted(players_scores.values())

    print(f"Total players: {total_players}")
    print(f"Total unique achievement: {len(unique_achievement)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(game_data.get("players")):.2f}")
    print(f"Score Ranking: {ranked_list}")


def game_analyse(game_data: dict) -> None:
    print("=== Game Analytics Dashboard ===")
    list_Comprehension(game_data)
    dict_Comprehension(game_data)
    set_Comprehension(game_data)
    combined_analysis(game_data)


if __name__ == "__main__":
    game_data = {
        'players': {
            'alice': {
                'level': 41, 'total_score': 2824, 'sessions_played': 13,
                'favorite_mode': 'ranked', 'achievements_count': 5
            },
            'bob': {
                'level': 16, 'total_score': 4657, 'sessions_played': 27,
                'favorite_mode': 'ranked', 'achievements_count': 2
            },
            'charlie': {
                'level': 44, 'total_score': 9935, 'sessions_played': 21,
                'favorite_mode': 'ranked', 'achievements_count': 7
            },
            'diana': {
                'level': 3, 'total_score': 1488, 'sessions_played': 21,
                'favorite_mode': 'casual', 'achievements_count': 4
            },
            'eve': {
                'level': 33, 'total_score': 1434, 'sessions_played': 81,
                'favorite_mode': 'casual', 'achievements_count': 7
            },
            'frank': {
                'level': 15, 'total_score': 8359, 'sessions_played': 85,
                'favorite_mode': 'competitive', 'achievements_count': 1
            }
        },
        'sessions': [
            {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
                'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
                'mode': 'casual', 'completed': True},
            {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
                'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
                'mode': 'ranked', 'completed': True},
            {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
                'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
                'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
                'mode': 'casual', 'completed': True},
            {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
                'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
                'mode': 'casual', 'completed': False},
            {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
                'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 98, 'score': 1102,
                'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 39, 'score': 2721,
                'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 46, 'score': 329,
                'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 56, 'score': 1196,
                'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 117, 'score': 1388,
                'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 118, 'score': 2733,
                'mode': 'competitive', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 22, 'score': 1110,
                'mode': 'ranked', 'completed': False},
            {'player': 'frank', 'duration_minutes': 79, 'score': 1854,
                'mode': 'ranked', 'completed': False},
            {'player': 'charlie', 'duration_minutes': 33, 'score': 666,
                'mode': 'ranked', 'completed': False},
            {'player': 'alice', 'duration_minutes': 101, 'score': 292,
                'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 25, 'score': 2887,
                'mode': 'competitive', 'completed': True},
            {'player': 'diana', 'duration_minutes': 53, 'score': 2540,
                'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 115, 'score': 147,
                'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 118, 'score': 2299,
                'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 42, 'score': 1880,
                'mode': 'casual', 'completed': False},
            {'player': 'alice', 'duration_minutes': 97, 'score': 1178,
                'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 18, 'score': 2661,
                'mode': 'competitive', 'completed': True},
            {'player': 'bob', 'duration_minutes': 52, 'score': 761,
                'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 46, 'score': 2101,
                'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
                'mode': 'casual', 'completed': True}
        ],
        'game_modes': ['casual', 'competitive', 'ranked'],
        'achievements': [
            'first_blood', 'level_master', 'speed_runner',
            'treasure_seeker', 'boss_hunter', 'pixel_perfect',
            'combo_king', 'explorer'
        ]
    }
    game_analyse(game_data)
