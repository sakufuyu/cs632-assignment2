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

    /**
     * Creates a specialized calculator function using closures.
     * 
     * @param {number} a - The first number to be used in operations.
     * @param {string} operationType - The type of operation ('add', 'subtract', 'multiply', 'divide').
     * @returns {function} A specialized calculator function that always uses the specified operation.
     * @throws {Error} If the operation type is not supported or if 'a' is not a number.
     */
    createSpecializedCalculator(a, operationType) {
        if (typeof a !== 'number') {
            throw new Error('First input must be a number');
        }

        switch (operationType) {
            case 'add':
                return (b) => {
                    if (typeof b !== 'number') {
                        throw new Error('Second input must be a number');
                    }
                    return this.add(a, b);
                }
            case 'subtract':
                return (b) => {
                    if (typeof b !== 'number') {
                        throw new Error('Second input must be a number');
                    }
                    return this.subtract(a, b);
               }
            case 'multiply':
                return (b) => {
                    if (typeof b !== 'number') {
                        throw new Error('Second input must be a number');
                    }
                    return this.multiply(a, b);
            }
            case 'divide':
                return (b) => {
                    if (typeof b !== 'number') {
                        throw new Error('Second input must be a number');
                    }
                    return this.divide(a, b);
            }
            default:
                throw new Error('Unsupported operation type');
        }
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

    console.log("\nSpecialized Calculator Tests:");
    
    // Test specialized calculator
    const add5 = calc.createSpecializedCalculator(5, "add");
    const subtract3 = calc.createSpecializedCalculator(3, "subtract");
    const multiplyBy2 = calc.createSpecializedCalculator(2, "multiply");
    const divideBy4 = calc.createSpecializedCalculator(4, "divide");
    
    console.log("Execute calculations:");
    console.log(`Add 5 to 10: ${add5(10)}`);
    console.log(`Subtract 3 from 10: ${subtract3(10)}`);
    console.log(`Multiply 2 by 5: ${multiplyBy2(5)}`);
    console.log(`Divide 4 by 16: ${divideBy4(16)}`);
    
    try {
        const result = divideBy4(0);
    } catch (e) {
        console.log(`Error caught: ${e.message}`);
    }
}

main()