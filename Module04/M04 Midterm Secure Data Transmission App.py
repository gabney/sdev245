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
encryption is saved in a file called "encryption_key.txt" and a security warning is printed \
to the console. 
If the user selects 'decrypt', then the encryption_key.txt file is read alongside the \
encrypted_message.txt file to decrypt the message.  This message is printed to console. \
The hash of this final message is generated, and compared to the hash of the original \
message.  The user is informed of whether they are identical or not.


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
    print(f"Hash of message saved to file {file_name}.txt")


# Function to generate an encrypted message using symmetric encryption with the cryptography module
def encrypt_this(encrypt_what):
    """This function generates a key for symmetric encryption, then uses that key to encrypt the encrypt_what parameter and save this encrypted message to a file called 'ecrypted_message.txt"""
    # Generates a random encryption key using Fernet for symmetric encryption
    sym_key = Fernet.generate_key()
    # Creates Fernet instance using sym_key
    fernet = Fernet(sym_key)
    # Decoes and writes key to file so it can be shared with the intended recipient
    sym_decode = sym_key.decode()
    with open("encryption_key.txt", "w") as f:
        f.write(sym_decode)

    # Prints message to console about encryption key location
    print("Your symmetric encryption key is saved in 'encryption_key.txt'. Be careful to only share this with the intended recipient of the encrypted file!")

    # Uses the key to encrypt the passed message parameter
    encrypted_message = fernet.encrypt(encrypt_what)
    # Writes the encrypted message to the encrypted_message.txt file to be shared
    with open("encrypted_message.txt", "w") as f2:
        f2.write(encrypted_message.decode())

    # Prints message to console about encrypted message location
    print("Your encrypted message is saved in 'encryption_key.txt'. This can only be decrypted using the symmetric encryption key.\n")


def decrypt_this():
    """This function reads the saved encryption_key.txt and encrypted_message.txt files and returns the decrypted message."""
    # Reads the encryption_key.txt file to find the symmetric key and encodes it for use in Fernet
    with open("encryption_key.txt", "r") as f:
        sym_decode = f.read()
    sym_key = sym_decode.encode()
    # Creates a Fernet instance using the symmetric key
    fernet = Fernet(sym_key)
    
    # Reads the encrypted_message.txt file to extract the encrypted message
    with open("encrypted_message.txt", "r") as f:
        encrypted_message = f.read()

    # Decrypts the message using the symmetric key
    decrypted_message = fernet.decrypt(encrypted_message)
    # Returns the decrypted message to the main body
    return decrypted_message


# Function to compare the value of the original hash and final hash to see if the messages are identical
def hash_validation():
    """This function reads the orginal_hash.txt and final_hash.txt files to compare their values.  Returns True or False."""
    # Extracts the hash of the original message
    with open("original_hash.txt", "r") as f:
        original_hash = f.read()
    # Extracts the hash of the final message
    with open("final_hash.txt", "r") as f2:
        final_hash = f2.read()

    #Checks to see if the original hash and final hash are identical, then returns True or False
    if original_hash == final_hash:
        return True
    else:
        return False
    
        
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
        print("Encryption and hashing process selected.")
        # Collects string input for plaintext secret message and encodes for processing
        secret_message = input("Please type your secret message: ").encode()

        # Generates a hash of the secret message and saves it to original_hash.txt
        hash_this(secret_message, "original_hash")

        # Generates an ecrypted version of the secret message, which is written to the file encrypted_message.txt
        encrypt_this(secret_message)


    # Decryption and hash comparison process
    elif what_do == "decrypt":
        print("Decryption and hash validation selected.")

        # Begins the decryption function, which requires encryption_key.txt and ecrypted_message.txt to be present in directory
        decrypted_message = decrypt_this()
        # Prints the decrypted message to the console
        print(f"The decrypted message is: {decrypted_message.decode()}")

        # Runs the hash generation function on the new decrypted message
        hash_this(decrypted_message, "final_hash")

        # Runs the hash validation function on original_hash.txt and final_hash.txt to see if they are identical
        identical_hashes = hash_validation()

        # Prints the result of the hash validation function to the user to let them know if the file was securely transferred
        if identical_hashes == True:
            print("The message hashes are identical. The secret message was transferred securely.\n")
        else:
            print("Sorry, the message hashes are not identical.\n")


    # Lets the user know if they typed a bad input
    else:
        error_input()

