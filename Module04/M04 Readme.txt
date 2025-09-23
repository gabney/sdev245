This is the readme file for 'M04 Midterm Secure Data Transmission App.py' for SDEV 245 by Gabriel Abney


This program allows the user to do two processes:

1. Input a message to be encrypted and saved to a file alongside its key after being hashed
2. Decrypt an encrypted message using the key and compare its hash to the original message hash

The program should inform the user of the valid inputs for navigation as well as data processing results, \
but further explanations follow:

Main menu:
Here, the user can navigate to either of the program processes. Valid inputs are 'encrypt' to go to the \
encryption, hashing, and key generation process or 'decrypt' to go to the decryption, hashing, and hash \
validation process.  The user returns to the main menu after either process is completed.

Encryption, hashing, and key generation:
In this part of the program, the user is prompted to enter a plaintext message.  This message will be used \
to create a hash value that is saved to the file 'original_hash.txt'.  After the hash is generated, a funtion \
generates a symmetric key and saves that key to the file 'encryption_key.txt'.  The file containing this key \
must be shared with the intended recipient of the encrypted message and stored in the program directory, but \
the user is warned to not share it with anyone else for secure communication with no tampering.  The symmetric \
key is used to encrypt the original secret message, and this new message is saved as 'encrypted_message.txt'.

Decryption, hashing, and hash validation:
For this part of the program to work, the user must have the 'encryption_key.txt', 'encrypted_message.txt', \
and 'original_hash' files from the original user who began the encryption process stored in the program directory. \
If they are present, then the decryption process begins as soon as this part of the program is entered.  The \
encryption key is read from its file, and used with the data from the encrypted message file to create the final \
decrypted message, which is presented to the user in the console.  After the decrypted message is created, the \
hashing algorithm creates a hash with the final message.  If the hash value from this final message is identical \
to the hash value from the original message, the user is informed that the message was securely transferred. \
If the hashes are not identical, the user is informed that they are not the same and that the message was not \
transferred securely.


This program demonstrates the CIA triad values of confidentiality, integrity, and availibility.  For confidentiality, \
this program uses a symmetric encryption algorithm, which means that only users who have the encryption key can \
read or write the encrrypted messages.  The data is otherwise unintelligible to those without it.  For integrity, \
this program generates a hash of the original message before encryption, as well as the final message after \
encryption.  This lets a user know that the message that was passed along has not been tampered with.  For \
availibility, this program does not require any online connection, only that it be run on a machine with \
Python3 and the appropriate packages installed.  No outside user can remove access to the messages.