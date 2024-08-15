import os

def display_history():
    if not os.path.exists('data/history.txt'):
        print("No history found.")
        return

    with open('data/history.txt', 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No history found.")
        else:
            for line in lines:
                print(line.strip())
