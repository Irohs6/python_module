# 🔷 CODE NEXUS - FLUXES DE DONNÉES POLYMORPHES DANS LA MATRICE NUMÉRIQUE

## 📋 Vue d'ensemble du projet

Ce projet explore les concepts avancés du **polymorphisme** et du **design orienté objet** en Python. Vous apprendrez comment créer des architectures flexibles et extensibles qui permettent à différents types d'objets de fonctionner à travers une interface commune.

### 🎯 Objectifs Pédagogiques

- ✅ Maîtriser l'utilisation d'ABC (Abstract Base Classes) et @abstractmethod
- ✅ Comprendre le polymorphisme par surcharge de méthodes
- ✅ Implémenter l'héritage et la composition de classes
- ✅ Utiliser les type hints avancés (Protocol, Union, Optional, etc.)
- ✅ Gérer les erreurs avec try/except
- ✅ Construire des systèmes complexes et extensibles

---

## 📚 Chapitre I: Fondations du Polymorphisme

### Qu'est-ce que le Polymorphisme ?

Le polymorphisme signifie **"plusieurs formes"**. En programmation orientée objet, c'est la capacité d'objets différents à répondre au même appel de méthode avec des comportements spécifiques à leur type.

### Exemple Simple

```python
# Même interface, comportements différents
processeur.process([1, 2, 3])        # Traite des nombres
processeur.process("Hello")          # Traite du texte
processeur.process("ERROR: Timeout") # Traite des logs
```

### Avantages du Polymorphisme

| Avantage | Description |
|----------|-------------|
| 🔄 **Flexibilité** | Ajouter de nouveaux types sans modifier le code existant |
| 📦 **Maintenabilité** | Code plus facile à comprendre et à maintenir |
| 🚀 **Extensibilité** | Évolutivité sans risque de casser le code existant |
| 🎯 **Abstraction** | Masquer la complexité des implémentations spécifiques |

---

## 🔧 Architecture du Projet

```
P05/
├── ex0/
│   └── stream_processor.py      # Fondations polymorphes
├── ex1/
│   └── data_stream.py           # Flux polymorphes avancés
├── ex2/
│   └── nexus_pipeline.py        # Intégration complète
└── SUJET_P05_TRADUIT_DETAILLE.md
```

---

# 🟢 EXERCICE 0: Les Fondations Polymorphes

## 📖 Présentation

### Titre: `stream_processor.py`

### 📝 Contexte Professionnel

Vous êtes **Ingénieur Data Specialist** chez Code Nexus. Votre première mission est de construire l'architecture fondamentale d'un système de traitement polymorphe. Cette base sera utilisée par tous les systèmes avancés du projet.

### 🎯 Objectif

Créer une architecture de classes abstraites qui permet de traiter différents types de données (nombres, texte, logs) à travers une **interface commune et cohérente**.

---

## 🏗️ Architecture Requise

### Classes à Implémenter

#### 1️⃣ **DataProcessor (ABC - Classe Abstraite)**

C'est la base de votre architecture. Tous les processeurs hériteront de cette classe.

**Responsabilités:**
- Définir l'interface commune que tous les processeurs doivent respecter
- Fournir une implémentation par défaut pour `format_output()`
- Obliger les sous-classes à implémenter `process()` et `validate()`

**Méthodes Abstraites:**
```python
@abstractmethod
def process(self, data: Any) -> str:
    """Traiter les données et retourner un résultat sous forme de string"""
    pass

@abstractmethod
def validate(self, data: Any) -> bool:
    """Valider si les données sont appropriées pour ce processeur"""
    pass
```

**Méthode Concrète (peut être override):**
```python
def format_output(self, result: str) -> str:
    """Formater la string de résultat (implémentation par défaut)"""
    return result
```

---

#### 2️⃣ **NumericProcessor**

Spécialisé dans le traitement des **nombres et listes numériques**.

