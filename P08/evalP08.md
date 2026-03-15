# Évaluation P08 — The Matrix

---

## Vue d'ensemble

| Exercice | Fichiers attendus | Fichiers présents | Statut |
|----------|-------------------|-------------------|--------|
| EX0 | `construct.py` | `construct.py` | ✅ Rendu |
| EX01 | `loading.py`, `requirements.txt`, `pyproject.toml` | `loading.py`, `requirements.txt`, `pyproject.toml`, `poetry.lock` | ⚠️ Partiel |
| EX02 | `oracle.py`, `.env.example`, `.gitignore` | `oracle.py`, `.env.example`, `.gitignore`, `.env` | ✅ Rendu |

---

## EX0 — construct.py

### ✅ Ce qui est bien
- Détection venv via `sys.prefix != sys.base_prefix` → méthode fiable, conforme au sujet
- Modules utilisés (`sys`, `os`, `site`) → conformes aux modules autorisés
- Affichage du chemin Python courant (`sys.executable`) ✅
- Affichage du nom du venv via `os.path.basename(sys.prefix)` ✅
- Instructions pour créer/activer le venv (Unix + Windows) ✅
- Affichage du chemin d'installation des packages via `site.getsitepackages()` ✅
- Type hint sur `main() -> None` ✅
- Shebang `#!/usr/bin/env python3` ✅
- Guard `if __name__ == "__main__"` ✅

### ❌ Ce qui ne va pas / Points d'amélioration
- **Faute de frappe** : `"Curent Python"` → devrait être `"Current Python"` (ligne 13)
- **Faute de frappe** : `"Environement Path"` → devrait être `"Environment Path"` (ligne 31)
- **Faute de frappe** : `"SUCESS"` → devrait être `"SUCCESS"` (ligne 34)
- **Espace manquant** : `"without affecting" + "the global system"` → il manque un espace entre les deux (la concaténation implicite donne `"affectingthe"`)
- **Pas de comparaison** global vs venv des chemins de packages → le sujet demande de **comparer** les chemins, vous affichez seulement celui du venv
- **Pas de gestion d'exceptions** → le sujet exige `try/except` (ex: `site.getsitepackages()` peut lever une exception dans certains environnements)
- **Pas de commentaires explicatifs** sur la détection d'environnement → exigé dans les exigences générales

### Note EX0 : 6/10

---

## EX01 — loading.py

### ✅ Ce qui est bien
- Fonction `check_dependency()` avec type hints ✅
- Utilisation de `importlib.import_module()` pour la détection dynamique ✅
- Gestion des dépendances manquantes avec messages utiles (`[OK]` / `[KO]`) ✅
- Instructions d'installation affichées si package manquant ✅
- Utilisation de `pandas`, `numpy`, `matplotlib` pour générer un graphique ✅
- Génération du fichier `matrix_analysis.png` ✅
- `pyproject.toml` bien structuré avec versions compatibles ✅
- `poetry.lock` présent (bonus, montre que poetry a été utilisé) ✅
- Guard `if __name__ == "__main__"` ✅

### ❌ Ce qui ne va pas / Points d'amélioration
- **`requirements.txt` VIDE** → contient seulement un commentaire, aucune dépendance listée. C'est un fichier explicitement demandé avec les versions. **Problème majeur.**
  - Attendu :
    ```
    pandas>=2.0.0
    numpy>=1.24.0
    matplotlib>=3.7.0
    requests>=2.31.0
    ```
