#Name: Leoanardo Pinto
#Date: 24/11/2023 
#Objective: Ping Host

#!/usr/bin/python3

import time
from datetime import datetime
import os
import platform

def ping(host):
    """
    Function to send a single ICMP packet (ping) to the specified host.
    Returns True if successful, False otherwise.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return os.system(" ".join(command)) == 0

def main():
    # Accept user input for target IP address
    host_to_ping = input("Enter the target IP address: ")
    
    # Open a text file for logging
    log_file = open("ping_log.txt", "a")
    
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        if ping(host_to_ping):
            status = "Network Active"
        else:
            status = "Network Inactive"
        
        log_entry = f"{timestamp} {status} to {host_to_ping}"
        print(log_entry)
        
        # Save the log entry to the text file
        log_file.write(log_entry + "\n")
        
        time.sleep(2)

if __name__ == "__main__":
    main()
