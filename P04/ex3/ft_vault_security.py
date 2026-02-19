#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as classified:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            content = classified.read()
            print(content.strip())
        with open("security_protocols.txt", "w") as security:
            new_protocol = "[CLASSIFIED] New security protocols archived"
            security.write(new_protocol + "\n")
            print("\nSECURE PRESERVATION:")
            print(new_protocol)
        print("Vault automatically sealed upon completion\n")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