- **Pas de `try/except`** dans `main()` → les exigences générales demandent la gestion d'exceptions. Si `savefig` échoue par exemple, le programme crash sans message utile.
- **Import double** : les packages sont importés une première fois dans `check_dependency()` puis ré-importés dans `main()`. Pas grave fonctionnellement (Python cache les imports) mais c'est redondant.
- **Pas de comparaison des versions** entre packages installés → le sujet demande de comparer les versions.
- **`requests` n'est jamais utilisé** dans le code → il est listé mais aucune fonctionnalité ne l'utilise (le sujet le marque optionnel, mais si on le check, autant l'utiliser ou ne pas le vérifier).
- **Pas de commentaires explicatifs** dans le code.

### Note EX01 : 5/10

---

## EX02 — oracle.py

### ✅ Ce qui est bien
- Utilisation de `python-dotenv` avec `load_dotenv()` ✅
- Vérification de toutes les 5 variables requises (`MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL`, `ZION_ENDPOINT`) ✅
- Messages différents selon la présence ou l'absence des variables ✅
- Vérification de sécurité affichée quand tout est OK ✅
- `.env.example` fourni avec les 5 variables ✅
- `.gitignore` exclut `.env` ✅
- Type hint sur `main() -> None` et `is_env: bool` ✅
- Guard `if __name__ == "__main__"` ✅

### ❌ Ce qui ne va pas / Points d'amélioration
- **Pas de gestion dev vs prod** → le sujet demande un comportement **différent** selon `MATRIX_MODE` (`development` vs `production`). Votre code ne change rien selon le mode.
- **API_KEY affichée potentiellement en clair** → le sujet insiste sur le fait de **ne jamais afficher les clés en clair**. Votre code ne masque pas `API_KEY`, mais il ne l'affiche pas non plus directement (OK sur ce point, mais il pourrait y avoir un check de sécurité plus explicite).
- **Messages en cas de variables manquantes** → le sujet attend des formats `[WARNING]` et `[ERROR]` spécifiques (ex: `[ERROR] API_KEY missing`). Vos messages sont trop génériques (`"API key is not set."` au lieu de `[ERROR] API_KEY missing - authentication unavailable`).
- **Pas de valeurs par défaut** → le sujet montre que `MATRIX_MODE` devrait avoir un fallback à `development` et `LOG_LEVEL` à `INFO`. Votre code n'utilise pas `os.getenv('MATRIX_MODE', 'development')`.
- **`import sys` inutilisé** → `sys` est importé mais jamais utilisé.
- **`.env.example` contient des vraies valeurs** → `DATABASE_URL=postgresql://user:password@prod-db/server` et `API_KEY=your_api_key_here` dans l'example c'est OK pour API_KEY (placeholder), mais le `DATABASE_URL` ressemble à une vraie connexion. L'example devrait avoir des placeholders partout.
- **`.env` contient les mêmes valeurs que `.env.example`** → en principe le `.env` devrait avoir vos **vraies** valeurs de dev, pas les mêmes placeholders.
- **Pas de `try/except`** → exigé par les exigences générales. Si `load_dotenv` échoue pour une raison inattendue, pas de gestion.
- **Pas de commentaires explicatifs** dans le code.

### Note EX02 : 5.5/10

---

## Exigences générales — Bilan transversal

| Exigence | Statut | Commentaire |
|----------|--------|-------------|
| Python 3.10+ | ✅ | Utilisation de `list[str]`, `tuple[bool, ...]` (syntaxe 3.10+) |
| Conformité flake8 | ⚠️ | Non vérifié, quelques lignes potentiellement longues |
| Type hints sur toutes les fonctions | ⚠️ | Présents sur `main()` et `check_dependency()` mais incomplet |
| Gestion exceptions `try/except` | ❌ | **Absent dans ex0 et ex02, minimal dans ex01** (seulement dans `check_dependency`) |
| Nommage `snake_case` | ✅ | Conforme |
| Commentaires explicatifs | ❌ | **Quasi absents partout** |
| Tester avec ET sans venv | ⚠️ | Non vérifiable ici, mais le code le supporte |

---

## Note globale estimée : 5.5/10

### Résumé des points critiques à corriger

1. **`requirements.txt` vide** → à remplir immédiatement avec les versions
2. **Ajouter `try/except`** dans les 3 exercices (exigence obligatoire)
3. **Ajouter des commentaires** explicatifs, surtout sur la détection d'environnement (ex0)
4. **Corriger les fautes de frappe** dans ex0 (`Curent`, `Environement`, `SUCESS`, espace manquant)
5. **Implémenter dev vs prod** dans ex02 (comportement différent selon `MATRIX_MODE`)
6. **Ajouter les valeurs par défaut** dans ex02 (`MATRIX_MODE` → `development`, `LOG_LEVEL` → `INFO`)
7. **Ajouter la comparaison** des chemins de packages dans ex0 (global vs venv)
8. **Utiliser les formats `[WARNING]`/`[ERROR]`** dans ex02 comme demandé dans le sujet
