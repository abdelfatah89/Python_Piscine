from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for all data stream types in the Nexus system."""
    def __init__(self, stream_id: str) -> None:
        """Initialize the stream with a unique ID and an empty data storage."""
        self.stream_id = stream_id
        self.processed_data: List[Any] = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a list of data items - must be implemented by subclasses."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Return the data batch as-is or apply basic filtering logic."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Generate a dictionary containing basic stream
        processing statistics."""
        return {
            "stream_id": self.stream_id,
            "type": "Generic Data Stream",
            "items_processed": len(self.processed_data)
        }


class SensorStream(DataStream):
    """Stream handler for environmental sensor data like temperature."""
    def __init__(self, stream_id: str) -> None:
        """Initialize sensor stream with temperature tracking capabilities."""
        super().__init__(stream_id)
        self.avg_temp = 0
        self.processed_data: List[Any] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        """Parse temperature readings and calculate the batch average."""
        if not data_batch:
            return "No data to process"

        for item in data_batch:
            try:
                if isinstance(item, str):
                    type_sensor, temp_str = item.split(":")

                if type_sensor.lower() == "temp":
                    temp = float(temp_str)
                    self.processed_data.append(temp)
            except Exception:
                continue

        if self.processed_data:
            self.avg_temp = sum(self.processed_data) / len(self.processed_data)
        return f"Sensor analysis: {len(data_batch)} \
readings processed, avg temp: {self.avg_temp:.1f}°C"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return detailed statistics including average temperature values."""
        stats = super().get_stats()
        if self.processed_data:
            self.avg_temp = sum(self.processed_data) / len(self.processed_data)

        stats.update({
            "type": "Environmental Data",
            "average_value": self.avg_temp
        })
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor readings based on high
        or low temperature thresholds."""
        if not criteria or criteria not in ["high_temp", "low_temp"]:
            return data_batch

        filtered: List[Any] = []
        for item in data_batch:
            try:
                if isinstance(item, str):
                    type_sensor, temp_str = item.split(":")
                    if type_sensor == "temp":
                        temp = float(temp_str)
                    else:
                        continue

                if criteria == "high_temp" and temp > 100:
                    filtered.append(item)
                elif criteria == "low_temp" and temp < 100:
                    filtered.append(item)

            except Exception:
                continue
        return filtered


class TransactionStream(DataStream):
    """Stream handler for financial buy and sell operations."""
    def __init__(self, stream_id: str) -> None:
        """Initialize transaction stream with net flow tracking."""
        super().__init__(stream_id)
        self.processed_data: List[float] = []
        self.net_flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Analyze financial transactions to calculate total net flow."""
        if not data_batch:
            return "No data to process"

        for item in data_batch:
            try:
                if isinstance(item, str) and ":" in item:
                    type_trans, unit_str = item.split(":")
                    unit = float(unit_str)
                else:
                    continue

                if type_trans.lower() == "sell":
                    self.processed_data.append(-unit)
                elif type_trans.lower() == "buy":
                    self.processed_data.append(unit)
            except Exception:
                continue
        self.net_flow = sum(self.processed_data)
        return f"Transaction analysis: {len(data_batch)} processed, \
net flow: {self.net_flow:+.2f} units"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return financial metrics including total operations and net flow."""
        stats = super().get_stats()
        self.net_flow = sum(self.processed_data)

        stats.update({
            "type": "Financial Data",
            "net_flow": self.net_flow
        })
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Extract transactions matching specific financial criteria
        like buy or sell."""
        if not criteria or criteria not in ["sell", "buy"]:
            return data_batch

        filtered: List[Any] = []
        for item in data_batch:
            try:
                if isinstance(item, str):
                    type_trans, unit_str = item.split(":")
                    unit = float(unit_str)
                else:
                    continue

                if criteria == "sell" and type_trans == criteria:
                    filtered.append(unit)
                elif criteria == "buy" and type_trans == criteria:
                    filtered.append(unit)

            except Exception:
                continue
        return filtered


class EventStream(DataStream):
    """Stream handler for system events and error logging."""
    def __init__(self, stream_id: str) -> None:
        """Initialize event stream with error and total event counters."""
        super().__init__(stream_id)
        self.errors = 0
        self.events = 0
        self.processed_data: List[str] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        """Log system events and count detected error occurrences."""
        if not data_batch:
            return "No data to process"

        for item in data_batch:
            try:
                if isinstance(item, str):
                    event = item
                else:
                    continue

                if "error" in event.lower():
                    self.errors += 1
                else:
                    self.events += 1
                self.processed_data.append(event)
            except Exception:
                continue
        return f"Event analysis: {len(data_batch)} events, \
{self.errors} errors detected"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return system health metrics including total
        events and error rate."""
        stats = super().get_stats()
        if self.processed_data:
            error_rate = f"\
{(self.errors / len(self.processed_data) * 100):.1f}%"
        else:
            error_rate = "0%"

        stats.update({
            "type": "System Event Stream",
            "error_rate": f"{error_rate}%"
            })

        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Separate standard system events from detected error logs."""
        if not criteria or criteria not in ["event", "error"]:
            return data_batch

        filtered: List[Any] = []
        for item in data_batch:
            try:
                if isinstance(item, str):
                    event = item
                else:
                    continue

                if criteria == "error" and "error" in event.lower():
                    filtered.append(event)
                elif criteria == "event" and "error" not in event.lower():
                    filtered.append(event)

            except Exception:
                continue
        return filtered


class StreamProcessor():
    """Manager class that orchestrates multiple polymorphic data streams."""
    def __init__(self) -> None:
        """Initialize the processor with an empty list of managed streams."""
        self.streams: List[DataStream] = list()

    def add_stream(self, stream: DataStream):
        """Register a new DataStream object into the processor."""
        self.streams.append(stream)

    def stream_all(self, data_batch: Dict[str, List[Any]]) -> List[str]:
        """Execute processing for all registered streams using batch data."""
        result = []
        for stream in self.streams:
            data = data_batch.get(stream.stream_id, [])
            report = stream.process_batch(data)
            result.append(f"[{stream.stream_id}] {report}")
        return result

    def get_all_stats(self):
        """Collect and return statistics from all managed data streams."""
        stats = []
        for stream in self.streams:
            stats.append(stream.get_stats())
        return stats


def data_stream():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    sensor_data = ["temp: 22.5", "humidity:65", "pressure:1013"]
    trans_data = ["buy:100", "sell:150", "buy:75"]
    events_data = ["login", "error", "logout"]

    stream_sensor = SensorStream("SENSOR_001")
    sensor_stats = stream_sensor.get_stats()
    sensor_process = stream_sensor.process_batch(sensor_data)
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {stream_sensor.stream_id}, \
Type: {sensor_stats.get("type")}")
    print(f"Processing sensor batch: {sensor_data}")
    print(sensor_process, '\n')

    stream_trans = TransactionStream("TRANS_001")
    trans_stats = stream_trans.get_stats()
    trans_process = stream_trans.process_batch(trans_data)
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {stream_trans.stream_id}, \
Type: {trans_stats.get("type")}")
    print(f"Processing transaction batch: {trans_data}")
    print(trans_process, '\n')

    stream_event = EventStream("EVENT_001")
    event_stats = stream_event.get_stats()
    event_process = stream_event.process_batch(events_data)
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {stream_event.stream_id}, \
Type: {event_stats.get("type")}")
    print(f"Processing transaction batch: {events_data}")
    print(event_process, '\n')

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    print("- Sensor data:", sensor_process)
    print("- Transaction data:", trans_process)
    print("- Event data:", event_process)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
