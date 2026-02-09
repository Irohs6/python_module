# 📚 GUIDE COMPLET P07 - DataDeck: Abstract Card Architecture

## 🎯 Vue d'ensemble du projet

### Objectif principal
Maîtriser les **classes abstraites** et les **patterns de conception** en Python à travers la création d'un moteur de jeu de cartes.

### Concepts clés à maîtriser
1. **ABC (Abstract Base Classes)** - Classes abstraites
2. **Interfaces multiples** - Héritage multiple
3. **Polymorphisme** - Même interface, comportements différents
4. **Design Patterns** - Factory et Strategy
5. **Type hints avancés** - Annotations de types

---

## 🏗️ Structure du projet (IMPORTANT!)

```
python_module/
├── __init__.py                    # ⚠️ OBLIGATOIRE à la racine!
├── ex0/
│   ├── __init__.py               # ⚠️ OBLIGATOIRE
│   ├── Card.py                   # Classe abstraite de base
│   ├── CreatureCard.py           # Première implémentation concrète
│   └── main.py                   # ⚠️ OBLIGATOIRE - Démonstration
├── ex1/
│   ├── __init__.py
│   ├── SpellCard.py
│   ├── ArtifactCard.py
│   ├── Deck.py
│   └── main.py
├── ex2/
│   ├── __init__.py
│   ├── Combatable.py
│   ├── Magical.py
│   ├── EliteCard.py
│   └── main.py
├── ex3/
│   ├── __init__.py
│   ├── GameStrategy.py
│   ├── CardFactory.py
│   ├── AggressiveStrategy.py
│   ├── FantasyCardFactory.py
│   ├── GameEngine.py
│   └── main.py
└── ex4/
    ├── __init__.py
    ├── Rankable.py
    ├── TournamentCard.py
    ├── TournamentPlatform.py
    └── main.py
```

### ⚠️ Règles d'exécution CRUCIALES

**Exécution depuis la racine uniquement:**
```bash
# ✅ CORRECT
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main

# ❌ FAUX - Ne marche pas!
cd ex0 && python3 main.py
python3 ex0/main.py
```

**Imports absolus obligatoires:**
```python
# ✅ CORRECT
from ex0.Card import Card
from ex1.SpellCard import SpellCard

# ❌ FAUX - Imports relatifs interdits
from ..ex0.Card import Card
from .Card import Card
```

---

## 📖 Exercice 0: Fondation des Cartes (Abstract Base Class)

### Concepts à comprendre

#### 1. Qu'est-ce qu'une classe abstraite?
Une classe abstraite est un **modèle/template** qui:
- ❌ **Ne peut PAS être instanciée** directement
- ✅ **Définit un contrat** que les sous-classes doivent respecter
- ✅ **Force l'implémentation** de certaines méthodes

#### 2. Pourquoi utiliser des classes abstraites?

**Exemple du monde réel: Les véhicules**
```python
from abc import ABC, abstractmethod

# ❌ Sans classe abstraite - Problème!
class Vehicle:
    def start_engine(self):
        pass  # Vide - chaque sous-classe peut l'oublier!

class Car(Vehicle):
    pass  # Oups! J'ai oublié start_engine()

# ✅ Avec classe abstraite - Solution!
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # DOIT être implémenté!

class Car(Vehicle):
    # Python me force à implémenter start_engine()
    def start_engine(self):
        return "Car engine started"
```

#### 3. Anatomie d'une classe abstraite

```python
from abc import ABC, abstractmethod
from typing import Dict

class Animal(ABC):  # 1. Hérite de ABC
    """Classe abstraite représentant un animal"""
    
    # 2. Constructeur (peut être concret)
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    # 3. Méthode abstraite (DOIT être implémentée)
    @abstractmethod
    def make_sound(self) -> str:
        """Chaque animal doit pouvoir émettre un son"""
        pass
    
    # 4. Méthode concrète (optionnelle)
    def get_info(self) -> Dict[str, any]:
        """Méthode commune à tous les animaux"""
        return {"name": self.name, "age": self.age}

# Implémentation concrète
class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow!"

# Utilisation
dog = Dog("Rex", 5)
print(dog.make_sound())  # Woof!
print(dog.get_info())    # {'name': 'Rex', 'age': 5}
```

