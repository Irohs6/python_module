# 🎮 Data Quest: The Pixel Dimension
## 📘 Sujet Complet Traduit et Détaillé - Maîtrise des Structures de Données Python

---

## 🌟 Introduction au Projet

Bienvenue dans **Data Quest: The Pixel Dimension** ! Après avoir conquis les bases de Python, maîtrisé les classes et dompté les exceptions, il est temps de devenir un **magicien des données** !

### 🎯 Objectif du Projet
Construire **"PixelMetrics 3000"** — une plateforme d'analytics gaming épique qui démontre la maîtrise des structures de données Python.

### 🗺️ Parcours d'Apprentissage
Pense à ce projet comme un voyage Pokémon, mais au lieu de capturer des créatures, tu collectes des **super-pouvoirs de données** :

| Niveau | Exercice | Structure | Concept |
|--------|----------|-----------|---------|
| **0** | 🎯 Command Quest | `sys.argv` | Communication ligne de commande |
| **1** | 📊 Score Cruncher | `Lists` | Analyser des séquences de scores |
| **2** | 📍 Position Tracker | `Tuples` | Coordonnées 3D immuables |
| **3** | 🏆 Achievement Hunter | `Sets` | Collections uniques |
| **4** | 🎒 Inventory Master | `Dicts` | Systèmes complexes clé-valeur |
| **5** | 🌊 Stream Wizard | `Generators` | Traitement de flux infinis |
| **6** | ⚗️ Data Alchemist | `Comprehensions` | Transformations élégantes |

---

## 📋 Instructions Générales

### ✅ Règles Obligatoires

#### Langage & Standards
```python
# Version Python
Python 3.10+

# Standard de code
flake8 (PEP 8)

# Type hints OBLIGATOIRES
def calculate_score(points: int) -> float:
    return points * 1.5
```

#### Imports Autorisés
```python
# ✅ Autorisé
import sys              # Pour sys.argv uniquement
import math             # Pour Ex2 (math.sqrt)
from collections import Counter  # Si nécessaire

# ❌ INTERDIT
import os
import json
import file operations
```

#### Gestion d'Erreurs
```python
# Toujours utiliser try/except pour éviter les crashes
try:
    score = int(user_input)
except ValueError:
    print("Erreur: entrée invalide")
    # Le programme continue, ne crash pas!
```

### 📁 Structure de Soumission
```
P03/
├── ex0/
│   └── ft_command_quest.py
├── ex1/
│   └── ft_score_analytics.py
├── ex2/
│   └── ft_coordinate_system.py
├── ex3/
│   └── ft_achievement_tracker.py
├── ex4/
│   └── ft_inventory_system.py
├── ex5/
│   └── ft_data_stream.py
└── ex6/
    └── ft_analytics_dashboard.py
```

---

## 📚 Exercice 0: Command Quest

### 🎯 Objectif
Maîtriser **sys.argv** pour recevoir des arguments depuis la ligne de commande.

### 📖 Concept Expliqué

#### Qu'est-ce que sys.argv?
```python
import sys

# Quand tu exécutes: python script.py hello world 42
# Python crée automatiquement:
sys.argv = ['script.py', 'hello', 'world', '42']
#           ↑ argv[0]    ↑ argv[1] ↑ argv[2] ↑ argv[3]
```

#### Schéma Visuel
```
Terminal:  python3 ft_command_quest.py hello world 42
               ↓          ↓             ↓      ↓     ↓
sys.argv = [argv[0],  argv[1],    argv[2], argv[3]]
           [script.py,  'hello',    'world', '42'  ]
                ↑                        ↑
          Nom du script          Arguments utilisateur
```

### 📋 Exigences

| Requis | Description |
|--------|-------------|
| **Imports** | `sys`, `sys.argv`, `len()`, `print()` |
| **Fonctionnalités** | Afficher nom du script, nombre d'arguments, liste des arguments |
| **Cas à gérer** | Aucun argument, plusieurs arguments, arguments avec espaces |
| **Output** | Format exact selon l'exemple du sujet |

### 💻 Exemple de Code Structure

```python
#!/usr/bin/env python3
import sys

def process_command_line():
    """Traite et affiche les arguments de la ligne de commande."""
    print("=== Command Quest ===")
    
    # Récupérer tous les arguments
    args = sys.argv
    program_name = args[0]
    arguments = args[1:]  # Tout sauf le nom du programme
    
    # Afficher le nom du programme
    print(f"Program name: {program_name}")
    
    # Cas 1: Aucun argument fourni
    if len(arguments) == 0:
        print("No arguments provided!")
    
    # Cas 2: Arguments fournis
    else:
        print(f"Arguments received: {len(arguments)}")
        for i, arg in enumerate(arguments, 1):  # Commence à 1
            print(f"Argument {i}: {arg}")
    
    # Total (programme + arguments)
    print(f"Total arguments: {len(args)}")

if __name__ == "__main__":
    process_command_line()
```

### 📤 Exemples d'Exécution

#### Cas 1: Sans arguments
```bash
$ python3 ft_command_quest.py
=== Command Quest ===
No arguments provided!
Program name: ft_command_quest.py
Total arguments: 1
```

#### Cas 2: Avec arguments
```bash
$ python3 ft_command_quest.py hello world 42
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 3
Argument 1: hello
Argument 2: world
Argument 3: 42
Total arguments: 4
```

