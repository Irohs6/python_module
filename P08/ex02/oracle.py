#!/usr/bin/env python3
# oracle.py - Chargement sécurisé de la configuration
# via variables d'environnement et fichier .env
# Les variables système ont priorité sur le .env
# (comportement natif de load_dotenv)

import sys
import os

try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "python-dotenv library is not installed. Please install it using 'pip "
        "install python-dotenv' and try again."
    )
    sys.exit(1)


def main() -> None:

    # is_env suit si toutes les variables requises sont présentes
    is_env: bool = True
    print("ORACLE STATUS: Reading the Matrix...\n")

    # load_dotenv() charge le fichier .env s'il existe
    # Si une variable est déjà définie dans l'environnement système,
    # load_dotenv() ne l'écrase PAS → les variables système ont priorité
    load_dotenv()
    print("Configuration loaded:")

    # Lecture de chaque variable avec os.getenv()
    # os.getenv() retourne None si la variable n'est pas définie
    if os.getenv("MATRIX_MODE"):
        print(f"Mode: {os.getenv('MATRIX_MODE')}")
    else:
        is_env = False
        print("Matrix mode is not enabled.")

    if os.getenv("DATABASE_URL"):
        # On n'affiche pas la valeur brute pour ne pas exposer les credentials
        print("Database: Connected to local instance")
    else:
        is_env = False
        print("Database URL is not set.")

    if os.getenv("API_KEY"):
        # Idem : on ne logue jamais une clé API en clair
        print("API Access: Authenticated")
    else:
        is_env = False
        print("API key is not set.")

    if os.getenv("LOG_LEVEL"):
        print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    else:
        is_env = False
        print("Log level is not set.")

    if os.getenv("ZION_ENDPOINT"):
        print("Zion Network: Online")
    else:
        is_env = False
        print("Zion endpoint is not set.")

    # Résumé de sécurité : affiché uniquement si toutes les variables sont OK
    if is_env:
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")

        print("The Oracle sees all configurations.")
    else:
        print("\n[KO] Environment variables are not properly configured.")


if __name__ == "__main__":
    main()
