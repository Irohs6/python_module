#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        data = file.read()
        print(data)
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
