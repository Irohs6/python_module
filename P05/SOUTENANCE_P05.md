# SOUTENANCE P05 — Polymorphic Data Streams

## Structure du projet (ce que tu rends)
```
P05/
├── ex0/stream_processor.py    ← ABC + 3 processors
├── ex1/data_stream.py         ← ABC + 3 streams + StreamProcessor
├── ex2/nexus_pipeline.py      ← Protocol + ABC + 3 adapters + NexusManager
└── main.py                    ← Tests automatiques (pas à toi)
```

---

## CONCEPTS CLÉS À MAÎTRISER

### 1. Classe Abstraite (ABC + @abstractmethod)
**Question type : "Pourquoi utiliser une classe abstraite ?"**
> Une ABC définit un **contrat** : toutes les sous-classes DOIVENT implémenter les méthodes abstraites. Si tu oublies, Python lève une `TypeError` à l'instanciation.

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:  # Obligatoire dans les enfants
        pass

    def format_output(self, result: str) -> str:  # Défaut, overridable
        return f"Output: {result}"
```

**Point clé :** Tu ne peux PAS faire `DataProcessor()` directement → c'est le but, ça force l'implémentation.

---

### 2. Method Overriding (surcharge de méthode)
**Question type : "Montre-moi un override dans ton code"**

| Classe | Méthode overridée | Comportement spécialisé |
|--------|-------------------|------------------------|
| `NumericProcessor` | `process()` | Calcule sum + avg |
| `TextProcessor` | `process()` | Compte chars + words |
| `LogProcessor` | `process()` + `format_output()` | Parse le level + format "LOG >>" |

```python
# Parent (défaut)
def format_output(self, result: str) -> str:
    return f"Output: {result}"

# LogProcessor (override)
def format_output(self, result: str) -> str:
    return f"LOG >> {result}"  # Comportement spécialisé
```

**Point clé :** La signature reste la même (`self, result: str -> str`), seul le comportement change.

---

### 3. Polymorphisme (même interface, comportement différent)
**Question type : "Comment le polymorphisme fonctionne ici ?"**

```python
# MÊME appel pour 3 types différents :
processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
for p in processors:
    p.validate(data)      # Chaque classe valide différemment
    p.process(data)       # Chaque classe traite différemment
    p.format_output(res)  # Chaque classe formate différemment
```

**Point clé :** Le code appelant n'a PAS besoin de savoir quel type il manipule. Il utilise juste l'interface commune `DataProcessor`.

---

### 4. `super().__init__()` — Appel au constructeur parent
**Question type : "Pourquoi `super()` ?"**

```python
class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)  # Initialise stream_id + data_processed
        self.total_readings = 0      # Ajoute ses propres attributs
```

**Point clé :** `super()` réutilise le code du parent au lieu de le copier. Sans ça, `self.stream_id` ne serait pas initialisé.

---

### 5. Protocol vs ABC (Ex2 — question probable)
**Question type : "Quelle différence entre Protocol et ABC ?"**

| | ABC | Protocol |
|---|-----|----------|
| **Héritage** | Obligatoire (`class X(ABC)`) | Pas nécessaire (duck typing) |
| **Vérification** | À l'instanciation | Structurelle (si ça a `process()`, ça marche) |
| **Utilisé pour** | `ProcessingPipeline` | `ProcessingStage` |

```python
# Protocol : pas besoin d'hériter
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...

# InputStage n'hérite PAS de ProcessingStage, mais ça marche
class InputStage:  # Pas de parenthèse
    def process(self, data: Any) -> Any:  # Même signature = compatible
        ...
```

**Point clé :** Les Stages utilisent le **duck typing** ("si ça marche comme un canard..."). Les Adapters utilisent l'**héritage classique** d'ABC.

---

### 6. Héritage des Adapters (Ex2)
**Question type : "Explique la hiérarchie de classes de l'ex2"**

```
ProcessingStage (Protocol)          ProcessingPipeline (ABC)
    ↑ duck typing                       ↑ héritage
InputStage                          JSONAdapter
TransformStage                      CSVAdapter
OutputStage                         StreamAdapter
                                        ↓ utilise
                                    NexusManager (orchestrateur)
