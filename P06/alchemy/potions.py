def healing_potion() -> str:
    """Brew a healing potion using fire and water elements."""
    from .elements import create_fire, create_water

    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    """Brew a strength potion using earth and fire elements."""
    from .elements import create_earth, create_fire

    earth_result = create_earth()
    fire_result = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    """Brew an invisibility potion using air and water elements."""
    from .elements import create_air, create_water

    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    """Brew a wisdom potion using all four elements."""
    from .elements import create_fire, create_water, create_earth, create_air

    fire = create_fire()
    water = create_water()
    earth = create_earth()
    air = create_air()
    return (
        f"Wisdom potion brewed with all elements: {fire}, "
        f"{water}, {earth}, {air}"
    )
