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


3. 
Problem:
Solution:
Reason: