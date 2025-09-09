"""
Module 2: Assignment - Encrypt/Decrypt Demo
Gabriel Abney
This program asks the user to select an encryption type,
then prompts user input for a phrase to be encrypted.
The program will 

Please note: This program uses the 'cryptography' and 'rsa' libraries
that can be installed to a system running python using the commands 
'pip install cryptography' and 'pip install rsa' if they are not
already installed.  See more about the libraries here:
https://pypi.org/project/cryptography/
https://pypi.org/project/rsa/
"""

#imports fernet module from cryptography library for symmetric encryption
from cryptography.fernet import Fernet

#imports rsa library for asymmetric encryption (simpler than in cryptography library)
import rsa

#explanation of variables to use later in program
encrypt_type = "" #variable to indicate symmetric or assymetric encryption
original_message = "" #user message to encrypt/decrypt
altered_message = "" #user message after encryption/decryption
sym_key = "" #stores the encryption key for symmetric encryption
what_do = "" #action to do in loop

#main loop of program
while True:
    print("Welcome to ACME encryption!")
    encrypt_type = input("Please type 's' for symmetric encryption or 'a' for asymmetric encryption: ")

    if encrypt_type == 's':
        sym_key = Fernet.generate_key() #generates a random key using Fernet
        fernet = Fernet(sym_key)
        print("Symmetric encryption selected.")
        print(f"Your encryption key: {sym_key}")
        while True:
            what_do = input("Please select 'decrypt' or 'encrypt' or type 'exit': ")
            if what_do == "encrypt":
                original_message = input("Type a plaintext message to encrypt: ")
                altered_message = fernet.encrypt(original_message.encode())
                print(f"Your encrypted message is: {altered_message}")
            elif what_do == "decrypt":
                original_message = input("Type your encrypted message to decrypt: ")
                altered_message = fernet.decrypt(original_message.encode())
                print(f"Your decrypted message is: {altered_message}")
            elif what_do == "exit":
                break
            else:
                print("Invalid input.  Try again.")

    elif encrypt_type == 'a':
        print("Asymmetric encryption selected.")
        original_message = input("Please type a message for encryption: ")
    else:
        print("Invalid encryption type.  Try again.")