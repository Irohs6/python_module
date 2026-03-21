
def artifact_sorter(artifact: list[dict]) -> list[dict]:
    return sorted(artifact, key=lambda artifact: artifact.get('power', 0),
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mages: mages.get('power', 0) >= min_power, mages)
                )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: '* ' + spell + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = [mage.get('power', 0) for mage in mages]
    power_total = sum(powers)
    len_total = len(powers)
    stats = {
        'max_power': (lambda power: max(power) if power else 0)(powers),
        'min_power': (lambda power: min(power) if power else 0)(powers),
        'avg_power': round(power_total / len_total, 2)
    }
    return stats


def main():
    # Lambda Sanctum Test Data
    artifacts = [
        {"name": "Shadow Blade", "power": 111, "type": "accessory"},
        {"name": "Storm Crown", "power": 87, "type": "relic"},
        {"name": "Ice Wand", "power": 61, "type": "focus"},
        {"name": "Shadow Blade", "power": 74, "type": "accessory"},
    ]
    mages = [
        {"name": "Morgan", "power": 92, "element": "ice"},
        {"name": "Kai", "power": 97, "element": "shadow"},
        {"name": "Storm", "power": 84, "element": "ice"},
        {"name": "Kai", "power": 65, "element": "light"},
        {"name": "Jordan", "power": 91, "element": "light"},
    ]
    spells = ["meteor", "tsunami", "lightning", "fireball"]

    print(artifact_sorter(artifacts))
    print()
    print(power_filter(mages, 85))
    print()
    print(spell_transformer(spells))
    print()
    print(mage_stats(mages))
    print(mage_stats.__getattribute__)


if __name__ == "__main__":
    main()
