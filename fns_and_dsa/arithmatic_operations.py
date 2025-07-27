# Arithmatic operations function


def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the operation argument.

    Parameters:
    - num1 (float): The first number
    - num2 (float): The second number
    - operation (str): One of 'add', 'subtract', 'multiply', or 'divide'

    Returns:
    - The result of the arithmetic operation, or a string error message
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"