### 🎯 Implémentation pour ex0

#### Card.py - La classe abstraite de base
```python
from abc import ABC, abstractmethod
from typing import Dict

class Card(ABC):
    """
    Classe abstraite de base pour toutes les cartes.
    Définit le contrat que TOUTES les cartes doivent respecter.
    """
    
    def __init__(self, name: str, cost: int, rarity: str):
        """
        Constructeur de base pour toutes les cartes.
        
        Args:
            name: Nom de la carte
            cost: Coût en mana pour jouer la carte
            rarity: Rareté (Common, Rare, Legendary)
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity
    
    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """
        Méthode abstraite - DOIT être implémentée par chaque carte.
        Jouer la carte et modifier l'état du jeu.
        
        Args:
            game_state: État actuel du jeu
            
        Returns:
            Résultat de l'action
        """
        pass
    
    def get_card_info(self) -> Dict:
        """
        Méthode concrète - disponible pour toutes les cartes.
        Retourne les informations de base de la carte.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__
        }
    
    def is_playable(self, available_mana: int) -> bool:
        """
        Méthode concrète - vérifie si on peut jouer la carte.
        """
        return available_mana >= self.cost
```

#### CreatureCard.py - Première implémentation
```python
from typing import Dict
from ex0.Card import Card

class CreatureCard(Card):
    """
    Carte créature avec attaque et santé.
    Implémente la méthode abstraite play().
    """
    
    def __init__(self, name: str, cost: int, rarity: str, 
                 attack: int, health: int):
        """
        Args:
            attack: Puissance d'attaque
            health: Points de vie
        """
        super().__init__(name, cost, rarity)  # Appel constructeur parent
        
        # Validation
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive")
        
        self.attack = attack
        self.health = health
    
    def play(self, game_state: Dict) -> Dict:
        """
        Implémentation de la méthode abstraite.
        Invoque la créature sur le champ de bataille.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
    
    def attack_target(self, target) -> Dict:
        """
        Méthode spécifique aux créatures.
        Attaque une cible.
        """
        return {
            "attacker": self.name,
            "target": target.name if hasattr(target, 'name') else str(target),
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
    
    def get_card_info(self) -> Dict:
        """
        Override de la méthode du parent pour ajouter attack/health.
        """
        info = super().get_card_info()  # Récupère info de base
        info["attack"] = self.attack
        info["health"] = self.health
        return info
```

#### main.py - Démonstration
```python
#!/usr/bin/env python3
"""Démonstration des classes abstraites avec Card et CreatureCard"""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard

def main():
    print("=== DataDeck Card Foundation ===\n")
    
    # Test 1: Création de créatures
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
    
    # Test 2: Affichage des infos
    print("CreatureCard Info:")
    print(dragon.get_card_info())
    
    # Test 3: Vérifier si jouable
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    
    # Test 4: Jouer la carte
    game_state = {"mana": 6, "battlefield": []}
    print(f"Play result: {dragon.play(game_state)}")
    
    # Test 5: Combat
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target(goblin)}")
    
    # Test 6: Mana insuffisant
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")
    
    # Test 7: Tentative d'instanciation de Card (devrait échouer)
    print("\nTrying to instantiate abstract Card directly:")
    try:
        card = Card("Test", 1, "Common")  # ❌ Erreur!
    except TypeError as e:
        print(f"Error: Can't instantiate abstract class")
    
    print("\nAbstract pattern successfully demonstrated!")

if __name__ == "__main__":
    main()
```

---

## 📖 Exercice 1: Deck Builder (Polymorphisme)

### Concepts à comprendre

#### 1. Le Polymorphisme
**"Plusieurs formes, même interface"**

