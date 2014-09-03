#PassGen
##A targeted password brute force tool

PassGen is intended to generate a potential password list for a target word using different combinations of capital letters and common substitutions.  It can also be used to make HTTP requests to see if any passwords from the list are valid.

Complete list of options:
- no options : generates a password list by replaceing the first character of the password and appending an extra character to the end.
- -f : generate a full password list.  This can make the password list quite lengthy.
- -n : generate a password list the appends 4 digit numbers to the end of the target password.
- -o : output file name
- -t : HTTP request target (example: http://mysite.com/login)
- -d : HTTP parameters (example: email=abe@test.com,password={0}).  The {0} specifies where the password will be inserted into the data.
- -g : Text to search for in the HTTP response.  Use this to determine when a password has worked.
- -n : Append numbers flag.  Appends the numbers 0-9999 to the end of all passwords
- -c : Copy to clipboard flag.  Copys results to the clipboard

##Examples:
###Basic Usage:
Generates a password list by replaceing the first character of the target password and appending an extra character to the end.

```
python passgen.py smith
```
###Passwords with numbers:
Generates a large number of potential passwords by replace the first character and appending a 4 digit number from 0-9999 to the end of the target password.

```
python passgen.py -n smith
```

###Full password list:
Genearates a large number of potential passwords by generating a list of every combination of replacement passwords

```
python passgen.py -f smith
```

###Basic password list used to make HTTP requests
Create a basic password list and uses it to make login requests.  If it finds the text "success" in the response it will say which password worked and exit.  Notice that ```&``` must be replaced with ```\&``` in the command line.

```
python passgen.py -t http://myTestSite.com/login -d email=smith@test.com\&password={0} -g success smith
```

Other stuff:
PassGen only substitutes characters for alpha characters.  This means that if you include numbers or symbols, they will not be replaced with any characters.

###Dependencies:
- [Requests](http://docs.python-requests.org/en/latest/user/install/#install)
- [Pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/)



