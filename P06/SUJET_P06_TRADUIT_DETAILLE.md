# Le Codex de l'Alchimiste - Maîtriser les Mystères des Imports Python

## Chapitre III - Introduction

Bienvenue dans Le Codex de l'Alchimiste !

En tant qu'apprenti alchimiste, vous découvrirez le système d'importation de Python à travers des expériences magiques pratiques. Chaque expérience s'appuie sur la précédente, créant un package complet de Laboratoire Alchimique qui démontre l'organisation professionnelle Python.

### ⚠️ PRÉREQUIS OBLIGATOIRES

Cette activité suppose une maîtrise solide des fondamentaux Python incluant :
- La syntaxe
- Les fonctions
- Les classes
- La gestion des erreurs
- Les listes et dictionnaires
- Les structures de données

Vous devez être à l'aise avec l'écriture de classes Python, la gestion des exceptions et le travail avec les collections avant de tenter cette activité axée sur les imports. Sans ces fondations, les concepts d'importation seront difficiles à comprendre.

### 🎯 Objectif Principal

**Concentrez-vous sur la compréhension du fonctionnement des imports, pas seulement sur leur mise en œuvre.**

Un véritable alchimiste comprend chaque étape du processus de transmutation ! Cette activité concerne l'organisation du code et les mécanismes d'importation. Gardez vos formules alchimiques simples (fonctions basiques) pour pouvoir vous concentrer sur les concepts d'importation.

### 📋 GESTION DES ERREURS

Toutes les fonctions doivent retourner des chaînes de caractères. Lors du test d'imports qui peuvent échouer (comme l'accès à des fonctions cachées), utilisez des blocs try/except et retournez des messages d'erreur descriptifs au lieu de laisser le programme planter.

---

## Chapitre IV - Instructions Générales

### IV.1 - Autorisé et Interdit

#### ✅ INGRÉDIENTS AUTORISÉS

- Tous les modules de la bibliothèque standard Python (`datetime`, `math`, `os`, `sys`, etc.)
- Créer vos propres modules et packages
- Tous les styles d'import : `import`, `from...import`, `import...as`
- Créer des fichiers `__init__.py` (Parchemins Sacrés)
- Imports absolus et relatifs
- Type hints et annotations

#### ❌ MAGIE NOIRE INTERDITE

- Bibliothèques externes (pas de `pip install`)
- Utiliser `eval()` ou `exec()` (transmutations dangereuses)
- Modifier `sys.path` directement
- Utiliser `importlib` pour des imports dynamiques
- Algorithmes complexes (gardez vos sorts simples)

---

### IV.2 - Structure du Laboratoire

Vous construirez votre Laboratoire Alchimique progressivement à travers quatre parties :

- **Partie I** : Le Parchemin Sacré (mystère du `__init__.py`)
- **Partie II** : Transmutation d'Import (maîtrise de `from...import`)
- **Partie III** : Le Grand Débat des Chemins (absolu vs relatif)
- **Partie IV** : Briser la Malédiction Circulaire (résolution des dépendances)

#### Structure Finale du Laboratoire

```
alchemy/                          # Votre package de laboratoire principal
├── __init__.py                   # Parchemin sacré principal
├── elements.py                   # Fonctions de sorts élémentaires basiques
├── potions.py                    # Fonctions de recettes de potions avancées
├── transmutation/                # Package de sorts de transformation
│   ├── __init__.py
│   ├── basic.py
│   └── advanced.py
└── grimoire/                     # Package de documentation de sorts
    ├── __init__.py
    ├── spellbook.py
    └── validator.py
```

**IMPORTANT** : Toutes les fonctions doivent être simples et retourner des chaînes. Concentrez-vous sur les concepts d'importation, pas sur la logique complexe. Gérez les erreurs en retournant des messages d'erreur descriptifs sous forme de chaînes.

---

## Chapitre V - Partie Obligatoire

### V.1 - Partie I : Le Parchemin Sacré

#### 🎯 Objectif

Découvrir la puissance du `__init__.py` - le parchemin sacré qui transforme les dossiers ordinaires en packages Python magiques.

#### 📚 Concepts à Maîtriser

##### 1. Le fichier `__init__.py`

Le fichier `__init__.py` est un fichier spécial qui indique à Python qu'un dossier doit être traité comme un package.

