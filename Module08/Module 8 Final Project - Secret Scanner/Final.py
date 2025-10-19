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


# Creates the ArgumentParser object for argparse
parser = argparse.ArgumentParser(description="Argument parser for SDEV 245 Final Project") 

parser.add_argument("searchtype", help="The type of search to conduct - file or directory")
parser.add_argument("searchloc", help="The location file or directory to search")


# Parses created arguments
args = parser.parse_args()

# regex tokens for common apps from https://github.com/odomojuli/regextokens
twitter_token = "[1-9][0-9]+-[0-9a-zA-Z]{40}"
google_API = "AIza[0-9A-Za-z-_]{35}"
facebook_token = "EAACEdEose0cBA[0-9A-Za-z]+"
stripe_standard_API = "sk_live_[0-9a-zA-Z]{24}"
mailchimp_token = "[0-9a-f]{32}-us[0-9]{1,2}"

with open 