**Responsabilités:**
- ✅ Valider que les données sont numériques
- ✅ Calculer la somme, la moyenne, et le count
- ✅ Formater les résultats numériques

**Exemple d'utilisation:**
```python
processor = NumericProcessor()
processor.validate([1, 2, 3, 4, 5])  # True
processor.process([1, 2, 3, 4, 5])   
# "Processed 5 numeric values, sum=15, avg=3.0"
```

---

#### 3️⃣ **TextProcessor**

Spécialisé dans le traitement des **chaînes de caractères et texte**.

**Responsabilités:**
- ✅ Valider que les données sont du texte
- ✅ Compter les caractères et les mots
- ✅ Formater les résultats textuels

**Exemple d'utilisation:**
```python
processor = TextProcessor()
processor.validate("Hello Nexus World")  # True
processor.process("Hello Nexus World")   
# "Processed text: 17 characters, 3 words"
```

---

#### 4️⃣ **LogProcessor**

Spécialisé dans le traitement des **entrées de log** avec niveaux (ERROR, INFO, WARNING, etc.).

**Responsabilités:**
- ✅ Valider que les données contiennent un niveau de log
- ✅ Extraire et classer le niveau (ERROR, INFO, WARNING)
- ✅ Formater les alertes appropriées

**Exemple d'utilisation:**
```python
processor = LogProcessor()
processor.validate("ERROR: Connection timeout")  # True
processor.process("ERROR: Connection timeout")   
# "[ALERT] ERROR level detected: Connection timeout"
```

---

## 📋 Spécifications Détaillées

### Signatures de Méthodes (OBLIGATOIRE)

```python
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    """Classe abstraite de base pour tous les processeurs"""
    
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return result string"""
        pass
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass
    
    def format_output(self, result: str) -> str:
        """Format the output string (can be overridden)"""
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        # Votre implémentation
        pass
    
    def validate(self, data: Any) -> bool:
        # Votre implémentation
        pass


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        # Votre implémentation
        pass
    
    def validate(self, data: Any) -> bool:
        # Votre implémentation
        pass


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        # Votre implémentation
        pass
    
    def validate(self, data: Any) -> bool:
        # Votre implémentation
        pass
```

---

## 🎨 Résultat Attendu

```
=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===

Initializing Numeric Processor...
Processing data: [1, 2, 3, 4, 5]
Validation: Numeric data verified
Output: Processed 5 numeric values, sum=15, avg=3.0

Initializing Text Processor...
Processing data: "Hello Nexus World"
Validation: Text data verified
Output: Processed text: 17 characters, 3 words

Initializing Log Processor...
Processing data: "ERROR: Connection timeout"
Validation: Log entry verified
Output: [ALERT] ERROR level detected: Connection timeout

=== Polymorphic Processing Demo ===
Processing multiple data types through same interface...
Result 1: Processed 3 numeric values, sum=6, avg=2.0
Result 2: Processed text: 12 characters, 2 words
Result 3: [INFO] INFO level detected: System ready

Foundation systems online. Nexus ready for advanced streams.
```

---

## ✅ Autorisé / ❌ Non Autorisé

### ✅ AUTORISÉ

| Technique | Raison |
|-----------|--------|
| **ABC et @abstractmethod** | Créer des interfaces polymorphes |
| **isinstance()** | Vérifier les types de données |
| **print()** | Afficher les résultats |
| **Type hints** | Améliorer la clarté du code |
| **try/except** | Gérer les erreurs gracieusement |
| **List/Dict comprehensions** | Traiter les données efficacement |

### ❌ NON AUTORISÉ

| Pratique | Raison |
|----------|--------|
| **eval()** | Risque de sécurité |
| **Bibliothèques externes** | Sauf si explicitement autorisées |
| **Variables globales** | Mauvaise pratique |
| **Modification de données en place** | Lors d'opérations de traitement |

---

## 💡 Conseils d'Implémentation

