from functools import wraps
from time import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs:
            raise SyntaxError("please enter the parameter 'key=value'")
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end - start:.4f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:

    def decorator(spell: callable):
        @wraps(spell)
        def power(*args, **kwargs):
            if not kwargs:
                raise SyntaxError("please enter the parameter 'key=value'")
            power_value = kwargs.get("power", 0)
            if power_value <= min_power:
                return "Insufficient power for this spell"
            else:
                return spell(*args, **kwargs)

        return power

    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(spell: callable):
        @wraps(spell)
        def cast_spel(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return spell(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return cast_spel
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 3 and all(c.isalpha() or c == " " for c in name):
            return True
        else:
            return False

    @power_validator(10)
    @spell_timer
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"{spell_name} and power : {power}"


@retry_spell(3)
def risky_spell():
    raise ValueError("oops")


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
    try:
        print(morgan.cast_spell(spell_name="tornado", power=15))
    except SyntaxError as error:
        print(error)
    for name in zip(mage_names, invalid_names):
        print(morgan.validate_mage_name(name))
    risky_spell()
