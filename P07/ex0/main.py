#!/usr/bin/env python3
from tools.card_generator import CardGenerator
from .CreatureCard import CreatureCard


def main():

    generator = CardGenerator()
    creature = generator.get_random_creature()
    dragon = CreatureCard(**creature)
    print(dragon.get_card_info())


if __name__ == "__main__":
    main()
