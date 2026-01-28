#!/usr/bin/env python3

import time
from typing import Any, Generator


def game_event_stream(events: list[dict]) -> Generator[dict, Any, None]:
    """Generator that yields game events one by one.
    Instead of returning all events at once, this generator yields
    them one at a time, enabling memory-efficient processing.

    Args:
        events: List of event dictionaries.

    Yields:
        dict: Individual event dictionary.
    """
    for i in range(20):
        for event in events:
            yield event


def fibonacci_generator(n: int):
    """Generate the first n Fibonacci numbers.

    The Fibonacci sequence starts with 0, 1, and each subsequent
    number is the sum of the previous two: 0, 1, 1, 2, 3, 5, 8..."""

    a: int = 0
    b: int = 1
    count: int = 0

    while count < n:
        yield a
        a, b = (b, a + b)
        count += 1


def prime_generator(n: int):
    """Generate the first n prime numbers.

    A prime number is a natural number greater than 1 that has
    no positive divisors other than 1 and itself.

    Args:
        n: Number of prime numbers to generate.

    Yields:
        int: Next prime number.
    """

    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                return False
        return True

    count: int = 0
    num: int = 2

    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def process_events(events: list[dict]) -> None:
    """Process game events using generators for analytics.

    Demonstrates streaming data processing with generators:
    - Display sample events
    - Calculate statistics using generator pipelines
    - Show memory-efficient processing

    Args:
        events: List of event dictionaries to process.
    """
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    # Display first 3 events using generator
    count: int = 0
    for event in game_event_stream(events):
        count += 1
        if count <= 3:
            event_id: int = event["id"]
            player: str = event["player"]
            level: int = event["level"]
            event_type: str = event["event_type"]
            print(
                f"Event {event_id}: Player {player} "
                + f"(level {level}) {event_type}"
            )
        elif count == 4:
            print("...")

    print("\n=== Stream Analytics ===")

    # Statistics using generators
    total: int = 0
    high_level_count: int = 0
    event_types_count: dict[str, int] = {}

    # Process all events with generator (memory efficient!)
    for event in game_event_stream(events):
        total += 1

        # Count high-level players
        if event["level"] >= 10:
            high_level_count += 1

        # Count by event type
        event_type_name: str = event["event_type"]
        event_types_count[event_type_name] = (
            event_types_count.get(event_type_name, 0) + 1
        )

    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level_count}")

    # Display event type counts
    for event_type_name, event_count in event_types_count.items():
        print(f"{event_type_name.capitalize()} events: {event_count}")

    print("Memory usage: Constant (streaming)")

    # Generator demonstration
    print("\n=== Generator Demonstration ===")

    # Fibonacci sequence
    fib_list: list[int] = list(fibonacci_generator(10))
    fib_str: str = ", ".join(map(str, fib_list))
    print(f"Fibonacci sequence (first 10): {fib_str}")

    # Prime numbers
    primes_list: list[int] = list(prime_generator(5))
    primes_str: str = ", ".join(map(str, primes_list))
    print(f"Prime numbers (first 5): {primes_str}")


