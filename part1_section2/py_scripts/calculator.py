
class Calculator:
    """
    A simple calculator class that provides basic arithmetic operations.

    This class implements addition, subtraction, multiplication, and division
    operations with error handling for common mathematical errors.
    """

    def __init__(self):
        """Initialize the Calculator object without initial state."""
        pass

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.

        Raises:
            ValueError: If either a or b is not a number.
        """
        if (not (isinstance(a, (int, float)) and isinstance(b, (int, float)))):
            raise ValueError("Both inputs must be numbers")
        return a + b

    def subtract(self, a, b):
        """
        Subtract two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The difference between a and b.

        Raises:
            ValueError: If either a or b is not a number.
        """
        if (not (isinstance(a, (int, float)) and isinstance(b, (int, float)))):
            raise ValueError("Both inputs must be numbers")
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.

        Raises:
            ValueError: If either a or b is not a number.
        """
        if (not (isinstance(a, (int, float)) and isinstance(b, (int, float)))):
            raise ValueError("Both inputs must be numbers")
        return a * b

    def divide(self, a, b):
        """
        Divide two numbers.

        Args:
            a (float): The dividend.
            b (float): The divisor.

        Returns:
            float: The quotient of a divided by b.

        Raises:
            ValueError: If either a or b is not a number.
            ZeroDivisionError: If b is zero.
        """
        if (not (isinstance(a, (int, float)) and isinstance(b, (int, float)))):
            raise ValueError("Both inputs must be numbers")
        if (b == 0):
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    calc = Calculator()

    # Test basic operations
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 7 * 6 = {calc.multiply(7, 6)}")
    print(f"Division: 15 / 3 = {calc.divide(15, 3)}")

    # Test error handling
    try:
        result = calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