**Ressources** :
- [Documentation officielle Python - Packages](https://docs.python.org/fr/3/tutorial/modules.html#packages)
- [Real Python - Python Modules and Packages](https://realpython.com/python-modules-packages/)
- [Guide complet sur __init__.py](https://www.geeksforgeeks.org/what-is-__init__-py-in-python/)

##### 2. Interface de Package

Le `__init__.py` contrôle ce qui est exposé au niveau du package. C'est comme une "vitrine" de votre module.

**Principe** :
```python
# Sans __init__.py ou __init__.py vide
import alchemy
alchemy.create_fire()  # ❌ AttributeError

# Avec __init__.py qui importe create_fire
from .elements import create_fire
# Maintenant accessible :
import alchemy
alchemy.create_fire()  # ✅ Fonctionne !
```

**Ressources** :
- [Understanding Python's __init__.py](https://towardsdatascience.com/whats-init-for-me-d70a312da583)

##### 3. Métadonnées de Package

Les variables comme `__version__` et `__author__` sont des conventions pour documenter votre package.

**Ressources** :
- [PEP 396 - Module Version Numbers](https://peps.python.org/pep-0396/)

#### 📝 Fichiers à Créer pour la Partie I

- `ft_sacred_scroll.py` - Script de démonstration (à la racine du dépôt)
- `alchemy/__init__.py` - Le parchemin sacré principal
- `alchemy/elements.py` - Sorts élémentaires basiques

#### 🔧 Instructions

Créez votre premier package alchimique et apprenez comment `__init__.py` contrôle quelle magie est disponible pour les autres alchimistes.

**alchemy/elements.py** doit contenir :
```python
def create_fire():
    return "Fire element created"

def create_water():
    return "Water element created"

def create_earth():
    return "Earth element created"

def create_air():
    return "Air element created"
```

**alchemy/__init__.py** doit contenir exactement :
```python
__version__ = "1.0.0"
__author__ = "Master Pythonicus"

# Import et expose UNIQUEMENT create_fire et create_water
from .elements import create_fire, create_water
# create_earth et create_air restent cachés
```

💡 **Point Clé** : Le fichier `__init__.py` contrôle l'interface du package. Les fonctions importées ici deviennent disponibles comme `alchemy.function_name`. Les fonctions non importées restent cachées et nécessitent un accès direct au module.

#### 📤 Exemple de Sortie Attendue

```bash
$> python3 ft_sacred_scroll.py
=== Sacred Scroll Mastery ===

Testing direct module access:
alchemy.elements.create_fire(): Fire element created
alchemy.elements.create_water(): Water element created
alchemy.elements.create_earth(): Earth element created
alchemy.elements.create_air(): Air element created

Testing package-level access (controlled by __init__.py):
alchemy.create_fire(): Fire element created
alchemy.create_water(): Water element created
alchemy.create_earth(): AttributeError - not exposed
alchemy.create_air(): AttributeError - not exposed

Package metadata:
Version: 1.0.0
Author: Master Pythonicus
```

#### 💭 Questions de Réflexion

1. Comment le Parchemin Sacré (`__init__.py`) contrôle-t-il quels sorts sont disponibles pour les autres alchimistes ?
2. Quelle est la différence entre ce qui existe dans un module et ce qui est exposé par le package ?
3. Pourquoi voudrait-on cacher certaines fonctions ?

---

### V.2 - Partie II : Transmutation d'Import

#### 🎯 Objectif

Maîtriser l'art du `from...import` - invoquer des sorts spécifiques depuis des grimoires distants sans apporter le livre entier.

#### 📚 Concepts à Maîtriser

##### 1. Les Différents Styles d'Import

Python offre plusieurs façons d'importer du code :

**Style 1 : Import de module complet**
```python
import alchemy.elements
result = alchemy.elements.create_fire()
```
✅ Avantages : Clarté, pas de confusion sur l'origine
❌ Inconvénients : Verbeux

**Style 2 : Import spécifique**
```python
from alchemy.elements import create_fire
result = create_fire()
```
✅ Avantages : Concis, code plus lisible
❌ Inconvénients : Possible confusion sur l'origine

**Style 3 : Import avec alias**
```python
from alchemy.potions import healing_potion as heal
result = heal()
```
✅ Avantages : Noms courts, évite les conflits
❌ Inconvénients : Peut masquer le nom original

**Style 4 : Imports multiples**
```python
from alchemy.elements import create_fire, create_water, create_earth
```
✅ Avantages : Pratique pour plusieurs imports
❌ Inconvénients : Lignes longues possibles

**Ressources** :
- [Python Import System - Real Python](https://realpython.com/python-import/)
- [Guide complet des imports Python](https://www.datacamp.com/tutorial/modules-in-python)
- [Best Practices pour les imports](https://peps.python.org/pep-0008/#imports)

##### 2. Namespace et Portée

Comprendre comment les imports affectent l'espace de noms de votre module.

**Ressources** :
- [Python Namespaces and Scope](https://realpython.com/python-namespaces-scope/)

#### 📝 Fichiers à Créer pour la Partie II

- `ft_import_transmutation.py` - Script de démonstration (à la racine du dépôt)
- `alchemy/potions.py` - Recettes de potions avancées

#### 🔧 Instructions

Développez votre laboratoire et apprenez différentes façons d'invoquer des formules magiques.

**alchemy/potions.py** doit contenir exactement :

```python
def healing_potion():
    from .elements import create_fire, create_water
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"

def strength_potion():
    from .elements import create_earth, create_fire
    earth_result = create_earth()
    fire_result = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"

def invisibility_potion():
    from .elements import create_air, create_water
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"

def wisdom_potion():
    from .elements import create_fire, create_water, create_earth, create_air
    fire = create_fire()
    water = create_water()
    earth = create_earth()
    air = create_air()
    return f"Wisdom potion brewed with all elements: {fire}, {water}, {earth}, {air}"
```

💡 **Point Clé** : Chaque fonction de potion doit importer et appeler les fonctions élémentaires requises, puis retourner une chaîne qui inclut les résultats élémentaires.

#### 📤 Exemple de Sortie Attendue

```bash
$> python3 ft_import_transmutation.py
=== Import Transmutation Mastery ===

Method 1 - Full module import:
alchemy.elements.create_fire(): Fire element created

Method 2 - Specific function import:
create_water(): Water element created

Method 3 - Aliased import:
heal(): Healing potion brewed with Fire element created and Water element created

Method 4 - Multiple imports:
create_earth(): Earth element created
create_fire(): Fire element created
strength_potion(): Strength potion brewed with Earth element created and Fire element created

All import transmutation methods mastered!
```

#### 💭 Questions de Réflexion

1. Quels sont les avantages et inconvénients de chaque méthode de transmutation d'import ?
2. Quand utiliser `import module` vs `from module import function` ?
3. Comment les imports affectent-ils la lisibilité du code ?

---

### V.3 - Partie III : Le Grand Débat des Chemins

#### 🎯 Objectif

Comprendre l'ancien débat entre imports absolus et relatifs - deux chemins différents pour atteindre la même formule magique.

#### 📚 Concepts à Maîtriser

##### 1. Imports Absolus

Les imports absolus utilisent le chemin complet depuis la racine du package.

```python
from alchemy.elements import create_fire
from alchemy.potions import healing_potion
```

✅ **Avantages** :
- Très clair et explicite
- Fonctionne de n'importe où
- Facile à comprendre pour les débutants

❌ **Inconvénients** :
- Verbeux
- Si vous renommez le package, il faut tout changer

**Ressources** :
- [Absolute vs Relative Imports](https://realpython.com/absolute-vs-relative-python-imports/)
- [PEP 328 - Imports: Multi-Line and Absolute/Relative](https://peps.python.org/pep-0328/)

##### 2. Imports Relatifs

Les imports relatifs utilisent la position relative dans la hiérarchie du package.

```python
from .elements import create_fire      # même niveau
from ..potions import healing_potion   # niveau parent
from .submodule import something       # sous-module
```

**Notation** :
- `.` = répertoire courant
- `..` = répertoire parent
- `...` = grand-parent (rarement utilisé)

✅ **Avantages** :
- Concis
- Facilite le déplacement/renommage de packages
- Montre clairement la structure

❌ **Inconvénients** :
- Peut être déroutant
- Ne fonctionne que dans les packages
- Erreurs si la structure change

**Ressources** :
- [Relative Imports in Python](https://www.geeksforgeeks.org/absolute-and-relative-imports-in-python/)
- [Understanding Relative Imports](https://www.pythoncentral.io/relative-imports-in-python/)

##### 3. Quand Utiliser Chaque Type ?

**Utilisez les imports absolus quand** :
- Vous importez depuis la bibliothèque standard
- Vous importez depuis des packages tiers
- Clarté maximale requise
- Code destiné à être exécuté directement

**Utilisez les imports relatifs quand** :
- À l'intérieur d'un package
- Structure de package complexe
- Package destiné à être déplacé/réutilisé

**Ressources** :
- [Python Import Best Practices](https://www.python.org/dev/peps/pep-0008/#imports)

#### 📝 Fichiers à Créer pour la Partie III

- `ft_pathway_debate.py` - Script de démonstration (à la racine)
- `alchemy/transmutation/__init__.py` - Initialiseur du package transmutation
- `alchemy/transmutation/basic.py` - Transmutations basiques
- `alchemy/transmutation/advanced.py` - Transmutations avancées

#### 🔧 Instructions

Créez une structure de laboratoire complexe et apprenez quand utiliser chaque type de chemin.

**alchemy/transmutation/basic.py** doit contenir :
```python
# Import absolu depuis la racine du package
from alchemy.elements import create_fire, create_earth

def lead_to_gold():
    fire_result = create_fire()
    return f"Lead transmuted to gold using {fire_result}"

def stone_to_gem():
    earth_result = create_earth()
    return f"Stone transmuted to gem using {earth_result}"
```

**alchemy/transmutation/advanced.py** doit contenir :
```python
# Import relatif depuis le même package
from .basic import lead_to_gold
# Import relatif depuis le package parent
from ..potions import healing_potion

def philosophers_stone():
    lead_result = lead_to_gold()
    potion_result = healing_potion()
    return f"Philosopher's stone created using {lead_result} and {potion_result}"

def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
```

**alchemy/transmutation/__init__.py** doit contenir :
```python
from .basic import lead_to_gold, stone_to_gem
from .advanced import philosophers_stone, elixir_of_life
```

💡 **Point Clé** : Le `__init__.py` du package transmutation expose toutes les fonctions de transmutation pour un accès facile. Cela démontre l'organisation au niveau du package.

#### 📤 Exemple de Sortie Attendue

```bash
$> python3 ft_pathway_debate.py
=== Pathway Debate Mastery ===

Testing Absolute Imports (from basic.py):
lead_to_gold(): Lead transmuted to gold using Fire element created
stone_to_gem(): Stone transmuted to gem using Earth element created

Testing Relative Imports (from advanced.py):
philosophers_stone(): Philosopher's stone created using Lead transmuted to gold using Fire element created and Healing potion brewed with Fire element created and Water element created
elixir_of_life(): Elixir of life: eternal youth achieved!

Testing Package Access:
alchemy.transmutation.lead_to_gold(): Lead transmuted to gold using Fire element created
alchemy.transmutation.philosophers_stone(): Philosopher's stone created using Lead transmuted to gold using Fire element created and Healing potion brewed with Fire element created and Water element created

Both pathways work! Absolute: clear, Relative: concise
```

#### 💭 Questions de Réflexion

1. Quand un alchimiste devrait-il utiliser des chemins absolus vs relatifs ?
2. Quels sont les compromis entre clarté et concision ?
3. Comment la structure du package influence-t-elle le choix ?

---

### V.4 - Partie IV : Briser la Malédiction Circulaire

#### 🎯 Objectif

Apprendre à identifier et briser la redoutable Malédiction de Dépendance Circulaire - quand les sorts essaient de s'invoquer mutuellement dans une boucle infinie, menaçant de détruire votre laboratoire !

#### 📚 Concepts à Maîtriser

##### 1. Qu'est-ce qu'une Dépendance Circulaire ?

Une dépendance circulaire se produit quand deux modules ou plus s'importent mutuellement :

```python
# module_a.py
from module_b import function_b

def function_a():
    return function_b()

# module_b.py
from module_a import function_a  # ⚠️ Problème circulaire !

def function_b():
    return function_a()
```

**Pourquoi c'est dangereux** :
- `ImportError` ou comportements imprévisibles
- Code difficile à tester
- Mauvaise architecture
- Problèmes de maintenance

**Ressources** :
- [Circular Imports in Python](https://stackabuse.com/python-circular-imports/)
- [Understanding Circular Dependencies](https://www.pythoncentral.io/circular-import-invalid/)
- [How to Avoid Circular Imports](https://realpython.com/python-import/#import-pitfalls-circular-imports)

##### 2. Méthodes pour Briser le Cercle

**Méthode 1 : Import Tardif (Late Import)**

Importer à l'intérieur d'une fonction plutôt qu'au niveau du module :

```python
# module_a.py
def function_a():
    from module_b import function_b  # Import à l'intérieur
    return function_b()
```

✅ Avantages : Simple, rapide à implémenter
❌ Inconvénients : Import répété si fonction appelée souvent

**Méthode 2 : Injection de Dépendance**

Passer les dépendances en paramètres :

```python
def function_a(validator_func):
    result = validator_func(data)
    return result
```

✅ Avantages : Testable, flexible, propre
❌ Inconvénients : Plus verbeux

**Méthode 3 : Module Partagé**

Créer un troisième module pour les fonctions communes :

```python
# utils.py
def shared_function():
    pass

# module_a.py
from utils import shared_function

# module_b.py
from utils import shared_function
```

✅ Avantages : Architecture propre, réutilisable
❌ Inconvénients : Nécessite restructuration

**Ressources** :
- [Dependency Injection in Python](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/)
- [Python Design Patterns](https://refactoring.guru/design-patterns/python)

##### 3. Bonnes Pratiques de Design

Pour éviter les dépendances circulaires :
- Concevoir une hiérarchie claire
- Suivre le principe de responsabilité unique
- Utiliser des interfaces/abstractions
- Réfléchir à l'architecture avant de coder

**Ressources** :
- [SOLID Principles in Python](https://realpython.com/solid-principles-python/)

#### 📝 Fichiers à Créer pour la Partie IV

- `ft_circular_curse.py` - Script de démonstration (à la racine)
- `alchemy/grimoire/__init__.py` - Initialiseur du package grimoire
- `alchemy/grimoire/spellbook.py` - Enregistre les sorts et leurs effets
- `alchemy/grimoire/validator.py` - Valide les ingrédients des sorts

#### 🔧 Instructions

Créez un scénario qui pourrait causer des imports circulaires, puis apprenez les techniques anciennes pour briser la malédiction.

**alchemy/grimoire/__init__.py** doit contenir :
```python
from .spellbook import record_spell
from .validator import validate_ingredients
```

**alchemy/grimoire/validator.py** doit contenir :
```python
def validate_ingredients(ingredients: str) -> str:
    """
    Valide les ingrédients d'un sort.
    
    Args:
        ingredients: Chaîne contenant les ingrédients
        
    Returns:
        "[ingredients] - VALID" ou "[ingredients] - INVALID"
    """
    valid_ingredients = ["fire", "water", "earth", "air"]
    
    # Vérifie si au moins un ingrédient valide est présent
    for valid in valid_ingredients:
        if valid in ingredients.lower():
            return f"{ingredients} - VALID"
    
    return f"{ingredients} - INVALID"
```

**alchemy/grimoire/spellbook.py** doit contenir :
```python
def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Enregistre un sort après validation des ingrédients.
    
    Utilise un import tardif pour éviter la dépendance circulaire.
    
    Args:
        spell_name: Nom du sort
        ingredients: Ingrédients du sort
        
    Returns:
        Message indiquant si le sort a été enregistré ou rejeté
    """
    # Import tardif pour éviter la dépendance circulaire
    from .validator import validate_ingredients
    
    validation_result = validate_ingredients(ingredients)
    
    if "VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell rejected: {spell_name} ({validation_result})"
```

💡 **Point Clé** : NE créez PAS de véritables imports circulaires dans votre code ! Démontrez votre compréhension en expliquant le problème et en implémentant une méthode de solution.

#### 📤 Exemple de Sortie Attendue

```bash
$> python3 ft_circular_curse.py
=== Circular Curse Breaking ===

Testing ingredient validation:
validate_ingredients("fire air"): fire air - VALID
validate_ingredients("dragon scales"): dragon scales - INVALID

Testing spell recording with validation:
record_spell("Fireball", "fire air"): Spell recorded: Fireball (fire air - VALID)
record_spell("Dark Magic", "shadow"): Spell rejected: Dark Magic (shadow - INVALID)

Testing late import technique:
record_spell("Lightning", "air"): Spell recorded: Lightning (air - VALID)

Circular dependency curse avoided using late imports!
All spells processed safely!
```

#### 💭 Questions de Réflexion

1. Qu'est-ce qui cause la Malédiction de Dépendance Circulaire et pourquoi est-elle dangereuse ?
2. Quelle technique de rupture de malédiction est la plus appropriée pour différentes situations ?
3. Comment peut-on concevoir du code pour éviter complètement ces problèmes ?

---

## Chapitre VI - Instructions de Soumission

Rendez votre travail dans votre dépôt Git comme d'habitude. Seul le travail dans votre dépôt sera évalué pendant la défense.

### 📂 Organisation des Fichiers

Tous les fichiers et répertoires doivent être créés à la racine de votre dépôt Git :

```
.
├── ft_sacred_scroll.py                    # Script Partie I
├── ft_import_transmutation.py             # Script Partie II
├── ft_pathway_debate.py                   # Script Partie III
├── ft_circular_curse.py                   # Script Partie IV
└── alchemy/                               # Package principal
    ├── __init__.py                        # Contrôle l'interface du package
    ├── elements.py                        # Fonctions élémentaires
    ├── potions.py                         # Fonctions de potions
    ├── transmutation/                     # Sous-package transmutation
    │   ├── __init__.py
    │   ├── basic.py                       # Transmutations basiques
    │   └── advanced.py                    # Transmutations avancées
    └── grimoire/                          # Sous-package grimoire
        ├── __init__.py
        ├── spellbook.py                   # Enregistrement de sorts
        └── validator.py                   # Validation d'ingrédients
```

### 📝 Points de Défense

Pendant l'évaluation, on pourra vous demander de :
- Expliquer les mécanismes d'importation
- Démontrer différents styles d'import
- Modifier votre laboratoire alchimique
- Justifier vos choix d'architecture

Assurez-vous de comprendre les quatre mystères sacrés, pas seulement l'implémentation.

### ✨ Conseils Finaux

- Concentrez-vous sur un code propre et bien organisé qui démontre clairement le système d'importation de Python
- Les fonctions alchimiques doivent être simples - la complexité réside dans la maîtrise des mystères de l'import
- Testez chaque partie indépendamment avant de passer à la suivante
- Commentez votre code pour expliquer les choix d'import

---

## 📚 Ressources Supplémentaires Générales

### Documentation Officielle
- [The import system (Python Docs)](https://docs.python.org/3/reference/import.html)
- [Modules (Python Tutorial)](https://docs.python.org/3/tutorial/modules.html)
- [PEP 8 - Style Guide](https://peps.python.org/pep-0008/)

### Tutoriels Complets
- [Real Python - Python Modules and Packages: An Introduction](https://realpython.com/python-modules-packages/)
- [Real Python - Absolute vs Relative Imports](https://realpython.com/absolute-vs-relative-python-imports/)
- [Python Packaging User Guide](https://packaging.python.org/)

### Articles Avancés
- [Understanding Python's Import Statement](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)
- [Python Import System Deep Dive](https://tenthousandmeters.com/blog/python-behind-the-scenes-11-how-the-python-import-system-works/)

### Vidéos
- [Corey Schafer - Python Modules](https://www.youtube.com/watch?v=CqvZ3vGoGs0)
- [ArjanCodes - Python Imports Explained](https://www.youtube.com/watch?v=rGQKHpjMn_M)

### Exercices Pratiques
- [Python Exercises - Modules](https://www.practicepython.org/)
- [Exercism - Python Track](https://exercism.org/tracks/python)

---

## 🎓 Conclusion

Ce projet vous permettra de maîtriser :
1. ✅ La structure des packages Python avec `__init__.py`
2. ✅ Les différents styles d'import et leurs cas d'usage
3. ✅ La différence entre imports absolus et relatifs
4. ✅ Comment éviter et résoudre les dépendances circulaires
5. ✅ Les bonnes pratiques d'organisation de code Python

**Rappel Final** : Cette activité nécessite une maîtrise solide des fondamentaux Python. Si vous avez des difficultés avec la syntaxe Python de base, les fonctions, les classes, les listes, les dictionnaires ou la gestion des erreurs, renforcez d'abord ces compétences. La maîtrise des imports s'appuie sur ces fondations - tenter cette activité sans elles mènera à la confusion et à la frustration.

Bon courage, jeune alchimiste ! 🧙‍♂️✨