#### Cas 3: Argument avec espaces
```bash
$ python3 ft_command_quest.py "Data Quest"
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 1
Argument 1: Data Quest
Total arguments: 2
```

### 💡 Points Clés
- `sys.argv[0]` = toujours le nom du script
- `sys.argv[1:]` = les arguments fournis par l'utilisateur
- Les guillemets `" "` permettent de grouper plusieurs mots en 1 argument

---

## 📚 Exercice 1: Score Cruncher

### 🎯 Objectif
Maîtriser les **Lists** en analysant des scores de joueurs.

### 📖 Concept Expliqué

#### Pourquoi les Lists?
```python
# Lists = Séquences ordonnées et mutables
scores = [1500, 2300, 1800]

# ✅ Caractéristiques:
- Ordre préservé      : scores[0] = 1500, scores[1] = 2300
- Mutable             : scores.append(2100)
- Accès par index     : scores[0]
- Opérations rapides  : sum(), max(), min(), len()
```

#### Schéma Visuel
```
Command Line:  python3 ft_score_analytics.py 1500 2300 1800
                                            ↓     ↓     ↓
                                     Parse & Convert to int
                                            ↓     ↓     ↓
List:                        scores = [1500, 2300, 1800]
                                       ↓     ↓     ↓
Calculs:                    sum() max() min() len() range()
                                       ↓
Statistiques:                Total: 5600, Average: 1866.7
                             High: 2300, Low: 1500, Range: 800
```

### 📋 Exigences

| Requis | Description |
|--------|-------------|
| **Structure** | `Lists` pour stocker les scores |
| **Imports** | `sys.argv`, fonctions built-in (sum, max, min, len, int) |
| **Try/Except** | Gérer les valeurs non-numériques (ex: "banana") |
| **Calculs** | Total, Average, High, Low, Range |
| **Format** | Output exact selon le sujet |

### 💻 Exemple de Code Structure

```python
#!/usr/bin/env python3
import sys

def parse_scores(args: list[str]) -> list[int]:
    """Parse les arguments et convertit en liste d'entiers."""
    scores = []
    for arg in args:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            # Ignore les valeurs invalides, continue avec les autres
            print(f"Warning: '{arg}' is not a valid score, ignored.")
    return scores

def compute_stats(scores: list[int]) -> dict:
    """Calcule les statistiques sur les scores."""
    return {
        "Total players": len(scores),
        "Total score": sum(scores),
        "Average score": sum(scores) / len(scores),
        "High score": max(scores),
        "Low score": min(scores),
        "Score range": max(scores) - min(scores)
    }

def print_results(scores: list[int], stats: dict) -> None:
    """Affiche les résultats."""
    print(f"Scores processed: {scores}")  # ← Pas de brackets supplémentaires!
    for key, value in stats.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    args = sys.argv[1:]  # Ignorer le nom du script
    
    if not args:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        sys.exit(0)
    
    scores = parse_scores(args)
    
    if not scores:
        print("No valid scores found!")
        sys.exit(0)
    
    stats = compute_stats(scores)
    
    print("=== Player Score Analytics ===")
    print_results(scores, stats)
```

### 📤 Exemples d'Exécution

#### Cas 1: Scores valides
```bash
$ python3 ft_score_analytics.py 1500 2300 1800 2100 1950
=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800, 2100, 1950]
Total players: 5
Total score: 9650
Average score: 1930.0
High score: 2300
Low score: 1500
Score range: 800
```

#### Cas 2: Sans arguments
```bash
$ python3 ft_score_analytics.py
=== Player Score Analytics ===
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
```

#### Cas 3: Avec valeurs invalides
```bash
$ python3 ft_score_analytics.py 1500 banana 2300 abc 1800
Warning: 'banana' is not a valid score, ignored.
Warning: 'abc' is not a valid score, ignored.
=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800]
Total players: 3
Total score: 5600
Average score: 1866.67
High score: 2300
Low score: 1500
Score range: 800
```

### 💡 Points Clés
- **Lists** parfaites pour données séquentielles
- **Try/except** évite les crashes sur données invalides
- Built-ins Python (sum, max, min) très efficaces pour calculs

---

## 📚 Exercice 2: Position Tracker

### 🎯 Objectif
Maîtriser les **Tuples** pour gérer des coordonnées 3D immuables.

### 📖 Concept Expliqué

#### Pourquoi les Tuples?

```python
# Tuples = Séquences ordonnées et IMMUABLES
position = (10, 20, 5)  # x, y, z

# ✅ Caractéristiques:
- Immuable            : position[0] = 15  ← ERREUR!
- Ordre préservé      : position[0] = x, position[1] = y, position[2] = z
- Plus léger          : Moins de mémoire que les lists
- Unpacking élégant   : x, y, z = position
- Hashable            : Peut être clé de dict
```

#### Tuple vs List - Comparaison Visuelle

```
LIST (Mutable)              TUPLE (Immutable)
┌─────────────────┐        ┌─────────────────┐
│ [10, 20, 5]     │        │ (10, 20, 5)     │
│  ↓   ↓   ↓      │        │  ↓   ↓   ↓      │
│ Peut changer ✅  │        │ Figé pour toujours ❌│
│ list[0] = 99 ✅  │        │ tuple[0] = 99 ❌ │
│ Plus lourd       │        │ Plus léger       │
│ Données changeantes│      │ Données fixes    │
└─────────────────┘        └─────────────────┘

Utilise LIST si:            Utilise TUPLE si:
- Ajout/Suppression        - Coordonnées fixes
- Données évolutives       - RGB colors
- Order matters            - Configuration
```

