"""
Module 8 Final Project - Secret Scanner
SDEV 245 Security and Secure Coding
Gabriel Abney

This program allows the user to search for common
regex patterns such as API tokens within a specified file 
or folder.  The interface is a CLI created with argparse.
The results of the search are stored in a log file called 
scanresults.txt in the same directory as the program.
"""


# Package Imports

# Argparse package used to make Command-Line-Interfaces (CLIs) with better functionality
import argparse 
# Regular Expressions package used to handle regular expressions for searching text
import re
# Pathlib module for handling file and directory paths
import pathlib



# ArgParse setup

# Creates the ArgumentParser object for argparse
parser = argparse.ArgumentParser(description="Argument parser for SDEV 245 Final Project") 
# adds arguments to argparse object
parser.add_argument("search_type", help="The type of search to conduct - file or directory")
parser.add_argument("search_loc", help="The location file or directory to search")
# Parses created arguments
args = parser.parse_args()



# Regex setup

# dictionary of common app tokens and their regex patterns from https://github.com/odomojuli/regextokensas
tokens = {
    "Twitter Token": "[1-9][0-9]+-[0-9a-zA-Z]{40}",
    "Google API Key": "AIza[0-9A-Za-z-_]{35}",
    "Facebook Access Token": "EAACEdEose0cBA[0-9A-Za-z]+",
    "Stripe Standard API Key": "sk_live_[0-9a-zA-Z]{24}",
    "Mailchimp Access Token": "[0-9a-f]{32}-us[0-9]{1,2}"
}



# Output log file for results to be stored (file will be created if it does not already exist)
log_file = "scanresults.txt"



# Functions

def scan(file_name):
    """Scans a file that is passed for regex patterns and logs matches."""
    with open(log_file, "a+") as log, open(file_name, "r") as f:
        log.write(f"Scan results for {file_name}:\n")
        for t in tokens: # iterates through all tokens in the dictionary
            pattern = re.compile(tokens[t]) # sets regex search pattern for app
            for line_index, line_text in enumerate(f): # makes an iterable object of line number and the line text string
                for match in re.finditer(pattern, line_text): # finds matching instances of the pattern and line text
                    log.write(f"Found {t} with value '{match.group()}' at line {line_index + 1}.\n")


def file_search(file_name):
    """Searches for a file in the local directory.  Must be passed a file name (including extension e.g. .txt) as parameter."""
    if pathlib.Path.is_file(pathlib.Path(file_name)): #checks to see if file exists before searching
        scan(file_name) # passes file to scan function
        print(f"Scanned {file_name}. See results in {log_file}.") # prints confirmation to console
    else:
        print(f"Error, file {file_name} does not exist.") # error message if file does not exist


def dir_search(dir_name):
    """Searches for a specified directory. If exists, populates a list of all files to sequentially pass to file_search() function."""
    if pathlib.Path.is_dir(pathlib.Path(dir_name)): #checks to see if directory exists before searching
        for item in pathlib.Path(dir_name).rglob("*"): # recursive globs to find all subdirectories and files in given directory
            if item.is_file():  # checks to see if identified item is a file
                file_search(item)  # passes file to file_search function
    else:
        print(f"Error, {dir_name} is not a valid directory.") # error message if file does not exist
    


# Main program body

if args.search_type == "file": # leads to file search
    file_search(args.search_loc)
elif args.search_type == "directory": # leads to directory search
    dir_search(args.search_loc)
else: # error if invalid search type
    print("Error. Valid search types are 'file' or 'directory'.")