"""
Module 8 Final Project - Secret Scanner
SDEV 245 Security and Secure Coding
Gabriel Abney

This program allows the user to search for common
regex patterns such as passwords within a specified file 
or folder.  The interface is a CLI created with argparse.
The results of the search are stored in a log file in the 
same directory as the program.
"""

# Package Imports

# Argparse package used to make Command-Line-Interfaces (CLIs) with better functionality
import argparse 

# Regular Expressions package used to handle regular expressions for searching text
import re

# Pathlib module for handling file and directory paths
from pathlib import Path


# Creates the ArgumentParser object for argparse
parser = argparse.ArgumentParser(description="Argument parser for SDEV 245 Final Project") 

parser.add_argument("search_type", help="The type of search to conduct - file or directory")
parser.add_argument("search_loc", help="The location file or directory to search")


# Parses created arguments
args = parser.parse_args()

# regex tokens for common apps from https://github.com/odomojuli/regextokens
twitter_token = "[1-9][0-9]+-[0-9a-zA-Z]{40}"
google_API_key = "AIza[0-9A-Za-z-_]{35}"
facebook_token = "EAACEdEose0cBA[0-9A-Za-z]+"
stripe_standard_API_key = "sk_live_[0-9a-zA-Z]{24}"
mailchimp_token = "[0-9a-f]{32}-us[0-9]{1,2}"

# simplified list of above tokens for ease of use later
tokens = [
    twitter_token,
    google_API_key,
    facebook_token,
    stripe_standard_API_key,
    mailchimp_token
]

# log file for results to be stored
log_file = "scanresults.txt"


# Functions
def scan():
    """Scans a file that is passed """
    pass

def file_search(file_name):
    """Searches for a file in the local directory.  Must be passed a file as parameter"""
    if Path.is_file(Path(file_name)): #checks to see if file exists before searching
        scan(file_name)
        print(f"Scanned f{file_name}. See results in {log_file}")
    else:
        print("Error. File does not exist.") # error message if file does not exist

def dir_search():
    pass
    

# Main program body

if args.search_type == "file": # leads to file search
    file_search(args.search_loc)
elif args.search_type == "directory": # leads to directory search
    pass
else: # error if invalid search type
    print("Error. Valid search types are 'file' or 'directory'.")