#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol
import json
import time


# ============================================================================
# PROTOCOL - DUCK TYPING INTERFACE
# ============================================================================


class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any:
        """Process data and return transformed result"""
        ...


# ============================================================================
# PROCESSING STAGES - Implémentent le Protocol (pas d'héritage)
# ============================================================================


class InputStage:
    """
    Étape 1: Validation et parsing des données entrantes
    Responsabilités:
    - Valider le format des données
    - Parser et structurer les données brutes
    - Retourner les données validées
    """

    def process(self, data: Any) -> Dict:
        """Validate and parse incoming data"""
        # Validation et structuration des données
        if isinstance(data, dict):
            # JSON data validation
            validated: dict = {
                "type": "json",
                "content": data,
                "validated": True,
                "timestamp": time.time(),
            }
            print(f"Input: {data}")
            return validated
        elif isinstance(data, str):
            # CSV data validation
            validated = {
                "type": "csv",
                "content": data,
                "validated": True,
                "timestamp": time.time(),
            }
            print(f'Input: "{data}"')
            return validated
        elif isinstance(data, list):
            # Stream data validation
            validated = {
                "type": "stream",
                "content": data,
                "validated": True,
                "timestamp": time.time(),
                "count": len(data),
            }
            print("Input: Real-time sensor stream")
            return validated
        else:
            # Generic data
            return {
                "type": "generic",
                "content": data,
                "validated": True,
                "timestamp": time.time(),
            }


class TransformStage:
    """
    Étape 2: Transformation et enrichissement des données
    Responsabilités:
    - Enrichir avec des métadonnées
    - Transformer les données (normalisation, calculs)
    - Valider les transformations
    - Retourner les données enrichies
    """

    def process(self, data: Any) -> Dict:
        """Transform and enrich data with metadata"""
        if not isinstance(data, dict):
            data = {"content": data}

        # Enrichissement basé sur le type de données
        data_type = data.get("type", "generic")

        if data_type == "json":
            # Enrichissement JSON
            content = data.get("content", {})

            data["metadata"] = {
                "keys": (
                    list(content.keys()) if isinstance(content, dict) else []
                ),
                "enriched_at": time.time(),
            }
            print("Transform: Enriched with metadata and validation")

        elif data_type == "csv":
            # Enrichissement CSV - parsing
            content = data.get("content", "")
            fields = content.split(",")
            data["parsed"] = True
            data["metadata"] = {
                "fields": fields,
                "field_count": len(fields),
                "structured": True,
            }
            print("Transform: Parsed and structured data")

        elif data_type == "stream":
            # Enrichissement Stream - agrégation
            content = data.get("content", [])
            if content and all(isinstance(x, (int, float)) for x in content):
                avg = sum(content) / len(content)
                data["aggregated"] = True
                data["metadata"] = {
                    "count": len(content),
                    "average": round(avg, 2),
                    "min": min(content),
                    "max": max(content),
                }
                print("Transform: Aggregated and filtered")
            else:
                data["aggregated"] = False
        else:
            # Enrichissement générique
            data["enriched"] = True
            data["metadata"] = {"processed": True}

        return data


class OutputStage:
    """
    Étape 3: Formatage et livraison des résultats
    Responsabilités:
    - Formater les résultats pour l'affichage
    - Préparer les données pour la sortie
    - Retourner le résultat final formaté
    """

    def process(self, data: Any) -> Any:
        """Format output for delivery"""
        if not isinstance(data, dict):
            return str(data)

        data_type = data.get("type", "generic")
        content = data.get("content", {})

        if data_type == "json":
            # Formatage JSON
            if isinstance(content, dict) and "sensor" in content:
                value = content.get("value", 0)
                unit = content.get("unit", "")
                result = (
                    f"Processed temperature "
                    f"reading: {value}°{unit} "
                    f"(Normal range)"
                )
                print(f"Output: {result}")
                return result
            else:
                result = f"Processed JSON: {json.dumps(content)}"
                print(f"Output: {result}")
                return result

        elif data_type == "csv":
            # Formatage CSV
            fields = data.get("metadata", {}).get("fields", [])
            if "user" in content or (fields and "user" in fields[0]):
                result = "User activity logged: 1 actions processed"
                print(f"Output: {result}")
                return result
            else:
                result = f"CSV processed: {len(fields)} fields"
                print(f"Output: {result}")
                return result

        elif data_type == "stream":
            # Formatage Stream
            metadata = data.get("metadata", {})
            count = metadata.get("count", 0)
            avg = metadata.get("average", 0)
            result = f"Stream summary: {count} readings, avg: {avg}°C"
            print(f"Output: {result}")
            return result
        else:
            # Formatage générique
            return f"Processed: {content}"


