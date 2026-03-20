#!/usr/bin/env python3
# loading.py - Vérification des dépendances et analyse de données
# Démontre la gestion de packages avec pip (requirements.txt)
# et Poetry (pyproject.toml)
import importlib


def check_dependency(packages_name: list[str]) -> tuple[bool, dict[str, str]]:
    """Vérifie si les packages sont disponibles et retourne leurs versions."""
    result = {}
    all_ok = True
    for package_name in packages_name:
        try:
            # importlib.import_module permet d'importer dynamiquement
            # sans connaître les noms à l'avance (utile pour la détection)
            module = importlib.import_module(package_name)
            # __version__ est la convention standard
            # pour les versions de packages
            version_info = getattr(module, "__version__", "unknown")
            result[package_name] = version_info
            print(f"[OK] {package_name} ({version_info})")
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
    # Liste des packages requis pour l'analyse de données
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    ok, _ = check_dependency(packages)
    if not ok:
        print("\nSome dependencies are missing. Please install them first.")
    else:
        # Import dynamique des modules après validation de leur présence
        modules = {}
        for package in packages:
            modules[package] = importlib.import_module(package)
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        # Génération de 1000 valeurs aléatoires selon une loi normale
        tab = modules["numpy"].random.randn(1000)
        print("Generating visualization...")
        # Création d'un DataFrame pandas pour structurer les données
        df = modules["pandas"].DataFrame(tab, columns=["Random"])
        # Histogramme de distribution avec matplotlib via l'API pandas
        plot = df.plot.hist(
            bins=50,
            title="Random Data Distribution",
            color="skyblue",
            edgecolor="black",
            alpha=0.7,
            figsize=(8, 5),
            grid=True,
        )
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
        # Sauvegarde du graphique dans un fichier image
        plot.get_figure().savefig("matrix_analysis.png")


if __name__ == "__main__":
    main()
