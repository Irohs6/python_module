#!/usr/bin/env python3

import sys
import os


def main() -> None:
    print("MATRIX STATUS: You're still plugged in\n")

    if sys.prefix == sys.base_prefix:
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

        print("Current Python:", sys.executable[-22:], "\n")
        print("Virtual Environment:", sys.prefix[-10:], "\n")
        print("Environement Path:", sys.prefix[-18:], "\n")

        print(
            "SUCESS: You're in an isolated environment!"
            "Safe to install packages without affecting"
            "the global system."
        )

        print(
            "Package installation path:",
            os.path.join(
                sys.prefix,
                "lib",
                f"python{sys.version_info.major}.{sys.version_info.
                                                  minor}",
                "site-packages",
            ),
        )


if __name__ == "__main__":
    main()
