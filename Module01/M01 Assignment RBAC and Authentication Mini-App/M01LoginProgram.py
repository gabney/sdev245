"""
Module 01 Assignment - RBAC and Authentication Mini-App
Gabriel Abney
This program allows the user to input a username and password, 
then checks if those inputs are valid user credentials.  If login
is successful, prompts the user to change settings and checks to see
if the user is authorized to change those settings.

This program demonstrates the CIA triad values of Confidentiality, 
Integrity, and Availability.  Confidentiality is maintained by only 
allowing valid accounts to login with appropriate passwords and by
only displaying an error code that does not indicate whether an account 
may or may not exist if login should fail. Integrity is maintained by 
giving accounts roles with authorization only to change their respective
settings.  Availability should not be an issue for this program, as 
invalid inputs are handled with errors without terminating the program 
loop and the program is run locally, even if it is downloadable from
GitHub.
"""

#initialized variables for user login input strings, and logged in Boolean
account = "" 
password = ""
loggedIn = False

#sentinel Boolean to exit main program loop
sentinel = True

#main program loop, which handles user authentication in the outer loop and user authorization in the inner loop
while sentinel == True:
    print("Welcome to the ACME login page.")
    print("For testing purposes, the ADMIN role username is 'admin' and password is 'adminPW',") #gives prompt for testing role authentication
    print("and the USER role username is 'user' and password is 'userPW'.")
    account = input("Please enter your username: ") #input for username
    password = input("Please enter your password: ") #input for password

    #conditional statements for handling authentication results
    if account == "admin" and password == "adminPW":
        print("Welcome admin!")
        loggedIn = True
    elif account == "user" and password == "userPW":
        print("Welcome user!")
        loggedIn = True
    else:
        print("Login failed, invalid username or password.")

    #inner loop, which iterates if authentication was successful
    while loggedIn == True:
        print("You can now attempt to change settings or logout.")
        print("For testing purposes, valid inputs are 'adminsettings', 'usersettings', or 'logout'.") #gives prompt for testing role authorization
        settings = input("Specify settings to change, or logout: ") #input for settings to change or exit value
        if settings == "adminsettings":
            if account == "admin": #checks to see if admin is logged in to change admin settings
                print("Admin settings changed successfully!")
            else:
                print("You are not authorized to change these settings.")
        elif settings == "usersettings": 
            if account == "user": #checks to see if user is logged in to change user settings
                print("User settings changed successfully!")
            else:
                print("You are not authorized to change these settings.")
        elif settings == "logout": #sentinel exit value for leaving the authorization loop
            print("Logged out successfully.")
            loggedIn = False
        else:
            print("Invalid setting to change.")