#### Formule de Distance 3D

```python
# Distance Euclidienne 3D
# Pour points P1(x1,y1,z1) et P2(x2,y2,z2):

distance = √[(x2-x1)² + (y2-y1)² + (z2-z1)²]

# C'est Pythagore en 3D!
# 2D: √(x² + y²)
# 3D: √(x² + y² + z²)

# En Python:
import math
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
```

### 📋 Exigences

| Requis | Description |
|--------|-------------|
| **Structure** | `Tuples` pour coordonnées (x, y, z) |
| **Imports** | `math.sqrt()`, `tuple()`, `int()`, `split()` |
| **Fonctionnalités** | Parsing de "x,y,z", calcul distance, unpacking |
| **Try/Except** | Gérer erreurs de parsing ("abc,def,ghi") |
| **Format** | **DEMO HARDCODÉE** (pas sys.argv ici!) |

### 💻 Exemple de Code Structure

```python
#!/usr/bin/env python3
import math

def parse_coordinate(coord_str: str) -> tuple[int, int, int] | None:
    """Parse une string 'x,y,z' en tuple (x, y, z)."""
    print(f'Parsing coordinates: "{coord_str}"')
    try:
        parts = coord_str.split(',')
        if len(parts) != 3:
            raise ValueError("Expected exactly 3 values (x,y,z)")
        
        x, y, z = int(parts[0]), int(parts[1]), int(parts[2])
        return (x, y, z)
    
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details- Type: {type(e).__name__}, Args: {e.args}")
        return None

def calculate_distance(p1: tuple[int, int, int], 
                      p2: tuple[int, int, int]) -> float:
    """Calcule la distance 3D entre deux points."""
    x1, y1, z1 = p1  # Unpacking!
    x2, y2, z2 = p2
    
    # Formule Euclidienne 3D
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance

def main():
    """Démonstration hardcodée (pas de sys.argv)."""
    print("=== Game Coordinate System ===\n")
    
    # Demo 1: Position créée
    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")
    
    origin = (0, 0, 0)
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}\n")
    
    # Demo 2: Parsing valide
    pos2 = parse_coordinate("3,4,0")
    if pos2:
        print(f"Parsed position: {pos2}")
        dist2 = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2:.1f}\n")
    
    # Demo 3: Parsing invalide
    pos3 = parse_coordinate("abc,def,ghi")
    print()
    
    # Demo 4: Unpacking
    if pos2:
        print("Unpacking demonstration:")
        x, y, z = pos2  # ← Magic unpacking!
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    main()
```

### 📤 Exemple d'Exécution

```bash
$ python3 ft_coordinate_system.py
=== Game Coordinate System ===

Position created: (10, 20, 5)
Distance between (0, 0, 0) and (10, 20, 5): 22.91

Parsing coordinates: "3,4,0"
Parsed position: (3, 4, 0)
Distance between (0, 0, 0) and (3, 4, 0): 5.0

Parsing coordinates: "abc,def,ghi"
Parsing invalid coordinates: "abc,def,ghi"
Error parsing coordinates: invalid literal for int() with base 10: 'abc'
Error details- Type: ValueError, Args: ("invalid literal for int() with base 10: 'abc'",)

Unpacking demonstration:
Player at x=3, y=4, z=0
Coordinates: X=3, Y=4, Z=0
```

### 💡 Points Clés
- **Tuples immuables** = parfaits pour coordonnées qui ne changent pas
- **Unpacking** (`x, y, z = position`) rend le code lisible
- **Demo hardcodée** (pas de sys.argv pour cet exercice)

---

## 📚 Exercice 3: Achievement Hunter

### 🎯 Objectif
Maîtriser les **Sets** pour gérer des collections uniques.

### 📖 Concept Expliqué

#### Pourquoi les Sets?

```python
# Sets = Collections NON ordonnées d'éléments UNIQUES
achievements = {'first_kill', 'level_10', 'boss_slayer'}

# ✅ Caractéristiques:
- Éléments uniques     : Pas de doublons automatiquement
- Non ordonnés         : Pas d'index [0], [1]...
- Test O(1)            : 'first_kill' in achievements → RAPIDE!
- Opérations ensembles : union, intersection, difference
```

#### Opérations de Sets - Schéma Visuel

```
Alice = {A, B, C, D}
Bob   = {B, C, E, F}

┌─────────────────────────────────────────────────┐
│ UNION (|) - Tout ce qui est dans A OU B        │
│ Alice | Bob = {A, B, C, D, E, F}               │
│                                                 │
│   ┌─────────┐                                  │
│   │  A   D  │                                  │
│   │    ┌────┼────┐                             │
│   │    │ B C│ E F│                             │
│   └────┼────┘    │                             │
│        └─────────┘                             │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ INTERSECTION (&) - Ce qui est dans A ET B       │
│ Alice & Bob = {B, C}                            │
│                                                 │
│   ┌─────────┐                                  │
│   │  A   D  │                                  │
│   │    ┌────┼────┐                             │
│   │    │ B C│ E F│  ← Zone commune             │
│   └────┼────┘    │                             │
│        └─────────┘                             │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ DIFFERENCE (-) - Ce qui est dans A mais pas B   │
│ Alice - Bob = {A, D}                            │
│                                                 │
│   ┌─────────┐                                  │
│   │  A   D  │  ← Uniquement Alice              │
│   │    ┌────┼────┐                             │
│   │    │ B C│ E F│                             │
│   └────┼────┘    │                             │
│        └─────────┘                             │
└─────────────────────────────────────────────────┘
```

