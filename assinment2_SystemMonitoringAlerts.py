#!/usr/bin/python3
# Authors: Ronald Jong,
# Seneca ID: 033295148
# This script monitors the /var/log/auth.log file for suspicious activity and sends alerts.

import os
import sys
import time

# Function to send an email alert
def send_email_alert(subject, message):
    """
    Sends an email alert with the given subject and message.
    """
    email = "rjong1@myseneca.ca"
    receving_email = "ronaldjong2323@gmail.com"
    command = f'echo "{message}" | mail -s "{subject}" {receving_email}'
    os.system(command)

# Function to monitor log file and changes
def monitor_log(log_file_path):
    ...

# Function to see if there is suspicios activity
def check_for_sus(log_entry):
    """
    Check the log entry for suspicios activity.
    """
    ...    
# Main function
def main():
    """
    Main function to initiate monitoring of the auth.log file.
    """
    # Path to the auth.log file
    auth_log_path = '/var/log/auth.log'
...

if __name__ == "__main__":
    main()