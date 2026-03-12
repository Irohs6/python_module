#!/usr/bin/env python3
from ast import mod
import importlib
from sys import version


def check_dependency(packages_name: list[str]) -> tuple[bool, dict[str, str]]:
    """Vérifie si les packages sont disponibles et retourne leurs versions."""
    result = {}
    all_ok = True
    for package_name in packages_name:
        try:
            module = importlib.import_module(package_name)
            version = getattr(module, "__version__", "unknown")
            result[package_name] = version
            print(f"[OK] {package_name} ({version})")
        except ModuleNotFoundError:
            result[package_name] = "MISSING"
            print(f"[KO] {package_name} - MISSING")
            print("     Install with: pip install -r requirements.txt")
            print("     Or with Poetry: poetry install")
            all_ok = False
    return all_ok, result


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    ok, versions = check_dependency(packages)
    if not ok:
        print("\nSome dependencies are missing. Please install them first.")
    else:
        modules = {}
        for package in packages:
            modules[package] = importlib.import_module(package)
        print("Analyzing Matrix data...")
        print('Processing 1000 data points...')
        tab = modules["numpy"].random.randn(1000)
        print("Generating visualization...")
        df = modules["pandas"].DataFrame(tab, columns=["Random"])
        plot = df.plot.hist(
                bins=50,
                title="Random Data Distribution",
                color="skyblue",
                edgecolor="black",
                alpha=0.7,
                figsize=(8, 5),
                grid=True
            )
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
        plot.get_figure().savefig("matrix_analysis.png")


if __name__ == "__main__":
    main()
