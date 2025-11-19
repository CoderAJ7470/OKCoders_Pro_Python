# Create a to-do list with the options to add/remove items, and mark items as complete
# Also allows the user to update/edit any todo item, its priority and/or status

import os
import json
import sys
import string

todo_items = []

FILE_PATH: string

def get_file_path_for_todos_file() -> string:
    FILE_PATH = os.path.join(os.path.dirname(__file__), 'Todos.json')

    return FILE_PATH


def add_item_to_list() -> None:
    print('\nBelow, please enter the item you want to add to your list, followed by the item\'s priority - "l" for Low, "m" for Medium, "h" for High (default is Low). Enter "q" at any time to exit the program. Note that if you quit, your data will not be saved.\n')

    while True:
        item = []
        todo_item = input('Todo Item (or "q" to quit): ').lower()

        if todo_item == "q":
            save_todos_to_file()
            break
            
        priority = input('Item priority (or "q" to quit): ').lower()

        if priority == "q":
            save_todos_to_file()
            break

        descriptive_priority = convert_letter_to_priority(priority)
        
        # Create the new list item
        item.append(todo_item.capitalize())
        item.append(descriptive_priority)
        item.append('To Do')

        # Add the list item to the todo_items list
        todo_items.append(item)

        show_todos()

        print('\nEnter the next item:')


def convert_letter_to_priority(letter: string) -> string:
    if letter == 'l':
        return 'Low'
    elif letter == 'm':
        return 'Med'
    elif letter == 'h':
        return 'High'
    else:
        return 'Unknown'
    
# Shows the to-do items, their priority and status in a tabular format
def show_todos() -> None:
    max_length_item: string

    print('\nShowing current to-do list:')

    # Get the length of the largest item description (string), out of all the nested lists in todo_items
    max_length_item = max(len(nested_list[0]) for nested_list in todo_items) + 2

    print(f"{'Item #':<8} {'Item':<{max_length_item}} {'Priority':<10} {'Status':<12}")
    print("-" * 55)

    for index, row in enumerate(todo_items):
        print(f"{index + 1:<8} {row[0]:<{max_length_item}} {row[1]:<10} {row[2]:<12}")
 

def save_todos_to_file() -> None:
    with open(get_file_path_for_todos_file(), 'w') as todos_file:
        json.dump(todo_items, todos_file)


def read_todos_from_file() -> None:
    global todo_items

    try:
        with open(get_file_path_for_todos_file(), 'r') as todos_file:
            todo_items = json.load(todos_file)
    except FileNotFoundError:
        print('No file was found from which the todo list could be read.')
    except json.JSONDecodeError:
        todo_items = []
        print("File is empty or contains invalid JSON. Starting with an empty to-do list.")


# Allows the user to update a to-do item's desccription, priority or status
def update_items() -> None:
    print('\nShowing current to-do list:')
    show_todos()

    # Get valid item number
    while True:
        todo_item_number = input('\nEnter the item number for the item you wish to edit/update (or "q" to quit): ')
        if todo_item_number == "q":
            return
        
        # Check that the user entered a valid number; otherwise, have them try again
        if todo_item_number.isdigit():
            index = int(todo_item_number) - 1
            if 0 <= index < len(todo_items):
                break

        print("Invalid item number. Try again.")

    # Get the nested list specified by the above index
    item = todo_items[index]

    # If all goes well, ask the user what they wish to update
    print("\nWhat would you like to update?")
    print("1. Description")
    print("2. Priority")
    print("3. Status")
    print("Q. Quit")

    while True:
        choice = input("Enter your choice: ").strip().lower()

        if choice == "q":
            return

        # Update description
        if choice == "1":
            new_desc = input("Enter your updated item description: ").strip()
            item[0] = new_desc
            break

        # Update priority
        elif choice == "2":
            new_priority = input("Enter new priority (Low / Med / High): ").strip()
            item[1] = new_priority
            break

        # Update status
        elif choice == "3":
            new_status = input("Enter new status (To Do / In-Progress / Completed): ").strip()
            item[2] = new_status
            break

        else:
            print("Invalid choice. Try again.")

    print('\nItem updated successfully!')


# Initial user action when the program runs
def handle_user_input() -> None:
    while True:
        if len(todo_items) == 0:
            print('Your to-do list is empty.\n')

        if len(todo_items) > 0:
            show_todos()
        
        user_choice = input('\nPlease enter "1" to add new items, or "2" to update existing items. Enter "q" at any time to exit: ')

        if user_choice == "q":
            save_todos_to_file()
            sys.exit(0)
        elif user_choice == "1":
            add_item_to_list()
        elif user_choice == "2":
            update_items()
        else:
            print('Sorry, you entered an invalid choice. Please check your input and try again.')


def run_program() -> None:
    handle_user_input()

if __name__ == "__main__":
    read_todos_from_file()
    run_program()

        