```python
# Exemple simple
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def area(self):
        return self.side ** 2

# Polymorphisme en action!
shapes = [Circle(5), Square(4), Circle(3)]
for shape in shapes:
    print(shape.area())  # Même méthode, résultats différents!
```

#### 2. Pourquoi c'est puissant pour un jeu de cartes?

```python
# Sans polymorphisme - HORRIBLE!
deck = []
deck.append(("creature", CreatureCard(...)))
deck.append(("spell", SpellCard(...)))
deck.append(("artifact", ArtifactCard(...)))

# Pour jouer une carte
for card_type, card in deck:
    if card_type == "creature":
        card.play_creature()
    elif card_type == "spell":
        card.cast_spell()
    elif card_type == "artifact":
        card.activate_artifact()
    # ... cauchemar à maintenir!

# Avec polymorphisme - MAGNIFIQUE!
deck = []
deck.append(CreatureCard(...))
deck.append(SpellCard(...))
deck.append(ArtifactCard(...))

# Pour jouer une carte
for card in deck:
    card.play()  # Même interface pour TOUTES les cartes!
```

### 🎯 Implémentation pour ex1

#### SpellCard.py
```python
from typing import Dict, List
from ex0.Card import Card

class SpellCard(Card):
    """
    Carte de sort - Effets instantanés.
    Les sorts sont consommés après utilisation.
    """
    
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """
        Args:
            effect_type: Type d'effet (damage, heal, buff, debuff)
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
    
    def play(self, game_state: Dict) -> Dict:
        """Joue le sort - effet instantané puis consommé"""
        effect_description = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Heal {self.cost} health",
            "buff": f"Buff target (+{self.cost} attack)",
            "debuff": f"Debuff target (-{self.cost} attack)"
        }.get(self.effect_type, "Unknown effect")
        
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_description
        }
    
    def resolve_effect(self, targets: List) -> Dict:
        """Résout l'effet du sort sur les cibles"""
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": [str(t) for t in targets],
            "resolved": True
        }
```

#### ArtifactCard.py
```python
from typing import Dict
from ex0.Card import Card

class ArtifactCard(Card):
    """
    Carte artefact - Effets permanents.
    Reste en jeu jusqu'à destruction.
    """
    
    def __init__(self, name: str, cost: int, rarity: str, 
                 durability: int, effect: str):
        """
        Args:
            durability: Nombre de tours avant destruction
            effect: Description de l'effet permanent
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
    
    def play(self, game_state: Dict) -> Dict:
        """Place l'artefact en jeu"""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }
    
    def activate_ability(self) -> Dict:
        """Active l'effet permanent de l'artefact"""
        self.durability -= 1
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability,
            "active": self.durability > 0
        }
```

#### Deck.py - Gestion du deck
```python
from typing import List, Dict, Optional
from random import shuffle as random_shuffle
from ex0.Card import Card

class Deck:
    """
    Gestionnaire de deck - Utilise le polymorphisme!
    Peut contenir N'IMPORTE quel type de carte.
    """
    
    def __init__(self):
        self.cards: List[Card] = []
    
    def add_card(self, card: Card) -> None:
        """Ajoute une carte au deck"""
        self.cards.append(card)
    
    def remove_card(self, card_name: str) -> bool:
        """Retire une carte par son nom"""
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False
    
    def shuffle(self) -> None:
        """Mélange le deck"""
        random_shuffle(self.cards)
    
    def draw_card(self) -> Optional[Card]:
        """Pioche une carte du dessus"""
        if self.cards:
            return self.cards.pop(0)
        return None
    
    def get_deck_stats(self) -> Dict:
        """Statistiques du deck"""
        if not self.cards:
            return {"total_cards": 0}
        
        # Compte les types de cartes (polymorphisme!)
        types = {}
        total_cost = 0
        
        for card in self.cards:
            card_type = card.__class__.__name__.replace("Card", "").lower()
            types[card_type] = types.get(card_type, 0) + 1
            total_cost += card.cost
        
        return {
            "total_cards": len(self.cards),
            **{f"{k}s": v for k, v in types.items()},
            "avg_cost": round(total_cost / len(self.cards), 1)
        }
```

