M05 Assignment - OWASP Top 10 Code Fix README
Gabriel Abney

The following sections answer the prompts to identify and explain the
security flaws in the code snippets and explain how my fix addresses
the vulnerability.


1. Broken Access Control
Problem:
The given code always returned the user .json data for the user with 
the specified ID, even if the error was returned.
Solution:
I put the 'res.json(user)' code into an ELSE clause so that the data is 
only returned if no error is sent.
Reason:
Per OWASP recommendations, resources should be denied by default. In initial
code, resources were returned regardless. With my update, resources were
returned only if no error arose.
https://owasp.org/Top10/A01_2021-Broken_Access_Control/


2. Broken Access Control
Problem:
The code get_account function would always return the account information
of whichever id is placed in the URL.
Solution:
My proposed solution would also get a token about the account logged in to
access the URL submitted.  If the user id matched the logged in account, 
then the account information would be returned.  Otherwise, only an error
message would be returned.
Reason:
Per OWASP, resources should be denied by default, and access to information
should only be granted to users with permissions or roles to view that info.
A user should not be able to view someone else's account by inputting the 
other user's account information into the request alone with no other checks.
https://owasp.org/Top10/A01_2021-Broken_Access_Control/


3. Cryptographic Failures
Problem:
The password is encrypted using MD5, an outdated algortithm.  Also, the byte
array is converted to a Hex Binary data type instead of keeping its data type.
Solution:
My solution uses the modern AES encryption algorithm, not an outdated one.
Additionally, I keep the encrypted password in its byte array data type 
when it is passed back.
Reason:
Per OWASP recommendations, deprecated encryption algorithms such as MD5 should
not be used.  Addiionally, keys should be stored in memory as byte arrays.
https://owasp.org/Top10/A02_2021-Cryptographic_Failures/


4. Cryptographic Failures
Problem:
Deprecated encryption algorithm SHA1 is used in hashing.
Solution:
Used superior AES encryption to create hash.
Reason:
Per OWASP guidelines, older deprecated encryption algorithms should be avoided.
https://owasp.org/Top10/A02_2021-Cryptographic_Failures/


5. Injection
Problem:
The query statement is composed on the fly from a string using variables from input.
Solution:
Using a statement preparer, we can create a prepared statement accepting only one unknown
parameter from user input.  This will by compiled by the database before execution and run with 
the one user parameter.
Reason:
Per OWASP, dynamic queries or non-parameterized calls should not be run.  The DBMS 
can compile a prepared statement before execution to provide known structure to 
a query that will not allow additional queries to be appended to a SQL statement.
https://owasp.org/Top10/A03_2021-Injection/


6. Injection
Problem: 
User inputs are accepted without validation/sanitization
Solution:
Use a sanitization method to clean the inputs before use in database
Reason:
Accepting user inputs without sanitization and validation can lead to errors or running hostile code.
https://owasp.org/Top10/A03_2021-Injection/



7. Insecure Design
Problem:
Any user can change any password in the database for any user using the form.
Solution:
Redesigned code to separate the posted form input from the ability to write to database.
Instead, the form should send an email to a user with the email address, where they can 
then reset their password.  This means that only users with access to the email can reset
the associated password.
Reason:
Secure apps need to be designed with security in mind, not just implemented securely.  No matter
how the code was implemented, this program would have allowed any user access to update data that
should be secure within the database.  Password updates need to be only available to users with 
appropriate access.
https://owasp.org/Top10/A04_2021-Insecure_Design/



8.Software and Data Integrity Failures
Problem:
Code uses script libraries sourced from a third party content delivery network.
Solution:
Save a local copy of the scripts to be run on the server, and have the source be internal
directory rather than a third-party host.
Reason:
Using scripts sourced from a third party is risky, as the application has no way of determining
the host of those scripts has been compromised.  Running third-party scripts can cause dangerous
code to be run locally, potentially exposing the user's private data to exfiltration.
https://cwe.mitre.org/data/definitions/830.html



9.Server-Side Request Forgery
Problem:
Initial code snippets accepts any input URL and gets requests from that URL to return.
Solution:
My code sanitizes the inputted URL to prevent redirects and ensure valid format, and 
additionally checks to see that the sanitized URL is in a whitelist of acceptable URLs 
before running.
Reason:
When an external URL is needed as an input to handle some sort of process, that URL needs
to match a basic format for acceptable IPV4/IPV6 address, with no redirects to other sites,
and also that the final sanitized address matches a local whitelist of sites to interact with.
https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html



10. Identification and Authentication Failures
Problem:
No checks on number of brute force login attempts.  Plaintext password is stored locally rather 
than a hash to compare to hash of user inputted password.
Solution:
Inputted password is hashed and compared to a local hash value rather than a plaintext password being stored
locally.  Additionally, number of login attempts is recorded, and login fails if too many recent attempts are
recorded.  Response is generic failure rather than specific about what caused error.
Reason:
Per OWASP recommendations, plaintext passwords should never be stored locally or transmitted unencrypted.  
Additionally, number of failed login attempts in a short time should be limited to prevent brute-force attacks.
https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/