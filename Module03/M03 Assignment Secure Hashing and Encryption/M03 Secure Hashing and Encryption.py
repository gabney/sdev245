"""
Module 03: Assignment - Secure Hashing and Ecryption
SDEV 245 Secruity and Secure Coding
Gabriel Abney

This program allows the user to select between the functions of \
SHA-256 hash generation, encryption using a simple substitution cipher, \
or generation of a digital signature.  If the user selects SHA-256 \
hash generation, the user is prompted to choose either text input, 
or a file input to have text written to.  The user then inputs a message, \
and is given the resulting 256-bit hash of the text/file as a printed output.  
If the user selects simple subsititution, they are prompted to select enchipher 
or decipher. For enchipher, the user is prompted to input a message, then they are given \
the resulting enciphered message.  For decipher, the user is prompted to input a \
previously enciphered message, and given the deciphered message as an output. \
If the user selects digital signature generation, a public and private key pair \
is generated for the user to use in later decryption and encryption.

Please note: this program uses the 'cryptography' library that must first be \
installed using pip with the command 'pip install cryptography'.  Read more here: \
https://pypi.org/project/cryptography/

"""

# imports libraries for use in program
# please note that cryptography library must be first installed using PIP
import hashlib # built in library for generating hashes
from pathlib import Path # built in library for generating filepaths for interacting files outside script
import cryptography # installed library for various cryptographic functions


# placeholder variables to be used later on in the program
what_do = '' # string from user inputs to navigate to different program functions
message_type = '' # string to control whether a text message or text file is what will be encrypted using SHA-256 
txt_message = '' # string text message to generate SHA-256 hash
txt_message_hash = '' # final hash of the txt_message input
file_message = '' # message to be written to file for SHA-256 hash
file_message_hash = '' # final hash of the secretmessage.txt file
enc_dec = '' # string to control whether to encrypt or decrypt the message
input_message = ''# string to store the user's method for substitution encryption/decryption
encrypted_message = '' # string to store final message after subsititution encryption
decrypted_message = '' # string to store final message after substitution decryption


while True: # main program body loop
    print("Welcome to the ACME encryption program.")
    what_do = input("Please type 'sha' for SHA-256 Hash Generation, 'sub' for simple substitution encryption, or 'sign' for digital certificate signing: ")
    

    if what_do == "sha": # SHA-256 hash generation
        while True:
            print("SHA-256 Hash Generation mode selected.")
            message_type = input("Type 'text' to input a simple text message, or type 'file' to save a message to a file, or type 'q' to quit: ") #prompts user to select text or file type
           
            if message_type == "text":
                txt_message = input("Type your text message to generate a SHA-256 Hash: ").encode() # collects user text input and encodes it as bytestream, as txt_message variable
                sha256_txt = hashlib.sha256() # initializes hashlib sha256 method with sha256_txt as the working variable
                sha256_txt.update(txt_message) # passes txt_message bytestream to sha256_txt
                txt_message_hash = sha256_txt.hexdigest() # converts the passed bytestream text to the final hashed format
                print(f"Your hash value for your message is: {txt_message_hash}")
            
            elif message_type == "file":
                file_message = input("Type your text message to store in secretmessage.txt and generate a SHA-256 Hash: ") # collects user text input to be written to secretmessage.txt file
                base_dir = Path(__file__).parent # get current directory path for successfully generating file
                file_path = base_dir / 'secretmessage.txt' #prepares to add secretmessage.txt in current directory
                f = open(f"{file_path}", 'w+') # opens secretmessage.txt in write+read mode, which will overwrite existing file or create a new file if it does not exist
                f.write(file_message) # writes the inputted secret message to the file
                sha256_file = hashlib.sha256() # initializes hashlib sha256 method with sha256_file as the working variable
                secret_data = f.read().encode() # reads the message in the secretmessage file, then encodes it as bytes as secret_data
                sha256_file.update(secret_data) # passes the encoded data to sha256_file
                file_message_hash = sha256_file.hexdigest() #converts the bytecode to the final hashed format
                print(f"Your hash value for your file is: {file_message_hash}")
            
            elif message_type == "q": # quits to main menu
                break
           
            else: # error message for bad input
                print("Invalid input. Try again.")


    elif what_do == "sub": # simple substitution encryption 
        while True:
            print("Simple substitution encryption mode selected.")
            enc_dec = input("Type 'enc' to encrypt a message, or 'dec' to decrypt a previously encrypted message, or type 'q' to quit: ") # user input to choose between encryption and decryption
            
            if enc_dec == "enc":
                input_message = input("Please type the message to encrypt: ") # gets user input for message to encrypt
                for character in input_message: # iterates through each character in input_message
                    new_character = chr(ord(character) + 10) # converts the character to ascii value, increments that value by 10, then converts back to ascii character
                    encrypted_message += new_character #adds each encrypted character to encrypted_message
                print(f"Your encrypted message is {encrypted_message}") # prints encrypted message

            elif enc_dec == "dec":
                input_message = input("Please type the message to decrypt: ") # gets user input for message to decrypt
                for character in input_message: # iterates through each character in input_message
                    new_character = chr(ord(character) - 10) # converts the character to ascii value, decrements that value by 10, then converts back to ascii character
                    decrypted_message += new_character #adds each encrypted character to decrypted_message
                print(f"Your encrypted message is {encrypted_message}") # prints decrypted message
                
            elif enc_dec == 'q': #quits to main menu
                break
           
            else: # error message for bad input
                print("Invalid input. Try again.")


    elif what_do == "sign":
        pass

    else:
        print("Invalid input. Try again.")