### 1. Validation des Données
```python
# NumericProcessor
def validate(self, data: Any) -> bool:
    if not isinstance(data, (list, tuple)):
        return False
    return all(isinstance(x, (int, float)) for x in data)
```

### 2. Traitement Polymorphe
```python
# Utiliser la même interface pour différents types
def process_all(processors: list[DataProcessor], data_list: list):
    results = []
    for processor, data in zip(processors, data_list):
        if processor.validate(data):
            result = processor.process(data)
            results.append(processor.format_output(result))
    return results
```

### 3. Gestion d'Erreurs
```python
try:
    if not processor.validate(data):
        raise ValueError(f"Invalid data for {processor.__class__.__name__}")
    return processor.process(data)
except Exception as e:
    print(f"Error: {e}")
```

---

## 🧪 Points de Contrôle

- ✓ Toutes les classes héritent de `DataProcessor`
- ✓ `process()` et `validate()` sont abstraites
- ✓ `format_output()` a une implémentation par défaut
- ✓ Chaque processeur traite son type de données
- ✓ Les erreurs sont gérées correctement
- ✓ Le polymorphisme fonctionne (même interface, comportements différents)

---

---

# 🟠 EXERCICE 1: Flux Polymorphes Avancés

## 📖 Présentation

### Titre: `data_stream.py`

### 📝 Contexte Professionnel

Promotion réussie! 🎉 Vous êtes maintenant **Senior Data Stream Engineer** chez Code Nexus. Votre nouveau défi: construire un **système de flux de données avancé** capable de traiter des **fluxes multiples et complexes** en simultané.

### 🎯 Objectif

Construire une architecture sophistiquée qui gère des **flux de données spécialisés** (capteurs, transactions, événements) avec **traitement par batch, filtrage et statistiques polymorphes**.

---

## 🏗️ Architecture Requise

### Classes à Implémenter

#### 1️⃣ **DataStream (ABC - Classe Abstraite)**

La base de votre système de flux. Gère les fonctionnalités communes à tous les flux.

**Responsabilités:**
- Stocker un identifiant de flux unique
- Gérer les statistiques du flux
- Fournir une interface commune pour tous les flux

**Attributs:**
```python
- stream_id: str              # Identifiant unique du flux
- data_processed: int         # Nombre d'éléments traités
- stats: Dict[str, Union[...]] # Statistiques du flux
```

**Méthodes Abstraites:**
```python
@abstractmethod
def process_batch(self, data_batch: List[Any]) -> str:
    """Traiter un batch de données et retourner un résumé"""
    pass
```

**Méthodes Concrètes (peuvent être override):**
```python
def filter_data(self, data_batch: List[Any], 
                criteria: Optional[str] = None) -> List[Any]:
    """Filtrer les données selon des critères (implémentation par défaut)"""
    pass

def get_stats(self) -> Dict[str, Union[str, int, float]]:
    """Retourner les statistiques du flux (implémentation par défaut)"""
    pass
```

---

#### 2️⃣ **SensorStream(stream_id)**

Spécialisé pour les **données de capteurs environnementaux**.

**Responsabilités:**
- ✅ Traiter les lectures de capteurs (température, humidité, pression)
- ✅ Calculer les moyennes et statistiques
- ✅ Filtrer les données anormales

**Exemple d'utilisation:**
```python
sensor = SensorStream("SENSOR_001")
data = [22.5, 23.1, 21.9, 24.0, 22.3]
result = sensor.process_batch(data)
# "Sensor analysis: 5 readings processed, avg temp: 22.76°C"

stats = sensor.get_stats()
# {'stream_id': 'SENSOR_001', 'processed': 5, 'avg_temp': 22.76}
```

---

#### 3️⃣ **TransactionStream(stream_id)**

Spécialisé pour les **données financières et transactions**.

**Responsabilités:**
- ✅ Traiter les opérations (buy/sell/transfer)
- ✅ Calculer les flux nets et les totaux
- ✅ Détecter les transactions suspectes

