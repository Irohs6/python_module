#!/usr/bin/env python3


def crisis_handler(filename: str, mode: str) -> None:
    """Attempts to open a file and handles FileNotFoundError,
        PermissionError and unexpected exceptions."""
    try:
        if mode == "crisis":
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        else:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")

        with open(filename, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis contained, investigation ongoing\n")


def main() -> None:
    """Runs several crisis and routine file
        access scenarios through crisis_handler."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt", "crisis")
    crisis_handler("classified_vault.txt", "crisis")
    crisis_handler("standard_archive.txt", "routine")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
