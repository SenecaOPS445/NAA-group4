#!/usr/bin/env python3

import sys
from timemodule import Time  
import time

'''
The function of this script is to get important messages from /var/log/auth.log and put them in a designated file.
This script should be imported together with a timemodule.py file specifically the Time script on OPS445 lab7f.py and must be run in the same directory with the file.
'''

# Function to check if the log file exists and is readable
def check_log_file(file_path: str) -> bool:
    try:
        with open(file_path, "r"):
            pass  # Just trying to open the file to check if it exists and is readable
    except FileNotFoundError:
        print("Error: The file", file_path, "does not exist.")
        return False
    except PermissionError:
        print("Error: Permission denied for", file_path)
        return False
    except Exception as example_error:
        print("An unexpected error occurred while accessing", file_path, ":", str(example_error))
        return False
    return True

# Function to read the log file line by line
def read_log_file(file_path: str):
    try:
        with open(file_path, "r") as f:
            return f.readlines()  # Read all lines in the file
    except Exception as e:
        print("An error occurred while reading", file_path, ":", str(e))
        return []

# Function to extract important messages from a list of lines
def filter_important_messages(lines, keywords):
    important_messages = []
    for line in lines:
        if contains_keywords(line, keywords):
            important_messages.append(line.strip())  # Add the line if it contains any of the keywords
    return important_messages

# Function to check if a line contains any of the specified keywords
def contains_keywords(line, keywords):
    for keyword in keywords:
        if keyword in line:
            return True
    return False

# Function to append important messages to the output file with timestamps
def write_messages_to_file(messages, output_file):
    try:
        with open(output_file, "a") as f:  # Open the file in append mode
            for message in messages:
                timestamp = get_current_time()
                f.write("[ " + timestamp + " ] Important message detected: " + message + "\n")
    except Exception as e:
        print("Error writing to file", output_file, ":", str(e))

# Function to monitor the log file for updates and write results to the output file
def monitor_log(output_file, keywords):
    file_path = '/var/log/auth.log'  # Hardcoded log file path

    if not check_log_file(file_path):
        return

    print("Monitoring", file_path, "for important messages...")
    print("Results will be saved to", output_file)

    # Initialize previous content to detect updates
    previous_lines = set()

    while True:
        # Read the current content of the file
        current_lines = read_log_file(file_path)

        # Identify new lines since the last check
        new_lines = set(current_lines) - previous_lines

        # Update the previous lines
        previous_lines.update(new_lines)

        # Filter and write important messages
        important_messages = filter_important_messages(new_lines, keywords)
        write_messages_to_file(important_messages, output_file)

        # Wait for a defined interval before checking again
        time.sleep(5)

# Function to get the current timestamp using the Time class
def get_current_time():
    current_time = Time(hour=12, minute=0, second=0)  # Example of creating a Time object with default values
    # We can modify the time or use any time-related operation
    return current_time.format_time()  # Returning formatted time as a string

# Direct code block for execution
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: sudo python3 auth_log_monitor.py <output_file_path>")
    else:
        output_file = sys.argv[1]

        # Ensure the output file ends with '.txt'
        if not output_file.endswith('.txt'):
            print("Error: The output file must have a '.txt' extension.")
            sys.exit(1)

        keywords = ["Failed password", "authentication failure", "Invalid user", "error"]

        monitor_log(output_file, keywords)
