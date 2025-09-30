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
Solution:
Reason:

https://owasp.org/Top10/A03_2021-Injection/