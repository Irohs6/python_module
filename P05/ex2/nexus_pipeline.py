#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol, Optional
from collections import deque


# ============================================================================
# PROTOCOL - DUCK TYPING INTERFACE
# ============================================================================


class ProcessingStage(Protocol):
    """
    Interface pour les étapes de traitement (duck typing).
    Toute classe avec une méthode process() peut être une étape.
    """

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

    def process(self, data: Any) -> Any:
        # TODO: Implémenter la validation et le parsing
        # Input: données brutes (string, dict, etc.)
        # Output: données validées et structurées
        pass


class TransformStage:
    """
    Étape 2: Transformation et enrichissement des données
    Responsabilités:
    - Enrichir avec des métadonnées
    - Transformer les données (normalisation, calculs)
    - Valider les transformations
    - Retourner les données enrichies
    """

    def process(self, data: Any) -> Any:
        # TODO: Implémenter la transformation et l'enrichissement
        # Input: données validées
        # Output: données enrichies avec métadonnées
        pass


class OutputStage:
    """
    Étape 3: Formatage et livraison des résultats
    Responsabilités:
    - Formater les résultats pour l'affichage
    - Préparer les données pour la sortie
    - Retourner le résultat final formaté
    """

    def process(self, data: Any) -> Any:
        # TODO: Implémenter le formatage de sortie
        # Input: données enrichies
        # Output: résultat formaté (string généralement)
        pass


# ============================================================================
# ABSTRACT PIPELINE BASE CLASS
# ============================================================================


