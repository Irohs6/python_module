#!/usr/bin/env python3
# construct.py - Détection et affichage de l'environnement Python virtuel
# Démontre la différence entre un environnement global et un venv isolé

import sys
import os
import site


def main() -> None:
    # sys.prefix pointe vers le répertoire de l'environnement actif
    # sys.base_prefix pointe toujours vers l'installation Python système
    # S'ils sont égaux, on est dans l'environnement global (pas de venv actif)
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")

        # sys.executable = chemin absolu de l'interpréteur Python utilisé
        print("Current Python: ", sys.executable)
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        # Instructions pour créer et activer un venv
        print(
            "To enter the construct, run: \n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n\n"
            "Then run this program again."
        )
    else:
        print("MATRIX STATUS: Welcome to the construct\n")

        # sys.executable pointe maintenant vers le python du venv
        print("Current Python:", sys.executable, "\n")
        # Le nom du venv est le dernier segment du chemin sys.prefix
        venv_name = os.path.basename(sys.prefix)
        print("Virtual Environment:", venv_name, "\n")
        print("Environment Path:", sys.prefix, "\n")

        print(
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting "
            "the global system.\n"
        )

        # site.getsitepackages() retourne la liste des répertoires
        # où pip installe les packages dans cet environnement
        try:
            pkg_path = site.getsitepackages()[0]
        except AttributeError:
            # Peut arriver dans des environnements restreints (Python < 3.10)
            pkg_path = "unavailable (restricted environment)"
        print("Package installation path:")
        print(pkg_path)


if __name__ == "__main__":
    main()
