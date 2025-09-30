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

2. Broken Access Control
