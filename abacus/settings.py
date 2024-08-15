import json
import os

# Default settings
DEFAULT_SETTINGS = {
    'precision': 2,
    'number_formatting': {
        'thousands_separator': ',',
        'decimal_separator': '.'
    },
    'expression_modes': {
        'fractional': False,
        'n_base': 10
    },
    'language': 'en'
}

SETTINGS_FILE = 'settings.json'

def load_settings():
    """Load settings from a JSON file or use default settings if file is not found."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as file:
            settings = json.load(file)
    else:
        settings = DEFAULT_SETTINGS
    return settings

def save_settings(settings):
    """Save settings to a JSON file."""
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)

def get_setting(settings, key, default=None):
    """Get a specific setting value."""
    keys = key.split('.')
    value = settings
    for k in keys:
        value = value.get(k, default)
    return value

def set_setting(settings, key, value):
    """Set a specific setting value."""
    keys = key.split('.')
    d = settings
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = value

def display_settings(settings):
    """Display current settings."""
    print("\nCurrent Settings:")
    print(f"Precision: {settings['precision']}")
    print(f"Number Formatting: Thousands Separator: {settings['number_formatting']['thousands_separator']}, Decimal Separator: {settings['number_formatting']['decimal_separator']}")
    print(f"Expression Modes: Fractional: {settings['expression_modes']['fractional']}, N-Base: {settings['expression_modes']['n_base']}")
    print(f"Language: {settings['language']}")

def update_precision(settings):
    """Update precision setting."""
    precision = input(f"Enter precision (current: {settings['precision']}): ")
    if precision.isdigit():
        set_setting(settings, 'precision', int(precision))
        save_settings(settings)
        print("Precision updated successfully.")
    else:
        print("Invalid precision value.")

def update_number_formatting(settings):
    """Update number formatting settings."""
    thousands_separator = input(f"Enter thousands separator (current: {settings['number_formatting']['thousands_separator']}): ")
    decimal_separator = input(f"Enter decimal separator (current: {settings['number_formatting']['decimal_separator']}): ")
    if thousands_separator:
        set_setting(settings, 'number_formatting.thousands_separator', thousands_separator)
    if decimal_separator:
        set_setting(settings, 'number_formatting.decimal_separator', decimal_separator)
    save_settings(settings)
    print("Number formatting updated successfully.")

def update_expression_modes(settings):
    """Update expression modes settings."""
    fractional = input(f"Enable fractional mode? (current: {settings['expression_modes']['fractional']}): ")
    if fractional.lower() in ['yes', 'true', '1']:
        set_setting(settings, 'expression_modes.fractional', True)
    else:
        set_setting(settings, 'expression_modes.fractional', False)
    
    n_base = input(f"Enter n-base (current: {settings['expression_modes']['n_base']}): ")
    if n_base.isdigit():
        set_setting(settings, 'expression_modes.n_base', int(n_base))
    
    save_settings(settings)
    print("Expression modes updated successfully.")

def update_language(settings):
    """Update language setting."""
    language = input(f"Enter language code (current: {settings['language']}): ")
    if language:
        set_setting(settings, 'language', language)
        save_settings(settings)
        print("Language updated successfully.")

def handle_settings_menu():
    """Display settings menu and handle user choices."""
    settings = load_settings()
    while True:
        display_settings_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == '1':
            update_precision(settings)
        elif choice == '2':
            update_number_formatting(settings)
        elif choice == '3':
            update_expression_modes(settings)
        elif choice == '4':
            update_language(settings)
        elif choice == '5' or choice == 'back':
            break
        else:
            print("Invalid choice. Please try again.")

def display_settings_menu():
    """Display the settings menu options."""
    print("\nSettings Menu:")
    print("1. Precision")
    print("2. Number Formatting")
    print("3. Expression Modes")
    print("4. Language")
    print("5. Back")
