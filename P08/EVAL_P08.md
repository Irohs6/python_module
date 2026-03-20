# Évaluation P08 — The Matrix

**Date :** 20 mars 2026
**Sujet :** Virtual environments, package management, environment configuration

---

## EX0 — `construct.py`

### Note : 8.5 / 10

### ✅ Ce qui fonctionne
- Détection du venv avec `sys.prefix == sys.base_prefix` → méthode correcte et standard ✅
- Affichage du chemin Python courant (`sys.executable`) ✅
- Affichage du nom du venv (`os.path.basename(sys.prefix)`) ✅
- Affichage du chemin du venv (`sys.prefix`) ✅
- Affichage du chemin des packages (`site.getsitepackages()[0]`) ✅
- Instructions de création/activation du venv affichées quand absent ✅
- Format de sortie conforme au sujet (MATRIX STATUS, WARNING, SUCCESS) ✅
- Type hints sur `main()` ✅
- Fonctionne (exit 0) ✅

### ❌ Ce qui ne va pas
- **Pas de commentaires dans le code** — le sujet demande explicitement
  "Include clear comments explaining your logic, especially for environment
  detection"

---

## EX01 — `loading.py` + `requirements.txt` + `pyproject.toml`

### Note : 8.5 / 10

### ✅ Ce qui fonctionne
- `check_dependency()` avec gestion des modules manquants ✅
- Affichage `[OK]` / `[KO]` avec versions ✅
- Instructions d'installation affichées si dépendance manquante ✅
- Génération du graphique avec matplotlib + pandas + numpy ✅
- Sauvegarde dans `matrix_analysis.png` ✅
- `pyproject.toml` correct avec toutes les dépendances ✅
- `requirements.txt` complété avec les 4 dépendances ✅
- Type hints présents ✅
- Fonctionne (exit 0) ✅

### ❌ Ce qui ne va pas

**MINEUR — Pas de fonction de comparaison pip vs Poetry** : le sujet demande
"Include a comparison function that shows installed package versions" et
"Show the differences between pip and Poetry through your program's output".
Le code ne montre aucune comparaison explicite entre les deux approches.

**MINEUR — Pas de commentaires** expliquant la logique (même remarque qu'EX0).

---

## EX02 — `oracle.py` + `.env.example` + `.gitignore`

### Note : 9 / 10

### ✅ Ce qui fonctionne
- `python-dotenv` utilisé correctement avec `load_dotenv()` sans conditionnel ✅
- Toutes les variables requises gérées (`MATRIX_MODE`, `DATABASE_URL`,
  `API_KEY`, `LOG_LEVEL`, `ZION_ENDPOINT`) ✅
- **Scénario 1 — avec `.env`** : charge et affiche correctement ✅
- **Scénario 2 — sans `.env`, variables système** : override fonctionne ✅
- **Scénario 3 — sans `.env`, sans variables** : affiche les manques proprement ✅
- `ImportError` sur `python-dotenv` géré avec `sys.exit(1)` ✅
- `.env.example` présent avec toutes les variables ✅
- `.gitignore` contient `.env` ✅
- Affichage conforme au sujet ✅
- Type hints présents ✅

### ❌ Ce qui ne va pas
- **Pas de commentaires** dans le code (même remarque que EX0)

---

## Résumé Global

| Exercice | Note | Problème principal |
|---|---|---|
| EX0 — construct.py | 9/10 | Pas de commentaires |
| EX01 — loading.py | 8.5/10 | Pas de comparaison pip vs Poetry, pas de commentaires |
| EX02 — oracle.py | 9/10 | Pas de commentaires |
| **MOYENNE** | **8.8/10** | |

---

## Priorités de correction avant soutenance

1. **EX0/EX01/EX02 :** Ajouter des commentaires expliquant la logique
   (exigence explicite du sujet)
