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
    receving_email = "parishapuri@gmail.com"
    # Makes the command to send an email with the subject and message
    command = f'echo "{message}" | mail -s "{subject}" {receving_email}'
    # Runs the command using the os.system method
    os.system(command)

# Function to monitor log file and changes
def monitor_log(log_file_path):
    #open the log file read
    with open(log_file_path, 'r') as file:
        # Move to the end of the file to look for new entrys
        file.seek(0, os.SEEK_END)
        while True:
            # Read the next line of the file
            line = file.readline()
            # if no new line is found, pause the script if no new line has been added.
            if not line:
                time.sleep(1)
                continue
            # Check the new log for suspiciouse activity
            check_for_sus(line)

# Function to see if there is suspicios activity
def check_for_sus(log_entry):
    """
    Check the log entry for suspicious activity.
    """
    # list of suspicious keywords which can indicate access to the server
    suspicious_keywords = ["Failed password","authentication failure","Invalid user","Accepted password" ]
    '''
    using for loop to check for keyword in the log file which will return True if any suspicous keyword 
    is detected or return False if no suspicios keyword is detected
    '''
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
