"""
Module 4 Midterm: Build a Secure Data Transmission App with Hashing and Encryption
SDEV 245 Security and Secure Coding
Gabriel Abney

This program allows the user to choose to save a message to encrypt or to decrypt an \
encrypted message that has already been saved. 
If the user selects 'encrypt', the are prompted to input a secret message that they want \
to encrypt.  An SHA-256 hash for the plaintext secret message is generated and written \
to a file called "hash_original.txt". Then the secret message is encrypted using \
symmetric enecryption and stored to a file called "encrypted_message.txt". The key for \
encryption is saved in a file called "encryption_key.txt", printed to console with a \
security warning, and then overwritten for security. \
If the user selects 'decrypt', then 



Please note:  This program uses the 'cryptography' library which must first be installed \
by using the 'pip install cryptography' command if not already installed.  Read the \
documentation for the cryptography library here: https://pypi.org/project/cryptography/
"""



# Libraries/packages/modules imported for this program

# Imports the Python3 built-in module for generating hashes
import hashlib

# Imports the Fernet module from the external cryptography library for symmetric encryption
from cryptography.fernet import Fernet



# Functions to be used later in the program

# Function to generate a hash of an input string and save it to a file.
def hash_this(hash_what, file_name):
    """This function generates a hash of the first parameter, then saves that hash to a file named after the second parameter."""
    # Initializes hashlib SHA256 method with name 'sha256_txt'
    sha256_txt = hashlib.sha256()
    # Passes the 'hash_what' parameter of the function to the hash generator
    sha256_txt.update(hash_what)
    # Creates the final hash
    digested_hash = sha256_txt.hexdigest()

    # Stores the final hash value in a file using the file_name parameter
    with open(f"{file_name}.txt", "w") as f:
        f.write(digested_hash)
    
    # Prints confirmation message to console.
    print(f"Hash saved to file {file_name}.txt")


# Function to generate an encrypted message using symmetric encryption with the cryptography module
def encrypt_this(encrypt_what):
    """This function generates a key for symmetric encryption, then uses that key to encrypt the encrypt_what parameter and save this encrypted message to a file called 'ecrypted_message.txt"""
    # Generates a random encryption key using Fernet for symmetric encryption
    sym_key = Fernet.generate_key()
    # Creates Fernet instance using sym_key
    fernet = Fernet(sym_key)
    # Writes key to file so it can be shared with the intended recipient
    with open(f"encryption_key.txt", "w") as f:
        f.write(sym_key)

    # Uses the key to encrypt the passed message parameter
    encrypted_message = fernet.encrypt(encrypt_what)
    # Writes the encrypted message to the console

    # Prints message to console about encryption key location
    print(f"Your symmetric encryption key is saved in 'encryption_key.txt'. Be careful to only share this with the intended recipient of the encrypted file!")



# Function to print error message, to keep code tidy later
def error_input():
    """This function prints an error message indicated the user inputted an invalid string."""
    print("Invalid input, try again.\n")



# Main program loop
while True:
    print("Welcome to the ACME secure data transmission program.")
    # Lets the user select between encryption and decryption processes
    what_do = input("Please type 'encrypt' to hash and ecrypt a message or 'decrypt' to decrypt a message and compare hash values: ")

    # Encryption and hashing processes
    if what_do == "encrypt":
        # Collects string input for plaintext secret message and encodes for processing
        secret_message = input("Please type your secret message: ").encode()

        # Generates a hash of the secret message and saves it to original_hash.txt
        hash_this(secret_message, "original_hash")

        # Generates a 
        encrypt_this(secret_message)

    #
    elif what_do == "decrypt":
        pass
    else:
        error_input()
    



"""
# debug, testing if fernet key is encoded
sym_key = Fernet.generate_key()
sym_key2 = sym_key.decode()
print(sym_key)
print(sym_key2)
"""