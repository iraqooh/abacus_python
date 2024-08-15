# calculations.py
import math
from abacus.utils import convert_units

def handle_calculation(choice):
    if choice == '1':
        arithmetic_operations()
    elif choice == '2':
        algebra_operations()
    elif choice == '3':
        trigonometry_operations()
    elif choice == '4':
        logarithm_operations()
    elif choice == '5':
        statistics_operations()
    elif choice == '6':
        finance_operations()
    elif choice == '7':
        calculus_operations()
    elif choice == '8':
        conversion_operations()
    elif choice == '9':
        constants_operations()
    elif choice == '10':
        programming_operations()
    else:
        print("Invalid option. Please try again.")

def arithmetic_operations():
    print("\nArithmetic Operations:")
    operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()
    if operation in ['add', 'subtract', 'multiply', 'divide']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        print(f"Result: {result}")

def algebra_operations():
    print("\nAlgebra Operations:")
    operation = input("Choose operation (solve_quadratic): ").strip().lower()
    if operation == 'solve_quadratic':
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Roots: {root1} and {root2}")
        elif discriminant == 0:
            root = -b / (2 * a)
            print(f"Root: {root}")
        else:
            print("The equation has no real roots.")

def trigonometry_operations():
    print("\nTrigonometry Operations:")
    operation = input("Choose operation (sin, cos, tan): ").strip().lower()
    angle = float(input("Enter the angle in degrees: "))
    angle_rad = math.radians(angle)
    if operation == 'sin':
        result = math.sin(angle_rad)
    elif operation == 'cos':
        result = math.cos(angle_rad)
    elif operation == 'tan':
        result = math.tan(angle_rad)
    else:
        print("Invalid operation. Please try again.")
        return
    print(f"Result: {result}")

def logarithm_operations():
    print("\nLogarithm Operations:")
    base = float(input("Enter the base of the logarithm: "))
    value = float(input("Enter the value to compute the logarithm: "))
    if base <= 0 or base == 1 or value <= 0:
        print("Invalid base or value for logarithm.")
        return
    result = math.log(value, base)
    print(f"Result: {result}")

def statistics_operations():
    print("\nStatistics Operations:")
    operation = input("Choose operation (mean, median): ").strip().lower()
    if operation == 'mean':
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        result = sum(numbers) / len(numbers)
        print(f"Mean: {result}")
    elif operation == 'median':
        numbers = sorted(map(float, input("Enter numbers separated by space: ").split()))
        n = len(numbers)
        if n % 2 == 0:
            result = (numbers[n//2 - 1] + numbers[n//2]) / 2
        else:
            result = numbers[n//2]
        print(f"Median: {result}")
    else:
        print("Invalid operation. Please try again.")

def finance_operations():
    print("\nFinance Operations:")
    operation = input("Choose operation (compound_interest): ").strip().lower()
    if operation == 'compound_interest':
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
        times = int(input("Enter the number of times interest is compounded per year: "))
        years = int(input("Enter the number of years: "))
        amount = principal * (1 + rate / times) ** (times * years)
        print(f"Future Value: {amount}")
    else:
        print("Invalid operation. Please try again.")

def calculus_operations():
    print("\nCalculus Operations:")
    operation = input("Choose operation (derivative): ").strip().lower()
    if operation == 'derivative':
        # Simplified derivative of f(x) = x^2
        x = float(input("Enter the value of x: "))
        result = 2 * x
        print(f"Derivative result: {result}")
    else:
        print("Invalid operation. Please try again.")

def conversion_operations():
    print("\nConversion Operations:")
    operation = input("Choose operation (length, weight): ").strip().lower()
    if operation == 'length':
        value = float(input("Enter the value to convert: "))
        unit = input("Enter the unit (meters to feet, feet to meters): ").strip().lower()
        if unit == 'meters to feet':
            result = value * 3.28084
        elif unit == 'feet to meters':
            result = value / 3.28084
        else:
            print("Invalid unit. Please try again.")
            return
        print(f"Converted value: {result}")
    elif operation == 'weight':
        value = float(input("Enter the value to convert: "))
        unit = input("Enter the unit (kg to lbs, lbs to kg): ").strip().lower()
        if unit == 'kg to lbs':
            result = value * 2.20462
        elif unit == 'lbs to kg':
            result = value / 2.20462
        else:
            print("Invalid unit. Please try again.")
            return
        print(f"Converted value: {result}")
    else:
        print("Invalid operation. Please try again.")

def constants_operations():
    print("\nConstants Operations:")
    operation = input("Choose operation (pi, e): ").strip().lower()
    if operation == 'pi':
        print(f"Pi: {math.pi}")
    elif operation == 'e':
        print(f"E: {math.e}")
    else:
        print("Invalid operation. Please try again.")

def programming_operations():
    print("\nProgramming Operations:")
    print("This section is reserved for programming-related calculations.")
    # Implement specific programming-related operations if needed.
