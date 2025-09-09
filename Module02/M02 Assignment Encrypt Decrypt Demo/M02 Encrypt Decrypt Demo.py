"""
Module 2: Assignment - Encrypt/Decrypt Demo
Gabriel Abney
This program asks the user to select an encryption type,
then prompts user input for a phrase to be encrypted or decrypted.
The symmetric encryption option generates a single key to use for both
encryption and decryption.  The asymmetric option generates a public
key for encryption and a private key for decryption.

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
public_key = "" #stores the public key for asymmetric encryption
private_key = "" #stores the private key for asymmetric encryption

#main loop of program
while True:
    print("Welcome to ACME encryption!")
    encrypt_type = input("Please type 's' for symmetric encryption or 'a' for asymmetric encryption: ")

    #symmetric encryption code
    if encrypt_type == 's':
        sym_key = Fernet.generate_key() #generates a random key using Fernet
        fernet = Fernet(sym_key) #creates Fernet instance using key
        print("Symmetric encryption selected.")
        print(f"Your encryption key: {sym_key}")
        #loop to hande encryption and decryption processs
        while True:
            what_do = input("Please select 'decrypt' or 'encrypt' or type 'exit': ") #asks user to choose to encrypt or decrypt
            if what_do == "encrypt":
                original_message = input("Type a plaintext message to encrypt: ")
                altered_message = fernet.encrypt(original_message.encode()) #encrypts message using sym_key
                print(f"Your encrypted message is: {altered_message}")
            elif what_do == "decrypt":
                original_message = input("Type your encrypted message to decrypt: ")
                altered_message = fernet.decrypt(original_message).decode() #decrypts message using sym_key
                print(f"Your decrypted message is: {altered_message}")
            elif what_do == "exit":
                break   #exits loop
            else:
                print("Invalid input.  Try again.") #error message

    #asymmetric encryption code
    elif encrypt_type == 'a':
        public_key, private_key = rsa.newkeys(128) #generates the public key and private key using a 128 bit key length
        print("Asymmetric encryption selected.")
        print(f"Your public key: {public_key}")
        print(f"Your private key: {private_key}")
        #loop to handle encryption and decryption process
        while True:
            what_do = input("Please select 'decrypt' or 'encrypt' or type 'exit': ") #asks user to choose to encrypt or decrypt
            if what_do == "encrypt":
                original_message = input("Type a plaintext message to encrypt using your public key: ")
                altered_message = rsa.encrypt(original_message.encode(), public_key) #encrypts message using public key
                print(f"Your encrypted message is: {altered_message}")
            elif what_do == "decrypt":
                original_message = input("Type your encrypted message to decrypt using your private key: ")
                altered_message = rsa.decrypt(original_message, private_key).decode() #decrypts message using private_key
                print(f"Your decrypted message is: {altered_message}")
            elif what_do == "exit":
                break   #exits loop
            else:
                print("Invalid input.  Try again.") #error message

    #error message if invalid input
    else:
        print("Invalid encryption type.  Try again.")