#!/usr/bin/env python3
"""
EXEMPLE SIMPLIFIÉ - Comprendre les concepts de base
Ceci est un exemple minimal pour comprendre les concepts avant de voir l'implémentation complète
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol


# =============================================================================
# EXEMPLE 1 : Protocol (Duck Typing)
# =============================================================================
print("=" * 60)
print("EXEMPLE 1 : Protocol - Duck Typing")
print("=" * 60)


class Animal(Protocol):
    """N'importe quelle classe avec une méthode speak() est un Animal"""

    def speak(self) -> str: ...


class Dog:
    """Pas besoin d'hériter de Animal !"""

    def speak(self) -> str:
        return "Woof!"


class Cat:
    """Pas besoin d'hériter de Animal !"""

    def speak(self) -> str:
        return "Meow!"


def make_sound(animal: Animal) -> None:
    """Cette fonction accepte tout objet avec une méthode speak()"""
    print(f"  {animal.__class__.__name__} says: {animal.speak()}")


# Test
dog = Dog()
cat = Cat()
make_sound(dog)  # Fonctionne !
make_sound(cat)  # Fonctionne aussi !

print(
    "\n✓ Protocol permet le duck typing : si ça a une méthode speak(), c'est un Animal\n"
)


# =============================================================================
# EXEMPLE 2 : ABC (Abstract Base Class)
# =============================================================================
print("=" * 60)
print("EXEMPLE 2 : ABC - Classe Abstraite")
print("=" * 60)


class Shape(ABC):
    """Classe abstraite - ne peut pas être instanciée"""

    @abstractmethod
    def area(self) -> float:
        """Méthode abstraite - DOIT être implémentée par les sous-classes"""
        pass

    def describe(self) -> str:
        """Méthode concrète - peut être héritée telle quelle"""
        return f"Je suis un {self.__class__.__name__}"


class Circle(Shape):
    """DOIT implémenter area() car elle hérite de Shape"""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius**2


class Rectangle(Shape):
    """DOIT implémenter area() car elle hérite de Shape"""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


# Test
# shape = Shape()  # ❌ ERREUR : Cannot instantiate abstract class
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"  {circle.describe()}: area = {circle.area():.2f}")
print(f"  {rectangle.describe()}: area = {rectangle.area():.2f}")

print("\n✓ ABC force les sous-classes à implémenter certaines méthodes\n")


# =============================================================================
# EXEMPLE 3 : Héritage avec super()
# =============================================================================
print("=" * 60)
print("EXEMPLE 3 : Héritage et super()")
print("=" * 60)


class Vehicle:
    """Classe parent"""

    def __init__(self, brand: str):
        self.brand = brand
        print(f"  Véhicule créé : {brand}")

    def start(self) -> str:
        return "Démarrage..."


class Car(Vehicle):
    """Classe enfant qui hérite de Vehicle"""

    def __init__(self, brand: str, model: str):
        super().__init__(brand)  # Appelle __init__ de Vehicle
        self.model = model
        print(f"  Voiture créée : {brand} {model}")

    def start(self) -> str:
        # Override - modifie le comportement
        base_message = super().start()  # Réutilise la méthode parent
        return f"{base_message} Moteur de {self.brand} {self.model}"


# Test
car = Car("Toyota", "Camry")
print(f"  {car.start()}")

print("\n✓ super() permet d'appeler les méthodes de la classe parent\n")


# =============================================================================
# EXEMPLE 4 : Polymorphisme
# =============================================================================
print("=" * 60)
print("EXEMPLE 4 : Polymorphisme")
print("=" * 60)


class Processor(ABC):
    """Classe abstraite pour les processeurs"""

    @abstractmethod
    def process(self, data: Any) -> str:
        pass


class UpperCaseProcessor(Processor):
    def process(self, data: Any) -> str:
        return str(data).upper()


class LowerCaseProcessor(Processor):
    def process(self, data: Any) -> str:
        return str(data).lower()


class ReverseProcessor(Processor):
    def process(self, data: Any) -> str:
        return str(data)[::-1]


def process_data_polymorphically(processors: list, data: str) -> None:
    """Traite les données avec différents processeurs"""
    print(f"  Données originales : '{data}'")
    for processor in processors:
        result = processor.process(data)
        print(f"  {processor.__class__.__name__}: '{result}'")


# Test
processors = [UpperCaseProcessor(), LowerCaseProcessor(), ReverseProcessor()]

process_data_polymorphically(processors, "Hello World")

print("\n✓ Polymorphisme : même interface, comportements différents\n")


# =============================================================================
# EXEMPLE 5 : Pipeline Simple (combine tout)
# =============================================================================
print("=" * 60)
print("EXEMPLE 5 : Pipeline Simple")
print("=" * 60)


class Stage(Protocol):
    """Protocol pour les étapes (duck typing)"""

    def process(self, data: Any) -> Any: ...


class ValidateStage:
    """Pas d'héritage - implémente juste l'interface"""

    def process(self, data: Any) -> Any:
        print(f"  ✓ Validation : {data}")
        return {"validated": True, "data": data}


class EnrichStage:
    """Pas d'héritage - implémente juste l'interface"""

    def process(self, data: Any) -> Any:
        print("  ✓ Enrichissement : ajout de metadata")
        data["metadata"] = {"timestamp": "2026-02-05"}
        return data


class FormatStage:
    """Pas d'héritage - implémente juste l'interface"""

    def process(self, data: Any) -> Any:
        print("  ✓ Formatage : préparation de la sortie")
        return f"Résultat : {data}"


class Pipeline(ABC):
    """Pipeline abstraite (ABC)"""

    def __init__(self, name: str):
        self.name = name
        self.stages = []

    def add_stage(self, stage: Stage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class DataPipeline(Pipeline):
    """Pipeline concrète qui hérite de Pipeline (ABC)"""

    def process(self, data: Any) -> Any:
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


# Test
pipeline = DataPipeline("MyPipeline")
pipeline.add_stage(ValidateStage())
pipeline.add_stage(EnrichStage())
pipeline.add_stage(FormatStage())

print(f"\nTraitement via {pipeline.name}:")
final_result = pipeline.process("test data")
print(f"\n{final_result}")

print("\n✓ Pipeline combine Protocol (stages) et ABC (pipeline)\n")


# =============================================================================
# RÉSUMÉ
# =============================================================================
print("=" * 60)
print("RÉSUMÉ DES CONCEPTS")
print("=" * 60)
print(
    """
1. Protocol (Duck Typing) :
   - Définit une interface sans héritage
   - Si ça a les bonnes méthodes, ça marche
   - Utilisé pour les STAGES dans l'exercice

2. ABC (Abstract Base Class) :
   - Classe abstraite avec méthodes abstraites
   - Force les sous-classes à implémenter certaines méthodes
   - Utilisé pour les PIPELINES dans l'exercice

3. super() :
   - Appelle les méthodes de la classe parent
   - Essentiel pour l'initialisation et la réutilisation

4. Polymorphisme :
   - Même interface, comportements différents
   - Permet de traiter différents types uniformément

5. Pipeline Pattern :
   - Chaîne des étapes de traitement
   - Chaque étape transforme les données
   - Modulaire et extensible
"""
)

print("=" * 60)
print("Maintenant vous pouvez comprendre nexus_pipeline.py !")
print("=" * 60)
