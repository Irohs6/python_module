#!/usr/bin/env python3

def display_inventory(data: dict, player_name: str):
    print(f"=== {player_name.capitalize()}'s Inventory  ===")
    categories = {}
    if player_name in data["players"]:

        for item, quantite in data["players"][player_name]["items"].items():

            item_info = data["catalog"][item]
            item_type = item_info["type"]

            if item_type in categories:
                categories[item_type] += quantite
            else:
                categories[item_type] = quantite

            print(
                f"{item} "
                f"({data['catalog'][item]['type']}, "
                f"{data['catalog'][item]['rarity']}):"
                f" {quantite}x @ "
                f"{data['catalog'][item]['value']} gold each = "
                f"{quantite * data['catalog'][item]['value']} gold"
            )

        print("\n")

        print(
            f"Inventory value: "
            f"{data['players'][player_name]['total_value']} gold"
        )

        print(f"Item count: "
              f"{data['players'][player_name]['item_count']} items")
        print("Categories: ", end="")
        for key, value in categories.items():
            print(f"{key}({value}) ", end=", ")
        print("\n")


def trade(data, player_one, player_two, item, quantities):
    if player_one in data["players"]:
        if item in data["players"][player_one]["items"]:
            data["players"][player_one]["items"][item] -= quantities
            data["players"][player_one]["total_value"] -= (
                data["catalog"][item]["value"] * quantities
            )
            data["players"][player_one]["item_count"] -= quantities
        else:
            return "Do not item in the inventory"
    if player_two in data["players"]:
        if item in data["players"][player_two]["items"]:
            data["players"][player_two]["items"][item] += quantities
        else:
            data["players"][player_two]["items"][item] = quantities
    data["players"][player_two]["total_value"] += (
        data["catalog"][item]["value"] * quantities
    )
    data["players"][player_two]["item_count"] += quantities

    return (
        f"=== Transaction: {player_one.capitalize()} gives "
        f"{player_two.capitalize()} {quantities} {item} ===\n"
        "Transaction successful!\n"
        f"\n=== Updated Inventories ===\n"
        f"{player_one.capitalize()} {item}: "
        f"{data['players'][player_one]['items'][item]}\n"
        f"{player_two.capitalize()} {item}:"
        f" {data['players'][player_two]['items'][item]}\n"
    )


def stat_inventory(data: dict):
    most_value = 0
    most_item = 0
    name: str
    name_item: str
    all_item = set()
    for player_name, player_data in data["players"].items():
        value = player_data["total_value"]
        item_count = player_data["item_count"]
        if most_value < value:
            most_value = value
            name = player_name
        if most_item < item_count:
            most_item = item_count
            name_item = player_name
            for item in player_data["items"].keys():
                if (
                    data["catalog"][item]["rarity"] == "rare"
                    or data["catalog"][item]["rarity"] == "legendary"
                ):
                    all_item.add(item)
    return (
        f"=== Inventory Analytics ===\n"
        f"Most valuable player: {name.capitalize()} ({most_value} gold)\n"
        f"Most items: {name_item.capitalize()} ({most_item} items)\n"
        f"Rarest items: {all_item}"
    )


if __name__ == "__main__":

    data = {
        "players": {
            "alice": {
                "items": {
                    "pixel_sword": 1,
                    "code_bow": 1,
                    "health_byte": 1,
                    "quantum_ring": 3,
                },
                "total_value": 1875,
                "item_count": 6,
            },
            "bob": {
                "items": {"code_bow": 3, "pixel_sword": 2},
                "total_value": 900,
                "item_count": 5,
            },
            "charlie": {
                "items": {"pixel_sword": 1, "code_bow": 1},
                "total_value": 350,
                "item_count": 2,
            },
            "diana": {
                "items": {
                    "code_bow": 3,
                    "pixel_sword": 3,
                    "health_byte": 3,
                    "data_crystal": 3,
                },
                "total_value": 4125,
                "item_count": 12,
            },
        },
        "catalog": {
            "pixel_sword": {"type": "weapon", "value": 150, "rarity": "common"},
            "quantum_ring": {"type": "accessory", "value": 500, "rarity": "rare"},
            "health_byte": {"type": "consumable", "value": 25, "rarity": "common"},
            "data_crystal": {"type": "material", "value": 1000, "rarity": "legendary"},
            "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
        },
    }

    display_inventory(data, "alice")
    display_inventory(data, "bob")
    print(trade(data, "alice", "bob", "pixel_sword", 1))
    display_inventory(data, "alice")
    display_inventory(data, "bob")

    print(stat_inventory(data))