**Exemple d'utilisation:**
```python
trans = TransactionStream("TRANS_001")
data = ["buy:100", "sell:150", "buy:75"]
result = trans.process_batch(data)
# "Transaction analysis: 3 operations, net flow: +25 units"

stats = trans.get_stats()
# {'stream_id': 'TRANS_001', 'operations': 3, 'net_flow': 25}
```

---

#### 4️⃣ **EventStream(stream_id)**

Spécialisé pour les **événements système et logs d'activité**.

**Responsabilités:**
- ✅ Traiter les événements système (login, error, logout, etc.)
- ✅ Compter les types d'événements
- ✅ Détecter les erreurs critiques

**Exemple d'utilisation:**
```python
events = EventStream("EVENT_001")
data = ["login", "error", "logout", "error", "login"]
result = events.process_batch(data)
# "Event analysis: 5 events, 2 errors detected"

stats = events.get_stats()
# {'stream_id': 'EVENT_001', 'total_events': 5, 'errors': 2}
```

---

#### 5️⃣ **StreamProcessor**

Le gestionnaire central qui orchestre tous les flux polymorphiquement.

**Responsabilités:**
- ✅ Gérer plusieurs flux simultanément
- ✅ Traiter les batches de données
- ✅ Appliquer les filtres et transformations
- ✅ Générer des rapports globaux

**Exemple d'utilisation:**
```python
manager = StreamProcessor()
manager.add_stream(sensor)
manager.add_stream(transactions)
manager.add_stream(events)

# Traiter tous les flux à travers la même interface
results = manager.process_all_streams(data_dict)
```

---

## 📋 Spécifications Détaillées

### Signatures de Méthodes (OBLIGATOIRE)

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union