---

## 📖 Exercice 2: Héritage Multiple

### Concepts à comprendre

#### 1. Interfaces multiples
Une classe peut implémenter **plusieurs interfaces** en même temps.

```python
# Exemple du monde réel
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

# Un canard peut voler ET nager!
class Duck(Flyable, Swimmable):
    def fly(self):
        return "Duck is flying"
    
    def swim(self):
        return "Duck is swimming"
```

#### 2. MRO (Method Resolution Order)
Python utilise le **C3 Linearization** pour résoudre l'ordre d'appel des méthodes.

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):  # Ordre important!
    pass

d = D()
print(d.method())  # "B" - car B est avant C
print(D.__mro__)   # Affiche l'ordre de résolution
```

### 🎯 Implémentation pour ex2

#### Combatable.py
```python
from abc import ABC, abstractmethod
from typing import Dict

class Combatable(ABC):
    """Interface pour les entités qui peuvent combattre"""
    
    @abstractmethod
    def attack(self, target) -> Dict:
        """Attaque une cible"""
        pass
    
    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """Défend contre des dégâts"""
        pass
    
    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """Retourne les stats de combat"""
        pass
```

#### Magical.py
```python
from abc import ABC, abstractmethod
from typing import Dict, List

class Magical(ABC):
    """Interface pour les entités magiques"""
    
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Lance un sort"""
        pass
    
    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """Canalise du mana"""
        pass
    
    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """Retourne les stats magiques"""
        pass
```

#### EliteCard.py - Héritage multiple!
```python
from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical

class EliteCard(Card, Combatable, Magical):
    """
    Carte Elite - Implémente 3 interfaces!
    - Card: Comportement de base
    - Combatable: Capacités de combat
    - Magical: Capacités magiques
    """
    
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, defense: int, mana_pool: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.defense_power = defense
        self.mana_pool = mana_pool
        self.current_health = 10
    
    # Implémentation de Card
    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card summoned with combat and magic abilities"
        }
    
    # Implémentation de Combatable
    def attack(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "melee"
        }
    
    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(incoming_damage, self.defense_power)
        taken = incoming_damage - blocked
        self.current_health -= taken
        
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.current_health > 0
        }
    
    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense_power,
            "health": self.current_health
        }
    
    # Implémentation de Magical
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        mana_cost = len(spell_name) % 5 + 1  # Simple calcul
        if self.mana_pool >= mana_cost:
            self.mana_pool -= mana_cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": mana_cost
            }
        return {"error": "Not enough mana"}
    
    def channel_mana(self, amount: int) -> Dict:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }
    
    def get_magic_stats(self) -> Dict:
        return {
            "mana_pool": self.mana_pool,
            "spellcasting_available": self.mana_pool > 0
        }
```

---

## 📖 Exercice 3: Design Patterns

### Concepts à comprendre

#### 1. Strategy Pattern
**Sépare l'algorithme de son utilisation**

```python
# Sans Strategy - Code rigide
class Game:
    def play_turn(self, mode):
        if mode == "aggressive":
            # Code agressif
            pass
        elif mode == "defensive":
            # Code défensif
            pass
        # Difficile d'ajouter de nouvelles stratégies!

# Avec Strategy - Flexible!
class GameStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class AggressiveStrategy(GameStrategy):
    def execute(self):
        return "Attack!"

class DefensiveStrategy(GameStrategy):
    def execute(self):
        return "Defend!"

class Game:
    def __init__(self, strategy: GameStrategy):
        self.strategy = strategy
    
    def play_turn(self):
        return self.strategy.execute()
    
    def change_strategy(self, new_strategy: GameStrategy):
        self.strategy = new_strategy  # Changement facile!
```

#### 2. Abstract Factory Pattern
**Crée des familles d'objets liés**

```python
# Factory pour créer des personnages thématiques
class CharacterFactory(ABC):
    @abstractmethod
    def create_warrior(self):
        pass
    
    @abstractmethod
    def create_mage(self):
        pass

class FantasyFactory(CharacterFactory):
    def create_warrior(self):
        return Knight()
    
    def create_mage(self):
        return Wizard()

class SciFiFactory(CharacterFactory):
    def create_warrior(self):
        return Soldier()
    
    def create_mage(self):
        return Technomancer()

# Utilisation - Toute une famille cohérente!
factory = FantasyFactory()
warrior = factory.create_warrior()  # Knight
mage = factory.create_mage()        # Wizard
```

---

## 🔗 Ressources Essentielles

### 📚 Documentation Officielle Python
- **ABC Module**: https://docs.python.org/3/library/abc.html
- **Type Hints**: https://docs.python.org/3/library/typing.html
- **Dataclasses**: https://docs.python.org/3/library/dataclasses.html
- **Enum**: https://docs.python.org/3/library/enum.html

### 🎓 Tutoriels Abstract Classes
- **Real Python - Abstract Classes**: https://realpython.com/python-interface/
- **Real Python - Multiple Inheritance**: https://realpython.com/inheritance-composition-python/
- **GeeksforGeeks - ABC**: https://www.geeksforgeeks.org/abstract-classes-in-python/

### 🎨 Design Patterns
- **Refactoring Guru - Strategy**: https://refactoring.guru/design-patterns/strategy/python/example
- **Refactoring Guru - Abstract Factory**: https://refactoring.guru/design-patterns/abstract-factory/python/example
- **Python Patterns**: https://python-patterns.guide/

### 📖 Livres recommandés
- **"Design Patterns: Elements of Reusable Object-Oriented Software"** (Gang of Four)
- **"Python Design Patterns"** by Chetan Giridhar
- **"Fluent Python"** by Luciano Ramalho (Chapitre sur les ABCs)

### 🎥 Vidéos YouTube
- **Corey Schafer - OOP in Python**: https://www.youtube.com/watch?v=ZDa-Z5JzLYM
- **ArjanCodes - Abstract Classes**: https://www.youtube.com/watch?v=xvFZjo5PgG0
- **mCoding - Python's ABC**: https://www.youtube.com/watch?v=VvVvQSGKmBQ

---

## 💡 Conseils et Astuces

### ✅ DO (À faire)
1. **Commencer simple** - Implémente ex0 parfaitement avant de continuer
2. **Tester constamment** - Vérifie chaque méthode individuellement
3. **Type hints partout** - Aide énormément pour le débogage
4. **Documenter** - Ajoute des docstrings claires
5. **Imports absolus** - Toujours depuis la racine
6. **main.py complets** - Démontre TOUTES les fonctionnalités

### ❌ DON'T (À éviter)
1. **Pas de logique complexe** - Focus sur les patterns, pas le gameplay
2. **Pas d'imports relatifs** - Utilise toujours les imports absolus
3. **Pas d'instanciation de classes abstraites** - Ça va planter!
4. **Pas de copier-coller** - Comprends chaque ligne
5. **Pas d'oubli des __init__.py** - Obligatoires partout!

---

## 🐛 Debugging Common Issues

### Erreur: "Can't instantiate abstract class"
```python
# ❌ Problème
card = Card("Test", 1, "Common")

# ✅ Solution
# Les classes abstraites ne peuvent pas être instanciées!
# Crée une sous-classe concrète à la place
card = CreatureCard("Test", 1, "Common", 1, 1)
```

### Erreur: "No module named ex0"
```python
# ❌ Problème - Mauvais répertoire ou imports relatifs
cd ex0
python3 main.py

# ✅ Solution - Exécute depuis la racine
cd /chemin/vers/python_module
python3 -m ex0.main
```

### Erreur: "Multiple bases have instance lay-out conflict"
```python
# ❌ Problème - Héritage multiple mal ordonné
class EliteCard(Magical, Card, Combatable):  # Mauvais ordre!
    pass

# ✅ Solution - Met la classe principale en premier
class EliteCard(Card, Combatable, Magical):  # Bon ordre!
    pass
```

### Warning: "Method 'play' is abstract in class 'Card'"
```python
# ❌ Problème - Méthode abstraite non implémentée
class MyCard(Card):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
    # Oups! Pas de méthode play()

# ✅ Solution - Implémente TOUTES les méthodes abstraites
class MyCard(Card):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
    
    def play(self, game_state):  # ✓ Implémentée!
        return {"effect": "played"}
```

---

## 📝 Checklist avant soumission

### Structure
- [ ] `__init__.py` à la racine du repository
- [ ] `__init__.py` dans chaque dossier ex0, ex1, ex2, ex3, ex4
- [ ] `main.py` dans chaque exercice
- [ ] Tous les fichiers .py requis présents

### Code
- [ ] Toutes les classes abstraites utilisent `ABC`
- [ ] Toutes les méthodes abstraites sont implémentées
- [ ] Type hints sur toutes les signatures
- [ ] Imports absolus (pas de relatifs)
- [ ] Docstrings sur les classes et méthodes importantes

### Tests
- [ ] `python3 -m ex0.main` fonctionne
- [ ] `python3 -m ex1.main` fonctionne
- [ ] `python3 -m ex2.main` fonctionne
- [ ] `python3 -m ex3.main` fonctionne
- [ ] `python3 -m ex4.main` fonctionne
- [ ] Aucune erreur d'import
- [ ] Outputs cohérents et informatifs

### Qualité
- [ ] Code conforme à flake8
- [ ] Pas de code dupliqué
- [ ] Gestion des erreurs appropriée
- [ ] Nommage clair et cohérent

---

## 🎯 Exemple Complet Minimal (ex0)

Voici un exemple ultra-simple et fonctionnel pour démarrer:

```bash
# Structure minimale
python_module/
├── __init__.py          # Vide ou avec: """DataDeck Project"""
├── ex0/
│   ├── __init__.py     # Vide
│   ├── Card.py         # Voir ci-dessous
│   ├── CreatureCard.py # Voir ci-dessous
│   └── main.py         # Voir ci-dessous
```

**Fichiers dans les sections précédentes du guide!**

---

## 🚀 Plan d'attaque recommandé

### Jour 1: Fondations
1. ✅ Lire le sujet complètement
2. ✅ Créer la structure de dossiers
3. ✅ Créer tous les `__init__.py`
4. ✅ Implémenter ex0 complètement
5. ✅ Tester ex0 jusqu'à ce que ce soit parfait

### Jour 2: Construction
1. ✅ Implémenter ex1 (SpellCard, ArtifactCard, Deck)
2. ✅ Tester le polymorphisme
3. ✅ Commencer ex2 (Interfaces)

### Jour 3: Patterns
1. ✅ Finir ex2 (Héritage multiple)
2. ✅ Implémenter ex3 (Strategy + Factory)
3. ✅ Tester les patterns

### Jour 4: Finalisation
1. ✅ Implémenter ex4 (Tournament)
2. ✅ Tests complets
3. ✅ Revue de code
4. ✅ Documentation

---

## 🎊 Conclusion

Ce projet est une **masterclass** en programmation orientée objet avancée. Les concepts que tu maîtrises ici sont utilisés dans:

- 🎮 **Moteurs de jeux** (Unity, Unreal Engine)
- 🌐 **Frameworks web** (Django, FastAPI)
- 📊 **Systèmes d'analyse de données** (pandas, scikit-learn)
- 🤖 **IA et Machine Learning** (TensorFlow, PyTorch)

**Prends ton temps, comprends les concepts, et bon code! 🚀**

---

*Guide créé pour le projet DataDeck P07 - École 42*
*Dernière mise à jour: Février 2026*
