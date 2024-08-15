# utils.py
import math

def convert_units(value, from_unit, to_unit):
    """Converts value from one unit to another.
    
    Supported conversions:
    - Length: meters to feet, feet to meters
    - Weight: kilograms to pounds, pounds to kilograms
    
    Parameters:
    value (float): The value to convert.
    from_unit (str): The unit to convert from.
    to_unit (str): The unit to convert to.
    
    Returns:
    float: The converted value.
    """
    conversion_factors = {
        'meters': 1,
        'feet': 3.28084,
        'kg': 1,
        'lbs': 2.20462
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit for conversion")
    
    # Convert value to a common unit (meters for length, kg for weight)
    base_value = value / conversion_factors[from_unit]
    
    # Convert base value to the target unit
    return base_value * conversion_factors[to_unit]

def format_number(value, precision=2, thousands_separator=','):
    """Formats a number with specified precision and thousands separator.
    
    Parameters:
    value (float): The number to format.
    precision (int): The number of decimal places.
    thousands_separator (str): The character used for thousands separation.
    
    Returns:
    str: The formatted number.
    """
    formatted_value = f"{value:,.{precision}f}"
    if thousands_separator != ',':
        formatted_value = formatted_value.replace(',', thousands_separator)
    return formatted_value

def parse_number(number_string):
    """Parses a number from a string, removing any formatting characters.
    
    Parameters:
    number_string (str): The string representing the number.
    
    Returns:
    float: The parsed number.
    """
    return float(number_string.replace(',', '').replace(' ', ''))

def validate_positive_number(value):
    """Validates that a number is positive.
    
    Parameters:
    value (float): The number to validate.
    
    Returns:
    bool: True if the number is positive, otherwise False.
    """
    return value > 0

def get_user_input(prompt, validation_func=None, error_message="Invalid input. Please try again."):
    """Prompts the user for input and validates it using a validation function.
    
    Parameters:
    prompt (str): The prompt to display to the user.
    validation_func (function): A function to validate the input.
    error_message (str): The message to display if validation fails.
    
    Returns:
    str: The valid input from the user.
    """
    while True:
        user_input = input(prompt).strip()
        if validation_func is None or validation_func(user_input):
            return user_input
        else:
            print(error_message)
