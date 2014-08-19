#PassGen
##A targeted password brute force tool

PassGen is intended to generate a potential password list for a target word using different combinations of capital letters and common substitutions.  For example, say you suspect someone is using their last name, "Smith" as their password.  By executing:
```
python passgen.py smith
```
You would generate 672 potential passwords in the format shown in the partial list below:
```
smith
smitH
smit#
smiTh
.
.
.
5M!+#
5M!7h
5M!7H
5M!7#
```
You can also output password lists to a file using the method below:

```
python passgen.py -o outputFile.txt smith
```
Or have the password list sent to your clipboard so you can paste it wherever you like using the method below:
```
python passgen.py -c smith
```

Complete list of options:
-o : output file name
-t : HTTP request target (example: http://mysite.com/login)
-d : HTTP parameters (example: email=abe@test.com,password={0})
-n : Append numbers flag.  Appends the numbers 0-9999 to the end of all passwords
-e : Extra character flag.  Appends 1 of the characters commonly used to meet password complexity requirements to all passwords
-c : Copy to clipboard flag.  Copys results to the clipboard

Other stuff:
PassGen only substitutes characters for alpha characters.  This means that if you include numbers or symbols, they will not be replaced with any characters.

###Dependencies:
- [Requests](http://docs.python-requests.org/en/latest/user/install/#install)
- [Pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/)