### 📋 Exigences

| Requis | Description |
|--------|-------------|
| **Structure** | `Sets` pour stocker achievements |
| **Imports** | `set()`, `len()`, `union()`, `intersection()`, `difference()` |
| **Opérations** | Union (tous), Intersection (communs), Difference (uniques) |
| **Demo** | 3 joueurs (alice, bob, charlie) avec leurs achievements |
| **Format** | Hardcodé (pas de sys.argv) |

### 💻 Exemple de Code Structure

```python
#!/usr/bin/env python3

def main():
    """Système de tracking des achievements."""
    print("=== Achievement Tracker System ===\n")
    
    # Définir les achievements de chaque joueur
    alice_achievements = {
        'first_kill', 'level_10', 
        'treasure_hunter', 'speed_demon'
    }
    
    bob_achievements = {
        'first_kill', 'level_10', 
        'boss_slayer', 'collector'
    }
    
    charlie_achievements = {
        'level_10', 'treasure_hunter', 
        'boss_slayer', 'speed_demon', 
        'perfectionist'
    }
    
    # Afficher les achievements
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}\n")
    
    print("=== Achievement Analytics ===")
    
    # UNION: Tous les achievements uniques
    all_achievements = alice_achievements.union(
        bob_achievements.union(charlie_achievements)
    )
    # Ou: alice_achievements | bob_achievements | charlie_achievements
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")
    
    # INTERSECTION: Achievements communs à TOUS
    common_all = alice_achievements.intersection(
        bob_achievements.intersection(charlie_achievements)
    )
    # Ou: alice_achievements & bob_achievements & charlie_achievements
    print(f"Common to all players: {common_all}")
    
    # RARE: Achievements que 1 seul joueur a
    # (Méthode avec comptage)
    from collections import Counter
    all_achs_list = (list(alice_achievements) + 
                    list(bob_achievements) + 
                    list(charlie_achievements))
    counts = Counter(all_achs_list)
    rare = {ach for ach, count in counts.items() if count == 1}
    print(f"Rare achievements (1 player): {rare}\n")
    
    # Comparaisons 2 à 2
    print(f"Alice vs Bob common: {alice_achievements & bob_achievements}")
    print(f"Alice unique: {alice_achievements - bob_achievements}")
    print(f"Bob unique: {bob_achievements - alice_achievements}")

if __name__ == "__main__":
    main()
```

### 📤 Exemple d'Exécution

```bash
$ python3 ft_achievement_tracker.py
=== Achievement Tracker System ===

Player alice achievements: {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
Player bob achievements: {'first_kill', 'level_10', 'boss_slayer', 'collector'}
Player charlie achievements: {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

=== Achievement Analytics ===
All unique achievements: {'boss_slayer', 'collector', 'first_kill', 'level_10', 'perfectionist', 'speed_demon', 'treasure_hunter'}
Total unique achievements: 7

Common to all players: {'level_10'}
Rare achievements (1 player): {'collector', 'perfectionist'}

Alice vs Bob common: {'first_kill', 'level_10'}
Alice unique: {'speed_demon', 'treasure_hunter'}
Bob unique: {'boss_slayer', 'collector'}
```

### 💡 Points Clés
- **Sets** éliminent automatiquement les doublons
- **Opérations mathématiques** (union, intersection) très puissantes
- **Test d'appartenance O(1)** ultra-rapide

---

## 📚 Exercice 4: Inventory Master

### 🎯 Objectif
Maîtriser les **Dictionaries** pour un système d'inventaire.

### 📖 Concept Expliqué

#### Pourquoi les Dictionaries?

```python
# Dicts = Paires clé-valeur, lookup O(1)
inventory = {
    'sword': 1,
    'potion': 5,
    'shield': 2
}

# ✅ Caractéristiques:
- Lookup O(1)         : inventory['sword'] → INSTANTANÉ
- Clé unique          : Chaque item une seule clé
- Valeur mutable      : inventory['potion'] = 10
- Itération facile    : .keys(), .values(), .items()
```

#### Dict Methods - Guide Visuel

```python
inventory = {'sword': 1, 'potion': 5, 'shield': 2}

┌──────────────────────────────────────────────┐
│ MÉTHODES ESSENTIELLES                        │
├──────────────────────────────────────────────┤
│ .keys()   → ['sword', 'potion', 'shield']   │
│ .values() → [1, 5, 2]                        │
│ .items()  → [('sword', 1), ('potion', 5)..] │
│ .get(key, default) → Safe access             │
│ 'sword' in inventory → True/False            │
└──────────────────────────────────────────────┘
```

### 📋 Exigences

