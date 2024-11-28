#!/usr/bin/python3
# Authors: Ronald Jong, Sambhav Sachdeva, Parisha Puri
# Seneca ID: 033295148, 166945220, 109847228
# This script monitors the /var/log/auth.log file for suspicious activity and sends alerts.

import os
import sys
import time

# Function to send an email alert
def send_email_alert(subject, message):
    """
    Sends an email alert with the given subject and message.
    """
    # Define the sender and receiver email
    email = "ppuri9@myseneca.ca"
    receiving_email = "parishapuri@gmail.com rjong1@myseneca.ca"
    # Makes the command to send an email with the subject and message
    command = f'echo "{message}" | mail -s "{subject}" {receiving_email}'
    # Prints the debug message
    print(f"Sending email alert: {subject} - {message.strip()}")
    # Runs the command using the os.system method
    os.system(command)

# Function to monitor log file and changes
def monitor_log(log_file_path):
    # Get the start time (for time limit feature)
    start_time = time.time()
    
    try:
        with open(log_file_path, 'r') as file:
            # Move to the end of the file to look for new entries
            file.seek(0, os.SEEK_END)
            while True:
                # Check if 60 seconds have passed, and if so, stop monitoring
                if time.time() - start_time > 60:
                    print("Monitoring session ended.")
                    break

                # Read the next line of the file
                line = file.readline()

                # If no new line is found, pause the script
                if not line:
                    time.sleep(1)
                    continue

                # Check the new log for suspicious activity
                if check_for_sus(line):
                    send_email_alert("Suspicious Activity Detected", line)
                    # Uncomment the next line if you want to send an email alert
                    # send_email_alert("Suspicious Activity Detected", f"Suspicious activity in log: {line}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        sys.exit(0)  # Exit cleanly when interrupted

# Function to check for suspicious activity
def check_for_sus(log_entry):
    """
    Check the log entry for suspicious activity.
    """
    # List of suspicious keywords which can indicate access to the server
    suspicious_keywords = ["Failed password", "authentication failure", "Invalid user", "Accepted password"]
    # Check if any suspicious keyword is in the log entry
    for keyword in suspicious_keywords:
        if keyword in log_entry:
            return True
    return False

# Main function
def main():
    """
    Main function to initiate monitoring of the auth.log file.
    """
    # Path to the auth.log file
    auth_log_path = '/var/log/auth.log'
    # Start monitoring the log file
    monitor_log(auth_log_path)

if __name__ == "__main__":
    main()
