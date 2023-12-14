#!/usr/bin/python3
#Name: Leonardo Pinto 

import time
import string

def offensive_dictionary_iterator():
    file_path = input("Enter the path to the wordlist file: ")

    try:
        with open(file_path, 'r') as file:
            words = file.read().split()

            for word in words:
                time.sleep(0.5)  # Add a delay of 1 second between words
                print(word)

    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

#read a word list from a file and allows the user to input strings for searching within the word list. If the user inputs 'exit', the loop breaks; 

def defensive_password_recognized():
    file_path = input("Enter the path to the word list file: ")

    try:
        with open(file_path, 'r') as file:
            words = file.read().split()

            while True:
                user_input = input("Enter a string to search in the word list (type 'exit' to quit): ")

                if user_input.lower() == 'exit':
                    break

                if user_input in words:
                    print(f"The string '{user_input}' is recognized!")
                else:
                    print(f"The string '{user_input}' is not in the word list.")

    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def defensive_password_complexity():
    password = input("Enter a password to check complexity: ")

    # Define password complexity
    min_length = 8
    min_uppercase = 1
    min_digits = 1
    min_symbols = 1

    # Check password complexity
    length_satisfied = len(password) >= min_length
    uppercase_satisfied = any(char.isupper() for char in password) >= min_uppercase
    digits_satisfied = any(char.isdigit() for char in password) >= min_digits
    symbols_satisfied = any(char in string.punctuation for char in password) >= min_symbols

    # Print results
    print(f"Password Length: {'Satisfied' if length_satisfied else 'Not Satisfied'}")
    print(f"Uppercase Letters: {'Satisfied' if uppercase_satisfied else 'Not Satisfied'}")
    print(f"Digits: {'Satisfied' if digits_satisfied else 'Not Satisfied'}")
    print(f"Symbols: {'Satisfied' if symbols_satisfied else 'Not Satisfied'}")

    if all([length_satisfied, uppercase_satisfied, digits_satisfied, symbols_satisfied]):
        print("Password Complexity: SUCCESS")
    else:
        print("Password Complexity: FAILURE")

if __name__ == "__main__":
    print("Select a mode:")
    print("1: Offensive; Dictionary Iterator")
    print("2: Defensive; Password Recognized")
    print("3: Defensive; Password Complexity")

    selected_mode = input("Enter the mode number: ")

    if selected_mode == "1":
        offensive_dictionary_iterator()
    elif selected_mode == "2":
        defensive_password_recognized()
    elif selected_mode == "3":
        defensive_password_complexity()
    else:
        print("Invalid mode selection. Please choose a valid mode.")



