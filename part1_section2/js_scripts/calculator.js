/*
A simple calculator class that provides basic arithmetic operations.
This class implements addition, subtraction, multiplication, and division.
operations with error handling for common mathematical errors.
*/

class Calculator {
    /**
     * Adds two numbers.
     * @param {number} a - The first number.
     * @param {number} b - The second number.
     * @returns {number} The sum of the two numbers.
     * @throws {Error} If either input is not a number.
     */
    add(a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Inputs must be numbers');
        }
        return a + b;
    }

    /**
     * Subtracts two numbers.
     * @param {number} a - The first number.
     * @param {number} b - The second number.
     * @returns {number} The difference between the two numbers.
     * @throws {Error} If either input is not a number.
     */
    subtract(a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Inputs must be numbers');
        }
        return a - b;
    }

    /**
     * Multiplies two numbers.
     * @param {number} a - The first number.
     * @param {number} b - The second number.
     * @returns {number} The product of the two numbers.
     * @throws {Error} If either input is not a number.
     */
    multiply(a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Inputs must be numbers');
        }
        return a * b;
    }

    /**
     * Divides two numbers.
     * @param {number} a - The dividend.
     * @param {number} b - The divisor.
     * @returns {number} The quotient of the two numbers.
     * @throws {Error} If either input is not a number.
     * @throws {Error} If the divisor is zero.
     */
    divide(a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Inputs must be numbers');
        }
        if (b === 0) {
            throw new Error('Cannot divide by zero');
        }
        return a / b;
    }
}

// Example usage
function main() {
    const calc = new Calculator();

    // Test basic operations
    console.log(`Addition: 5 + 3 = ${calc.add(5, 3)}`);
    console.log(`Subtraction: 10 - 4 = ${calc.subtract(10, 4)}`);
    console.log(`Multiplication: 7 * 6 = ${calc.multiply(7, 6)}`);
    console.log(`Division: 15 / 3 = ${calc.divide(15, 3)}`);
    
    // Test error handling
    try {
        const result = calc.divide(10, 0);
    } catch (e) {
        console.log(`Error caught: ${e.message}`);
    }
}

main()