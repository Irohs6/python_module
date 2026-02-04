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
        self.total_readings = 0
        self.sum_temp = 0
        self.count_temp = 0

    def filter_data(self, data_batch, criteria=None):
        if criteria == "temp":
            return [data for data in data_batch if data.startswith("temp")]
        elif criteria == "humidity":
            return [data for data in data_batch if data.startswith("humidity")]
        return data_batch

    def process_batch(self, data_batch: List[Any]) -> str:

        if not isinstance(data_batch, list):
            raise TypeError("invalid type")

        self.data_processed += len(data_batch)
        self.total_readings += len(data_batch)

        temps = [
            float(data.split(":")[1]) for data in data_batch if data.startswith("temp")
        ]

        if not temps:
            return "No temperature data to process"

        self.sum_temp += sum(temps)
        self.count_temp += len(temps)

        stats = self.get_stats()
        return (
            f"Stream ID: {stats['stream_id']}, Type: Environmental Data\n"
            f"Processing sensor batch: {data_batch}\n"
            f"Sensor analysis: {stats['total_readings']} readings processed, "
            f"avg temp: {stats['avg_temp']:.1f}°C"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return specialized sensor statistics"""
        stats = super().get_stats()
        if self.count_temp > 0:
            stats["total_readings"] = self.total_readings
            stats["avg_temp"] = self.sum_temp / self.count_temp
        return stats


class TransactionStream(DataStream):

    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.total_operations = 0
        self.total_net_flow = 0

    def filter_data(self, data_batch, criteria=None):
        """Filter transactions by type"""
        if criteria == "buy":
            return [data for data in data_batch if data.startswith("buy")]
        elif criteria == "sell":
            return [data for data in data_batch if data.startswith("sell")]
        elif criteria == "large":
            # Filter large transactions (>100 units)
            result = []
            for data in data_batch:
                try:
                    if ":" not in data:
                        raise ValueError(f"Invalid transaction format: {data}")
                    _, str_value = data.split(":", 1)
                    value = int(str_value)
                    if value > 100:
                        result.append(data)
                except (ValueError, IndexError) as e:
                    # Skip invalid transactions but continue processing
                    print(f"Warning: Skipping invalid transaction '{data}': {e}")
                    continue
            return result
        return data_batch

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise TypeError("invalid type")
        else:
            self.data_processed += len(data_batch)
            self.total_operations += len(data_batch)
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

            self.total_net_flow += total_value

            stats = self.get_stats()
            net_flow = stats["net_flow"]
            if net_flow > 0:
                msg = f"net flow: +{net_flow} units"
            else:
                msg = f"net flow: {net_flow} units"
            return (
                f"Stream ID: {stats['stream_id']}, Type: Financial Data\n"
                f"Processing transaction batch: {data_batch}\n"
                f"Transaction analysis: {stats['total_operations']} operations, "
                f"{msg}"
            )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return specialized transaction statistics"""
        stats = super().get_stats()
        stats["total_operations"] = self.total_operations
        stats["net_flow"] = self.total_net_flow
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.total_events = 0
        self.total_errors = 0

    def filter_data(self, data_batch, criteria=None):
        """Filter events by type"""
        if criteria == "error":
            return [data for data in data_batch if data == "error"]
        elif criteria == "login":
            return [data for data in data_batch if data == "login"]
        elif criteria == "logout":
            return [data for data in data_batch if data == "logout"]
        elif criteria == "critical":
            # Filter critical events (errors or specific event types)
            return [
                data for data in data_batch if data in ["error", "critical", "alert"]
            ]
        return data_batch

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise TypeError("invalid type")
        else:
            self.data_processed += len(data_batch)
            self.total_events += len(data_batch)
            error: int = 0
            for data in data_batch:
                if data == "error":
                    error += 1
            self.total_errors += error

            stats = self.get_stats()
            error_text = "error" if error == 1 else "errors"
            return (
                f"Stream ID: {stats['stream_id']}, Type: System Events\n"
                f"Processing event batch: {data_batch}\n"
                f"Event analysis: {stats['total_events']} events, "
                f"{error} {error_text} detected"
            )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return specialized event statistics"""
        stats = super().get_stats()
        stats["total_events"] = self.total_events
        stats["total_errors"] = self.total_errors
        return stats


class StreamProcessor:
    """Gestionnaire des flux polymorphiques"""

    def __init__(self):
        self.streams = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all_streams(self, data_dict: Dict[str, List]) -> List[str]:
        results = []
        for stream in self.streams:
            if stream.stream_id in data_dict:
                results.append(stream.process_batch(data_dict[stream.stream_id]))
        return results


if __name__ == "__main__":
    # Test SensorStream
    print("=== SENSOR STREAM ===")
    sensor = SensorStream("SENSOR_001")
    sensor_result = sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"])
    # print(f"Stats: {sensor.get_stats()}\n")
    print(f"{sensor_result}")

    # Test TransactionStream
    print("=== TRANSACTION STREAM ===")
    trans = TransactionStream("TRANS_001")
    trans_result = trans.process_batch(["buy:100", "sell:150", "buy:75"])
    print(f"{trans_result}")
    # print(f"Stats: {trans.get_stats()}\n")

    # Test EventStream
    print("=== EVENT STREAM ===")
    events = EventStream("EVENT_001")
    events_result = events.process_batch(["login", "error", "logout"])
    print(f"{events_result}")
    # print(f"Stats: {events.get_stats()}\n")

    # Test StreamProcessor
    print("=== STREAM PROCESSOR ===")
    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(trans)
    manager.add_stream(events)

    data_dict = {
        "sensor_stream": ["temp:22.5", "humidity:65", "pressure:1013"],
        "transaction_stream": ["buy:100", "sell:150", "buy:75"],
        "event_stream": ["login", "error", "logout"],
    }

    results = manager.process_all_streams(data_dict)
    print(f"All results: {results}")
