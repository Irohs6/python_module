#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any, Dict, Union, List, Optional


class DataStream(ABC):
    """Classe abstraite de base pour tous les flux de données"""

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.data_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return analysis"""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria (can be overridden)"""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics (can be overridden)"""
        return {
            "stream_id": self.stream_id,
            "data_processed": self.data_processed,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, List):
            raise TypeError("invalid type")


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:

        pass


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:

        pass


class StreamProcessor:
    """Gestionnaire des flux polymorphiques"""

    def __init__(self):
        self.streams = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all_streams(self, data_dict: Dict[str, List]) -> List[str]:
        for stream in self.streams:
            stream.process_batch(data_dict)
        pass