class DataStream(ABC):
    """Classe abstraite de base pour tous les flux de données"""
    
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.data_processed = 0
    
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return analysis"""
        pass
    
    def filter_data(self, data_batch: List[Any], 
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria (can be overridden)"""
        return data_batch  
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics (can be overridden)"""
        return {
            'stream_id': self.stream_id,
            'data_processed': self.data_processed
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        # Votre implémentation
        pass


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        # Votre implémentation
        pass


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        # Votre implémentation
        pass


class StreamProcessor:
    """Gestionnaire des flux polymorphiques"""
    def __init__(self):
        self.streams = []
    
    def add_stream(self, stream: DataStream):
        self.streams.append(stream)
    
    def process_all_streams(self, data_dict: Dict[str, List]) -> List[str]:
        # Votre implémentation
        pass
```

---

## 🎨 Résultat Attendu

```
=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

Initializing Sensor Stream...
Stream ID: SENSOR_001, Type: Environmental Data
Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
Sensor analysis: 3 readings processed, avg temp: 22.5°C

Initializing Transaction Stream...
Stream ID: TRANS_001, Type: Financial Data
Processing transaction batch: [buy:100, sell:150, buy:75]
Transaction analysis: 3 operations, net flow: +25 units

Initializing Event Stream...
Stream ID: EVENT_001, Type: System Events
Processing event batch: [login, error, logout]
Event analysis: 3 events, 1 error detected

=== Polymorphic Stream Processing ===
Processing mixed stream types through unified interface...
Batch 1 Results:
- Sensor data: 2 readings processed
- Transaction data: 4 operations processed
- Event data: 3 events processed

Stream filtering active: High-priority data only
Filtered results: 2 critical sensor alerts, 1 large transaction

All streams processed successfully. Nexus throughput optimal.
```

---

## ✅ Autorisé / ❌ Non Autorisé

### ✅ AUTORISÉ

| Technique | Raison |
|-----------|--------|
| **ABC et @abstractmethod** | Créer l'interface polymorphe |
| **isinstance()** | Vérifier les types et instances |
| **print()** | Afficher les résultats |
| **Type hints avancés** | List, Dict, Optional, Union, Any |
| **try/except** | Gérer les erreurs |
| **List comprehensions** | Filtrer et transformer les données |
| **super()** | Appeler les méthodes parentes |
| **Héritage** | Classes dérivées et spécialisées |

### ❌ NON AUTORISÉ

| Pratique | Raison |
|----------|--------|
| **pandas/numpy** | Non autorisés (sauf si spécifié) |
| **eval()** | Risque de sécurité |
| **Globals excessifs** | Code non maintenable |
| **Modification in-place** | Lors du filtrage (créer copies) |

---

## 💡 Conseils d'Implémentation

### 1. Traitement Polymorphe des Flux
```python
# Même interface pour tous les flux
for stream in manager.streams:
    if isinstance(stream, DataStream):
        result = stream.process_batch(data)
        stats = stream.get_stats()
```

### 2. Filtrage de Données
```python
def filter_data(self, data_batch: List[Any], 
                criteria: Optional[str] = None) -> List[Any]:
    if criteria == "high-priority":
        return [d for d in data_batch if self.is_priority(d)]
    return data_batch
```

### 3. Statistiques Spécialisées
```python
def get_stats(self) -> Dict[str, Union[str, int, float]]:
    return {
        'stream_id': self.stream_id,
        'total_readings': len(self.readings),
        'avg_temp': sum(self.readings) / len(self.readings)
    }
```

---

## 🧪 Points de Contrôle

- ✓ `DataStream` est abstraite avec `process_batch()` abstraite
- ✓ `filter_data()` et `get_stats()` ont des implémentations par défaut
- ✓ Les 3 flux spécialisés héritent de `DataStream`
- ✓ `StreamProcessor` gère les flux polymorphiquement
- ✓ Chaque flux traite son domaine spécifique
- ✓ Filtrage et statistiques fonctionnent correctement
- ✓ Gestion d'erreurs appropriée

---

---

# 🔵 EXERCICE 2: Intégration Nexus Complète

## 📖 Présentation

### Titre: `nexus_pipeline.py`

### 📝 Contexte Professionnel

🚀 **PROMOTION FINALE!** Vous êtes maintenant **Chief Architecture Engineer** chez Code Nexus. Votre mission ultime: construire le **système de pipeline complet** qui intègre tous les composants précédents dans une **architecture d'entreprise scalable**.

### 🎯 Objectif

Créer une **pipeline de traitement de données complète** qui démontre le **polymorphisme avancé** au niveau entreprise, avec **chaînage de pipelines, récupération d'erreurs, et monitoring de performance**.

---

## 🏗️ Architecture Requise

### Concept: Protocol et Duck Typing

Avant de continuer, comprenez la différence:

| Concept | Explication |
|---------|------------|
| **ABC (Abstract Base Class)** | Héritage explicite, contrat fort |
| **Protocol (Duck Typing)** | Interface implicite, "if it quacks like a duck..." |

```python
from typing import Protocol

class ProcessingStage(Protocol):
    """Interface pour toute classe avec une méthode process()"""
    def process(self, data: Any) -> Any: ...

# N'importe quelle classe avec process() est un ProcessingStage!
```

---

### Classes à Implémenter

#### 1️⃣ **ProcessingStage (Protocol)**

Interface basée sur duck typing pour tous les étapes de traitement.

**Contrat:**
```python
class ProcessingStage(Protocol):
    """Toute classe avec process() peut être une étape"""
    def process(self, data: Any) -> Any:
        """Traiter les données"""
        ...
```

---

#### 2️⃣ **InputStage() / TransformStage() / OutputStage()**

Les trois étapes de base d'une pipeline.

**InputStage** - Valider et parser l'entrée
```python
class InputStage:
    """Valide et parse les données entrantes"""
    def process(self, data: Any) -> Any:
        # Valider et parser
        return parsed_data
```

**TransformStage** - Enrichir et transformer
```python
class TransformStage:
    """Enrichit et transforme les données"""
    def process(self, data: Any) -> Any:
        # Ajouter métadonnées, valider
        return enriched_data
```

**OutputStage** - Formater et livrer
```python
class OutputStage:
    """Formate et livre les résultats"""
    def process(self, data: Any) -> Any:
        # Formater et préparer
        return formatted_output
```

---

#### 3️⃣ **ProcessingPipeline (ABC)**

La base pour toutes les pipelines. Gère l'orchestration des étapes.

**Responsabilités:**
- ✅ Gérer une liste d'étapes
- ✅ Orchestrer le flux de données
- ✅ Fournir une interface commune

**Attributs:**
```python
- pipeline_id: str
- stages: List[ProcessingStage]
- stats: Dict[str, Any]
```

**Méthodes:**
```python
@abstractmethod
def process(self, data: Any) -> Union[str, Any]:
    """Process data through the pipeline"""
    pass

def add_stage(self, stage: ProcessingStage):
    """Ajouter une étape à la pipeline"""
    pass

def get_stats(self) -> Dict[str, Any]:
    """Retourner les statistiques"""
    pass
```

---

#### 4️⃣ **JSONAdapter(pipeline_id) / CSVAdapter(pipeline_id) / StreamAdapter(pipeline_id)**

Des adaptateurs spécialisés pour différents formats de données.

**JSONAdapter** - Traiter JSON
```python
class JSONAdapter(ProcessingPipeline):
    """Adaptateur pour données JSON"""
    def process(self, data: Any) -> Union[str, Any]:
        # Parse JSON, traite, formate
        return result
```

**CSVAdapter** - Traiter CSV
```python
class CSVAdapter(ProcessingPipeline):
    """Adaptateur pour données CSV"""
    def process(self, data: Any) -> Union[str, Any]:
        # Parse CSV, traite, formate
        return result
```

**StreamAdapter** - Traiter flux temps réel
```python
class StreamAdapter(ProcessingPipeline):
    """Adaptateur pour flux en temps réel"""
    def process(self, data: Any) -> Union[str, Any]:
        # Agrège flux, traite, formate
        return result
```

---

#### 5️⃣ **NexusManager**

Le gestionnaire central de toute l'architecture.

**Responsabilités:**
- ✅ Créer et gérer les pipelines
- ✅ Orchestrer le chaînage de pipelines
- ✅ Gérer les erreurs et la récupération
- ✅ Monitorer les performances

**Exemple d'utilisation:**
```python
manager = NexusManager()
manager.add_pipeline(json_pipeline)
manager.add_pipeline(csv_pipeline)
manager.add_pipeline(stream_pipeline)

# Traiter une chaîne de pipelines
result = manager.process_chain([data1, data2, data3])

# Afficher les statistiques
manager.print_stats()
```

---

## 📋 Spécifications Détaillées

### Signatures de Méthodes (OBLIGATOIRE)

```python
from abc import ABC, abstractmethod
from typing import Protocol, Any, Union, Dict, List, Optional

class ProcessingStage(Protocol):
    """Interface pour les étapes de traitement (duck typing)"""
    def process(self, data: Any) -> Any:
        """Process data through this stage"""
        ...


class InputStage:
    """Étape d'entrée - Validation et parsing"""
    def process(self, data: Any) -> Any:
        # Votre implémentation
        pass


