#!/usr/bin/env python3

if __name__ == "__main__":
    alice_success: set[str] = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    }

    bob_success: set[str] = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }

    charlie_success: set[str] = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }
    all_success: set[str] = alice_success.union(bob_success, charlie_success)

    common: set[str] = alice_success.intersection(bob_success, charlie_success)

    diff_alice = alice_success.difference(bob_success, charlie_success)

    diff_bob = bob_success.difference(alice_success, charlie_success)

    diff_charlie = charlie_success.difference(bob_success, alice_success)

    rare: set[str] = diff_alice.union(diff_bob, diff_charlie)

    print("=== Achievement Tracker System ===\n")

    print(f"Player alice achievements: {alice_success}")
    print(f"Player bob achievements: {bob_success}")
    print(f"Player charlie achievements: {charlie_success}\n")

    print("=== Achievement Analytics ===")
    print(f"All unique achivements: " f"{all_success}")
    print(f"Total unique achievements: " f"{len(all_success)}\n")

    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice_success.intersection(bob_success)}")
    print(f"Alice unique: {alice_success.difference(bob_success)}")
    print(f"Bob unique: {bob_success.difference(alice_success)}")

    data = {
        "alice": [
            "first_blood",
            "pixel_perfect",
            "speed_runner",
            "first_blood",
            "first_blood",
        ],
        "bob": [
            "level_master",
            "boss_hunter",
            "treasure_seeker",
            "level_master",
            "level_master",
        ],
        "charlie": [
            "treasure_seeker",
            "boss_hunter",
            "combo_king",
            "first_blood",
            "boss_hunter",
            "first_blood",
            "boss_hunter",
            "first_blood",
        ],
        "diana": [
            "first_blood",
            "combo_king",
            "level_master",
            "treasure_seeker",
            "speed_runner",
            "combo_king",
            "combo_king",
            "level_master",
        ],
        "eve": [
            "level_master",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
        ],
        "frank": [
            "explorer",
            "boss_hunter",
            "first_blood",
            "explorer",
            "first_blood",
            "boss_hunter",
        ],
    }
