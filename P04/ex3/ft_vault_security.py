#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as classified, open(
            "security_protocols.txt", "r"
        ) as security:
            print("Vault connection established with failsafe protocols")
            content = classified.read()
            print("SECURE EXTRACTION:")
            print(content)
            content_security = security.read()
            print("SECURE PRESERVATION:")
            print(content_security)
            print("Vault operations completed successfully.\n")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        print("All vault operations completed with maximum security.")
