#!/usr/bin/env python3


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
                or (
                    category == "medium"
                    and 2000 <= player_data["total_score"] <= 5000
                )
                or (category == "low" and player_data["total_score"] < 2000)
            )
        )
        for category in ["high", "medium", "low"]
    }
    print(f"Score categories: {score_categories}")

    # Compter les achievements par joueur
    achievement_counts: dict[str, int] = {
        player_name: len(player_data["achievements"])
        for player_name, player_data in data["players"].items()
    }
    print(f"Achievement counts: {achievement_counts}")


def demonstrate_set_comprehensions(data: dict) -> None:
    """Démontrer l'utilisation des set comprehensions."""
    print("=== Set Comprehension Examples ===")

    # Extraire tous les joueurs uniques
    unique_players: set[str] = {
        player_name for player_name in data["players"].keys()
    }
    print(f"Unique players: {unique_players}")

    # Tous les game modes uniques
    unique_achievements: set[str] = {
            achievement
            for player in data["players"].values()
            for achievement in player["achievements"]
        }
    print(f"Unique achievements: {unique_achievements}")

    # Joueurs ayant participé à des sessions
    active_session_players: set[str] = {
        session_data["player"] for session_data in data["sessions"]
    }
    print(f"Active session players: {active_session_players}")


def combined_analysis(data: dict) -> None:
    """Combiner plusieurs techniques pour une analyse complète."""
    print("=== Combined Analysis ===")

    # Nombre total de joueurs (set comprehension)
    total_players: int = len(
        {player_name for player_name in data["players"].keys()}
    )
    print(f"Total players: {total_players}")

    # Nombre total d'achievements uniques (direct access)
    total_achievements: int = len({
        achievement
        for player in data["players"].values()
        for achievement in player["achievements"]
    })
    print(f"Total unique achievements: {total_achievements}")

    # Score moyen (list comprehension + sum)
    all_scores: list[int] = [
        player_data["total_score"] for player_data in data["players"].values()
    ]
    average_score: float = (
        sum(all_scores) / len(all_scores) if all_scores else 0
    )
    print(f"Average score: {average_score:.1f}")
    # Top performer (dict comprehension + max)
    player_stats: dict[str, tuple[int, int]] = {
        player_name: (
            player_data["total_score"],
            len(player_data["achievements"]),
        )
        for player_name, player_data in data["players"].items()
    }
    top_score: int = max(
        player_stats[player_name][0]
        for player_name in player_stats.keys()
    )
    top_player_name = next(
        player_name
        for player_name in player_stats
        if player_stats[player_name][0] == top_score
    )
    top_score, top_achievements = player_stats[top_player_name]
    print(
        f"Top performer: {top_player_name} "
        f"({top_score} points, {top_achievements} achievements)"
    )


def main():
    data = {
        "players": {
            "alice":
                {
                    "level": 41,
                    "total_score": 2824,
                    "sessions_played": 13,
                    "favorite_mode": "ranked",
                    "achievements":
                    [
                        "first_blood",
                        "level_master",
                        "speed_runner",
                        "boss_hunter",
                        "pixel_perfect",
                    ],
                },
            "bob":
                {
                    "level": 16,
                    "total_score": 4657,
                    "sessions_played": 27,
                    "favorite_mode": "ranked",
                    "achievements":
                    [
                        "first_blood",
                        "combo_king",
                        "explorer",
                    ],
                },
            "charlie":
                {
                    "level": 44,
                    "total_score": 9935,
                    "sessions_played": 21,
                    "favorite_mode": "ranked",
                    "achievements":
                    [
                        "first_blood",
                        "level_master",
                        "speed_runner",
                        "treasure_seeker",
                        "boss_hunter",
                        "pixel_perfect",
                        "combo_king",
                        "explorer",
                    ],
                },
            "diana":
                {
                    "level": 3,
                    "total_score": 1488,
                    "sessions_played": 21,
                    "favorite_mode": "casual",
                    "achievements":
                    [
                        "first_blood",
                        "level_master",
                        "speed_runner",
                        "combo_king",
                        "explorer",
                    ],
                },
            "eve":
                {
                    "level": 33,
                    "total_score": 1434,
                    "sessions_played": 81,
                    "favorite_mode": "casual",
                    "achievements_count": 7,
                    "achievements":
                    [
                        "first_blood",
                        "level_master",
                        "speed_runner",
                        "treasure_seeker",
                        "boss_hunter",
                        "pixel_perfect",
                        "combo_king",
                        "explorer",
                    ],
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