```

- `JSONAdapter`, `CSVAdapter`, `StreamAdapter` **héritent** de `ProcessingPipeline`
- Chacun **override** la méthode `process()` pour son format
- `NexusManager` les manipule **polymorphiquement** (il ne sait pas quel adapter il utilise)

---

### 7. Pipeline Chaining (Ex2)
**Question type : "Comment fonctionne le chaining ?"**

```python
def chain_pipelines(self, pipeline_ids, data):
    result = data
    for pipeline_id in pipeline_ids:
        pipeline = self.pipelines[pipeline_id]
        result = pipeline.process(result)  # Output de A → Input de B
    return result
```

**Point clé :** Le résultat d'un pipeline est passé comme donnée au suivant. C'est le **pattern pipeline**.

---

### 8. Error Handling
**Question type : "Comment gères-tu les erreurs ?"**

- **Ex0 :** `validate()` lève `TypeError`/`ValueError`, capturées par `try/except`
- **Ex1 :** `StreamProcessor.process_all_streams()` avec `try/except` par stream
- **Ex2 :** `simulate_error_recovery()` — provoque une vraie `ValueError`, la capture, puis récupère avec des données de secours

```python
# Ex2 - Vraie récupération d'erreur
try:
    raise ValueError("Invalid data format")
except ValueError:
    # Récupération avec backup
    self.pipelines[first_id].process(backup_data)
```

---

### 9. Type Annotations
**Question type : "Pourquoi les annotations de type ?"**

```python
def process_batch(self, data_batch: List[Any]) -> str:
def get_stats(self) -> Dict[str, Union[str, int, float]]:
def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
```

- `Any` : n'importe quel type
- `List[Any]` : liste de n'importe quoi
- `Dict[str, Union[str, int, float]]` : dict avec clés str, valeurs str/int/float
- `Optional[str]` : `str` ou `None`
- `-> None` sur tous les `__init__`

**Point clé :** Les annotations ne changent PAS le comportement du code, mais documentent les types attendus et permettent la vérification statique.

---

## QUESTIONS PIÈGES COURANTES

### "Que se passe-t-il si tu n'implémentes pas une méthode abstraite ?"
> `TypeError: Can't instantiate abstract class X with abstract method process`
> Python refuse de créer l'objet.

### "Peut-on instancier `DataProcessor` directement ?"
> Non, c'est une ABC. `DataProcessor()` → `TypeError`.

### "Pourquoi `LogProcessor` override `format_output()` mais pas les autres ?"
> Parce que `NumericProcessor` et `TextProcessor` utilisent le format par défaut du parent (`"Output: ..."`). `LogProcessor` a besoin d'un format différent (`"LOG >> ..."`).

### "Quelle est la différence entre `@abstractmethod` et une méthode normale dans l'ABC ?"
> `@abstractmethod` = OBLIGATOIRE à implémenter. Méthode normale = fournit un comportement par défaut que les enfants PEUVENT override.

### "Si on te demande d'ajouter un nouveau type de processor, comment tu fais ?"
> Je crée une nouvelle classe qui hérite de `DataProcessor` et j'implémente `process()` et `validate()`. C'est tout. Le reste du code fonctionne automatiquement grâce au polymorphisme.

```python
class XMLProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return "Processed XML data"
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and data.startswith("<")
```

### "Pourquoi `isinstance()` dans le sujet ?"
> Pour vérifier le type à l'exécution. Exemple : `isinstance(data, list)` vérifie si `data` est bien une liste avant de la traiter.

---

## COMMANDES UTILES PENDANT LA SOUTENANCE

```bash
# Lancer les tests
python main.py

# Lancer un exercice seul
python ex0/stream_processor.py
python ex1/data_stream.py
python ex2/nexus_pipeline.py

# Vérifier flake8
python -m flake8 ex0/stream_processor.py ex1/data_stream.py ex2/nexus_pipeline.py
```

---

## RÉSUMÉ EN 30 SECONDES

> **P05 = Polymorphisme par héritage.**
> - On crée une **classe abstraite** (ABC) qui définit l'interface commune.
> - Les **sous-classes** implémentent (override) les méthodes abstraites avec leur propre logique.
> - Le code appelant utilise **la même interface** pour tous les types → c'est le **polymorphisme**.
> - Ex0 = base simple (3 processors), Ex1 = streams avec stats (3 streams + manager), Ex2 = pipeline complet (Protocol + ABC + adapters + chaining + error recovery).