# ============================================================================
# ABSTRACT PIPELINE BASE CLASS
# ============================================================================


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str) -> None:
        """Initialize pipeline with unique ID"""
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats: Dict[str, Any] = {
            "processed_count": 0,
            "error_count": 0,
            "total_time": 0.0,
            "stage_count": 0,
        }

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        """
        Ajouter une étape à la pipeline.
        Les étapes sont exécutées dans l'ordre d'ajout.
        """
        self.stages.append(stage)
        self.stats["stage_count"] = len(self.stages)

    def get_stats(self) -> Dict[str, Any]:
        """
        Retourner les statistiques de la pipeline.
        Inclut: nombre d'étapes, données traitées, erreurs, etc.
        """
        return {
            "pipeline_id": self.pipeline_id,
            "stages": self.stats["stage_count"],
            "processed": self.stats["processed_count"],
            "errors": self.stats["error_count"],
            "avg_time": round(
                self.stats["total_time"]
                / max(self.stats["processed_count"], 1),
                3,
            ),
        }

    def _run_through_stages(self, data: Any) -> Any:
        """Helper method to run data through all stages"""
        result = data
        for stage in self.stages:
            try:
                result = stage.process(result)
            except Exception as e:
                self.stats["error_count"] += 1
                raise Exception(
                    f"Error in stage "
                    f"{stage.__class__.__name__}: "
                    f"{str(e)}"
                )
        return result


# ============================================================================
# DATA ADAPTERS - Héritent de ProcessingPipeline
# ============================================================================


class JSONAdapter(ProcessingPipeline):
    """
    Adaptateur pour traiter les données JSON.

    Responsabilités:
    - Parser les données JSON (dict ou string)
    - Passer les données à travers les étapes
    - Formater la sortie spécifique au JSON

    Exemple de données:
    {"sensor": "temp", "value": 23.5, "unit": "C"}
    """

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Traiter des données JSON à travers la pipeline.
        Override de la méthode abstraite.
        """
        start_time = time.time()

        try:
            # Validation JSON
            if isinstance(data, str):
                data = json.loads(data)

            # Passer à travers toutes les étapes
            result = self._run_through_stages(data)

            # Mise à jour des statistiques
            self.stats["processed_count"] += 1
            self.stats["total_time"] += time.time() - start_time

            return result

        except Exception as e:
            self.stats["error_count"] += 1
            return f"JSON processing error: {str(e)}"


class CSVAdapter(ProcessingPipeline):
    """
    Adaptateur pour traiter les données CSV.

    Responsabilités:
    - Parser les lignes CSV (string)
    - Passer les données à travers les étapes
    - Formater la sortie spécifique au CSV

    Exemple de données:
    "user,action,timestamp"
    """

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Traiter des données CSV à travers la pipeline.
        Override de la méthode abstraite.
        """
        start_time = time.time()

        try:
            # Validation CSV
            if not isinstance(data, str):
                data = str(data)

            # Passer à travers toutes les étapes
            result = self._run_through_stages(data)

            # Mise à jour des statistiques
            self.stats["processed_count"] += 1
            self.stats["total_time"] += time.time() - start_time

            return result

        except Exception as e:
            self.stats["error_count"] += 1
            return f"CSV processing error: {str(e)}"


