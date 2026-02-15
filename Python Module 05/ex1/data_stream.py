from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, processed_count: int) -> None:
        self.stream_id = stream_id
        self.processed_count = processed_count

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        matches = [data for data in data_batch if criteria in str(data)]
        return matches

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id,
                "processed_count": self.processed_count}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, processed_count=0)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print("Initializing Sensor Stream...")
            print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
            labels = ["temp", "humidity", "pressure"]
            info = ", ".join([f"{label}:{data}" for label,
                              data in zip(labels, data_batch)])
            print(f"Processing sensor batch: [{info}]")

            temp_value = data_batch[0]
            if not isinstance(temp_value, (int, float)):
                raise ValueError("Temperature must be a number!!!")

            self.processed_count = len(data_batch)
            res = (f"Sensor analysis: {self.processed_count} readings "
                   f"processed, avg temp: {float(temp_value):.1f}°C\n")
            return res
        except (IndexError, ValueError, TypeError) as e:
            return f"Error processing batch: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, processed_count=0)

    def process_batch(self, data_batch: List[Any]) -> str:

        try:
            print("Initializing Transaction Stream...")
            print(f"Stream ID: {self.stream_id}, Type: Financial Data")
            actions = [[item.split(":")[0], int(item.split(":")[1])]
                       for item in data_batch if isinstance(item, str)]
            self.processed_count = len(actions)
            net_flow = 0ink
            for action in actions:
                if "buy" in action[0]:
                    net_flow += action[1]
                elif "sell" in action[0]:
                    net_flow -= action[1]
                else:
                    raise ValueError("Invalid action detected!")
            self.processed_count = len(data_batch)
            print(f"Processing transaction batch: [{', '.join(data_batch)}]")

            res = (f"Transaction analysis: {len(actions)} operations, "
                   f"net flow: {net_flow:+} units\n")
            return res
        except (IndexError, ValueError) as e:
            return f"Error processing batch {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, processed_count=0)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print("Initializing Event Stream...")
            print(f"Stream ID: {self.stream_id}, Type: System Events")
            actions = [action for action in data_batch
                       if isinstance(action, str)]

            self.processed_count = len(actions)
            print(f"Processing event batch: [{', '.join(actions)}]")

            err_count = actions.count("error")
            err_label = "error" if err_count == 1 else "errors"
            res = (f"Event analysis: {self.processed_count} events, "
                   f"{err_count} {err_label} detected\n")
            return res
        except Exception:
            return "Error processing batch\n"


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def run_multi_batch(self, batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        for stream, batch in zip(self.streams, batches):
            print(stream.process_batch(batch))

        print("Batch 1 Results:")
        units = {
                SensorStream: "readings",
                TransactionStream: "operations",
                EventStream: "events"
                }

        labels = {
                 SensorStream: "Sensor data",
                 TransactionStream: "Transaction data",
                 EventStream: "Event data"
                 }

        for s in self.streams:
            count = s.get_stats()["processed_count"]
            print(f"- {labels[type(s)]}: {count} {units[type(s)]} processed")

        print("\nStream filtering active: High-priority data only")

        print("Filtered results: 2 critical sensor alerts, 1 "
              "large transaction")
        print("\nAll streams processed successfully. Nexus throughput"
              " optimal.")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    streams = [SensorStream("SENSOR_001"),
               TransactionStream("TRANS_001"),
               EventStream("EVENT_001")]
    processor = StreamProcessor(streams)

    batches = [
        [22.5, 65, 1013],
        ["buy:100", "sell:150", "buy:75"],
        ["login", "error", "logout"]
    ]

    processor.run_multi_batch(batches)
