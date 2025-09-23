"""
Module 4 Midterm: Build a Secure Data Transmission App with Hashing and Encryption
SDEV 245 Security and Secure Coding
Gabriel Abney

This program allows the user to input a secret message that they want to encrypt.  A hash \
for the plaintext secret message is generated and written to a file called \
"hash_original.txt" and then the secret message is encrypted using the SHA-256 algorithm. \
This encrypted message is stored to a 



Please note:  This program uses the 'cryptography' library which must first be installed \
by using the 'pip install cryptography' command if not already installed.  Read the \
documentation for the cryptography library here: https://pypi.org/project/cryptography/
"""



# Libraries/packages/libraries imported for this program

# Imports the Python3 built-in module for generating hashes
import hashlib
# Imports the fernet module from the external cryptography library for symmetric encryption
from cryptography.fernet import Fernet



# Functions to be used later in the program

# Function to generate a hash of a message.
def hash_this(hash_what, file_name):
    """This function generates a hash of the first parameter, then prints that hash to a file named after the second parameter."""
    sha256_txt = hashlib.sha256() # initializes hashlib sha256 method with sha256_txt as the working variable
    sha256_txt.update(hash_what) # passes txt_message bytestream to sha256_txt
    with open(f"{file_name}.txt", "w") as f:



def error_message():
    """This function prints an error message indicated the user inputted an invalid string."""
    print("Invalid input, try again.")




# Main program loop
while True:
    print("Welcome to the ACME secure data transmission program.")
    input("Please type 'encrypt' to ")



"""
# demonstrates that encoding and decoding fernet is similar text just saved differently
sym_key = Fernet.generate_key()
sym_key2 = sym_key.decode()
print(sym_key)
print(sym_key2)
"""