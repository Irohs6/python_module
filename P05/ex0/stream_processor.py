#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


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
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"

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
        """Validate if data is numeric."""
        if not isinstance(data, str):
            raise TypeError("Text data must be a string")
        return True


class LogProcessor(DataProcessor):
    """Processor for text data."""

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
    processors = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello Nexus"),
        (LogProcessor(), "INFO: System ready"),
        ]

    for processor, data in processors:
        try:
            processor.validate(data)
            print(processor.format_output(processor.process(data)))
        except Exception as e:
            print(f"Error: {e}")
