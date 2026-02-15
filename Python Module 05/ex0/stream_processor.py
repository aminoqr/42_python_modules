from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if data is None:
            return False
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, int) and not isinstance(i, float):
                    return False
            return True
        return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            if isinstance(data, (int, float)):
                data_len = 1
                data_sum = data
                data_avg = data
            else:
                data_len = len(data)
                data_sum = sum(data)
                data_avg = data_sum/data_len

            result_str = (f"Processed {data_len} numeric "
                          f"values, sum={data_sum}, avg={data_avg:.1f}")

        else:
            result_str = ("ERROR Output:Invalid data!")

        return self.format_output(result_str)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            char_count = len(data)
            word_count = len(data.split(" "))
            res = (f"Processed text: "
                   f"{char_count} characters, {word_count} words")
        else:
            res = ("ERROR Output:Invalid data!")

        return self.format_output(res)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if data.startswith("ERROR: ") or data.startswith("INFO: "):
            return True
        else:
            return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            splitted = data.split(":", 1)
            lvl = splitted[0]
            msg = splitted[1].strip()
            if "ERROR" in lvl:
                res = (f"[ALERT] {lvl} level detected: {msg}")
            else:
                res = (f"[INFO] {lvl} level detected: {msg}")
        else:
            res = ("ERROR Output:Invalid log entry!")

        return self.format_output(res)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    processors = [[1, 2, 3, 4, 5], "Hello Nexus World",
                  "ERROR: Connection timeout"]
    instances = [NumericProcessor(), TextProcessor(), LogProcessor()]

    txts = ["Initializing Numeric Processor...",
            "Initializing Text Processor...",
            "Initializing Log Processor..."]

    veris = ["Validation: Numeric data verified",
             "Validation: Text data verified",
             "Validation: Log entry verified"]

    for processor, data, text, veri in zip(instances, processors, txts, veris):
        res = processor.process(data)
        print(text)
        print(veri)
        print(f"Processing data: {data}")
        print("Output: ", end="")
        print(res)
        print()

    print("Processing multiple data types through same interface...")
    new_processors = [[1, 2, 3],
                      "Hello World!",
                      "INFO: System ready"]
    i = 1
    for processor, data in zip(instances, new_processors):
        res = processor.process(data)
        print(f"Result {i}: {res}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")
