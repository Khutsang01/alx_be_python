# Robust Division Calculator with Command Line Arguments


def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling ZeroDivisionError and ValueError.

    Args:
        numerator (str): The numerator as a string.
        denominator (str): The denominator as a string.

    Returns:
        str: A string message with the result of the division or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"An unexpected error occurred: {e}"