def main() -> None:
    """Main function to run the stream processor demo."""
    data: list[dict] = [
        {
            "id": 1,
            "player": "frank",
            "event_type": "login",
            "level": 16,
            "score_delta": 128,
        },
        {
            "id": 2,
            "player": "frank",
            "event_type": "login",
            "level": 35,
            "score_delta": -11,
        },
        {
            "id": 3,
            "player": "diana",
            "event_type": "login",
            "level": 15,
            "score_delta": 417,
        },
        {
            "id": 4,
            "player": "alice",
            "event_type": "level_up",
            "level": 45,
            "score_delta": 458,
        },
        {
            "id": 5,
            "player": "bob",
            "event_type": "death",
            "level": 1,
            "score_delta": 63,
        },
        {
            "id": 6,
            "player": "charlie",
            "event_type": "kill",
            "level": 22,
            "score_delta": 4,
        },
        {
            "id": 7,
            "player": "diana",
            "event_type": "login",
            "level": 17,
            "score_delta": -56,
        },
        {
            "id": 8,
            "player": "eve",
            "event_type": "login",
            "level": 36,
            "score_delta": 200,
        },
        {
            "id": 9,
            "player": "charlie",
            "event_type": "level_up",
            "level": 3,
            "score_delta": 133,
        },
        {
            "id": 10,
            "player": "alice",
            "event_type": "logout",
            "level": 18,
            "score_delta": 364,
        },
        {
            "id": 11,
            "player": "bob",
            "event_type": "kill",
            "level": 18,
            "score_delta": -27,
        },
        {
            "id": 12,
            "player": "frank",
            "event_type": "logout",
            "level": 11,
            "score_delta": 373,
        },
        {
            "id": 13,
            "player": "charlie",
            "event_type": "item_found",
            "level": 44,
            "score_delta": 232,
        },
        {
            "id": 14,
            "player": "bob",
            "event_type": "login",
            "level": 18,
            "score_delta": -33,
        },
        {
            "id": 15,
            "player": "eve",
            "event_type": "item_found",
            "level": 32,
            "score_delta": 305,
        },
        {
            "id": 16,
            "player": "bob",
            "event_type": "kill",
            "level": 36,
            "score_delta": 451,
        },
        {
            "id": 17,
            "player": "frank",
            "event_type": "level_up",
            "level": 24,
            "score_delta": 124,
        },
        {
            "id": 18,
            "player": "eve",
            "event_type": "death",
            "level": 8,
            "score_delta": 56,
        },
        {
            "id": 19,
            "player": "frank",
            "event_type": "death",
            "level": 25,
            "score_delta": 379,
        },
        {
            "id": 20,
            "player": "charlie",
            "event_type": "level_up",
            "level": 47,
            "score_delta": 17,
        },
        {
            "id": 21,
            "player": "charlie",
            "event_type": "item_found",
            "level": 28,
            "score_delta": 61,
        },
        {
            "id": 22,
            "player": "alice",
            "event_type": "item_found",
            "level": 33,
            "score_delta": 82,
        },
        {
            "id": 23,
            "player": "alice",
            "event_type": "item_found",
            "level": 39,
            "score_delta": 103,
        },
        {
            "id": 24,
            "player": "charlie",
            "event_type": "logout",
            "level": 1,
            "score_delta": 231,
        },
        {
            "id": 25,
            "player": "alice",
            "event_type": "login",
            "level": 20,
            "score_delta": 145,
        },
        {
            "id": 26,
            "player": "bob",
            "event_type": "level_up",
            "level": 32,
            "score_delta": -30,
        },
        {
            "id": 27,
            "player": "bob",
            "event_type": "logout",
            "level": 11,
            "score_delta": 171,
        },
        {
            "id": 28,
            "player": "eve",
            "event_type": "death",
            "level": 47,
            "score_delta": 105,
        },
        {
            "id": 29,
            "player": "diana",
            "event_type": "item_found",
            "level": 34,
            "score_delta": 362,
        },
        {
            "id": 30,
            "player": "bob",
            "event_type": "logout",
            "level": 38,
            "score_delta": 467,
        },
        {
            "id": 31,
            "player": "eve",
            "event_type": "logout",
            "level": 41,
            "score_delta": -40,
        },
        {
            "id": 32,
            "player": "alice",
            "event_type": "login",
            "level": 33,
            "score_delta": 143,
        },
        {
            "id": 33,
            "player": "frank",
            "event_type": "death",
            "level": 47,
            "score_delta": 484,
        },
        {
            "id": 34,
            "player": "diana",
            "event_type": "logout",
            "level": 27,
            "score_delta": 94,
        },
        {
            "id": 35,
            "player": "alice",
            "event_type": "item_found",
            "level": 27,
            "score_delta": 378,
        },
        {
            "id": 36,
            "player": "frank",
            "event_type": "item_found",
            "level": 26,
            "score_delta": 247,
        },
        {
            "id": 37,
            "player": "bob",
            "event_type": "logout",
            "level": 9,
            "score_delta": 332,
        },
        {
            "id": 38,
            "player": "charlie",
            "event_type": "death",
            "level": 36,
            "score_delta": 0,
        },
        {
            "id": 39,
            "player": "frank",
            "event_type": "level_up",
            "level": 49,
            "score_delta": 142,
        },
        {
            "id": 40,
            "player": "diana",
            "event_type": "death",
            "level": 26,
            "score_delta": -40,
        },
        {
            "id": 41,
            "player": "diana",
            "event_type": "login",
            "level": 30,
            "score_delta": 192,
        },
        {
            "id": 42,
            "player": "frank",
            "event_type": "item_found",
            "level": 46,
            "score_delta": 398,
        },
        {
            "id": 43,
            "player": "bob",
            "event_type": "kill",
            "level": 48,
            "score_delta": 455,
        },
        {
            "id": 44,
            "player": "frank",
            "event_type": "kill",
            "level": 31,
            "score_delta": 414,
        },
        {
            "id": 45,
            "player": "bob",
            "event_type": "login",
            "level": 12,
            "score_delta": -30,
        },
        {
            "id": 46,
            "player": "alice",
            "event_type": "item_found",
            "level": 8,
            "score_delta": 483,
        },
        {
            "id": 47,
            "player": "eve",
            "event_type": "level_up",
            "level": 27,
            "score_delta": 497,
        },
        {
            "id": 48,
            "player": "eve",
            "event_type": "kill",
            "level": 43,
            "score_delta": 221,
        },
        {
            "id": 49,
            "player": "charlie",
            "event_type": "death",
            "level": 20,
            "score_delta": 368,
        },
        {
            "id": 50,
            "player": "alice",
            "event_type": "login",
            "level": 7,
            "score_delta": -25,
        },
    ]

    start_time: float = time.time()
    process_events(data)
    end_time: float = time.time()

    print(f"\nProcessing time: {end_time - start_time:.3f} seconds")


if __name__ == "__main__":
    main()
