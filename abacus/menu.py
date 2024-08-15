from abacus.calculations import handle_calculation
from abacus.history import display_history
from abacus.settings import handle_settings_menu

def display_main_menu():
    print("\nMain Menu:")
    print("1. Calculator")
    print("2. History")
    print("3. Settings")
    print("4. Exit")

def display_calculator_menu():
    print("\nCalculator Menu:")
    print("1. Arithmetics")
    print("2. Algebra")
    print("3. Trigonometry")
    print("4. Logarithm")
    print("5. Statistics")
    print("6. Finance")
    print("7. Calculus")
    print("8. Conversion")
    print("9. Constants")
    print("10. Programming")
    print("11. Back")

def handle_main_menu_input(choice):
    if choice == '1':
        handle_calculator_menu()
    elif choice == '2':
        display_history()
    elif choice == '3':
        handle_settings_menu()
    else:
        print("Invalid option. Please try again.")

def handle_calculator_menu():
    while True:
        display_calculator_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice in ['11', 'back']:
            break
        else:
            handle_calculation(choice)