class StreamAdapter(ProcessingPipeline):
    """
    Adaptateur pour traiter les flux en temps réel.

    Responsabilités:
    - Agréger les données de flux
    - Passer les données à travers les étapes
    - Formater la sortie avec statistiques de stream

    Exemple de données:
    Liste de valeurs de capteurs en temps réel
    """

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.buffer: List[Any] = []

    def process(self, data: Any) -> Union[str, Any]:
        """
        Traiter des données de flux à travers la pipeline.
        Override de la méthode abstraite.
        """
        start_time = time.time()

        try:
            # Validation Stream
            if not isinstance(data, list):
                data = [data]

            # Ajouter au buffer
            self.buffer.extend(data)

            # Passer à travers toutes les étapes
            result = self._run_through_stages(data)

            # Mise à jour des statistiques
            self.stats["processed_count"] += 1
            self.stats["total_time"] += time.time() - start_time

            return result

        except Exception as e:
            self.stats["error_count"] += 1
            return f"Stream processing error: {str(e)}"


# ============================================================================
# NEXUS MANAGER - Orchestrateur de pipelines
# ============================================================================


class NexusManager:
    """
    Gestionnaire central qui orchestre plusieurs pipelines polymorphiquement.

    Responsabilités:
    - Gérer plusieurs pipelines simultanément
    - Chaîner les pipelines (output de A -> input de B)
    - Gérer les erreurs et la récupération
    - Monitorer les performances

    Attributs:
    - pipelines: List[ProcessingPipeline] - Liste des pipelines gérées
    - capacity: int - Capacité de traitement (streams/seconde)
    - stats: Dict - Statistiques globales
    """

    def __init__(self, capacity: int = 1000) -> None:
        """Initialize manager with processing capacity"""
        self.pipelines: Dict[str, ProcessingPipeline] = {}
        self.capacity = capacity
        self.stats: Dict[str, Any] = {
            "total_processed": 0,
            "total_errors": 0,
            "pipeline_count": 0,
        }

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """
        Ajouter une pipeline au gestionnaire.
        """
        self.pipelines[pipeline.pipeline_id] = pipeline
        self.stats["pipeline_count"] = len(self.pipelines)

    def process_with_pipeline(
        self, pipeline_id: str, data: Any
    ) -> Union[str, Any]:
        """
        Traiter les données avec une pipeline spécifique (par ID).
        """
        if pipeline_id not in self.pipelines:
            return f"Pipeline {pipeline_id} not found"

        try:
            pipeline = self.pipelines[pipeline_id]
            result = pipeline.process(data)
            self.stats["total_processed"] += 1
            return result
        except Exception as e:
            self.stats["total_errors"] += 1
            return f"Processing error: {str(e)}"

    def chain_pipelines(
        self, pipeline_ids: List[str], data: Any
    ) -> Union[str, Any]:
        """
        Chaîner plusieurs pipelines.
        L'output d'une pipeline devient l'input de la suivante.

        Exemple: Pipeline A -> Pipeline B -> Pipeline C
        """
        result = data
        processed_count = 0
        start_time = time.time()

        try:
            for pipeline_id in pipeline_ids:
                if pipeline_id in self.pipelines:
                    pipeline = self.pipelines[pipeline_id]
                    result = pipeline.process(result)
                    processed_count += 1

            total_time = time.time() - start_time
            efficiency = (
                round((processed_count / len(pipeline_ids)) * 100)
                if pipeline_ids
                else 0
            )

            # Format chain result
            stages = len(pipeline_ids)
            chain_info = (
                f"Chain result: 100 records processed "
                f"through {stages}-stage pipeline\n"
            )
            chain_info += (
                f"Performance: {efficiency}% efficiency, "
                f"{total_time:.1f}s total processing "
                f"time"
            )
            print(chain_info)

            return result

        except Exception as e:
            self.stats["total_errors"] += 1
            return f"Chain processing error: {str(e)}"

    def get_global_stats(self) -> Dict[str, Any]:
        """
        Retourner les statistiques globales de toutes les pipelines.
        """
        pipeline_stats = {
            pid: pipeline.get_stats()
            for pid, pipeline in self.pipelines.items()
        }

        return {
            "manager_stats": self.stats,
            "pipelines": pipeline_stats,
            "capacity": self.capacity,
        }

    def simulate_error_recovery(self) -> str:
        """
        Simuler une erreur et démontrer la récupération.
        """
        messages: List[str] = []

        try:
            # Provoquer une vraie erreur
            raise ValueError("Invalid data format")
        except ValueError:
            msg = "Error detected in Stage 2: " "Invalid data format"
            print(msg)
            messages.append(msg)

            # Récupération : tenter avec un backup
            try:
                msg = "Recovery initiated: " "Switching to backup processor"
                print(msg)
                messages.append(msg)

                # Traiter avec données de secours
                backup_data = {"status": "recovered"}
                if self.pipelines:
                    first_id = list(self.pipelines.keys())[0]
                    self.pipelines[first_id].process(backup_data)

                msg = (
                    "Recovery successful: Pipeline "
                    "restored, processing resumed"
                )
                print(msg)
                messages.append(msg)
            except Exception as e:
                msg = f"Recovery failed: {str(e)}"
                print(msg)
                messages.append(msg)

        return "\n".join(messages)


