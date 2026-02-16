from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmute lead to gold using fire (absolute import)."""
    fire_result = create_fire()
    return f"Lead transmuted to gold using {fire_result}"


def stone_to_gem() -> str:
    """Transmute stone to gem using earth (absolute import)."""
    earth_result = create_earth()
    return f"Stone transmuted to gem using {earth_result}"
