This is the readme file for the SDEV 245 Module 02 Assignment Encrypt Decrypt Demo by Gabriel Abney

This program demonstrates the use of both Symmetric and Asymmetric Encryption and decryption methods for altering data.
The program accepts plaintext, unecrypted inputs from the user and then utilizes the Python cryptography and rsa libraries to encrypt that data using keys generated in the program.  These keys are displayed to the user of the program, but ideally a symmetric encyption key would be carefully shared with both the sender and receiver of encrypted data.  For asymmetric encryption, the public key would be freely available to encrypt data, while the private key would only be known by the receiver, who would then use it to decrypt the data.  

Please read the program text prompts, as they should navigate the user through the program step by step.  However, a brief guide follows:
First, the user will be asked whether they want to use symmetric or asymmetric encryption.  Valid inputs are 's' for symmetric encryption or 'a' for asymmetric encryption.
Upon selecting one  of these options, the relevant key(s) will be generated and displayed to the user.  Then, the user will be asked if they want to encrypt or decrypt data using the key.  Valid inputs are 'encrypt' to proceed with encryption, 'decrypt' to proceed with decryption, or 'exit' to go back to the original set of options.
After selecting 'encrypt' or 'decrypt', the user is prompted to enter a string of either plaintext or ciphered data, respectively.  The program will then return the string having been altered by the encrypt/decrypt process.

