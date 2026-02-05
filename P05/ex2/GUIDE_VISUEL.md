# 🎓 Guide Visuel - Nexus Integration

## 📊 Diagramme de l'Architecture Complète

```
                    ┌─────────────────────────────────┐
                    │      NexusManager               │
                    │  ┌──────────────────────────┐   │
                    │  │ pipelines: Dict          │   │
                    │  │ capacity: 1000           │   │
                    │  │ stats: Dict              │   │
                    │  └──────────────────────────┘   │
                    │                                 │
                    │  + add_pipeline()               │
                    │  + process_with_pipeline()      │
                    │  + chain_pipelines()            │
                    │  + simulate_error_recovery()    │
                    └────────┬────────────────────────┘
                             │
                ┏━━━━━━━━━━━━┻━━━━━━━━━━━━┓
                ┃     contient / gère      ┃
                ┗━━━━━━━━━━━━┳━━━━━━━━━━━━┛
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│  JSONAdapter     │ │   CSVAdapter     │ │  StreamAdapter   │
├──────────────────┤ ├──────────────────┤ ├──────────────────┤
│ pipeline_id      │ │ pipeline_id      │ │ pipeline_id      │
│ stages: []       │ │ stages: []       │ │ stages: []       │
│ stats: {}        │ │ stats: {}        │ │ stats: {}        │
│                  │ │                  │ │ buffer: []       │
├──────────────────┤ ├──────────────────┤ ├──────────────────┤
│ + process()      │ │ + process()      │ │ + process()      │
└────────┬─────────┘ └────────┬─────────┘ └────────┬─────────┘
         │                    │                    │
         │  hérite de         │  hérite de         │  hérite de
         │                    │                    │
         └────────────────────┼────────────────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │  ProcessingPipeline    │  ◄── ABC (Abstract)
                  ├────────────────────────┤
                  │ pipeline_id: str       │
                  │ stages: List           │
                  │ stats: Dict            │
                  ├────────────────────────┤
                  │ + add_stage()          │
                  │ + process() [ABSTRACT] │
                  │ + get_stats()          │
                  │ + _run_through_stages()│
                  └────────┬───────────────┘
                           │
                           │  utilise
                           ▼
                  ┌────────────────────────┐
                  │  ProcessingStage       │  ◄── Protocol
                  ├────────────────────────┤
                  │ + process(data) -> Any │
                  └────────┬───────────────┘
                           │
            ┏━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┓
            ┃     implémentent             ┃
            ┗━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┛
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ InputStage   │  │TransformStage│  │ OutputStage  │
├──────────────┤  ├──────────────┤  ├──────────────┤
│+ process()   │  │+ process()   │  │+ process()   │
└──────────────┘  └──────────────┘  └──────────────┘
     │                  │                  │
     │                  │                  │
     └──────────────────┴──────────────────┘
                        │
                        ▼
            Pas d'héritage ! Juste une
            méthode process() (Duck Typing)
```

## 🔄 Flux de Données - Traitement Simple

```
┌────────────────────────────────────────────────────────────────────┐
│                    TRAITEMENT JSON                                  │
└────────────────────────────────────────────────────────────────────┘

Input Data: {"sensor": "temp", "value": 23.5, "unit": "C"}
    │
    ▼
┌─────────────────────────────────────────────┐
│  manager.process_with_pipeline()            │
│  "JSON_PIPELINE_001"                        │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  JSONAdapter   │
         │  .process()    │
         └────────┬───────┘
                  │
    ┏━━━━━━━━━━━━┻━━━━━━━━━━━━┓
    ┃  _run_through_stages()   ┃
    ┗━━━━━━━━━━━━┳━━━━━━━━━━━━┛
                  │
    ┌─────────────┴─────────────┐
    │                           │
    ▼                           │
┌─────────────┐                 │
│ InputStage  │                 │
│ .process()  │                 │
└──────┬──────┘                 │
       │                        │
       │ {"type": "json",       │
       │  "content": {...},     │
       │  "validated": True}    │
       │                        │
       ▼                        │
┌─────────────────┐             │
│ TransformStage  │             │
│ .process()      │             │
└──────┬──────────┘             │
       │                        │
       │ {"type": "json",       │
       │  "enriched": True,     │
       │  "metadata": {...}}    │
       │                        │
       ▼                        │
┌─────────────┐                 │
│ OutputStage │                 │
│ .process()  │                 │
└──────┬──────┘                 │
       │                        │
       │ "Processed temp        │
       │  reading: 23.5°C"      │
       │                        │
       └────────────────────────┘
                  │
                  ▼
         Result: "Processed temperature reading: 23.5°C (Normal range)"
```

## 🔗 Flux de Données - Chaînage de Pipelines

```
┌────────────────────────────────────────────────────────────────────┐
│                    PIPELINE CHAINING                                │
└────────────────────────────────────────────────────────────────────┘

Input: {"records": 100, "source": "raw_data"}
    │
    ▼
┌──────────────────────────────────────────────────┐
│  manager.chain_pipelines()                       │
│  ["JSON_PIPELINE", "CSV_PIPELINE", "STREAM_..."] │
└──────────────────┬───────────────────────────────┘
                   │
    ┌──────────────┴──────────────┐
    │                             │
    ▼                             │
┌─────────────────┐               │
│  PIPELINE A     │               │
│  (JSONAdapter)  │               │
└────────┬────────┘               │
         │                        │
         │ result = Process JSON  │
         │                        │
         ▼                        │
┌─────────────────┐               │
│  PIPELINE B     │               │
│  (CSVAdapter)   │               │
└────────┬────────┘               │
         │                        │
         │ result = Process CSV   │
         │                        │
         ▼                        │
┌─────────────────┐               │
│  PIPELINE C     │               │
│  (StreamAdapter)│               │
└────────┬────────┘               │
         │                        │
         │ result = Process Stream│
         │                        │
         └────────────────────────┘
                   │
                   ▼
    "100 records processed through 3-stage pipeline"
    "Performance: 100% efficiency, 0.0s"
```

