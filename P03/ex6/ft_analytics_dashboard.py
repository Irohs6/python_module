#!/usr/bin/env python3
"""
Exercise 6: Data Alchemist - Analytics Dashboard

Objectif: Démontrer la maîtrise des COMPREHENSIONS Python
pour transformer et analyser des données.

Concepts:
- LIST COMPREHENSIONS: Filtrage et transformation
- DICT COMPREHENSIONS: Création de mappings et groupements
- SET COMPREHENSIONS: Extraction de valeurs uniques
"""


def demonstrate_list_comprehensions(data: dict) -> None:
    """Démontrer l'utilisation des list comprehensions."""
    # Filtrer les joueurs avec score > 2000
    high_scorers: list[str] = [
        player_name
        for player_name, player_data in data["players"].items()
        if player_data["total_score"] > 2000
    ]

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")

    # Doubler les scores des high scorers
    scores_doubled: list[int] = [
        player_data["total_score"] * 2
        for player_data in data["players"].values()
        if player_data["total_score"] > 2000
    ]
    print(f"Scores doubled: {scores_doubled}")

    # Joueurs actifs (avec beaucoup de sessions)
    active_players: list[str] = [
        player_name
        for player_name, player_data in data["players"].items()
        if player_data["sessions_played"] > 20
    ]
    print(f"Active players: {active_players}")


def demonstrate_dict_comprehensions(data: dict) -> None:
    """Démontrer l'utilisation des dict comprehensions."""
    print("=== Dict Comprehension Examples ===")

    # Mapping joueur -> score total
    player_scores: dict[str, int] = {
        player_name: player_data["total_score"]
        for player_name, player_data in data["players"].items()
    }
    print(f"Player scores: {player_scores}")

    # Grouper par catégories de score
    score_categories: dict[str, int] = {
        category: sum(
            1
            for player_data in data["players"].values()
            if (
                (category == "high" and player_data["total_score"] > 5000)
                or (category == "medium" and 2000 <= player_data["total_score"] <= 5000)
                or (category == "low" and player_data["total_score"] < 2000)
            )
        )
        for category in ["high", "medium", "low"]
    }
    print(f"Score categories: {score_categories}")

    # Compter les achievements par joueur
    achievement_counts: dict[str, int] = {
        player_name: player_data["achievements_count"]
        for player_name, player_data in data["players"].items()
    }
    print(f"Achievement counts: {achievement_counts}")


def demonstrate_set_comprehensions(data: dict) -> None:
    """Démontrer l'utilisation des set comprehensions."""
    print("=== Set Comprehension Examples ===")

    # Extraire tous les joueurs uniques
    unique_players: set[str] = {player_name for player_name in data["players"].keys()}
    print(f"Unique players: {unique_players}")

    # Tous les game modes uniques
    unique_modes: set[str] = {game_mode for game_mode in data["game_modes"]}
    print(f"Unique game modes: {unique_modes}")

    # Joueurs ayant participé à des sessions
    active_session_players: set[str] = {
        session_data["player"] for session_data in data["sessions"]
    }
    print(f"Active session players: {active_session_players}")


def combined_analysis(data: dict) -> None:
    """Combiner plusieurs techniques pour une analyse complète."""
    print("=== Combined Analysis ===")

    # Nombre total de joueurs (set comprehension)
    total_players: int = len({player_name for player_name in data["players"].keys()})
    print(f"Total players: {total_players}")

    # Nombre total d'achievements uniques (direct access)
    total_achievements: int = len(data["achievements"])
    print(f"Total unique achievements: {total_achievements}")

    # Score moyen (list comprehension + sum)
    all_scores: list[int] = [
        player_data["total_score"] for player_data in data["players"].values()
    ]
    average_score: float = sum(all_scores) / len(all_scores) if all_scores else 0
    print(f"Average score: {average_score:.1f}")

    # Top performer (dict comprehension + max)
    player_stats: dict[str, tuple[int, int]] = {
        player_name: (
            player_data["total_score"],
            player_data["achievements_count"],
        )
        for player_name, player_data in data["players"].items()
    }
    top_player_name: str = max(
        player_stats.keys(),
        key=lambda player_name: player_stats[player_name][0],
    )
    top_score, top_achievements = player_stats[top_player_name]
    print(
        f"Top performer: {top_player_name} "
        f"({top_score} points, {top_achievements} achievements)"
    )


def main():
    data = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 32,
                "score": 1478,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 17,
                "score": 1570,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 15,
                "score": 2361,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 34,
                "score": 1285,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "alice",
                "duration_minutes": 53,
                "score": 1238,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 1555,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 92,
                "score": 2754,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 98,
                "score": 1102,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 39,
                "score": 2721,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 46,
                "score": 329,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 117,
                "score": 1388,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 22,
                "score": 1110,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 79,
                "score": 1854,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "charlie",
                "duration_minutes": 33,
                "score": 666,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 101,
                "score": 292,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 53,
                "score": 2540,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 115,
                "score": 147,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 118,
                "score": 2299,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 42,
                "score": 1880,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 97,
                "score": 1178,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 18,
                "score": 2661,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 46,
                "score": 2101,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
        ],
    }
    print("=== Game Analytics Dashboard ===\n")

    demonstrate_list_comprehensions(data)
    print()

    demonstrate_dict_comprehensions(data)
    print()

    demonstrate_set_comprehensions(data)
    print()

    combined_analysis(data)


if __name__ == "__main__":
    main()
