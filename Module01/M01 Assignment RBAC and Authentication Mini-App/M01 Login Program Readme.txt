This is the README for the SDEV 245 M01 Authentication Mini App by Gabriel Abney

This program allows the user to input a username and password, 
then checks if those inputs are valid user credentials.  If login
is successful, prompts the user to change settings and checks to see
if the user is authorized to change those settings.

Please be sure to read the prompts within the print statements of the program if you get stuck.
Login credentials for admin: username = 'admin' and password = 'adminPW'
Login credentials for user: username = 'user' and password = 'userPW'
Authorized settings inputs for admin: 'adminsettings' and 'logout'
Authorized settings inputs for user: 'usersettings' and 'logout'

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

