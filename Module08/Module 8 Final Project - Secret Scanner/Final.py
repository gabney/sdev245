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

# Arguments for argparse parse object
# example mandatory argument
#parser.add_argument("name", help="The name of the user.")
# example optional argument
#parser.add_argument("--greet", action="store_true", help="Include a greeting.") 

parser.add_argument("searchtype", help="The type of search to conduct - file or directory")
parser.add_argument("searchloc", help="The location of search to conduct")

# Parses created arguments
args = parser.parse_args() 