#!/usr/bin/env python3

if __name__ == "__main__":
    alice_success = {'first_kill', 'level_10', 'treasure_hunter',
                     'speed_demon'}

    bob_success = {'first_kill', 'level_10', 'boss_slayer', 'collector'}

    charlie_success = {'level_10', 'treasure_hunter', 'boss_slayer',
                       'speed_demon', 'perfectionist'}

    all_success = alice_success.union(bob_success.union(charlie_success))
    common = alice_success.intersection
    (bob_success.intersection(charlie_success))
    rare = alice_success.symmetric_difference(
        bob_success.symmetric_difference(charlie_success))
    rare = rare.symmetric_difference(common)
    print("=== Achievement Tracker System ===\n")

    print(f"Player alice achievements: {alice_success}")
    print(f"Player bob achievements: {bob_success}")
    print(f"Player charlie achievements: {charlie_success}\n")

    print("=== Achievement Analytics ===")
    print(f"All unique achivements: "
          f"{all_success}")
    print(f"Total unique achievements: "
          f"{len(all_success)}\n")

    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice_success.intersection(bob_success)}")
    print(f"Alice unique: {alice_success.difference(bob_success)}")
    print(f"Bob unique: {bob_success.difference(alice_success)}")
