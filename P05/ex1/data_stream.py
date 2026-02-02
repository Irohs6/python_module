#!/usr/bin/env python3


from abc import ABC, abstractmethod
from encodings.punycode import T
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

# sensor_result = sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"])


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise TypeError("invalid type")
        else:
            self.data_processed += 1
            return (f"Stream ID: {self.stream_id}, Type: Environemental Data\n"
                    f"Processing sensor batch: {data_batch}\n"
                    f"Sensor analysis: {len(data_batch)} reading processed,"
                    f"avg temp: {data_batch[0]}")


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise TypeError("invalid type")
        else:
            self.data_processed += 1
            op_type: str
            str_value: str
            total_value = 0
            for data in data_batch:
                op_type, str_value = data.split(":", 1)
                value = int(str_value)

                if op_type == "buy":
                    total_value += value
                elif op_type == "sell":
                    total_value -= value
                else:
                    raise ValueError(f"unknown operation type: {op_type}")

                if total_value > 0:
                    msg = f"net flow: +{total_value} units"
                else:
                    msg = f"deficit flow: {total_value} units"
            return (f"Stream ID: {self.stream_id}, Type: Financial Data\n"
                    f"Processing transaction batch:: {data_batch}\n"
                    f"Transaction analysis:  {len(data_batch)}  operations, "
                    f"{msg}")


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise TypeError("invalid type")
        else:
            self.data_processed += 1
            error: int = 0
            for data in data_batch:
                if data == "error":
                    error += 1
            return (f"Stream ID: {self.stream_id}, Type: Environemental Data\n"
                    f"Processing event batch: {data_batch}\n"
                    f"Event analysis: {len(data_batch)} events, "
                    f"{error} error detected")


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


if __name__ == "__main__":
    # Test SensorStream
    print("=== SENSOR STREAM ===")
    sensor = SensorStream("SENSOR_001")
    sensor_result = sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"])
    print(f"Result: {sensor_result}")
    print(f"Stats: {sensor.get_stats()}\n")

    # Test TransactionStream
    print("=== TRANSACTION STREAM ===")
    trans = TransactionStream("TRANS_001")
    trans_result = trans.process_batch(["buy:100", "sell:150", "buy:75"])
    print(f"Result: {trans_result}")
    print(f"Stats: {trans.get_stats()}\n")

    # Test EventStream
    print("=== EVENT STREAM ===")
    events = EventStream("EVENT_001")
    events_result = events.process_batch(["login", "error", "logout"])
    print(f"Result: {events_result}")
    print(f"Stats: {events.get_stats()}\n")

    # Test StreamProcessor
    print("=== STREAM PROCESSOR ===")
    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(trans)
    manager.add_stream(events)

    data_dict = {
        "sensor_stream": ["temp:22.5", "humidity:65", "pressure:1013"],
        "transaction_stream": ["buy:100", "sell:150", "buy:75"],
        "event_stream": ["login", "error", "logout"]
    }

    results = manager.process_all_streams(data_dict)
    print(f"All results: {results}")