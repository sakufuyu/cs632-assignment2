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
    
    return 0;
}