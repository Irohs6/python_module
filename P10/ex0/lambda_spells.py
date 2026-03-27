def artifact_sorter(artifact: list[dict]) -> list[dict]:
    return sorted(
        artifact, key=lambda artifact: artifact.get("power", 0), reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(
        filter(lambda mages: mages.get("power", 0) >= min_power, mages)
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages), 2
        ),
    }
    return powers


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

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for i in range(len(sorted_artifacts) - 1):
        print(
            f"{sorted_artifacts[i]['name']} "
            f"({sorted_artifacts[i]['power']} power) comes before "
            f"{sorted_artifacts[i+1]['name']} "
            f"({sorted_artifacts[i+1]['power']} power)"
        )
    print()

    print("Testing power filter (min 85)...")
    filtered = power_filter(mages, 85)
    for mage in filtered:
        print(f"{mage['name']} qualifies with {mage['power']} power")
    print()

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print()

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max power: {stats['max_power']}, Min power: {stats['min_power']}, "
        f"Avg power: {stats['avg_power']}"
    )


if __name__ == "__main__":
    main()
