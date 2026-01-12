#!/usr/bin/env python3

if __name__ == "__main__":
    alice_achivement = {'first_kill', 'level_10', 'treasure_hunter',
                        'speed_demon'}

    bob_achivement = {'first_kill', 'level_10', 'boss_slayer', 'collector'}

    charlie_achivement = {'level_10', 'treasure_hunter', 'boss_slayer',
                          'speed_demon', 'perfectionist'}

    print("=== Achievement Analytics ===")
    print(f"All unique achivement: "
          f"{alice_achivement | bob_achivement | charlie_achivement}")
    print(f"Total unique achivement: "
          f"{len(alice_achivement | bob_achivement | charlie_achivement)}")
    
    print(f"Common to all players: "
          f"{alice_achivement & bob_achivement & charlie_achivement}")
    print(alice_achivement - bob_achivement - charlie_achivement)