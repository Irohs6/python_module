def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    cap_seed_type = seed_type.capitalize()
    if unit == "grams":
        msg = f"{cap_seed_type} seeds: {quantity} grams total"
    elif unit == "packets":
        msg = f"{cap_seed_type} seeds: {quantity} packets available"
    elif unit == "area":
        msg = f"{cap_seed_type} seeds: covers {quantity} square meters"
    else:
        msg = "Unknown unit type"
    print(msg)
