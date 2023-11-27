from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate a key for encryption and decryption."""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Encrypt a target file and replace it with the encrypted version."""
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    """Decrypt a target file and replace it with the decrypted version."""
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(data)

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def encrypt_string(cleartext, key):
    """Encrypt a string and print the ciphertext."""
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(cleartext.encode())
    print("Ciphertext:", ciphertext.decode())

def decrypt_string(ciphertext, key):
    """Decrypt a string and print the cleartext."""
    cipher_suite = Fernet(key)
    cleartext = cipher_suite.decrypt(ciphertext.encode())
    print("Cleartext:", cleartext.decode())

def main():
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    mode = input("Enter the mode (1/2/3/4): ")

    key = generate_key()

    if mode in ('1', '2'):
        file_path = input("Enter the file path: ")
        if mode == '1':
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
        elif mode == '2':
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
    elif mode in ('3', '4'):
        if mode == '3':
            cleartext = input("Enter the cleartext string: ")
            encrypt_string(cleartext, key)
        elif mode == '4':
            ciphertext = input("Enter the ciphertext string: ")
            decrypt_string(ciphertext, key)

if __name__ == "__main__":
    main()
