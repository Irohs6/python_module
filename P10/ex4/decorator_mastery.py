from functools import wraps
from time import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end - start:.4f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    pass


def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    @spell_timer
    def cast_spell(self, spell_name: str, power: int) -> str:
        print(f"{spell_name} and power : {power}")


if __name__ == "__main__":

    mages = [
        {"name": "Casey", "power": 99, "element": "earth"},
        {"name": "Morgan", "power": 92, "element": "water"},
        {"name": "Morgan", "power": 80, "element": "lightning"},
        {"name": "Phoenix", "power": 90, "element": "lightning"},
        {"name": "Alex", "power": 61, "element": "wind"},
    ]

    # Master's Tower Test Data
    test_powers = [18, 9, 27, 27]
    spell_names = ["tornado", "blizzard", "earthquake", "heal"]
    mage_names = ["Alex", "Sage", "Luna", "Morgan", "Phoenix", "Kai"]
    invalid_names = ["Jo", "A", "Alex123", "Test@Name"]

    morgan = MageGuild()
    print(morgan.cast_spell("tornado", 18))

