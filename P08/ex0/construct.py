#!/usr/bin/env python3

import sys
import os
import site


def main() -> None:

    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")

        print("Curent Python: ", sys.executable)
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print(
            "To enter the construct, run: \n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n\n"
            "Then run this program again."
        )
    else:
        print("MATRIX STATUS: Welcome to the construct\n")

        print("Current Python:", sys.executable, "\n")
        venv_name = os.path.basename(sys.prefix)
        print("Virtual Environment:", venv_name, "\n")
        print("Environement Path:", sys.prefix, "\n")

        print(
            "SUCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting"
            "the global system.\n"
        )

        print("Package installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()