class TransformStage:
    """Étape de transformation - Enrichissement"""
    def process(self, data: Any) -> Any:
        # Votre implémentation
        pass


class OutputStage:
    """Étape de sortie - Formatage"""
    def process(self, data: Any) -> Any:
        # Votre implémentation
        pass


class ProcessingPipeline(ABC):
    """Classe abstraite pour toutes les pipelines"""
    
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats: Dict[str, Any] = {}
    
    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Process data through the pipeline"""
        pass
    
    def add_stage(self, stage: ProcessingStage):
        """Add a processing stage"""
        self.stages.append(stage)
    
    def get_stats(self) -> Dict[str, Any]:
        """Return pipeline statistics"""
        return self.stats


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        # Votre implémentation
        pass


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        # Votre implémentation
        pass


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        # Votre implémentation
        pass


class NexusManager:
    """Gestionnaire central de l'architecture"""
    
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []
    
    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)
    
    def process_all(self, data_dict: Dict) -> List:
        # Votre implémentation
        pass
    
    def process_chain(self, data_list: List) -> Any:
        """Chaîner plusieurs pipelines"""
        # Votre implémentation
        pass
    
    def get_stats(self) -> Dict[str, Any]:
        """Retourner les statistiques globales"""
        # Votre implémentation
        pass