| Requis | Description |
|--------|-------------|
| **Structure** | `Dict` pour inventaire {item: quantity} |
| **Input** | sys.argv avec format `item:quantity` |
| **Parsing** | Extraire item et quantité de chaque arg |
| **Stats** | Total items, types uniques, most/least abundant |
| **Catégories** | Abundant (4+), Moderate (2-3), Scarce (1) |
| **Suggestions** | Items à restock (quantité = 1) |
| **Demo** | Utilisation de .keys(), .values(), .items() |

### 💻 Exemple de Code Structure

```python
#!/usr/bin/env python3
import sys

def parse_inventory(args: list[str]) -> dict[str, int]:
    """Parse les arguments 'item:quantity' en dictionnaire."""
    inventory = {}
    for arg in args:
        try:
            # Split sur ':'
            if ':' not in arg:
                print(f"Warning: '{arg}' invalid format, expected 'item:quantity'")
                continue
            
            item, qty_str = arg.split(':', 1)
            quantity = int(qty_str)
            
            if quantity < 0:
                print(f"Warning: negative quantity for '{item}', ignored")
                continue
            
            inventory[item] = quantity
        
        except ValueError:
            print(f"Warning: '{arg}' has invalid quantity, ignored")
    
    return inventory

def calculate_stats(inventory: dict[str, int]) -> dict:
    """Calcule les statistiques d'inventaire."""
    total_items = sum(inventory.values())
    unique_types = len(inventory.keys())
    
    # Most/Least abundant
    most_item = max(inventory, key=inventory.get)
    least_item = min(inventory, key=inventory.get)
    
    return {
        'total': total_items,
        'unique': unique_types,
        'most': (most_item, inventory[most_item]),
        'least': (least_item, inventory[least_item])
    }

def categorize_items(inventory: dict[str, int]) -> dict:
    """Catégorise les items par abondance."""
    categories = {
        'Abundant': {},   # 4+
        'Moderate': {},   # 2-3
        'Scarce': {}      # 1
    }
    
    for item, qty in inventory.items():
        if qty >= 4:
            categories['Abundant'][item] = qty
        elif qty >= 2:
            categories['Moderate'][item] = qty
        else:
            categories['Scarce'][item] = qty
    
    return categories

def get_restock_suggestions(inventory: dict[str, int]) -> list[str]:
    """Liste les items à restockrer (qty = 1)."""
    return [item for item, qty in inventory.items() if qty == 1]

def calculate_percentages(inventory: dict[str, int]) -> dict[str, float]:
    """Calcule les pourcentages de chaque item."""
    total = sum(inventory.values())
    return {item: (qty / total * 100) for item, qty in inventory.items()}

def print_inventory_report(inventory: dict[str, int]) -> None:
    """Affiche le rapport complet d'inventaire."""
    stats = calculate_stats(inventory)
    categories = categorize_items(inventory)
    restock = get_restock_suggestions(inventory)
    percentages = calculate_percentages(inventory)
    
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {stats['total']}")
    print(f"Unique item types: {stats['unique']}\n")
    
    print("=== Current Inventory ===")
    # Trier par quantité décroissante
    sorted_inv = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for item, qty in sorted_inv:
        unit = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({percentages[item]:.1f}%)")
    
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {stats['most'][0]} ({stats['most'][1]} units)")
    print(f"Least abundant: {stats['least'][0]} ({stats['least'][1]} unit)")
    
    print("\n=== Item Categories ===")
    for category, items in categories.items():
        if items:
            print(f"{category}: {items}")
    
    print("\n=== Management Suggestions ===")
    if restock:
        print(f"Restock needed: {restock}")
    else:
        print("No items need restocking")
    
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup- 'sword' in inventory: {'sword' in inventory}")

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if not args:
        print("=== Inventory System Analysis ===")
        print("No items provided. Usage: python3 ft_inventory_system.py item1:qty1 item2:qty2 ...")
        sys.exit(0)
    
    inventory = parse_inventory(args)
    
    if not inventory:
        print("No valid items found!")
        sys.exit(0)
    
    print_inventory_report(inventory)
```

### 📤 Exemple d'Exécution

```bash
$ python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1
=== Inventory System Analysis ===
Total items in inventory: 12
Unique item types: 5

=== Current Inventory ===
potion: 5 units (41.7%)
armor: 3 units (25.0%)
shield: 2 units (16.7%)
sword: 1 unit (8.3%)
helmet: 1 unit (8.3%)

=== Inventory Statistics ===
Most abundant: potion (5 units)
Least abundant: sword (1 unit)

=== Item Categories ===
Moderate: {'potion': 5}
Scarce: {'sword': 1, 'shield': 2, 'armor': 3, 'helmet': 1}

=== Management Suggestions ===
Restock needed: ['sword', 'helmet']

=== Dictionary Properties Demo ===
Dictionary keys: ['sword', 'potion', 'shield', 'armor', 'helmet']
Dictionary values: [1, 5, 2, 3, 1]
Sample lookup- 'sword' in inventory: True
```

### 💡 Points Clés
- **Dicts** parfaits pour mappings clé-valeur
- **Parsing** du format `item:quantity` avec split
- **Methods** (.keys(), .values(), .items()) essentiels

---

## 📚 Exercice 5: Stream Wizard

### 🎯 Objectif
Maîtriser les **Generators** pour traitement de flux mémoire-efficace.

### 📖 Concept Expliqué

#### Pourquoi les Generators?

