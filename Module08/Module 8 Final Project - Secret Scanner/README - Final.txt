Module 8 Final Project - Secret Scanner - Readme
SDEV 245 Security and Secure Coding
Gabriel Abney

This is the readme file for the Module 08 Final Project by Gabriel Abney.


BRIEF OVERVIEW:

This program searches local files or local directories for regex patterns for API keys and auth 
tokens for common apps such as twitter or google. The patterns for these tokens are taken from 
the list found at https://github.com/odomojuli/regextokens. After scanning the local files,
successful hits for matching patterns are logged in a file named "scanresults.txt" that is 
generated in the 


HOW TO USE:

This program is run from the command line! Set the current working directory to match the 
Final.py, then run with the command 'Python Final.py <search type> <search location>', where 
the final two parameters in angled brackets specify parameters necessary to run the program.


COMMAND LINE INPUT PARAMETERS:

The first parameter to specify at command-line runtime is <search type>. The first valid value for
<search type> is 'file', to specify a specific file in the same directory as the Final.py program.
The second valid value for <search type> is 'directory', which specifies a subdirectory of the Final.py 
program's directory. 

The second parameter to specify at runtime is <search location>.  If 'file' was selected previously, 
valid values are a filename in the program directory, with the file extension included 
(e.g. 'filename.txt'). If 'directory' was selected previously, valid inputs are subdirectories 
of the Final.py program directory.

Example folders and files with fake tokens are included in the GitHub folder in order to test
the efficacy of the program.


OUTPUT FILE
The results of the searches are logged into a file named 'scanresults.txt' that is generated
in the same directory as the Final.py program.  In this file, successful matches of the regex
tokens in the scanned files are recorded, with the file name, line location within the file, 
and matching token recorded.