```

---

## 🎨 Résultat Attendu

```
=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===

Initializing Nexus Manager...
Pipeline capacity: 1000 streams/second

Creating Data Processing Pipeline...
Stage 1: Input validation and parsing
Stage 2: Data transformation and enrichment
Stage 3: Output formatting and delivery

=== Multi-Format Data Processing ===

Processing JSON data through pipeline...
Input: {"sensor": "temp", "value": 23.5, "unit": "C"}
Transform: Enriched with metadata and validation
Output: Processed temperature reading: 23.5°C (Normal range)

Processing CSV data through same pipeline...
Input: "user,action,timestamp"
Transform: Parsed and structured data
Output: User activity logged: 1 actions processed

Processing Stream data through same pipeline...
Input: Real-time sensor stream
Transform: Aggregated and filtered
Output: Stream summary: 5 readings, avg: 22.1°C

=== Pipeline Chaining Demo ===
Pipeline A -> Pipeline B -> Pipeline C
Data flow: Raw -> Processed -> Analyzed -> Stored
Chain result: 100 records processed through 3-stage pipeline
Performance: 95% efficiency, 0.2s total processing time

=== Error Recovery Test ===
Simulating pipeline failure...
Error detected in Stage 2: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed

Nexus Integration complete. All systems operational.
```

---

## ✅ Autorisé / ❌ Non Autorisé

### ✅ AUTORISÉ

| Technique | Raison |
|-----------|--------|
| **ABC et @abstractmethod** | Architecture abstraite |
| **Protocol** | Duck typing et interfaces implicites |
| **isinstance()** | Vérifier les types |
| **print()** | Afficher les résultats |
| **Type hints avancés** | Protocol, Union, Optional, Any, etc. |
| **try/except** | Gestion d'erreurs et récupération |
| **List/Dict comprehensions** | Traitement de données |
| **super()** | Appels aux classes parentes |
| **Héritage** | Spécialisation |
| **collections** | Structures de données avancées (deque, Counter, etc.) |

### ❌ NON AUTORISÉ

| Pratique | Raison |
|----------|--------|
| **pandas/numpy/autres libs** | Non autorisées (sauf collections) |
| **eval()/exec()** | Risque de sécurité |
| **Globals excessifs** | Code non maintenable |
| **Module random** | Pas d'aléatoire (sauf si spécifié) |

---

## 💡 Conseils d'Implémentation

### 1. Pipeline Composée avec Étapes
```python
class ProcessingPipeline(ABC):
    def execute_stages(self, data: Any) -> Any:
        """Exécuter toutes les étapes en chaîne"""
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result
```

### 2. Chaînage de Pipelines
```python
def process_chain(self, data_list: List) -> Any:
    """Chaîner les pipelines: output 1 = input 2"""
    result = data_list[0]
    for pipeline in self.pipelines[:-1]:
        result = pipeline.process(result)
    return self.pipelines[-1].process(result)
```

### 3. Gestion d'Erreurs et Récupération
```python
def safe_process(self, pipeline: ProcessingPipeline, 
                 data: Any) -> Union[str, Any]:
    try:
        return pipeline.process(data)
    except Exception as e:
        print(f"Error in {pipeline.pipeline_id}: {e}")
        print("Recovery initiated...")
        # Implémente la logique de récupération
