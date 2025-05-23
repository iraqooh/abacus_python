from menu import display_main_menu, handle_main_menu_input

def main():
    print("Welcome to Abacus Command Line Calculator!")
    while True:
        display_main_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice in ['4', 'exit', 'quit']:
            print("Exiting Abacus. Goodbye!")
            break
        handle_main_menu_input(choice)

if __name__ == "__main__":
    main()
