"""Calculator module providing basic arithmetic operations."""


class Calculator:
    """A simple calculator class."""

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b. Raises ValueError on division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