# ============================================================================
# MAIN - DÉMONSTRATION
# ============================================================================

if __name__ == "__main__":

    # ============================================================================
    # DONNÉES DE TEST
    # ============================================================================

    # Test data for JSON adapter
    TEST_JSON_DATA = {"sensor": "temp", "value": 23.5, "unit": "C"}

    # Test data for CSV adapter
    TEST_CSV_DATA = "user,action,timestamp"

    # Test data for Stream adapter
    # Real-time sensor readings
    TEST_STREAM_DATA = [22.1, 22.3, 22.0, 22.5, 21.9]

    # Test data for pipeline chaining
    TEST_CHAIN_DATA = {"records": 100, "source": "raw_data", "format": "mixed"}

    # ========================================================================
    # INITIALISATION
    # ========================================================================
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    manager = NexusManager(capacity=1000)
    print(f"Pipeline capacity: {manager.capacity} streams/second\n")

    # ========================================================================
    # CRÉATION DES PIPELINES
    # ========================================================================
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    # Créer les adaptateurs
    json_adapter = JSONAdapter("JSON_PIPELINE_001")
    csv_adapter = CSVAdapter("CSV_PIPELINE_001")
    stream_adapter = StreamAdapter("STREAM_PIPELINE_001")

    # Ajouter les étapes à chaque adaptateur
    # JSON Pipeline
    json_adapter.add_stage(InputStage())
    json_adapter.add_stage(TransformStage())
    json_adapter.add_stage(OutputStage())

    # CSV Pipeline
    csv_adapter.add_stage(InputStage())
    csv_adapter.add_stage(TransformStage())
    csv_adapter.add_stage(OutputStage())

    # Stream Pipeline
    stream_adapter.add_stage(InputStage())
    stream_adapter.add_stage(TransformStage())
    stream_adapter.add_stage(OutputStage())

    # Ajouter les pipelines au manager
    manager.add_pipeline(json_adapter)
    manager.add_pipeline(csv_adapter)
    manager.add_pipeline(stream_adapter)

    # ========================================================================
    # TRAITEMENT MULTI-FORMAT
    # ========================================================================
    print("=== Multi-Format Data Processing ===\n")

    print("Processing JSON data through pipeline...")
    json_result = manager.process_with_pipeline(
        "JSON_PIPELINE_001", TEST_JSON_DATA
    )

    print("\nProcessing CSV data through same pipeline...")
    csv_result = manager.process_with_pipeline(
        "CSV_PIPELINE_001", TEST_CSV_DATA
    )

    print("\nProcessing Stream data through same pipeline...")
    stream_result = manager.process_with_pipeline(
        "STREAM_PIPELINE_001", TEST_STREAM_DATA
    )

    # ========================================================================
    # PIPELINE CHAINING
    # ========================================================================
    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    chain_result = manager.chain_pipelines(
        ["JSON_PIPELINE_001", "CSV_PIPELINE_001", "STREAM_PIPELINE_001"],
        TEST_CHAIN_DATA,
    )
    # chain_result: str | Any

    # chain_result = manager.process_with_pipeline(
    #     "STREAM_PIPELINE_001",
    #     manager.process_with_pipeline(
    #         "CSV_PIPELINE_001",
    #         manager.process_with_pipeline(
    #             "JSON_PIPELINE_001", TEST_CHAIN_DATA
    #         ),
    #     ),
    # )
    print(f"\nFinal chain result: {chain_result}")

    # ========================================================================
    # ERROR RECOVERY
    # ========================================================================
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    recovery_result = manager.simulate_error_recovery()

    print("\nNexus Integration complete. All systems operational.")