```python
# PROBLÈME: List charge TOUT en mémoire
def million_numbers_list():
    result = []
    for i in range(1_000_000):
        result.append(i)
    return result  # ← 1 million d'int en RAM (8 MB)

numbers = million_numbers_list()  # BOOM! Mémoire saturée


# SOLUTION: Generator produit UN à la fois
def million_numbers_gen():
    for i in range(1_000_000):
        yield i  # ← Produit 1, pause, continue

numbers = million_numbers_gen()  # Juste 100 bytes!
```

#### Generator vs List - Visualisation

```
┌────────────────────────────────────────────────┐
│ LIST (Eager Evaluation)                        │
├────────────────────────────────────────────────┤
│                                                │
│ def get_numbers():                             │
│     result = []                                │
│     for i in range(1000):                      │
│         result.append(i)                       │
│     return result  # ← Retourne TOUT           │
│                                                │
│ Mémoire: 1000 int × 28 bytes = 28 KB          │
│ Temps avant utilisation: Attendre TOUT        │
└────────────────────────────────────────────────┘

┌────────────────────────────────────────────────┐
│ GENERATOR (Lazy Evaluation)                    │
├────────────────────────────────────────────────┤
│                                                │
│ def get_numbers():                             │
│     for i in range(1000):                      │
│         yield i  # ← Produit 1, PAUSE         │
│                                                │
│ Mémoire: ~100 bytes (juste le generator)      │
│ Temps avant utilisation: IMMÉDIAT             │
│ Produit les valeurs ON-DEMAND                 │
└────────────────────────────────────────────────┘
```

#### Le Keyword `yield`

```python
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n      # ← 1. Retourne n, PAUSE ici
        n -= 1       # ← 2. Continue après next()
    print("Blastoff!")

# Utilisation:
gen = countdown(3)
print(next(gen))  # Affiche "Starting...", retourne 3, PAUSE
print(next(gen))  # Reprend, retourne 2, PAUSE
print(next(gen))  # Reprend, retourne 1, PAUSE
print(next(gen))  # Reprend, affiche "Blastoff!", StopIteration
```

### 📋 Exigences

| Requis | Description |
|--------|-------------|
| **Generators** | Fonctions avec `yield` keyword |
| **Imports** | `next()`, `iter()`, `range()`, `len()` |
| **Demos** | game_event_stream, high_level_filter |
| **Classiques** | fibonacci_generator, prime_generator |
| **Analytics** | Count events, filter high-level, etc. |
| **Hardcodé** | Liste de 50-1000 events prédéfinis |

### 💻 Exemple de Code Structure

```python
#!/usr/bin/env python3
import time

def game_event_stream(events: list[dict]):
    """Generator qui yield les events un par un."""
    for event in events:
        yield event

def high_level_filter(events: list[dict], min_level: int = 10):
    """Generator qui filtre les high-level players."""
    for event in events:
        if event['data']['level'] >= min_level:
            yield event

def event_type_filter(events: list[dict], event_type: str):
    """Generator qui filtre par type d'event."""
    for event in events:
        if event['event_type'] == event_type:
            yield event

def fibonacci_generator(n: int):
    """Generate les n premiers nombres de Fibonacci."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def prime_generator(n: int):
    """Generate les n premiers nombres premiers."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

def process_events(events: list[dict]):
    """Traite les events avec generators."""
    print("=== Game Data Stream Processor ===")
    print(f"Processing {len(events)} game events...\n")
    
    # Afficher premiers events
    count = 0
    for event in game_event_stream(events):
        count += 1
        if count <= 3:  # Afficher seulement les 3 premiers
            player = event['player']
            level = event['data']['level']
            event_type = event['event_type']
            print(f"Event {event['id']}: Player {player} "
                  f"(level {level}) {event_type}")
        elif count == 4:
            print("...")
    
    print(f"\n=== Stream Analytics ===")
    
    # Stats avec generators
    total = 0
    high_level_count = 0
    event_types_count = {}
    
    for event in game_event_stream(events):
        total += 1
        
        # Count high-level
        if event['data']['level'] >= 10:
            high_level_count += 1
        
        # Count par type
        etype = event['event_type']
        event_types_count[etype] = event_types_count.get(etype, 0) + 1
    
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level_count}")
    
    for etype, count in event_types_count.items():
        print(f"{etype.capitalize()} events: {count}")
    
    print("Memory usage: Constant (streaming)")
    
    # Demo generators classiques
    print("\n=== Generator Demonstration ===")
    
    # Fibonacci
    fib = list(fibonacci_generator(10))
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib))}")
    
    # Primes
    primes = list(prime_generator(5))
    print(f"Prime numbers (first 5): {', '.join(map(str, primes))}")

if __name__ == "__main__":
    # Sample data (50 events)
    events = [
        {
            "id": 1,
            "player": "alice",
            "event_type": "kill",
            "timestamp": "2024-01-01T10:00",
            "data": {"level": 15, "score_delta": 100}
        },
        {
            "id": 2,
            "player": "bob",
            "event_type": "treasure",
            "timestamp": "2024-01-01T10:05",
            "data": {"level": 8, "score_delta": 50}
        },
        {
            "id": 3,
            "player": "charlie",
            "event_type": "level_up",
            "timestamp": "2024-01-01T10:10",
            "data": {"level": 12, "score_delta": 200}
        },
        # ... Ajouter 47 events de plus
    ]
    
    start_time = time.time()
    process_events(events)
    end_time = time.time()
    
    print(f"\nProcessing time: {end_time - start_time:.3f} seconds")
```

