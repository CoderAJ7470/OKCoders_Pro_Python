# Build a logfile parser that extracts timestamps, email addresses and error messages from server logs

import string
import os
import re

FILE_PATH: string

# Looking for the sample_logs.txt file with the full filepath
def get_logs_file_path() -> string:
    FILE_PATH = os.path.join(os.path.dirname(__file__), 'sample_logs.txt')

    return FILE_PATH

def show_timestamps():
    timestamps_list = []
    timestamp_regex_compiled = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    try:
        with open(get_logs_file_path(), 'r') as log_file:
          logs = log_file.readlines()

        for log in logs:
            timestamp_match = timestamp_regex_compiled.search(log)
            if timestamp_match:
                timestamps_list.append(timestamp_match.group())

        print("Showing all timestamps (in the order they are present in the file, from top to bottom):\n")

        for timestamp in timestamps_list:
            print(f'{timestamp}\n')
    except FileNotFoundError:
        print('No file was found from which the todo list could be read.')

def show_email_addresses():
    emails_list = []
    emails_regex_compiled = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    try:
        with open(get_logs_file_path(), 'r') as log_file:
          logs = log_file.readlines()

        for log in logs:
            email_match = emails_regex_compiled.search(log)

            if email_match:
                emails_list.append(email_match.group())

        # Remove any emails with more than one instance in the log file
        unique_emails = list(dict.fromkeys(emails_list))

        print("Showing all emails (in the order they are present in the file, from top to bottom):\n")

        for email in unique_emails:
            print(f'{email}\n')
    except FileNotFoundError:
        print('No file was found from which the todo list could be read.')

# Shows the user all error messages in the log file
def show_error_messages():
    errors_list = []
    errors_regex_compiled = re.compile(r'ERROR.+')

    try:
        with open(get_logs_file_path(), 'r') as log_file:
          logs = log_file.readlines()

        for log in logs:
            error_match = errors_regex_compiled.search(log)
            
            if error_match:
                errors_list.append(error_match.group())

        # Remove any emails with more than one instance in the log file
        unique_errors = list(dict.fromkeys(errors_list))

        for error in unique_errors:
            print(f'{error}\n')
    except FileNotFoundError:
        print('No file was found from which the todo list could be read.')
        
# Handles all user input
def handle_user_input() -> None:
    while True:
        user_choice: string

        print('Please choose from the options below:\n')

        print('Enter "1" to show all timestamps')
        print('Enter "2" to show all email addresses')
        print('Enter "3" to show error messages by user')
        print('Or "q" to quit')

        user_choice = input('\n> ')

        if user_choice == '1':
            show_timestamps()
        elif user_choice == '2':
            show_email_addresses()
        elif user_choice == '3':
            show_error_messages()
        elif user_choice == 'q':
            break
        else:
            print('\nSorry, invalid input. Please check your entry and try again.\n')

def run_program() -> None:
    handle_user_input()

if __name__ == "__main__":
    run_program()