## 🎯 Concepts Visuels

### 1. Protocol vs ABC

```
┌───────────────────────────────────────────────────────────┐
│                      PROTOCOL                             │
├───────────────────────────────────────────────────────────┤
│  class ProcessingStage(Protocol):                         │
│      def process(self, data: Any) -> Any: ...            │
│                                                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │InputStage│  │Transform │  │ Output   │              │
│  │          │  │  Stage   │  │  Stage   │              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       │             │             │                      │
│       └─────────────┴─────────────┘                      │
│              Implémentent juste                          │
│              process() - pas d'héritage !                │
│                                                           │
│  ✓ Flexible                                              │
│  ✓ Duck typing                                           │
│  ✓ Pas besoin d'hériter                                  │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│                         ABC                               │
├───────────────────────────────────────────────────────────┤
│  class ProcessingPipeline(ABC):                           │
│      @abstractmethod                                      │
│      def process(self, data): pass                        │
│                                                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  JSON    │  │   CSV    │  │  Stream  │              │
│  │ Adapter  │  │ Adapter  │  │ Adapter  │              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       │             │             │                      │
│       └─────────────┴─────────────┘                      │
│           Héritent de                                    │
│           ProcessingPipeline                             │
│           DOIVENT implémenter process()                  │
│                                                           │
│  ✓ Structure stricte                                     │
│  ✓ Force l'implémentation                                │
│  ✓ Héritage obligatoire                                  │
└───────────────────────────────────────────────────────────┘
```

### 2. Polymorphisme en Action

```
┌──────────────────────────────────────────────────────┐
│         MÊME INTERFACE, COMPORTEMENTS DIFFÉRENTS      │
└──────────────────────────────────────────────────────┘

manager.process_with_pipeline(pipeline_id, data)
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │  JSON   │ │   CSV   │ │ Stream  │
   │ Adapter │ │ Adapter │ │ Adapter │
   └─────────┘ └─────────┘ └─────────┘
        │           │           │
        ▼           ▼           ▼
   Parse JSON  Parse CSV   Aggregate
   Validate    Structure   Calculate
   Format      Count       Summary

  MÊME APPEL ────────────────► RÉSULTATS DIFFÉRENTS
```

### 3. Héritage avec super()

```
┌────────────────────────────────────────────────┐
│  class ProcessingPipeline(ABC):                │
│      def __init__(self, pipeline_id):          │
│          self.pipeline_id = pipeline_id        │
│          self.stages = []                      │
│          self.stats = {}                       │
└────────────────┬───────────────────────────────┘
                 │
                 │  hérite
                 │
┌────────────────▼───────────────────────────────┐
│  class JSONAdapter(ProcessingPipeline):        │
│      def __init__(self, pipeline_id):          │
│          super().__init__(pipeline_id) ◄───┐   │
│                                            │   │
│          # Appelle __init__ du parent ─────┘   │
│          # Initialise pipeline_id, stages      │
└────────────────────────────────────────────────┘

SANS super() : ❌ Les attributs du parent ne sont pas initialisés
AVEC super() : ✓ Tout est correctement initialisé
```

## 📝 Checklist Pratique

```
☐  Je comprends Protocol (duck typing)
   └─ Toute classe avec process() fonctionne
   └─ Pas besoin d'hériter

☐  Je comprends ABC (classe abstraite)
   └─ Ne peut pas être instanciée
   └─ Force l'implémentation de certaines méthodes
   └─ Les sous-classes DOIVENT hériter

☐  Je sais utiliser super()
   └─ Appelle les méthodes du parent
   └─ Essentiel dans __init__

☐  Je comprends le polymorphisme
   └─ Même interface, comportements différents
   └─ Permet de traiter uniformément

☐  Je comprends l'architecture
   └─ Manager → Pipelines → Stages
   └─ Composition et héritage
```

## 🚀 Exercice Pratique

Essayez de créer votre propre adapter :

```python
class XMLAdapter(ProcessingPipeline):
    """Adapter pour traiter du XML"""
    
    def __init__(self, pipeline_id: str):
        # TODO : Initialiser avec super()
        pass
    
    def process(self, data: Any) -> Union[str, Any]:
        # TODO : Parser XML et traiter
        pass

# Utilisation
xml_adapter = XMLAdapter("XML_PIPELINE_001")
xml_adapter.add_stage(InputStage())
xml_adapter.add_stage(TransformStage())
xml_adapter.add_stage(OutputStage())

manager.add_pipeline(xml_adapter)
result = manager.process_with_pipeline("XML_PIPELINE_001", xml_data)
```

---

## 📚 Ressources Supplémentaires

- **Protocol** : PEP 544 - Structural Subtyping (Duck Typing)
- **ABC** : PEP 3119 - Abstract Base Classes
- **super()** : Understanding Python's Super
- **Polymorphisme** : SOLID Principles - Liskov Substitution
- **Pipeline Pattern** : Enterprise Integration Patterns

## ✨ Points Clés à Retenir

1. **Protocol** = Interface flexible (duck typing)
2. **ABC** = Structure stricte (héritage forcé)
3. **super()** = Réutilisation du code parent
4. **Polymorphisme** = Traitement uniforme de différents types
5. **Pipeline** = Chaîne modulaire de traitement

---

🎓 **Félicitations !** Vous maîtrisez maintenant les concepts avancés de Python pour construire des systèmes d'entreprise robustes et maintenables.
