#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    import alchemy.elements
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())

    print("\nMethod 2 - Specific function import:")
    from alchemy.elements import create_water
    print("create_water():", create_water())

    print("\nMethod 3 - Aliased import:")
    from alchemy.potions import healing_potion as heal
    print("heal():", heal())

    print("\nMethod 4 - Multiple imports:")
    from alchemy.elements import create_fire, create_air
    print("create_fire():", create_fire())
    print("create_air():", create_air())
    from alchemy.potions import wisdom_potion as wis
    print("\nwisdom_potion():", wis())

    print("\nAll import transmutation methods mastered!")
