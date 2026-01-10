#!/usr/bin/env python3

import sys


def process_command_line():
    """Process command line arguments and display them."""
    print("=== Command Quest ===")
    args = sys.argv
    program_name = args[0]
    arguments = args[1:]

    print(f"Program name: {program_name}")
    if arguments:
        print(f"Arguments received: {len(arguments)}")
        for i, arg in enumerate(arguments, 1):
            print(f"Argument {i}: {arg}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    process_command_line()
