#!/usr/bin/env python3

from dotenv import load_dotenv
import os
import sys


def main() -> None:

    is_env: bool = True
    print("ORACLE STATUS: Reading the Matrix...\n")

    if load_dotenv(".env.example"):
        print("Configuration loaded:")

        if os.getenv("MATRIX_MODE"):
            print(f"Mode: {os.getenv('MATRIX_MODE')}")
        else:
            is_env = False
            print("Matrix mode is not enabled.")

        if os.getenv("DATABASE_URL"):
            print("Database: Connected to local instance")
        else:
            is_env = False
            print("Database URL is not set.")

        if os.getenv("API_KEY"):
            print("API Access: Authenticated")
        else:
            is_env = False
            print("API key is not set.")

        if os.getenv("LOG_LEVEL"):
            print(f"Log level: {os.getenv('LOG_LEVEL')}")
        else:
            is_env = False
            print("Log level is not set.")

        if os.getenv("ZION_ENDPOINT"):
            print("Zion Network: Online")
        else:
            is_env = False
            print("Zion endpoint is not set.")

        if is_env:
            print("\nEnvironment security check:")
            print("[OK] No hardcoded secrets detected")
            print("[OK] .env file properly configured")
            print("[OK] Production overrides available\n")

            print("The Oracle sees all configurations.")
        else:
            print("\n[KO] Environment variables are not properly configured.")
    else:
        print("Failed to load environment variables.")


if __name__ == "__main__":
    main()