class ProcessingPipeline(ABC):
    """
    Classe abstraite de base pour toutes les pipelines.
    Gère l'orchestration des étapes de traitement.

    Attributs:
    - pipeline_id: str - Identifiant unique de la pipeline
    - stages: List[ProcessingStage] - Liste des étapes de traitement
    - stats: Dict - Statistiques de traitement
    """

    def __init__(self, pipeline_id: str):
        # TODO: Initialiser les attributs
        # - pipeline_id
        # - stages (liste vide)
        # - stats (dict pour les statistiques)
        pass

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """
        Traiter les données à travers la pipeline.
        Méthode abstraite - doit être implémentée par les sous-classes.
        """
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        """
        Ajouter une étape à la pipeline.
        Les étapes sont exécutées dans l'ordre d'ajout.
        """
        # TODO: Ajouter l'étape à la liste des stages
        pass

    def get_stats(self) -> Dict[str, Any]:
        """
        Retourner les statistiques de la pipeline.
        Inclut: nombre d'étapes, données traitées, erreurs, etc.
        """
        # TODO: Retourner les statistiques
        pass


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

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)
        # TODO: Ajouter des attributs spécifiques si nécessaire

    def process(self, data: Any) -> Union[str, Any]:
        """
        Traiter des données JSON à travers la pipeline.
        Override de la méthode abstraite.
        """
        # TODO: Implémenter le traitement JSON
        # 1. Valider que c'est du JSON (dict ou string JSON)
        # 2. Passer à travers toutes les étapes
        # 3. Formater et retourner le résultat
        pass


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

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)
        # TODO: Ajouter des attributs spécifiques si nécessaire

    def process(self, data: Any) -> Union[str, Any]:
        """
        Traiter des données CSV à travers la pipeline.
        Override de la méthode abstraite.
        """
        # TODO: Implémenter le traitement CSV
        # 1. Parser le CSV (split par virgule, etc.)
        # 2. Passer à travers toutes les étapes
        # 3. Formater et retourner le résultat
        pass


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

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)
        # TODO: Ajouter des attributs spécifiques (buffer, agregation, etc.)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Traiter des données de flux à travers la pipeline.
        Override de la méthode abstraite.
        """
        # TODO: Implémenter le traitement de flux
        # 1. Agréger les données du flux
        # 2. Passer à travers toutes les étapes
        # 3. Formater et retourner le résultat avec stats
        pass


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

    def __init__(self, capacity: int = 1000):
        # TODO: Initialiser les attributs
        # - pipelines (liste vide)
        # - capacity
        # - stats (dict pour statistiques globales)
        pass

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """
        Ajouter une pipeline au gestionnaire.
        """
        # TODO: Ajouter la pipeline à la liste
        pass

    def process_with_pipeline(self, pipeline_id: str, data: Any) -> Union[str, Any]:
        """
        Traiter les données avec une pipeline spécifique (par ID).
        """
        # TODO: Trouver la pipeline par ID et traiter les données
        pass

    def chain_pipelines(self, pipeline_ids: List[str], data: Any) -> Union[str, Any]:
        """
        Chaîner plusieurs pipelines.
        L'output d'une pipeline devient l'input de la suivante.

        Exemple: Pipeline A -> Pipeline B -> Pipeline C
        """
        # TODO: Implémenter le chaînage de pipelines
        # 1. Passer data à travers la première pipeline
        # 2. Utiliser le résultat comme input pour la suivante
        # 3. Répéter pour toutes les pipelines
        # 4. Retourner le résultat final
        pass

    def get_global_stats(self) -> Dict[str, Any]:
        """
        Retourner les statistiques globales de toutes les pipelines.
        """
        # TODO: Agréger les stats de toutes les pipelines
        pass

    def simulate_error_recovery(self) -> str:
        """
        Simuler une erreur et démontrer la récupération.
        """
        # TODO: Implémenter la simulation d'erreur et récupération
        pass


# ============================================================================
# DONNÉES DE TEST
# ============================================================================

# Test data for JSON adapter
TEST_JSON_DATA = {"sensor": "temp", "value": 23.5, "unit": "C"}

# Test data for CSV adapter
TEST_CSV_DATA = "user,action,timestamp"

# Test data for Stream adapter
TEST_STREAM_DATA = [22.1, 22.3, 22.0, 22.5, 21.9]  # Real-time sensor readings

# Test data for pipeline chaining
TEST_CHAIN_DATA = {"records": 100, "source": "raw_data", "format": "mixed"}


# ============================================================================
# MAIN - DÉMONSTRATION
# ============================================================================

if __name__ == "__main__":
    # ========================================================================
    # INITIALISATION
    # ========================================================================
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    # TODO: Créer le NexusManager
    # manager = NexusManager(capacity=1000)
    # print(f"Pipeline capacity: {manager.capacity} streams/second\n")

    # ========================================================================
    # CRÉATION DES PIPELINES
    # ========================================================================
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    # TODO: Créer les adaptateurs
    # json_adapter = JSONAdapter("JSON_PIPELINE_001")
    # csv_adapter = CSVAdapter("CSV_PIPELINE_001")
    # stream_adapter = StreamAdapter("STREAM_PIPELINE_001")

    # TODO: Ajouter les étapes à chaque adaptateur
    # json_adapter.add_stage(InputStage())
    # json_adapter.add_stage(TransformStage())
    # json_adapter.add_stage(OutputStage())
    # ... (pareil pour csv et stream)

    # TODO: Ajouter les pipelines au manager
    # manager.add_pipeline(json_adapter)
    # manager.add_pipeline(csv_adapter)
    # manager.add_pipeline(stream_adapter)

    # ========================================================================
    # TRAITEMENT MULTI-FORMAT
    # ========================================================================
    print("=== Multi-Format Data Processing ===\n")

    print("Processing JSON data through pipeline...")
    # TODO: Traiter les données JSON
    # json_result = manager.process_with_pipeline("JSON_PIPELINE_001", TEST_JSON_DATA)
    # Afficher: Input, Transform, Output

    print("\nProcessing CSV data through same pipeline...")
    # TODO: Traiter les données CSV
    # csv_result = manager.process_with_pipeline("CSV_PIPELINE_001", TEST_CSV_DATA)
    # Afficher: Input, Transform, Output

    print("\nProcessing Stream data through same pipeline...")
    # TODO: Traiter les données Stream
    # stream_result = manager.process_with_pipeline("STREAM_PIPELINE_001", TEST_STREAM_DATA)
    # Afficher: Input, Transform, Output

    # ========================================================================
    # PIPELINE CHAINING
    # ========================================================================
    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    # TODO: Démontrer le chaînage de pipelines
    # chain_result = manager.chain_pipelines(
    #     ["JSON_PIPELINE_001", "CSV_PIPELINE_001", "STREAM_PIPELINE_001"],
    #     TEST_CHAIN_DATA
    # )
    # Afficher: Chain result avec 100 records, 3 stages, performance

    # ========================================================================
    # ERROR RECOVERY
    # ========================================================================
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    # TODO: Simuler erreur et récupération
    # recovery_result = manager.simulate_error_recovery()
    # Afficher: Error detected, Recovery initiated, Recovery successful

    print("\nNexus Integration complete. All systems operational.")
