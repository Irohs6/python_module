#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as lost_archive:
            print("Vault connection established with failsafe protocols")
            content = lost_archive.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix.\n"
              "STATUS: Crisis handled, system stable\n")
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as security:
            security_content = security.read()
            print(security_content)
    except PermissionError:
        print("RESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, security maintained\n")

    print("ROUTINE ACCESS: Attempting access to "
          "'standard_archive.txt'...\n")
    try:
        with open("standard_archive.txt", "r") as standard:
            standard_content = standard.read()
            print(f"SUCCESS: Archive recovered - ``{standard_content}''\n"
                  "STATUS: Normal operations resumed\n")
    except (FileNotFoundError, PermissionError):
        print("CRISIS ALERT: Attempting access to 'standard_archive.txt'"
              "...\nRESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, security maintained\n")

    print("All crisis scenarios handled successfully. Archives secure.")
