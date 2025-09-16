This is the readme file for the 'M03 Secure Hashing and Encryption.py' program by Gabriel Abney for SDEV 245

This program allows the user to perform three categories of processes: 

1. Create hash files for either text or files
2. Encrypt or decrypt text messages using a simple subsititution cipher
3. Sign data using a self-signed certificate

Please follow the messages in the console while running the program, as they include valid inputs to navigate through the program.
Further instructions for each section follow below:

Main menu:
Allows the user to navigate to specific processes of the program.  Valid inputs are 'sha' for navigating to the SHA-256 hashing process, \
'sub' for navigating to the simple substitution cipher encrypt/decrypt process, and 'sign' for navigating to the digital signing process. \

SHA-256 hash generation process:
The user will be prompted to choose either 'text' or 'file' depending on what they want to generate a hash for.  They user can also type \
'q' to quit back to the main menu. For 'text', the user will be asked to input a text message.  This message is immediately translated to \
bytecode and a hash is generated using the SHA-256 hash generation in the hashlib library built into python.  The resulting hash code is \
printed to the console.  If 'file' is selected, a more complicated process occurs, but the user is initially asked to input a message.  \
A file named secretmessage.txt is created in the directory where the python script is run, and the user's message is written to the file. \
After that, the data on the file is read, encoded into bytecode, and a hash is generated and displayed for the user in the console.

Simple substitution process:
The user will be prompted to input either 'enc' to encrypt a message or 'dec' to decrypt a message.  The user can also type 'q' to quit \
back to the main menu.  For encrypt, the user is asked to input a plaintext message.  The characters in this message are converted to \
their ASCII ordinal values, incremented by 10, and converted back to new characters.  The final message composed of the enciphered \
characters is printed to the console for the user.  For decrypt, a similar process occurs, but the user is prompted to input a previously \
encrypted message.  The ASCII ordinal codes are decremented by 10 to undo the prior encryption, and the resultig decrypted message is \
printed to the console.

Digital signing process:
When selected, a private key and public key are generated.  The user can type 'sign' to input a message to sign using the private key, \
type 'verify' to input a message to verify by using the public key, or 'keys' to display information about the generated keys.

