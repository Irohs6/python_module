#!/usr/bin/env python3

import sys


def main() -> None:
    """Reads archivist input and writes messages to stdout and stderr."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    arch_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {status}\n")

    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )

    sys.stdout.write("[STANDARD] Data transmission complete\n\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
