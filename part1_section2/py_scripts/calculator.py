
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

    def create_specialized_calculator(self, a, operation_type):
        """
        Creates a specialized calculator function using closures.

        Args:
            a (float): The first number
            operation_type (str): The type of operation
                ('add', 'subtract', 'multiply', 'divide')

        Returns:
            function: A specialized calculator function that always
            uses the specified operation

        Raises:
            ValueError: If the operation type is not supported
        """
        if (not (isinstance(a, (int, float)))):
            raise ValueError("Both inputs must be numbers")

        # The outer function creates a closure,
        # capturing the operation_type variable
        if (operation_type == "add"):
            def specialized_calculator(b):
                if (not isinstance(b, (int, float))):
                    raise ValueError("Both inputs must be numbers")
                return self.add(a, b)
        elif (operation_type == "subtract"):
            def specialized_calculator(b):
                if (not isinstance(b, (int, float))):
                    raise ValueError("Both inputs must be numbers")
                return self.subtract(a, b)
        elif (operation_type == "multiply"):
            def specialized_calculator(b):
                if (not isinstance(b, (int, float))):
                    raise ValueError("Both inputs must be numbers")
                return self.multiply(a, b)
        elif (operation_type == "divide"):
            def specialized_calculator(b):
                if (not isinstance(b, (int, float))):
                    raise ValueError("Both inputs must be numbers")
                if (b == 0):
                    raise ZeroDivisionError("Cannot divide by zero")
                return self.divide(a, b)
        else:
            raise ValueError("Unsupported operation type")
        return specialized_calculator


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

    print("\nSpecialized Calculator Tests:")
    # Test specialized calculator
    add_5 = calc.create_specialized_calculator(5, "add")
    subtract_3 = calc.create_specialized_calculator(3, "subtract")
    multiply_by_2 = calc.create_specialized_calculator(2, "multiply")
    divide_by_4 = calc.create_specialized_calculator(4, "divide")

    print("Execute calculations:")
    print(f"Add 5 to 10: {add_5(10)}")
    print(f"Subtract 3 from 10: {subtract_3(10)}")
    print(f"Multiply 2 by 5: {multiply_by_2(5)}")
    print(f"Divide 4 by 16: {divide_by_4(16)}")
    try:
        result = divide_by_4(0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
