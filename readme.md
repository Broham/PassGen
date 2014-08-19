#PassGen
##A targeted password brute force tool

PassGen is intended to take a word suspected as being the base for a password and generate a potential password list using different combinations of capital letters and common substitutions.  For example, say you suspect someone is using their last name, "Smith" as their password.  By executing:
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
Or have the password list sent to your clipboard so you can past it whereve you like using the method below:
```
python passgen.py -c smith
```
Other stuff:
PassGen only substitutes characters for alph characters.  This means that if you includ numbers or symbols, they will not be replaced with any characters.

###Dependencies:
[Requests](http://docs.python-requests.org/en/latest/user/install/#install)
[Pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/)



