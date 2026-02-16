#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional  # noqa: F401


class DataProcessor(ABC):
    """Abstract base class for data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return the result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric data."""

    def process(self, data: Any) -> str:
        total = sum(data)
        avg = total / len(data)
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={total}, avg={avg}"
        )

    def validate(self, data: Any) -> bool:
        """Validate if data is numeric."""
        if not isinstance(data, (list, tuple)):
            raise TypeError("type incorrect")
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("List must contain only numbers")
        return True


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def process(self, data: Any) -> str:
        return (
            f"Processed text: {len(data)} characters, "
            f"{len(data.split())} words"
        )

    def validate(self, data: Any) -> bool:
        """Validate if data is text."""
        if not isinstance(data, str):
            raise TypeError("Text data must be a string")
        return True


class LogProcessor(DataProcessor):
    """Processor for log data."""

    def process(self, data: Any) -> str:
        level, message = data.split(":", 1)
        level = level.strip()
        message = message.strip()

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {message}"
        return f"[{level}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            raise TypeError("Log data must be a string")

        if not any(level in data for level in ["ERROR", "INFO", "WARNING"]):
            raise ValueError("Invalid log level")

        return True

    def format_output(self, result: str) -> str:
        return f"LOG >> {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    processors = [
        (NumericProcessor(), [1, 2, 3, 4, 5]),
        (TextProcessor(), "Hello Nexus World"),
        (LogProcessor(), "ERROR: Connection timeout"),
    ]

    for processor, data in processors:
        try:
            if isinstance(processor, NumericProcessor):
                print("\nInitializing Numeric Processor...")
                print(f'Processing data: {data}')
            elif isinstance(processor, TextProcessor):
                print("\nInitializing Text Processor...")
                print(f'Processing data: "{data}"')
            elif isinstance(processor, LogProcessor):
                print("\nInitializing Log Processor...")
                print(f'Processing data: "{data}"')
            processor.validate(data)
            print(f"Validation: "
                  f"{processor.__class__.__name__[:-9]} "
                  f"data verified")
            print(processor.format_output(
                processor.process(data)
            ))
        except Exception as e:
            print(f"Error: {e}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types "
          "through same interface...")

    poly_data = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello Nexus"),
        (LogProcessor(), "INFO: System ready"),
    ]

    for i, (processor, data) in enumerate(poly_data, 1):
        try:
            processor.validate(data)
            result = processor.process(data)
            print(f"Result {i}: {result}")
        except Exception as e:
            print(f"Error: {e}")

    print("\nFoundation systems online. "
          "Nexus ready for advanced streams.")
