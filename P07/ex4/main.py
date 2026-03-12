#!/usr/bin/env python3

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    try:
        print("=== DataDeck Tournament Platform ===\n")

        platform = TournamentPlatform()

        dragon = TournamentCard("Fire Dragon", 6, "legendary", 8, 10, 1200)
        wizard = TournamentCard("Ice Wizard", 5, "epic", 7, 9, 1150)

        print("Registering Tournament Cards...\n")
        dragon_id = platform.register_card(dragon)
        wizard_id = platform.register_card(wizard)

        for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
            stats = card.get_tournament_stats()
            print(f"{card.name} (ID: {card_id}):")
            print(f"- Interfaces: {stats['interfaces']}")
            print(f"- Rating: {stats['rating']}")
            print(f"- Record: {stats['record']}\n")

        print("Creating tournament match...")
        result = platform.create_match(dragon_id, wizard_id)
        print(f"Match result: {result}")

        print("\nTournament Leaderboard:")
        for entry in platform.get_leaderboard():
            card = platform._cards[entry['card_id']]
            print(f"{entry['rank']}. {entry['name']} - "
                  f"Rating: {entry['rating']} "
                  f"({card.wins}-{card.losses})")

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())

        result = platform.create_match(dragon_id, wizard_id)
        print(f"Match result: {result}")
        
        print("\nTournament Leaderboard:")
        for entry in platform.get_leaderboard():
            card = platform._cards[entry['card_id']]
            print(f"{entry['rank']}. {entry['name']} - "
                  f"Rating: {entry['rating']} "
                  f"({card.wins}-{card.losses})")

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())
        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