```

### 4. Monitoring de Performance
```python
import time

def process_with_metrics(self, pipeline, data):
    start = time.time()
    result = pipeline.process(data)
    duration = time.time() - start
    
    pipeline.stats['processing_time'] = duration
    pipeline.stats['efficiency'] = (1 - duration / 1.0) * 100
    
    return result
```

---

## 🧪 Points de Contrôle

- ✓ `ProcessingStage` est un Protocol (duck typing)
- ✓ `InputStage`, `TransformStage`, `OutputStage` implémentent `process()`
- ✓ `ProcessingPipeline` est abstraite
- ✓ Les trois adaptateurs héritent de `ProcessingPipeline`
- ✓ `NexusManager` gère plusieurs pipelines
- ✓ Chaînage de pipelines fonctionne correctement
- ✓ Gestion d'erreurs et récupération implémentées
- ✓ Statistiques et monitoring en place

---

---

# 📝 Résumé Global du Projet

## 🎓 Ce que Vous Apprendrez

### Ex0: Fondations
- ✅ ABC et classes abstraites
- ✅ Polymorphisme par surcharge de méthodes
- ✅ Interface commune pour types différents

### Ex1: Avancé
- ✅ Héritage et spécialisation
- ✅ Composition et gestion des collections
- ✅ Filtrage et statistiques polymorphes

### Ex2: Entreprise
- ✅ Protocol et duck typing
- ✅ Composition de pipelines
- ✅ Architecture scalable
- ✅ Gestion d'erreurs et récupération

---

## 🏆 Critères de Succès

Pour réussir ce projet, vous devez démontrer:

1. **Polymorphisme Maîtrisé**
   - Même interface, comportements différents
   - Utilisation correcte de l'héritage

2. **Code Propre et Maintenable**
   - Type hints corrects partout
   - Gestion d'erreurs appropriée
   - Code bien organisé

3. **Extensibilité**
   - Facile d'ajouter de nouveaux types
   - Architecture flexible
   - Respect des principes SOLID

4. **Compréhension Profonde**
   - Capable d'expliquer le polymorphisme
   - Compréhend les avantages du design
   - Peut étendre le système

---

## 📚 Ressources Recommandées

### Concepts Clés
- [ABC - Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Type Hints](https://docs.python.org/3/library/typing.html)
- [Protocol (PEP 544)](https://www.python.org/dev/peps/pep-0544/)

### Patterns de Design
- Strategy Pattern (Ex0)
- Adapter Pattern (Ex2)
- Pipeline Pattern (Ex2)

---

## 🎯 Prochaines Étapes

1. **Lisez attentivement** les spécifications de chaque exercice
2. **Commencez par Ex0** (fondations)
3. **Montez progressivement** vers la complexité
4. **Testez régulièrement** votre code
5. **Refactorisez si nécessaire** pour plus de clarté

---

## ❓ Questions de Réflexion

### Pour chaque exercice, réfléchissez à:

**Ex0:**
- Comment le polymorphisme me permet-il de traiter différents types?
- Qu'est-ce qui rend une classe abstraite utile?

**Ex1:**
- Comment les flux polymorphes simplifient la gestion de données?
- Quels sont les avantages d'avoir des statistiques spécifiques par type?

**Ex2:**
- Comment Protocol diffère-t-il d'ABC?
- Pourquoi le chaînage de pipelines est-il puissant?

---

## 📬 Soumission

Fichiers à soumettre:
- `P05/ex0/stream_processor.py`
- `P05/ex1/data_stream.py`
- `P05/ex2/nexus_pipeline.py`

**Rappel:** Seuls les fichiers dans votre repository seront évalués!

---

**Code Nexus - Bienvenue à bord, Engineer! 🚀**