### 📤 Exemple d'Exécution

```bash
$ python3 ft_data_stream.py
=== Game Data Stream Processor ===
Processing 1000 game events...

Event 1: Player alice (level 5) killed monster
Event 2: Player bob (level 12) found treasure
Event 3: Player charlie (level 8) leveled up
...

=== Stream Analytics ===
Total events processed: 1000
High-level players (10+): 342
Treasure events: 89
Level-up events: 156
Memory usage: Constant (streaming)

=== Generator Demonstration ===
Fibonacci sequence (first 10): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
Prime numbers (first 5): 2, 3, 5, 7, 11

Processing time: 0.045 seconds
```

### 💡 Points Clés
- **yield** transforme une fonction en generator
- **Lazy evaluation** = produit valeurs on-demand
- **Mémoire constante** même avec millions d'events

---

## 📚 Exercice 6: Data Alchemist

### 🎯 Objectif
Maîtriser les **Comprehensions** (list/dict/set) pour transformations élégantes.

### 📖 Concept Expliqué

#### Pourquoi les Comprehensions?

```python
# OLD WAY (Amateur, 5 lignes)
result = []
for item in items:
    if item > 10:
        result.append(item * 2)

# PYTHONIC WAY (Pro, 1 ligne)
result = [item * 2 for item in items if item > 10]

# ✅ Avantages:
- Plus court (1 ligne vs 4)
- Plus rapide (~30% selon contexte)
- Plus lisible (une fois habitué)
- Standard Python professionnel
```

#### Les 3 Types de Comprehensions

```python
# 1. LIST COMPREHENSION
# Structure: [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
# → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(10) if x % 2 == 0]
# → [0, 2, 4, 6, 8]


# 2. DICT COMPREHENSION
# Structure: {key_expr: value_expr for item in iterable if condition}
squares_dict = {x: x**2 for x in range(5)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

inverted = {v: k for k, v in original.items()}
# → Inverse les clés et valeurs


# 3. SET COMPREHENSION
# Structure: {expression for item in iterable if condition}
unique_letters = {char for word in words for char in word}
# → Set de toutes les lettres uniques
```

### 📋 Exigences

| Requis | Description |
|--------|-------------|
| **List Comp** | Filtrage, transformation, extraction |
| **Dict Comp** | Mappings, groupements, comptages |
| **Set Comp** | Déduplication, uniques |
| **Demo** | Exemples clairs de chaque type |
| **Data** | Hardcodée (scores, players, achievements) |
| **Clarté** | Chaque comprehension bien commentée |

### 💻 Exemple de Code Structure

```python
#!/usr/bin/env python3

def demonstrate_list_comprehensions():
    """Démontre les list comprehensions."""
    print("=== List Comprehension Examples ===")
    
    # Sample data
    scores = [2300, 1800, 2150, 1500, 2050, 1200]
    players = ['alice', 'bob', 'charlie', 'diana', 'eve', 'frank']
    
    # Ex1: Filtrage
    high_scorers = [players[i] for i, score in enumerate(scores) 
                    if score > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    
    # Ex2: Transformation
    doubled = [score * 2 for score in scores]
    print(f"Scores doubled: {doubled[:4]}")  # Premiers 4
    
    # Ex3: Extraction conditionnelle
    active = [p for p in players[:3]]
    print(f"Active players: {active}")

def demonstrate_dict_comprehensions():
    """Démontre les dict comprehensions."""
    print("\n=== Dict Comprehension Examples ===")
    
    # Sample data
    players = ['alice', 'bob', 'charlie']
    scores = [2300, 1800, 2150]
    
    # Ex1: Mapping
    player_scores = {p: s for p, s in zip(players, scores)}
    print(f"Player scores: {player_scores}")
    
    # Ex2: Groupement par catégories
    all_scores = [2300, 1800, 2150, 1500, 2050, 1200]
    score_categories = {
        'high': len([s for s in all_scores if s > 2000]),
        'medium': len([s for s in all_scores if 1500 <= s <= 2000]),
        'low': len([s for s in all_scores if s < 1500])
    }
    print(f"Score categories: {score_categories}")
    
    # Ex3: Comptages
    achievement_counts = {
        'alice': 5,
        'bob': 3,
        'charlie': 7
    }
    print(f"Achievement counts: {achievement_counts}")

def demonstrate_set_comprehensions():
    """Démontre les set comprehensions."""
    print("\n=== Set Comprehension Examples ===")
    
    # Sample data
    events = [
        {'player': 'alice', 'region': 'north'},
        {'player': 'bob', 'region': 'east'},
        {'player': 'alice', 'region': 'central'},
        {'player': 'charlie', 'region': 'north'},
    ]
    
    # Ex1: Joueurs uniques
    unique_players = {event['player'] for event in events}
    print(f"Unique players: {unique_players}")
    
    # Ex2: Achievements uniques
    all_achievements = [
        ['first_kill', 'level_10'],
        ['level_10', 'boss_slayer'],
        ['first_kill', 'boss_slayer']
    ]
    unique_achs = {ach for achs in all_achievements for ach in achs}
    print(f"Unique achievements: {unique_achs}")
    
    # Ex3: Régions actives
    active_regions = {event['region'] for event in events}
    print(f"Active regions: {active_regions}")

def combined_analysis():
    """Analyse combinée utilisant toutes les comprehensions."""
    print("\n=== Combined Analysis ===")
    
    # Data
    players_data = {
        'alice': {'score': 2300, 'achievements': 5},
        'bob': {'score': 1800, 'achievements': 3},
        'charlie': {'score': 2150, 'achievements': 7},
        'diana': {'score': 2050, 'achievements': 4}
    }
    
    # Total unique players (set)
    total_players = len(players_data)
    print(f"Total players: {total_players}")
    
    # Total achievements (sum)
    total_achievements = sum(data['achievements'] 
                            for data in players_data.values())
    print(f"Total unique achievements: {total_achievements}")
    
    # Average score (list comp + sum)
    avg_score = sum(data['score'] for data in players_data.values()) / total_players
    print(f"Average score: {avg_score:.1f}")
    
    # Top performer (max with key)
    top_player = max(players_data.items(), 
                    key=lambda x: (x[1]['score'], x[1]['achievements']))
    print(f"Top performer: {top_player[0]} "
          f"({top_player[1]['score']} points, "
          f"{top_player[1]['achievements']} achievements)")

def main():
    """Point d'entrée principal."""
    print("=== Game Analytics Dashboard ===\n")
    
    demonstrate_list_comprehensions()
    demonstrate_dict_comprehensions()
    demonstrate_set_comprehensions()
    combined_analysis()

if __name__ == "__main__":
    main()
```

