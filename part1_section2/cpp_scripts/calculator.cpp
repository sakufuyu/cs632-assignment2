#include <iostream>
#include <stdexcept>
#include <string>

/**
A simple calculator class that provides basic arithmetic operations.
This class implements addition, subtraction, multiplication, and division
operations with error handling for common mathematical errors.
*/
class Calculator {
public:
    /*Initialize the Calculator object without initial state.*/
    Calculator() {}

    /**
    Add to numbers together
    @param a First number
    @param b Second number
    @return Sum of a and b
    */
    double add(double a, double b) {
        return a + b;
    }

    /**
    Subtract the second number from the first number.
    @param a First number
    @param b Second number
    @return The difference of a and b
    */
    double subtract(double a, double b) {
        return a - b;
    }

    /**
    Multiply two numbers together.
    @param a First number
    @param b Second number
    @return The product of a and b
    */
    double multiply(double a, double b) {
        return a * b;
    }

    /**
    Divide the first number by the second number.
    @param a First number
    @param b Second number
    @return The quotient of a divided by b
    @throws ZeroDivisionError if b is zero
    */
    double divide(double a, double b) {
        if (b == 0) {
            throw std::invalid_argument("Cannot divide by zero");
        }
        return a / b;
    }

    /**
    Creates a specialized calculator function using closures.
    @param a The first number to be used in operations
    @param operationType The type of operation ('add', 'subtract', 'multiply', 'divide')
    @return A specialized calculator function that always uses the specified operation
    @throws invalid_argument If the operation type is not supported
    */
    std::function<double(double)> createSpecializedCalculator(double a, const std::string& operationType) {
        // Creating a closure by capturing 'this' pointer and 'a' value
        if (operationType == "add") {
            // Return a lambda that capture 'this' and 'a'
            return [this, a](double b) -> double { return this->add(a, b); };
        } else if (operationType == "subtract") {
            return [this, a](double b) -> double { return this->subtract(a, b); };
        } else if (operationType == "multiply") {
            return [this, a](double b) -> double { return this->multiply(a, b); };
        } else if (operationType == "divide") {
            return [this, a](double b) -> double {
                if (b == 0) {
                    throw std::invalid_argument("Cannot divide by zero");
                }
                return this->divide(a, b);
            };
        } else {
            throw std::invalid_argument("Unsupported operation type");
        }
    }
};

int main() {
    Calculator calc;
    
    // Test basic operations
    std::cout << "Addition: 5 + 3 = " << calc.add(5, 3) << std::endl;
    std::cout << "Subtraction: 10 - 4 = " << calc.subtract(10, 4) << std::endl;
    std::cout << "Multiplication: 7 * 6 = " << calc.multiply(7, 6) << std::endl;
    std::cout << "Division: 15 / 3 = " << calc.divide(15, 3) << std::endl;
    
    // Test error handling
    try {
        double result = calc.divide(10, 0);
    } catch (const std::exception& e) {
        std::cout << "Error caught: " << e.what() << std::endl;
    }

    std::cout << "\nSpecialized Calculator Tests:" << std::endl;
    
    // Test specialized calculator
    auto add5 = calc.createSpecializedCalculator(5, "add");
    auto subtract3 = calc.createSpecializedCalculator(3, "subtract");
    auto multiplyBy2 = calc.createSpecializedCalculator(2, "multiply");
    auto divideBy4 = calc.createSpecializedCalculator(4, "divide");
    
    std::cout << "Execute calculations:" << std::endl;
    std::cout << "Add 5 to 10: " << add5(10) << std::endl;
    std::cout << "Subtract 3 from 10: " << subtract3(10) << std::endl;
    std::cout << "Multiply 2 by 5: " << multiplyBy2(5) << std::endl;
    std::cout << "Divide 4 by 16: " << divideBy4(16) << std::endl;
    
    try {
        double result = divideBy4(0);
    } catch (const std::exception& e) {
        std::cout << "Error caught: " << e.what() << std::endl;
    }
    
    return 0;
}