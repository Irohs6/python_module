# 🎯 SOUTENANCE ORALE - P03: Structures de Données Python

## 📋 Table des Matières
1. [Introduction au Module P03](#introduction)
2. [Exercice 0: Command Quest](#exercice-0)
3. [Exercice 1: Score Analytics](#exercice-1)
4. [Exercice 2: Coordinate System](#exercice-2)
5. [Exercice 3: Achievement Tracker](#exercice-3)
6. [Exercice 4: Inventory System](#exercice-4)
7. [Exercice 5: Data Stream](#exercice-5)
8. [Exercice 6: Analytics Dashboard](#exercice-6)
9. [Conclusion](#conclusion)

---

## 🎓 Introduction au Module P03 {#introduction}

### Objectifs Pédagogiques
Le module P03 se concentre sur les **structures de données avancées** en Python :
- **Tuples** : Collections ordonnées et immuables
- **Dictionnaires** : Mappings clé-valeur performants
- **Sets** : Collections non ordonnées d'éléments uniques
- **Générateurs** : Création de séquences lazy (évaluation paresseuse)
- **Comprehensions** : Syntaxe concise pour créer des collections

### Technologies Utilisées
- Python 3.11+
- Type hints pour la clarté du code
- Structures de données natives Python

---

## 📝 Exercice 0: Command Quest {#exercice-0}

### 🎯 Objectif
Démontrer la maîtrise des **tuples** et de l'**unpacking** en Python.

### 💡 Concepts Clés

#### 1. Les Tuples
```python
# Création de tuples
command = ("attack", 45, "sword")
position = (10, 20)

# Tuples immuables - IMPOSSIBLE de modifier
# command[0] = "defend"  # ❌ TypeError!
```

#### 2. L'Unpacking (Déballage)
```python
# Unpacking simple
action, damage, weapon = ("attack", 45, "sword")
print(f"Action: {action}, Dégâts: {damage}, Arme: {weapon}")

# Unpacking avec *
first, *middle, last = (1, 2, 3, 4, 5)
# first = 1, middle = [2, 3, 4], last = 5
```

#### 3. Unpacking dans les Boucles
```python
commands = [
    ("attack", 45, "sword"),
    ("defend", 0, "shield"),
    ("heal", -20, "potion")
]

for action, damage, item in commands:
    print(f"{action} avec {item}: {damage} points")
```

### 📊 Exemple d'Implémentation
```python
def process_commands(commands: list[tuple]) -> None:
    """Traite une liste de commandes de jeu."""
    for action_type, damage_value, item_used in commands:
        if action_type == "attack":
            print(f"⚔️ Attaque avec {item_used}: {damage_value} dégâts")
        elif action_type == "defend":
            print(f"🛡️ Défense avec {item_used}")
        elif action_type == "heal":
            print(f"💚 Soin avec {item_used}: {abs(damage_value)} PV")

# Utilisation
game_commands = [
    ("attack", 45, "sword"),
    ("defend", 0, "shield"),
    ("heal", -20, "potion")
]

process_commands(game_commands)
```

### ✨ Points Importants à Mentionner
- Les tuples sont **immuables** : protection contre les modifications accidentelles
- **Performance** : Les tuples sont plus rapides que les listes
- **Unpacking** : Syntaxe élégante pour extraire les valeurs
- Idéal pour des données qui ne doivent **jamais changer**

---

## 📊 Exercice 1: Score Analytics {#exercice-1}

### 🎯 Objectif
Maîtriser les **dictionnaires** pour le stockage et la manipulation de données structurées.

### 💡 Concepts Clés

#### 1. Création et Accès aux Dictionnaires
```python
# Création
player_stats = {
    "name": "Alice",
    "level": 25,
    "score": 1500,
    "achievements": ["first_win", "speed_run"]
}

# Accès
print(player_stats["name"])  # Alice
print(player_stats.get("rank", "Unranked"))  # Valeur par défaut
```

#### 2. Modification et Ajout
```python
# Modifier
player_stats["level"] = 26

# Ajouter
player_stats["team"] = "Dragons"

# Mise à jour multiple
player_stats.update({"score": 1600, "health": 100})
```

#### 3. Itération sur les Dictionnaires
```python
# Itérer sur les clés
for key in player_stats:
    print(key)

# Itérer sur clés et valeurs
for key, value in player_stats.items():
    print(f"{key}: {value}")

# Itérer sur les valeurs uniquement
for value in player_stats.values():
    print(value)
```

### 📊 Exemple d'Implémentation
```python
def analyze_player_performance(players: dict) -> None:
    """Analyse les performances des joueurs."""
    
    # Trouver le meilleur score
    best_player = max(
        players.items(),
        key=lambda player_tuple: player_tuple[1]["score"]
    )
    
    player_name, player_data = best_player
    print(f"🏆 Meilleur joueur: {player_name}")
    print(f"   Score: {player_data['score']}")
    
    # Moyenne des scores
    total_score = sum(data["score"] for data in players.values())
    average_score = total_score / len(players)
    print(f"📊 Score moyen: {average_score:.1f}")

# Utilisation
game_players = {
    "alice": {"level": 25, "score": 1500},
    "bob": {"level": 18, "score": 1200},
    "charlie": {"level": 30, "score": 2000}
}

analyze_player_performance(game_players)
```

### ✨ Points Importants à Mentionner
- Dictionnaires : **O(1)** pour l'accès, insertion, suppression
- **Flexibilité** : Clés de tout type hashable (strings, nombres, tuples)
- **Méthodes essentielles** : `.get()`, `.items()`, `.keys()`, `.values()`
- Idéal pour représenter des **objets structurés**

---

## 📐 Exercice 2: Coordinate System {#exercice-2}

### 🎯 Objectif
Combiner **tuples** et **dictionnaires** pour gérer des systèmes de coordonnées.

### 💡 Concepts Clés

#### 1. Tuples comme Clés de Dictionnaire
```python
# Les tuples sont hashables → peuvent être des clés
game_map = {
    (0, 0): "spawn",
    (5, 3): "treasure",
    (10, 10): "boss",
    (-2, 4): "shop"
}

# Accès par coordonnées
location_type = game_map[(5, 3)]  # "treasure"
```

#### 2. Structures Imbriquées
```python
# Dictionnaire de tuples
positions = {
    "player1": (10, 20),
    "player2": (15, 25)
}

# Dictionnaire avec tuples comme clés et valeurs complexes
terrain = {
    (0, 0): {"type": "grass", "walkable": True},
    (1, 0): {"type": "water", "walkable": False},
    (2, 0): {"type": "mountain", "walkable": False}
}
```

#### 3. Calculs avec Coordonnées
```python
def calculate_distance(point1: tuple[int, int], 
                      point2: tuple[int, int]) -> float:
    """Calcule la distance euclidienne entre deux points."""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Utilisation
distance = calculate_distance((0, 0), (3, 4))
print(f"Distance: {distance}")  # 5.0
```

### 📊 Exemple d'Implémentation
```python
def analyze_game_map(game_map: dict[tuple[int, int], str]) -> None:
    """Analyse la carte de jeu."""
    
    print("=== Carte de Jeu ===")
    
    # Afficher toutes les positions
    for coordinates, location_type in game_map.items():
        x_coord, y_coord = coordinates
        print(f"Position ({x_coord}, {y_coord}): {location_type}")
    
    # Trouver les limites de la carte
    all_x = [coord[0] for coord in game_map.keys()]
    all_y = [coord[1] for coord in game_map.keys()]
    
    print(f"\n📏 Dimensions:")
    print(f"   X: {min(all_x)} à {max(all_x)}")
    print(f"   Y: {min(all_y)} à {max(all_y)}")
    
    # Compter les types de lieux
    location_counts = {}
    for location_type in game_map.values():
        location_counts[location_type] = (
            location_counts.get(location_type, 0) + 1
        )
    
    print(f"\n📊 Types de lieux:")
    for location_type, count in location_counts.items():
        print(f"   {location_type}: {count}")

# Utilisation
world_map = {
    (0, 0): "spawn",
    (5, 3): "treasure",
    (10, 10): "boss",
    (2, 8): "treasure",
    (7, 4): "shop"
}

analyze_game_map(world_map)
```

### ✨ Points Importants à Mentionner
- **Tuples comme clés** : Parfait pour les coordonnées (immuables)
- Combinaison puissante : tuple + dict = structures complexes
- **Applications réelles** : Cartes, grilles, positions spatiales
- Performance : Accès O(1) même avec coordonnées complexes

---

## 🏆 Exercice 3: Achievement Tracker {#exercice-3}

### 🎯 Objectif
Maîtriser les **sets** (ensembles) pour gérer des collections uniques.

### 💡 Concepts Clés

#### 1. Création et Opérations de Base
```python
# Création
achievements = {"first_kill", "level_10", "speed_run"}
new_achievements = set()

# Ajout
achievements.add("boss_defeated")

# Suppression
achievements.remove("first_kill")  # ❌ KeyError si absent
achievements.discard("first_kill")  # ✅ Pas d'erreur si absent
```

#### 2. Opérations Ensemblistes
```python
alice_achievements = {"first_kill", "level_10", "speed_run"}
bob_achievements = {"level_10", "boss_defeated", "treasure_hunter"}

# Union (tous les achievements)
all_achievements = alice_achievements | bob_achievements
# ou: all_achievements = alice_achievements.union(bob_achievements)

# Intersection (achievements communs)
common = alice_achievements & bob_achievements
# ou: common = alice_achievements.intersection(bob_achievements)

# Différence (ce qu'Alice a mais pas Bob)
alice_only = alice_achievements - bob_achievements
# ou: alice_only = alice_achievements.difference(bob_achievements)

# Différence symétrique (pas en commun)
unique = alice_achievements ^ bob_achievements
```

#### 3. Tests d'Appartenance
```python
achievements = {"first_kill", "level_10", "speed_run"}

# Vérification rapide O(1)
if "level_10" in achievements:
    print("Achievement débloqué!")

# Sous-ensemble
basic_achievements = {"first_kill", "level_10"}
is_subset = basic_achievements.issubset(achievements)  # True
```

### 📊 Exemple d'Implémentation
```python
def track_achievements(
    player_achievements: dict[str, set[str]]
) -> None:
    """Suit les achievements des joueurs."""
    
    print("=== Achievement Tracker ===\n")
    
    # Tous les achievements uniques du jeu
    all_game_achievements = set()
    for achievements in player_achievements.values():
        all_game_achievements |= achievements  # Union
    
    print(f"🎮 Total achievements disponibles: {len(all_game_achievements)}")
    print(f"Achievements: {sorted(all_game_achievements)}\n")
    
    # Analyser chaque joueur
    for player_name, achievements in player_achievements.items():
        completion_rate = (
            len(achievements) / len(all_game_achievements) * 100
        )
        print(f"👤 {player_name}:")
        print(f"   Débloqués: {len(achievements)}")
        print(f"   Progression: {completion_rate:.1f}%")
        
        # Achievements manquants
        missing = all_game_achievements - achievements
        if missing:
            print(f"   À débloquer: {sorted(missing)[:3]}...")
        print()
    
    # Achievements que TOUT LE MONDE a
    common_achievements = set(all_game_achievements)
    for achievements in player_achievements.values():
        common_achievements &= achievements
    
    if common_achievements:
        print(f"🌟 Achievements communs à tous: {common_achievements}")

# Utilisation
players = {
    "alice": {"first_kill", "level_10", "speed_run", "explorer"},
    "bob": {"first_kill", "level_10", "boss_defeated"},
    "charlie": {"first_kill", "treasure_hunter", "explorer"}
}

track_achievements(players)
```

### ✨ Points Importants à Mentionner
- **Sets = Collections uniques** : Pas de doublons automatiquement
- Performance : O(1) pour test d'appartenance
- **Opérations ensemblistes** : Union, intersection, différence
- Idéal pour : Déduplication, comparaisons, appartenance

---

## 🎒 Exercice 4: Inventory System {#exercice-4}

### 🎯 Objectif
Créer un **système d'inventaire complexe** combinant dictionnaires, sets et tuples.

### 💡 Concepts Clés

#### 1. Structure d'Inventaire Complexe
```python
inventory = {
    "weapons": {
        "sword": {"damage": 50, "durability": 100, "type": "melee"},
        "bow": {"damage": 35, "durability": 80, "type": "ranged"}
    },
    "potions": {
        "health": {"effect": "heal", "power": 50, "count": 3},
        "mana": {"effect": "restore_mana", "power": 30, "count": 5}
    },
    "equipped": {
        "weapon": "sword",
        "armor": "plate"
    }
}
```

#### 2. Gestion des Items
```python
def add_item(inventory: dict, category: str, 
             item_name: str, properties: dict) -> None:
    """Ajoute un item à l'inventaire."""
    if category not in inventory:
        inventory[category] = {}
    
    inventory[category][item_name] = properties

def remove_item(inventory: dict, category: str, item_name: str) -> bool:
    """Retire un item de l'inventaire."""
    if category in inventory and item_name in inventory[category]:
        del inventory[category][item_name]
        return True
    return False
```

#### 3. Recherche et Filtrage
```python
def find_items_by_type(inventory: dict, item_type: str) -> list[str]:
    """Trouve tous les items d'un type donné."""
    matching_items = []
    
    for category_items in inventory.values():
        if isinstance(category_items, dict):
            for item_name, properties in category_items.items():
                if isinstance(properties, dict):
                    if properties.get("type") == item_type:
                        matching_items.append(item_name)
    
    return matching_items
```

### 📊 Exemple d'Implémentation Complète
```python
class GameInventory:
    """Système de gestion d'inventaire de jeu."""
    
    def __init__(self):
        self.items: dict[str, dict] = {}
        self.equipped: set[str] = set()
        self.max_weight: int = 100
        self.current_weight: int = 0
    
    def add_item(self, item_name: str, item_data: dict) -> bool:
        """Ajoute un item si capacité disponible."""
        item_weight = item_data.get("weight", 1)
        
        if self.current_weight + item_weight > self.max_weight:
            print(f"❌ Inventaire plein! ({self.current_weight}/{self.max_weight})")
            return False
        
        self.items[item_name] = item_data
        self.current_weight += item_weight
        print(f"✅ {item_name} ajouté ({item_weight}kg)")
        return True
    
    def equip_item(self, item_name: str) -> bool:
        """Équipe un item."""
        if item_name not in self.items:
            print(f"❌ {item_name} non trouvé dans l'inventaire")
            return False
        
        if not self.items[item_name].get("equippable", False):
            print(f"❌ {item_name} ne peut pas être équipé")
            return False
        
        self.equipped.add(item_name)
        print(f"⚔️ {item_name} équipé")
        return True
    
    def get_stats(self) -> dict:
        """Calcule les stats totales avec items équipés."""
        total_damage = 0
        total_defense = 0
        
        for item_name in self.equipped:
            item_data = self.items[item_name]
            total_damage += item_data.get("damage", 0)
            total_defense += item_data.get("defense", 0)
        
        return {
            "damage": total_damage,
            "defense": total_defense,
            "weight": self.current_weight,
            "capacity": self.max_weight
        }
    
    def display(self) -> None:
        """Affiche l'inventaire complet."""
        print("\n=== 🎒 INVENTAIRE ===")
        print(f"Poids: {self.current_weight}/{self.max_weight}kg\n")
        
        # Grouper par catégorie
        categories: dict[str, list[str]] = {}
        for item_name, item_data in self.items.items():
            category = item_data.get("category", "misc")
            if category not in categories:
                categories[category] = []
            categories[category].append(item_name)
        
        # Afficher par catégorie
        for category, items in categories.items():
            print(f"📦 {category.upper()}:")
            for item_name in sorted(items):
                equipped_marker = "⚔️ " if item_name in self.equipped else "  "
                item_data = self.items[item_name]
                print(f"  {equipped_marker}{item_name} ({item_data.get('weight', 1)}kg)")
        
        # Afficher stats
        if self.equipped:
            stats = self.get_stats()
            print(f"\n📊 Stats avec équipement:")
            print(f"   Dégâts: {stats['damage']}")
            print(f"   Défense: {stats['defense']}")

# Utilisation
inventory = GameInventory()

# Ajouter des items
inventory.add_item("sword", {
    "damage": 50,
    "weight": 10,
    "category": "weapons",
    "equippable": True
})
inventory.add_item("shield", {
    "defense": 30,
    "weight": 15,
    "category": "armor",
    "equippable": True
})
inventory.add_item("health_potion", {
    "healing": 50,
    "weight": 1,
    "category": "consumables",
    "equippable": False
})

# Équiper des items
inventory.equip_item("sword")
inventory.equip_item("shield")

# Afficher
inventory.display()
```

### ✨ Points Importants à Mentionner
- **Structure complexe** : Dict de dicts, sets pour équipement
- **Encapsulation** : Logique métier dans des fonctions/classes
- **Validation** : Vérification des contraintes (poids, capacité)
- **Application réelle** : Systèmes RPG, gestion de ressources

---

## 🌊 Exercice 5: Data Stream {#exercice-5}

### 🎯 Objectif
Maîtriser les **générateurs** pour un traitement efficace des données en mémoire.

### 💡 Concepts Clés

#### 1. Qu'est-ce qu'un Générateur?
```python
# Fonction normale - Retourne toute la liste
def get_numbers_list(n: int) -> list[int]:
    result = []
    for i in range(n):
        result.append(i)
    return result  # 💾 Tout en mémoire!

# Générateur - Yield un par un
def get_numbers_generator(n: int):
    for i in range(n):
        yield i  # 🚀 Un seul en mémoire à la fois!

# Utilisation
numbers_list = get_numbers_list(1000000)  # 💾 ~8MB en mémoire!
numbers_gen = get_numbers_generator(1000000)  # 🚀 ~96 bytes seulement!
```

#### 2. Création de Générateurs
```python
# Avec yield
def fibonacci_generator(n: int):
    """Génère les n premiers nombres de Fibonacci."""
    fibonacci_current = 0
    fibonacci_next = 1
    count = 0
    
    while count < n:
        yield fibonacci_current
        fibonacci_current, fibonacci_next = (
            fibonacci_next,
            fibonacci_current + fibonacci_next
        )
        count += 1

# Utilisation
for number in fibonacci_generator(10):
    print(number, end=" ")  # 0 1 1 2 3 5 8 13 21 34
```

#### 3. Générateurs en Pipeline
```python
# Pipeline de traitement
def read_events(events: list[dict]):
    """Générateur qui lit les événements."""
    for event in events:
        yield event

def filter_high_level(events, min_level: int = 10):
    """Filtre les joueurs de haut niveau."""
    for event in events:
        if event["level"] >= min_level:
            yield event

def extract_scores(events):
    """Extrait juste les scores."""
    for event in events:
        yield event["score"]

# Pipeline complet - LAZY EVALUATION!
events = [
    {"player": "alice", "level": 25, "score": 1500},
    {"player": "bob", "level": 5, "score": 200},
    {"player": "charlie", "level": 30, "score": 2000}
]

# Rien n'est calculé tant qu'on n'itère pas!
high_level_scores = extract_scores(filter_high_level(read_events(events)))

# Maintenant on calcule, un par un
for score in high_level_scores:
    print(score)  # 1500, 2000
```

### 📊 Exemple d'Implémentation Complète
```python
def game_event_stream(events: list[dict]):
    """Générateur qui yield les événements un par un."""
    for event in events:
        yield event

def high_level_filter(events: list[dict], min_level: int = 10):
    """Générateur qui filtre les joueurs de haut niveau."""
    for event in events:
        if event["data"]["level"] >= min_level:
            yield event

def event_type_filter(events: list[dict], event_type: str):
    """Générateur qui filtre par type d'événement."""
    for event in events:
        if event["event_type"] == event_type:
            yield event

def process_events(events: list[dict]) -> None:
    """Traite les événements avec des générateurs."""
    
    print("=== Game Data Stream Processor ===")
    print(f"Processing {len(events)} game events...\n")
    
    # Afficher les 3 premiers événements
    event_count = 0
    for event in game_event_stream(events):
        event_count += 1
        if event_count <= 3:
            event_id = event["id"]
            player_name = event["player"]
            player_level = event["data"]["level"]
            event_type = event["event_type"]
            print(f"Event {event_id}: Player {player_name} " +
                  f"(level {player_level}) {event_type}")
        elif event_count == 4:
            print("...")
    
    print("\n=== Stream Analytics ===")
    
    # Compter avec générateur (mémoire constante!)
    total_events = 0
    high_level_count = 0
    event_type_counts: dict[str, int] = {}
    
    for event in game_event_stream(events):
        total_events += 1
        
        # Compter high-level
        if event["data"]["level"] >= 10:
            high_level_count += 1
        
        # Compter par type
        event_type_name = event["event_type"]
        event_type_counts[event_type_name] = (
            event_type_counts.get(event_type_name, 0) + 1
        )
    
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    
    for event_type_name, event_count in event_type_counts.items():
        print(f"{event_type_name.capitalize()} events: {event_count}")
    
    print("Memory usage: Constant (streaming) 🚀")

# Générateur Fibonacci
def fibonacci_generator(n: int):
    """Génère les n premiers nombres de Fibonacci."""
    fibonacci_current = 0
    fibonacci_next = 1
    count = 0
    
    while count < n:
        yield fibonacci_current
        fibonacci_current, fibonacci_next = (
            fibonacci_next,
            fibonacci_current + fibonacci_next
        )
        count += 1

# Générateur de nombres premiers
def prime_generator(n: int):
    """Génère les n premiers nombres premiers."""
    
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                return False
        return True
    
    count = 0
    num = 2
    
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Démonstration
print("\n=== Generator Demonstration ===")

# Fibonacci
fib_list = list(fibonacci_generator(10))
print(f"Fibonacci (10): {', '.join(map(str, fib_list))}")

# Primes
prime_list = list(prime_generator(5))
print(f"Primes (5): {', '.join(map(str, prime_list))}")
```

### ✨ Points Importants à Mentionner
- **Efficacité mémoire** : Un élément à la fois, pas toute la liste
- **Lazy evaluation** : Calcul à la demande
- **yield vs return** : yield suspend, return termine
- **Pipelines** : Chaîner plusieurs générateurs
- **Cas d'usage** : Gros fichiers, streams infinis, traitement temps réel

### 📈 Comparaison Performance
```
Liste (1M éléments):
- Mémoire: ~8 MB
- Création: Immédiate (tout calculé)

Générateur (1M éléments):
- Mémoire: ~96 bytes
- Création: Lazy (calculé à la demande)
```

---

## 📊 Exercice 6: Analytics Dashboard {#exercice-6}

### 🎯 Objectif
Maîtriser les **comprehensions** (list/dict/set) pour du code élégant et pythonique.

### 💡 Concepts Clés

#### 1. List Comprehensions
```python
# ❌ Boucle classique (amateur)
result = []
for number in range(10):
    if number % 2 == 0:
        result.append(number * 2)

# ✅ List comprehension (professionnel)
result = [number * 2 for number in range(10) if number % 2 == 0]

# Syntaxe générale:
# [expression for item in iterable if condition]
```

**Exemples Pratiques:**
```python
# Filtrer les scores élevés
high_scores = [score for score in scores if score > 1000]

# Transformer les noms en majuscules
upper_names = [name.upper() for name in player_names]

# Extraire des données imbriquées
player_levels = [
    player_data["level"]
    for player_data in players.values()
    if player_data["active"]
]
```

#### 2. Dict Comprehensions
```python
# Créer un mapping
player_scores = {
    player_name: player_data["score"]
    for player_name, player_data in players.items()
}

# Inverser un dictionnaire
score_to_player = {
    score: player_name
    for player_name, score in player_scores.items()
}

# Filtrer un dictionnaire
high_scorers = {
    player_name: score
    for player_name, score in player_scores.items()
    if score > 2000
}

# Syntaxe générale:
# {key_expr: value_expr for item in iterable if condition}
```

#### 3. Set Comprehensions
```python
# Extraire des valeurs uniques
unique_levels = {
    player_data["level"]
    for player_data in players.values()
}

# Joueurs ayant participé (déduplication automatique)
active_players = {
    session["player"]
    for session in sessions
}

# Syntaxe générale:
# {expression for item in iterable if condition}
```

### 📊 Exemple d'Implémentation Complète
```python
def demonstrate_list_comprehensions(data: dict) -> None:
    """Démontrer l'utilisation des list comprehensions."""
    
    # Filtrer les joueurs avec score > 2000
    high_scorers = [
        player_name
        for player_name, player_data in data["players"].items()
        if player_data["total_score"] > 2000
    ]
    
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    
    # Doubler les scores des high scorers
    scores_doubled = [
        player_data["total_score"] * 2
        for player_data in data["players"].values()
        if player_data["total_score"] > 2000
    ]
    print(f"Scores doubled: {scores_doubled}")
    
    # Joueurs actifs (avec beaucoup de sessions)
    active_players = [
        player_name
        for player_name, player_data in data["players"].items()
        if player_data["sessions_played"] > 20
    ]
    print(f"Active players: {active_players}")


def demonstrate_dict_comprehensions(data: dict) -> None:
    """Démontrer l'utilisation des dict comprehensions."""
    
    print("\n=== Dict Comprehension Examples ===")
    
    # Mapping joueur -> score total
    player_scores = {
        player_name: player_data["total_score"]
        for player_name, player_data in data["players"].items()
    }
    print(f"Player scores: {player_scores}")
    
    # Grouper par catégories de score
    score_categories = {
        category: sum(
            1
            for player_data in data["players"].values()
            if (
                (category == "high" and player_data["total_score"] > 5000)
                or (
                    category == "medium"
                    and 2000 <= player_data["total_score"] <= 5000
                )
                or (category == "low" and player_data["total_score"] < 2000)
            )
        )
        for category in ["high", "medium", "low"]
    }
    print(f"Score categories: {score_categories}")
    
    # Compter les achievements par joueur
    achievement_counts = {
        player_name: player_data["achievements_count"]
        for player_name, player_data in data["players"].items()
    }
    print(f"Achievement counts: {achievement_counts}")


def demonstrate_set_comprehensions(data: dict) -> None:
    """Démontrer l'utilisation des set comprehensions."""
    
    print("\n=== Set Comprehension Examples ===")
    
    # Extraire tous les joueurs uniques
    unique_players = {
        player_name for player_name in data["players"].keys()
    }
    print(f"Unique players: {unique_players}")
    
    # Tous les game modes uniques
    unique_modes = {
        game_mode for game_mode in data["game_modes"]
    }
    print(f"Unique game modes: {unique_modes}")
    
    # Joueurs ayant participé à des sessions
    active_session_players = {
        session_data["player"] for session_data in data["sessions"]
    }
    print(f"Active session players: {active_session_players}")


def combined_analysis(data: dict) -> None:
    """Combiner plusieurs techniques pour une analyse complète."""
    
    print("\n=== Combined Analysis ===")
    
    # Nombre total de joueurs (set comprehension)
    total_players = len(
        {player_name for player_name in data["players"].keys()}
    )
    print(f"Total players: {total_players}")
    
    # Nombre total d'achievements uniques
    total_achievements = len(data["achievements"])
    print(f"Total unique achievements: {total_achievements}")
    
    # Score moyen (list comprehension + sum)
    all_scores = [
        player_data["total_score"]
        for player_data in data["players"].values()
    ]
    average_score = sum(all_scores) / len(all_scores) if all_scores else 0
    print(f"Average score: {average_score:.1f}")
    
    # Top performer (dict comprehension + max)
    player_stats = {
        player_name: (
            player_data["total_score"],
            player_data["achievements_count"],
        )
        for player_name, player_data in data["players"].items()
    }
    top_player_name = max(
        player_stats.keys(),
        key=lambda player_name: player_stats[player_name][0],
    )
    top_score, top_achievements = player_stats[top_player_name]
    print(
        f"Top performer: {top_player_name} "
        f"({top_score} points, {top_achievements} achievements)"
    )
```

### ✨ Points Importants à Mentionner

#### Avantages des Comprehensions
1. **Lisibilité** : Code plus concis et expressif
2. **Performance** : Optimisé en interne par Python
3. **Pythonic** : Style idiomatique et professionnel
4. **Composabilité** : Facile à combiner et chaîner

#### Quand Utiliser?
- ✅ **Transformations simples** : Mapping, filtrage
- ✅ **Création de collections** : Lists, dicts, sets
- ✅ **Une seule opération** : Pas trop complexe
- ❌ **Logique complexe** : Mieux vaut une boucle explicite
- ❌ **Effets de bord** : Pas de modifications externes

#### Comparaison
```python
# ❌ Style amateur
result = []
for item in items:
    if item > 10:
        result.append(item * 2)

# ✅ Style professionnel
result = [item * 2 for item in items if item > 10]
```

---

## 🎓 Conclusion {#conclusion}

### 📚 Récapitulatif des Compétences Acquises

#### Structures de Données Maîtrisées
| Structure | Usage Principal | Performance |
|-----------|----------------|-------------|
| **Tuples** | Données immuables, clés dict | O(1) accès |
| **Dictionnaires** | Mappings clé-valeur | O(1) accès/insertion |
| **Sets** | Collections uniques | O(1) appartenance |
| **Générateurs** | Streaming, lazy evaluation | O(1) mémoire |

#### Concepts Avancés
1. **Unpacking** : Extraction élégante de données
2. **Opérations ensemblistes** : Union, intersection, différence
3. **Structures imbriquées** : Combinaisons complexes
4. **Comprehensions** : Syntaxe pythonique concise
5. **Lazy evaluation** : Efficacité mémoire

### 🎯 Applications Pratiques

#### Gaming
- 🎮 Systèmes d'inventaire
- 🏆 Tracking d'achievements
- 📊 Analytics de performance
- 🗺️ Gestion de cartes et positions

#### Développement Réel
- 📈 Traitement de données volumineuses
- 🔍 Analyses et statistiques
- 💾 Optimisation mémoire
- ⚡ Performance et rapidité

### 💡 Best Practices Démontrées

#### Code Quality
✅ **Type hints** pour la clarté
✅ **Variables descriptives** (pas de `i`, `j`, `x`)
✅ **Docstrings** pour documentation
✅ **Comprehensions** pour la concision
✅ **Générateurs** pour l'efficacité

#### Performance
✅ Structures appropriées (dict pour lookup O(1))
✅ Sets pour déduplication et appartenance
✅ Générateurs pour gros volumes
✅ Comprehensions (optimisées en interne)

### 🚀 Points Forts du Module

1. **Progression logique** : Du simple au complexe
2. **Thématique cohérente** : Gaming pour l'engagement
3. **Pratique réelle** : Cas d'usage concrets
4. **Performance focus** : Efficacité et optimisation
5. **Code professionnel** : Standards de l'industrie

### 📊 Comparaison Avant/Après

#### Avant P03
```python
# Code amateur
result = []
for x in list1:
    if x > 10:
        result.append(x * 2)

# Lookup lent
for item in list_items:
    if item == target:
        found = True
```

#### Après P03
```python
# Code professionnel
result = [x * 2 for x in list1 if x > 10]

# Lookup rapide
if target in set_items:  # O(1) au lieu de O(n)
    found = True
```

### 🎤 Message de Fin

Ce module P03 représente une **étape cruciale** dans la maîtrise de Python :
- Passage du **débutant au développeur compétent**
- Maîtrise des **structures de données fondamentales**
- Capacité à écrire du **code performant et élégant**
- Compréhension des **trade-offs** (mémoire vs vitesse)

Les compétences acquises sont **directement applicables** en entreprise et constituent la base de tout développement Python professionnel.

---

## 📝 Questions Fréquentes

### Q1: Tuple vs Liste, quand utiliser?
**Réponse:** 
- **Tuple** si les données ne doivent **jamais changer** (coordonnées, dates, configurations)
- **Liste** si vous avez besoin de **modifier** (append, remove, sort)

### Q2: Dictionnaire vs Set, différence?
**Réponse:**
- **Dict** : Paires clé-valeur `{"alice": 100, "bob": 200}`
- **Set** : Juste des valeurs uniques `{"alice", "bob"}`

### Q3: Quand utiliser un générateur?
**Réponse:**
- **Gros volumes de données** (fichiers, logs, streams)
- **Séquences infinies** (nombres, événements temps réel)
- **Pipeline de traitement** (plusieurs étapes de filtrage)
- **Optimisation mémoire** critique

### Q4: Comprehensions vs boucles?
**Réponse:**
- **Comprehension** : Simple, une opération, création de collection
- **Boucle** : Logique complexe, multiples opérations, effets de bord

### Q5: Performance des structures?
**Réponse:**
```
Accès par index:
- Liste: O(1) ✅
- Tuple: O(1) ✅

Recherche d'élément:
- Liste: O(n) ❌
- Set: O(1) ✅
- Dict: O(1) ✅

Ajout d'élément:
- Liste: O(1) en fin ✅
- Set: O(1) ✅
- Dict: O(1) ✅
```

---

**Préparé pour la soutenance du Module P03**
**Structures de Données Avancées en Python**

*Bonne soutenance! 🎓🚀*
