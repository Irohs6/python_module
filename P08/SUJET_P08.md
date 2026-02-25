# SUJET P08 — The Matrix: Welcome to the Real World of Data Engineering
# Récapitulatif en français

---

## Thème général

Le projet P08 tourne autour de la métaphore de **The Matrix** :
- L'environnement virtuel Python = "Le Construct" (espace d'entraînement isolé)
- Les packages = "Les programmes" (armes chargées dans l'esprit)
- Les variables d'environnement = "La Mainframe" (configuration secrète de l'Oracle)

L'objectif est de maîtriser les **3 piliers de l'environnement Python professionnel** :
1. Les environnements virtuels (venv)
2. La gestion des dépendances (pip & Poetry)
3. La configuration sécurisée (variables d'environnement / .env)

---

## Exigences générales

- Python 3.10+
- Code conforme flake8
- Type hints sur toutes les fonctions
- Gestion des exceptions avec try/except
- Nommage snake_case
- Commentaires explicatifs sur la détection d'environnement
- Tester avec ET sans venv, avec ET sans dépendances

---

## EX0 — Entering the Matrix (`construct.py`)

### Ce qui est attendu

Créer un programme `construct.py` qui :
- **Détecte** si on est dans un environnement virtuel ou non
- **Affiche** des informations sur l'environnement Python courant
- **Fournit des instructions** pour créer et activer un venv si aucun n'est détecté
- **Compare** les chemins de packages global vs venv

### Modules autorisés
`sys`, `os`, `site`

### Comment détecter un venv ?

Il existe 3 façons principales :
```python
# Méthode 1 : sys.prefix != sys.base_prefix (la plus fiable)
import sys
in_venv = sys.prefix != sys.base_prefix

# Méthode 2 : variable d'environnement VIRTUAL_ENV
import os
in_venv = os.environ.get('VIRTUAL_ENV') is not None

# Méthode 3 : hasattr(sys, 'real_prefix') (pour virtualenv)
in_venv = hasattr(sys, 'real_prefix')
```

### Exemple de sortie — HORS venv

```
MATRIX STATUS: You're still plugged in
Current Python: /usr/bin/python3.11
Virtual Environment: None detected
WARNING: You're in the global environment!
The machines can see everything you install.
To enter the construct, run:
    python -m venv matrix_env
    source matrix_env/bin/activate    # Sur Unix
    matrix_env\Scripts\activate       # Sur Windows
Then run this program again.
```

### Exemple de sortie — DANS le venv

```
MATRIX STATUS: Welcome to the construct
Current Python: /path/to/matrix_env/bin/python
Virtual Environment: matrix_env
Environment Path: /path/to/matrix_env
SUCCESS: You're in an isolated environment!
Safe to install packages without affecting the global system.
Package installation path:
    /path/to/matrix_env/lib/python3.11/site-packages
```

### Commandes de test

```bash
# Test hors venv
python3 construct.py

# Créer et activer le venv
python3 -m venv matrix_env
source matrix_env/bin/activate

# Test dans le venv
python3 construct.py
```

### Ressources

- Documentation officielle venv :
  https://docs.python.org/3/library/venv.html
- sys.prefix vs sys.base_prefix expliqué :
  https://docs.python.org/3/library/sys.html#sys.prefix
- module site (chemins de packages) :
  https://docs.python.org/3/library/site.html
- Real Python — Virtual Environments (excellent tutoriel) :
  https://realpython.com/python-virtual-environments-a-primer/

---

## EX01 — Loading Programs (`loading.py` + `requirements.txt` + `pyproject.toml`)

### Ce qui est attendu

Créer un programme `loading.py` qui :
- **Utilise pandas** pour manipuler des données
- **Utilise numpy** pour des calculs numériques
- **Utilise matplotlib** pour générer une visualisation
- **Gère les dépendances manquantes** avec des messages d'erreur utiles
- **Compare les versions** des packages installés
- **Génère une image** `matrix_analysis.png`

Fournir **2 fichiers de dépendances** :
- `requirements.txt` → pour pip
- `pyproject.toml` → pour Poetry

### Modules autorisés
`pandas`, `requests` (optionnel), `matplotlib`, `numpy`, `sys`, `importlib`

### Comment détecter si un package est installé ?

```python
import importlib

def check_dependency(package_name: str) -> tuple[bool, str]:
    """Vérifie si un package est disponible et retourne sa version."""
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, ''
```

### Structure requirements.txt (pip)

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
requests>=2.31.0
```

### Structure pyproject.toml (Poetry)

```toml
[tool.poetry]
name = "loading"
version = "0.1.0"
description = "Matrix data analysis"

[tool.poetry.dependencies]
python = "^3.10"
pandas = "^2.0.0"
numpy = "^1.24.0"
matplotlib = "^3.7.0"
requests = "^2.31.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### Exemple de sortie

```
LOADING STATUS: Loading programs...
Checking dependencies:
[OK] pandas (2.1.0) - Data manipulation ready
[OK] numpy (1.24.0) - Numerical computing ready
[OK] matplotlib (3.7.2) - Visualization ready
Analyzing Matrix data...
Processing 1000 data points...
Generating visualization...
Analysis complete!
Results saved to: matrix_analysis.png
```

### Sortie si dépendances manquantes

```
LOADING STATUS: Loading programs...
Checking dependencies:
[KO] pandas - MISSING
     Install with: pip install -r requirements.txt
     Or with Poetry: poetry install
```

### Commandes de test

```bash
# Test sans dépendances (doit afficher les erreurs)
python3 loading.py

# Installation via pip
pip install -r requirements.txt
python3 loading.py

# Installation via Poetry
poetry install
poetry run python loading.py
```

### Ressources

- pandas — manipulation de données :
  https://pandas.pydata.org/docs/getting_started/index.html
- numpy — calcul numérique :
  https://numpy.org/doc/stable/user/quickstart.html
- matplotlib — visualisation :
  https://matplotlib.org/stable/tutorials/introductory/quick_start.html
- importlib — import dynamique :
  https://docs.python.org/3/library/importlib.html
- Poetry — guide débutant :
  https://python-poetry.org/docs/basic-usage/
- pip vs Poetry comparaison :
  https://realpython.com/dependency-management-python-poetry/
- requirements.txt best practices :
  https://pip.pypa.io/en/stable/reference/requirements-file-format/

---

## EX02 — Accessing the Mainframe (`oracle.py` + `.env.example` + `.gitignore`)

### Ce qui est attendu

Créer un programme `oracle.py` qui :
- **Charge la configuration** depuis des variables d'environnement
- **Utilise un fichier `.env`** pour les réglages de développement
- **Gère dev vs prod** (comportement différent selon MATRIX_MODE)
- **Gère les erreurs** si des variables sont manquantes
- **Sécurise les secrets** (ne jamais afficher les clés en clair)

Fournir :
- `.env.example` → modèle de configuration (sans vraies valeurs)
- `.gitignore` → exclure `.env` du versioning

### Variables de configuration requises

| Variable | Description | Exemple |
|---|---|---|
| `MATRIX_MODE` | Mode dev ou prod | `development` |
| `DATABASE_URL` | URL de connexion BDD | `sqlite:///matrix.db` |
| `API_KEY` | Clé API secrète | `secret123` |
| `LOG_LEVEL` | Niveau de log | `DEBUG` |
| `ZION_ENDPOINT` | URL du réseau | `http://localhost:8000` |

### Modules autorisés
`os`, `sys`, `python-dotenv`

### Comment utiliser python-dotenv ?

```python
from dotenv import load_dotenv
import os

# Charge automatiquement le fichier .env du répertoire courant
load_dotenv()

# Lire une variable avec valeur par défaut
matrix_mode = os.getenv('MATRIX_MODE', 'development')
api_key = os.getenv('API_KEY')  # None si absent

# Vérifier qu'une variable critique est présente
if api_key is None:
    print("[WARNING] API_KEY non configurée !")
```

### Exemple de sortie (avec .env configuré)

```
ORACLE STATUS: Reading the Matrix...
Configuration loaded:
Mode: development
Database: Connected to local instance
API Access: Authenticated
Log Level: DEBUG
Zion Network: Online
Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available
The Oracle sees all configurations.
```

### Sortie sans configuration

```
ORACLE STATUS: Reading the Matrix...
[WARNING] MATRIX_MODE not set, defaulting to: development
[WARNING] DATABASE_URL not configured
[ERROR] API_KEY missing - authentication unavailable
[WARNING] LOG_LEVEL not set, defaulting to: INFO
[WARNING] ZION_ENDPOINT not set
```

### Commandes de test

```bash
# Sans configuration
python3 oracle.py

# Avec fichier .env
cp .env.example .env
# Éditer .env avec les vraies valeurs
python3 oracle.py

# Override par variables d'environnement (priorité sur .env)
MATRIX_MODE=production API_KEY=secret123 python3 oracle.py
```

### Important : sécurité

- `.env` doit être dans `.gitignore` (ne JAMAIS committer les secrets)
- `.env.example` est commité (modèle sans valeurs réelles)
- Ne jamais afficher une API_KEY en clair dans les logs
- python-dotenv doit être installé : `pip install python-dotenv`

### Ressources

- python-dotenv documentation :
  https://pypi.org/project/python-dotenv/
  https://saurabh-kumar.com/python-dotenv/
- os.environ / os.getenv :
  https://docs.python.org/3/library/os.html#os.environ
- 12-Factor App — configuration :
  https://12factor.net/config
- Variables d'environnement expliquées :
  https://realpython.com/python-environment-variables/
- Sécurité des secrets dans les projets Python :
  https://blog.gitguardian.com/secrets-api-management/

---

## Résumé des fichiers à rendre

```
P08/
├── ex0/
│   └── construct.py          ← détection venv
├── ex01/
│   ├── loading.py            ← analyse de données
│   ├── requirements.txt      ← dépendances pip
│   └── pyproject.toml        ← dépendances Poetry
└── ex02/
    ├── oracle.py             ← gestion config .env
    ├── .env.example          ← modèle de .env (commité)
    └── .gitignore            ← exclut .env (non commité)
```

## Points clés à retenir pour la soutenance

1. **Pourquoi un venv ?** → Isoler les dépendances projet, éviter les conflits entre projets
2. **pip vs Poetry ?** → pip = simple, Poetry = gestion avancée des versions + lock file
3. **Pourquoi .env ?** → Séparer le code de la configuration, ne pas hardcoder les secrets
4. **sys.prefix vs sys.base_prefix** → La différence indique si on est dans un venv
5. **importlib.import_module()** → Import dynamique pour tester la disponibilité d'un package
