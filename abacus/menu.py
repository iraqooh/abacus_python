from calculations import handle_calculation
from history import display_history
from settings import handle_settings_menu

def display_main_menu():
    print("\nMain Menu:\n1. Calculator\t2. History\n3. Settings\t4. Exit")

def display_calculator_menu():
    calculator_menu_items = [
        "Arithmetics", "Algebra", 'Trigonometry', 'Logarithm',
        'Statistics', 'Finance', 'Calculus', 'Conversion',
        'Constants', 'Programming', 'Back'
    ]
    # for index in range(1, len(calculator_menu_items)):
    #     if index % 3 < 3:

    print("\nCalculator Menu:")
    print("1. Arithmetics".ljust(15), "2. Algebra".ljust(15), "3. Trigonometry".ljust(15))
    print("4. Logarithm".ljust(15), "5. Statistics".ljust(15), "6. Finance".ljust(15))
    print("7. Calculus".ljust(15), "8. Conversion".ljust(15), "9. Constants".ljust(15))
    print("10. Programming".ljust(15), "11. Back".ljust(15))

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
