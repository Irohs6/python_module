#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List


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
        """Format the output for numeric processing."""
        return result


class NumericProcessor(DataProcessor):
    """Processor for numeric data."""

    def process(self, data: Any) -> str:
        """Process numeric data by calculating its square."""
        return (
            f"Processing data: {data}\n"
            "Validation: Numeric data verified\n"
            f"Output: Processed {len(data)} numeric values,"
            f" sum={sum(data)}, avg={sum(data) / len(data)}"
        )

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
        return (
            f"Processing data: {data}\n"
            "Validation: Text data verified\n"
            f"Output: Processed  text: {len(data)} characters,"
            f" {len(data.split())}"
        )

    def validate(self, data: Any) -> bool:
        """Validate if data is numeric."""
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Format the output for numeric processing."""
        return result


if __name__ == "__main__":
    data = [1, 2, 3]
    numeric_proces = NumericProcessor()
    text_proces = TextProcessor()

    try:
        for process in (numeric_proces, text_proces):
            if process.validate(data):
                result = process.process(data)
                print(process.format_output(result))
            else:
                raise TypeError("Type incorrect")
    except TypeError as e:
        print(str(e))
