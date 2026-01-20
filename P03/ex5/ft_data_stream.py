#!/usr/bin/env python3
"""
Exercise 5: Stream Wizard
Demonstrates generator usage for memory-efficient data streaming.
"""

import time


def game_event_stream(events: list[dict]):
    """Generator that yields game events one by one.

    Instead of returning all events at once, this generator yields
    them one at a time, enabling memory-efficient processing.

    Args:
        events: List of event dictionaries.

    Yields:
        dict: Individual event dictionary.
    """
    for event in events:
        yield event


def high_level_filter(events: list[dict], min_level: int = 10):
    """Generator that filters events for high-level players.

    Args:
        events: List of event dictionaries.
        min_level: Minimum player level to include (default: 10).

    Yields:
        dict: Event from a player with level >= min_level.
    """
    for event in events:
        if event["data"]["level"] >= min_level:
            yield event


def event_type_filter(events: list[dict], event_type: str):
    """Generator that filters events by type.

    Args:
        events: List of event dictionaries.
        event_type: Type of event to filter (e.g., 'kill', 'level_up').

    Yields:
        dict: Event matching the specified type.
    """
    for event in events:
        if event["event_type"] == event_type:
            yield event


def fibonacci_generator(n: int):
    """Generate the first n Fibonacci numbers.

    The Fibonacci sequence starts with 0, 1, and each subsequent
    number is the sum of the previous two: 0, 1, 1, 2, 3, 5, 8...

    Args:
        n: Number of Fibonacci numbers to generate.

    Yields:
        int: Next Fibonacci number in the sequence.
    """
    fibonacci_current: int = 0
    fibonacci_next: int = 1
    count: int = 0

    while count < n:
        yield fibonacci_current
        fibonacci_current, fibonacci_next = (
            fibonacci_next,
            fibonacci_current + fibonacci_next,
        )
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
    print("=== Game Data Stream Processor ===")
    print(f"Processing {len(events)} game events...\n")

    # Display first 3 events using generator
    count: int = 0
    for event in game_event_stream(events):
        count += 1
        if count <= 3:
            event_id: int = event["id"]
            player: str = event["player"]
            level: int = event["data"]["level"]
            event_type: str = event["event_type"]
            print(f"Event {event_id}: Player {player} " +
                  f"(level {level}) {event_type}")
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
        if event["data"]["level"] >= 10:
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
            "timestamp": "2024-01-01T23:17",
            "data": {"level": 16, "score_delta": 128, "zone": "pixel_zone_2"},
        },
        {
            "id": 2,
            "player": "frank",
            "event_type": "login",
            "timestamp": "2024-01-22T23:57",
            "data": {"level": 35, "score_delta": -11, "zone": "pixel_zone_5"},
        },
        {
            "id": 3,
            "player": "diana",
            "event_type": "login",
            "timestamp": "2024-01-01T02:13",
            "data": {"level": 15, "score_delta": 417, "zone": "pixel_zone_5"},
        },
        {
            "id": 4,
            "player": "alice",
            "event_type": "level_up",
            "timestamp": "2024-01-07T22:41",
            "data": {"level": 45, "score_delta": 458, "zone": "pixel_zone_4"},
        },
        {
            "id": 5,
            "player": "bob",
            "event_type": "death",
            "timestamp": "2024-01-19T08:51",
            "data": {"level": 1, "score_delta": 63, "zone": "pixel_zone_4"},
        },
        {
            "id": 6,
            "player": "charlie",
            "event_type": "kill",
            "timestamp": "2024-01-05T06:48",
            "data": {"level": 22, "score_delta": 4, "zone": "pixel_zone_1"},
        },
        {
            "id": 7,
            "player": "diana",
            "event_type": "login",
            "timestamp": "2024-01-12T11:38",
            "data": {"level": 17, "score_delta": -56, "zone": "pixel_zone_4"},
        },
        {
            "id": 8,
            "player": "eve",
            "event_type": "login",
            "timestamp": "2024-01-30T12:05",
            "data": {"level": 36, "score_delta": 200, "zone": "pixel_zone_5"},
        },
        {
            "id": 9,
            "player": "charlie",
            "event_type": "level_up",
            "timestamp": "2024-01-07T22:04",
            "data": {"level": 3, "score_delta": 133, "zone": "pixel_zone_3"},
        },
        {
            "id": 10,
            "player": "alice",
            "event_type": "logout",
            "timestamp": "2024-01-28T03:24",
            "data": {"level": 18, "score_delta": 364, "zone": "pixel_zone_3"},
        },
        {
            "id": 11,
            "player": "bob",
            "event_type": "kill",
            "timestamp": "2024-01-12T06:42",
            "data": {"level": 18, "score_delta": -27, "zone": "pixel_zone_5"},
        },
        {
            "id": 12,
            "player": "frank",
            "event_type": "logout",
            "timestamp": "2024-01-18T23:15",
            "data": {"level": 11, "score_delta": 373, "zone": "pixel_zone_4"},
        },
        {
            "id": 13,
            "player": "charlie",
            "event_type": "item_found",
            "timestamp": "2024-01-23T17:14",
            "data": {"level": 44, "score_delta": 232, "zone": "pixel_zone_1"},
        },
        {
            "id": 14,
            "player": "bob",
            "event_type": "login",
            "timestamp": "2024-01-26T10:25",
            "data": {"level": 18, "score_delta": -33, "zone": "pixel_zone_2"},
        },
        {
            "id": 15,
            "player": "eve",
            "event_type": "item_found",
            "timestamp": "2024-01-11T06:41",
            "data": {"level": 32, "score_delta": 305, "zone": "pixel_zone_4"},
        },
        {
            "id": 16,
            "player": "bob",
            "event_type": "kill",
            "timestamp": "2024-01-05T07:47",
            "data": {"level": 36, "score_delta": 451, "zone": "pixel_zone_3"},
        },
        {
            "id": 17,
            "player": "frank",
            "event_type": "level_up",
            "timestamp": "2024-01-14T18:25",
            "data": {"level": 24, "score_delta": 124, "zone": "pixel_zone_2"},
        },
        {
            "id": 18,
            "player": "eve",
            "event_type": "death",
            "timestamp": "2024-01-03T01:55",
            "data": {"level": 8, "score_delta": 56, "zone": "pixel_zone_2"},
        },
        {
            "id": 19,
            "player": "frank",
            "event_type": "death",
            "timestamp": "2024-01-20T02:24",
            "data": {"level": 25, "score_delta": 379, "zone": "pixel_zone_5"},
        },
        {
            "id": 20,
            "player": "charlie",
            "event_type": "level_up",
            "timestamp": "2024-01-28T00:43",
            "data": {"level": 47, "score_delta": 17, "zone": "pixel_zone_5"},
        },
        {
            "id": 21,
            "player": "charlie",
            "event_type": "item_found",
            "timestamp": "2024-01-11T03:18",
            "data": {"level": 28, "score_delta": 61, "zone": "pixel_zone_4"},
        },
        {
            "id": 22,
            "player": "alice",
            "event_type": "item_found",
            "timestamp": "2024-01-29T23:16",
            "data": {"level": 33, "score_delta": 82, "zone": "pixel_zone_5"},
        },
        {
            "id": 23,
            "player": "alice",
            "event_type": "item_found",
            "timestamp": "2024-01-10T20:32",
            "data": {"level": 39, "score_delta": 103, "zone": "pixel_zone_2"},
        },
        {
            "id": 24,
            "player": "charlie",
            "event_type": "logout",
            "timestamp": "2024-01-18T16:58",
            "data": {"level": 1, "score_delta": 231, "zone": "pixel_zone_4"},
        },
        {
            "id": 25,
            "player": "alice",
            "event_type": "login",
            "timestamp": "2024-01-30T11:56",
            "data": {"level": 20, "score_delta": 145, "zone": "pixel_zone_1"},
        },
        {
            "id": 26,
            "player": "bob",
            "event_type": "level_up",
            "timestamp": "2024-01-03T02:46",
            "data": {"level": 32, "score_delta": -30, "zone": "pixel_zone_5"},
        },
        {
            "id": 27,
            "player": "bob",
            "event_type": "logout",
            "timestamp": "2024-01-22T15:35",
            "data": {"level": 11, "score_delta": 171, "zone": "pixel_zone_5"},
        },
        {
            "id": 28,
            "player": "eve",
            "event_type": "death",
            "timestamp": "2024-01-07T17:48",
            "data": {"level": 47, "score_delta": 105, "zone": "pixel_zone_3"},
        },
        {
            "id": 29,
            "player": "diana",
            "event_type": "item_found",
            "timestamp": "2024-01-21T11:28",
            "data": {"level": 34, "score_delta": 362, "zone": "pixel_zone_1"},
        },
        {
            "id": 30,
            "player": "bob",
            "event_type": "logout",
            "timestamp": "2024-01-03T10:01",
            "data": {"level": 38, "score_delta": 467, "zone": "pixel_zone_2"},
        },
        {
            "id": 31,
            "player": "eve",
            "event_type": "logout",
            "timestamp": "2024-01-01T02:45",
            "data": {"level": 41, "score_delta": -40, "zone": "pixel_zone_2"},
        },
        {
            "id": 32,
            "player": "alice",
            "event_type": "login",
            "timestamp": "2024-01-28T10:04",
            "data": {"level": 33, "score_delta": 143, "zone": "pixel_zone_3"},
        },
        {
            "id": 33,
            "player": "frank",
            "event_type": "death",
            "timestamp": "2024-01-07T17:08",
            "data": {"level": 47, "score_delta": 484, "zone": "pixel_zone_5"},
        },
        {
            "id": 34,
            "player": "diana",
            "event_type": "logout",
            "timestamp": "2024-01-26T15:51",
            "data": {"level": 27, "score_delta": 94, "zone": "pixel_zone_1"},
        },
        {
            "id": 35,
            "player": "alice",
            "event_type": "item_found",
            "timestamp": "2024-01-14T11:27",
            "data": {"level": 27, "score_delta": 378, "zone": "pixel_zone_1"},
        },
        {
            "id": 36,
            "player": "frank",
            "event_type": "item_found",
            "timestamp": "2024-01-21T03:03",
            "data": {"level": 26, "score_delta": 247, "zone": "pixel_zone_1"},
        },
        {
            "id": 37,
            "player": "bob",
            "event_type": "logout",
            "timestamp": "2024-01-07T17:28",
            "data": {"level": 9, "score_delta": 332, "zone": "pixel_zone_2"},
        },
        {
            "id": 38,
            "player": "charlie",
            "event_type": "death",
            "timestamp": "2024-01-08T02:28",
            "data": {"level": 36, "score_delta": 0, "zone": "pixel_zone_1"},
        },
        {
            "id": 39,
            "player": "frank",
            "event_type": "level_up",
            "timestamp": "2024-01-27T00:05",
            "data": {"level": 49, "score_delta": 142, "zone": "pixel_zone_2"},
        },
        {
            "id": 40,
            "player": "diana",
            "event_type": "death",
            "timestamp": "2024-01-16T06:55",
            "data": {"level": 26, "score_delta": -40, "zone": "pixel_zone_2"},
        },
        {
            "id": 41,
            "player": "diana",
            "event_type": "login",
            "timestamp": "2024-01-13T08:59",
            "data": {"level": 30, "score_delta": 192, "zone": "pixel_zone_4"},
        },
        {
            "id": 42,
            "player": "frank",
            "event_type": "item_found",
            "timestamp": "2024-01-26T17:42",
            "data": {"level": 46, "score_delta": 398, "zone": "pixel_zone_2"},
        },
        {
            "id": 43,
            "player": "bob",
            "event_type": "kill",
            "timestamp": "2024-01-07T01:37",
            "data": {"level": 48, "score_delta": 455, "zone": "pixel_zone_1"},
        },
        {
            "id": 44,
            "player": "frank",
            "event_type": "kill",
            "timestamp": "2024-01-02T01:37",
            "data": {"level": 31, "score_delta": 414, "zone": "pixel_zone_5"},
        },
        {
            "id": 45,
            "player": "bob",
            "event_type": "login",
            "timestamp": "2024-01-17T02:54",
            "data": {"level": 12, "score_delta": -30, "zone": "pixel_zone_5"},
        },
        {
            "id": 46,
            "player": "alice",
            "event_type": "item_found",
            "timestamp": "2024-01-28T07:25",
            "data": {"level": 8, "score_delta": 483, "zone": "pixel_zone_2"},
        },
        {
            "id": 47,
            "player": "eve",
            "event_type": "level_up",
            "timestamp": "2024-01-02T19:05",
            "data": {"level": 27, "score_delta": 497, "zone": "pixel_zone_5"},
        },
        {
            "id": 48,
            "player": "eve",
            "event_type": "kill",
            "timestamp": "2024-01-30T08:13",
            "data": {"level": 43, "score_delta": 221, "zone": "pixel_zone_2"},
        },
        {
            "id": 49,
            "player": "charlie",
            "event_type": "death",
            "timestamp": "2024-01-05T21:41",
            "data": {"level": 20, "score_delta": 368, "zone": "pixel_zone_3"},
        },
        {
            "id": 50,
            "player": "alice",
            "event_type": "login",
            "timestamp": "2024-01-15T19:36",
            "data": {"level": 7, "score_delta": -25, "zone": "pixel_zone_5"},
        },
    ]

    start_time: float = time.time()
    process_events(data)
    end_time: float = time.time()

    print(f"\nProcessing time: {end_time - start_time:.3f} seconds")


if __name__ == "__main__":
    main()
