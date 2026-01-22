#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class for data processors."""

    @abstractmethod
    def process(self, data: str) -> str:
        """Process the input data and return the result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string"""
        pass


class NumericProcessor(DataProcessor):
    """Processor for numeric data."""

    def process(self, data: Any) -> str:
        """Process numeric data by calculating its square."""
        if self.validate(data):
            return (
                f"Processing data: {data}\n"
                "Validation: Numeric data verified\n"
                f"Output: Processed {len(data)} numeric values,"
                f" sum={sum(data)}, avg={len(data) / sum(data)}"
            )
        else:
            return "Not processing no numeric value"

    def validate(self, data: Any) -> bool:
        """Validate if data is numeric."""
        if not isinstance(data, (list, tuple)):
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def format_output(self, result: str) -> str:
        """Format the output for numeric processing."""
        return result


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def process(self, data: Any) -> str:
        """Process numeric data by calculating its square."""
        if self.validate(data):
            return (
                f"Processing data: {data}\n"
                "Validation: Text data verified\n"
                f"Output: Processed  text: {len(data)} characters,"
                f" {len(data.split())}"
            )
        else:
            return "Not processing no numeric value"

    def validate(self, data: Any) -> bool:
        """Validate if data is numeric."""
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Format the output for numeric processing."""
        return result


if __name__ == "__main__":
    data = [1, 2, 3]
    numeric_proces = NumericProcessor()
    result = numeric_proces.process(data)
    print(numeric_proces.format_output(result))
    text_proces = TextProcessor()
    result = text_proces.process(data)
    print(text_proces.format_output(result))
