#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    arch_id = input("Input Stream active. Enter archivist ID:")
    status = input("Input Stream active. Enter status report: ")
    sys.stdout.write(f"[ARCHIVIST {arch_id}] STATUS REPORT: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("Data transmission complete.\n")

    print("Three-channel communication test successful.")