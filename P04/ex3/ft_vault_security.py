#!/usr/bin/env python3


def main() -> None:
    """Opens classified_data.txt for reading and writes to
        security_protocols.txt."""

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as classified:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            content = classified.read()
            print(content)
        with open("security_protocols.txt", "w") as security:
            new_protocol = "[CLASSIFIED] New security protocols archived"
            security.write(content)
            print("\nSECURE PRESERVATION:")
            print(new_protocol)
        print("Vault automatically sealed upon completion\n")
    except FileNotFoundError:
        print("Error: classified_data.txt not found.")
    finally:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
