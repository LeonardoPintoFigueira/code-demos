import time
from datetime import datetime
import os
import platform
import smtplib
from email.mime.text import MIMEText

def ping(host):
    """
    Function to send a single ICMP packet (ping) to the specified host.
    Returns True if successful, False otherwise.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return os.system(" ".join(command)) == 0

def send_email(subject, body, to_email):
    """
    Function to send an email notification.
    """
    sender_email = "your_email@gmail.com"  # Replace with your Gmail email address
    sender_password = "your_password"  # Replace with your Gmail app password
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())

def main():
    host_to_ping = input("Enter the target IP address: ")
    admin_email = input("Enter your email address: ")
    admin_password = input("Enter your email password: ")

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        status_before = "Network Active" if ping(host_to_ping) else "Network Inactive"
        time.sleep(2)
        status_after = "Network Active" if ping(host_to_ping) else "Network Inactive"

        log_entry = f"{timestamp} {status_before} to {status_after} to {host_to_ping}"
        print(log_entry)

        if status_before != status_after:
            subject = f"Host Status Change: {host_to_ping}"
            body = f"Host status changed from {status_before} to {status_after} at {timestamp}"
            send_email(subject, body, admin_email)

if __name__ == "__main__":
    main()