### 📤 Exemple d'Exécution

```bash
$ python3 ft_analytics_dashboard.py
=== Game Analytics Dashboard ===

=== List Comprehension Examples ===
High scorers (>2000): ['alice', 'charlie', 'diana']
Scores doubled: [4600, 3600, 4300, 4100]
Active players: ['alice', 'bob', 'charlie']

=== Dict Comprehension Examples ===
Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}
Score categories: {'high': 3, 'medium': 2, 'low': 1}
Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}

=== Set Comprehension Examples ===
Unique players: {'alice', 'bob', 'charlie', 'diana'}
Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
Active regions: {'north', 'east', 'central'}

=== Combined Analysis ===
Total players: 4
Total unique achievements: 12
Average score: 2062.5
Top performer: alice (2300 points, 5 achievements)
```

### 💡 Points Clés
- **List comp**: `[expr for item in iterable if cond]`
- **Dict comp**: `{key: val for item in iterable if cond}`
- **Set comp**: `{expr for item in iterable if cond}`
- **Pythonic** et **performant** !

---

## 📊 Tableau Récapitulatif des Structures

| Structure | Usage | Exemple | Complexité |
|-----------|-------|---------|------------|
| **List** | Séquence ordonnée mutable | `[1, 2, 3]` | Accès O(1), Search O(n) |
| **Tuple** | Séquence ordonnée immutable | `(x, y, z)` | Accès O(1), Immutable |
| **Set** | Collection unique non ordonnée | `{'a', 'b'}` | Test O(1), Union O(n+m) |
| **Dict** | Mapping clé-valeur | `{'key': val}` | Lookup O(1) |
| **Generator** | Séquence lazy | `yield x` | Memory O(1) |
| **Comprehension** | Transformation élégante | `[x*2 for x in ...]` | Temps ~O(n) |

---

## ✅ Checklist Finale

### Avant de Soumettre:
- [ ] Tous les exercices nommés correctement (ft_*.py)
- [ ] Type hints sur toutes les fonctions
- [ ] Try/except pour gestion d'erreurs
- [ ] Code conforme flake8
- [ ] Output correspond aux exemples du sujet
- [ ] Tests avec différents inputs
- [ ] Commentaires clairs sur le code

### Test de Qualité:
```bash
# Flake8
flake8 ex*/ft_*.py

# Test basique
python3 ex0/ft_command_quest.py hello world
python3 ex1/ft_score_analytics.py 1500 2300 1800
# etc...
```

---

## 🎯 Conseils de Réussite

### 💡 Best Practices:
1. **Lis le sujet LIGNE PAR LIGNE** (surtout les exemples d'output!)
2. **Teste avec plusieurs inputs** (cas normaux + edge cases)
3. **Type hints partout** (c'est obligatoire)
4. **Try/except** pour éviter les crashes
5. **Commentaires clairs** pour expliquer la logique

### 🚫 Erreurs Courantes:
- ❌ Oublier sys.argv[1:] (ignorer le nom du script)
- ❌ Ne pas gérer les cas vides (no args)
- ❌ Format de sortie différent du sujet
- ❌ Pas de try/except sur les conversions
- ❌ Utiliser print() dans les fonctions de calcul

### ⚡ Optimisations:
- Fonctions modulaires (une responsabilité par fonction)
- Noms de variables descriptifs
- Éviter la duplication de code
- Utiliser les built-ins Python (sum, max, min, etc.)

---

## 📚 Ressources Supplémentaires

### Documentation Officielle:
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Dicts](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Generators](https://docs.python.org/3/howto/functional.html#generators)
- [Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

---

**Bon courage pour ton projet Data Quest! 🚀**

*Document créé le 17 janvier 2026*
