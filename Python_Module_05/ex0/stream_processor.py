from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class defining the mandatory
    interface for all data processors."""
    def __init__(self, data: Any = None):
        """Initialize processor with input data and an empty storage list."""
        self.data = data
        self.data_list: List[Any] = list()

    @abstractmethod
    def process(self, data: Any) -> str:
        """Abstract method to execute data transformation logic."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Abstract method to verify if the input
        data matches required format."""
        pass

    def format_output(self, result: str) -> str:
        """Standardize the presentation of the processed result."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized in calculating sums
    and averages for numeric lists."""
    def __init__(self, data: Any = None) -> None:
        """Initialize numeric processor with math tracking variables."""
        super().__init__(data)
        self.numbers = list()

    def validate(self, data: Any) -> bool:
        """Check if the provided input is a list
        containing only valid numbers."""
        if not isinstance(data, list):
            return False
        try:
            for number in data:
                float(number)
            return True
        except (ValueError, TypeError):
            return False

    def process(self, data: Any) -> str:
        """Convert input to floats and calculate the total sum and average."""
        numbers = [float(number) for number in data]
        total = sum(numbers)
        avg = total / len(numbers) if numbers else 0
        return ("Processed {} numeric values, sum={}, avg={}".format(
            len(numbers), total, avg))

    def format_output(self, result: str) -> str:
        """Print formatted numeric analysis report with validation status."""

        if self.validate(self.data):
            return (
                f"\nInitializing Numeric Processor...\n"
                f"Processing data: {self.data}\n"
                f"Validation: Numeric data verified\n"
                f"Output: {result}"
            )

        return (
            "\nInitializing Numeric Processor...\n"
            "Validation: Data Error (check if all data is Numeric)"
        )


class TextProcessor(DataProcessor):
    """Processor designed to analyze string characteristics like word count."""
    def __init__(self, data: Any = None) -> None:
        """Initialize text processor using the base data structure."""
        super().__init__(data)

    def validate(self, data: Any) -> bool:
        """Verify that the input data is a string."""
        if isinstance(data, str):
            return True
        return False

    def process(self, data: Any) -> str:
        """Calculate character and word counts from the input text."""
        words = data.split()
        word_count = len(words)
        char_count = len(data)
        return "Processed text: {} characters, {} words".format(
            char_count, word_count)

    def format_output(self, result: str) -> str:
        """Print formatted text analysis report with validation status."""
        if self.validate(self.data):
            return (
                f"\nInitializing Text Processor...\n"
                f'Processing data: "{self.data}"\n'
                f"Validation: Text data verified\n"
                f"Output: {result}"
            )
        return (
            "\nInitializing Text Processor...\n"
            "Validation: Data Error (check if data is Text)"
        )


class LogProcessor(DataProcessor):
    """Processor for categorizing and formatting system log entries."""
    def __init__(self, data: Any = None) -> None:
        """Initialize log processor with supported severity levels."""
        super().__init__(data)
        self.logs = ["ERROR", "INFO", "DEBUG"]

    def validate(self, data: Any) -> bool:
        """Ensure the input is a string containing a recognized log level."""
        if isinstance(data, str):
            for level in self.logs:
                if level in data:
                    self.type_log = level
                    return True
        return False

    def process(self, data: Any) -> str:
        """Parse log messages and apply specific
        alert prefixes based on level."""
        level, msg = data.split(":", 1)
        message = msg.strip()
        type_log = "[ALERT]" if level == "ERROR" else f"[{level}]"
        return f"{type_log} {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        """Print formatted log entry report with validation status."""
        if self.validate(self.data):
            return (
                f"\nInitializing Log Processor...\n"
                f'Processing data: "{self.data}"\n'
                f"Validation: Log Entry verified\n"
                f"Output: {result}"
            )

        return (
            "\nInitializing Log Processor...\n"
            "Validation: Invalid log format"
            )


def stream_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    numeric_processor_testing = NumericProcessor([1, 2, 3, 4, 5])
    numeric_result = numeric_processor_testing.process([1, 2, 3, 4, 5])
    print(numeric_processor_testing.format_output(numeric_result))

    text_processor_testing = TextProcessor("Hello Nexus World")
    text_result = text_processor_testing.process("Hello Nexus World")
    print(text_processor_testing.format_output(text_result))

    log_processor_testing = LogProcessor("ERROR: Connection timeout")
    log_result = log_processor_testing.process("ERROR: Connection timeout")
    print(log_processor_testing.format_output(log_result))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    print(f"Result 1: {numeric_processor_testing.process([8, 10, 6])}")
    print(f"Result 2: {text_processor_testing.process("Abdelfatah laktaoui")}")
    print(f"Result 3: {log_processor_testing.process("INFO: System ready")}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
