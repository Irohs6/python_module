#!/usr/bin/env python3
"""
Data Quest: Exercise 5 - Stream Wizard
Using generators with 'yield' keyword for memory-efficient data streams.
Authorized functions: next(), iter(), range(), len(), print()
"""

import time
import random


# Seed for reproducible random events
random.seed(42)


# ============================================================================
# PART 1: Game Event Generator (Memory-Efficient Streaming)
# ============================================================================


def generate_game_events(count=1000):
    """
    Generator that yields game events one by one.
    Memory-efficient: creates events on-demand instead of storing all in memory.
    """
    players = ['alice', 'bob', 'charlie', 'diana', 'eve', 'frank']
    event_types = ['killed monster', 'found treasure', 'leveled up', 
                   'died', 'discovered area', 'completed quest']
    
    for event_id in range(1, count + 1):
        event = {
            'id': event_id,
            'player': random.choice(players),
            'level': random.randint(1, 20),
            'event_type': random.choice(event_types)
        }
        yield event


def high_level_players_stream(events, min_level=10):
    """
    Generator that filters high-level player events.
    Only yields events where player level >= min_level.
    """
    for event in events:
        if event['level'] >= min_level:
            yield event


def filter_by_event_type(events, event_type):
    """
    Generator that filters events by type.
    Yields only events matching the specified event_type.
    """
    for event in events:
        if event_type in event['event_type']:
            yield event


# ============================================================================
# PART 2: Classic Generator Examples
# ============================================================================


def fibonacci_generator(n):
    """
    Generator for Fibonacci sequence.
    Yields first n Fibonacci numbers without storing them all.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(n):
    """
    Generator for prime numbers.
    Yields first n prime numbers on-demand.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


# ============================================================================
# PART 3: Stream Processing Functions
# ============================================================================


def process_events_streaming(count=1000):
    """
    Process events using streaming (generator).
    Memory-efficient: processes one event at a time.
    """
    print(f"Processing {count} game events...")
    
    # Generate events on-demand
    events = generate_game_events(count)
    
    # Display first 3 events as examples
    example_count = 0
    stats = {
        'total': 0,
        'high_level': 0,
        'treasure': 0,
        'level_up': 0
    }
    
    for event in events:
        stats['total'] += 1
        
        # Show first 3 events
        if example_count < 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['event_type']}")
            example_count += 1
        elif example_count == 3:
            print("...")
            example_count += 1
        
        # Collect statistics while streaming
        if event['level'] >= 10:
            stats['high_level'] += 1
        if 'treasure' in event['event_type']:
            stats['treasure'] += 1
        if 'leveled up' in event['event_type']:
            stats['level_up'] += 1
    
    return stats


def demonstrate_memory_difference():
    """
    Demonstrate the difference between storing all vs streaming.
    """
    print("\n=== Memory Efficiency Demonstration ===\n")
    
    # Method 1: Store everything (memory-intensive)
    print("Method 1: Store All Events (Memory-Intensive)")
    print("Creating list with 1000 events...")
    all_events = list(generate_game_events(1000))
    print(f"Memory: Stored {len(all_events)} events in list")
    print(f"Each event takes memory space")
    
    # Method 2: Stream with generator (memory-efficient)
    print("\nMethod 2: Stream Events (Memory-Efficient)")
    print("Using generator to process events...")
    event_stream = generate_game_events(1000)
    print("Memory: Only current event in memory")
    print("Previous events discarded after processing")
    
    # Process stream
    processed = 0
    for _ in event_stream:
        processed += 1
    print(f"Processed {processed} events with minimal memory")


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================


def main():
    """Demonstrate stream processing with generators."""
    print("=== Game Data Stream Processor ===\n")
    
    # Start timing
    start_time = time.time()
    
    # Process events using streaming
    stats = process_events_streaming(1000)
    
    # Calculate processing time
    processing_time = time.time() - start_time
    
    # Display analytics
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['level_up']}")
    print(f"Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")
    
    # Generator demonstrations
    print("\n=== Generator Demonstration ===")
    
    # Fibonacci generator
    fib_gen = fibonacci_generator(10)
    fib_numbers = [str(num) for num in fib_gen]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_numbers)}")
    
    # Prime generator
    prime_gen = prime_generator(5)
    prime_numbers = [str(num) for num in prime_gen]
    print(f"Prime numbers (first 5): {', '.join(prime_numbers)}")
    
    # Memory difference demonstration
    demonstrate_memory_difference()
    
    # Answer the question
    print("\n=== Understanding Generators ===")
    print("\nHow do generators enable memory-efficient processing?")
    print("• Generators create values on-demand using 'yield'")
    print("• Only one value exists in memory at a time")
    print("• Previous values are discarded after use")
    print("• Perfect for processing large datasets")
    
    print("\nWhat makes for-in loops perfect for streaming data?")
    print("• for-in loops automatically call next() on iterators")
    print("• They process one item at a time")
    print("• No need to load entire dataset into memory")
    print("• Natural fit for generator functions")


if __name__ == "__main__":
    main()
