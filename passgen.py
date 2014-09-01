import sys
import getopt
import pyperclip
from substitute import fullSub
from substitute import basicSub
from substitute import appendNumbers
from request import makeRequests


#get the password and options from the command line
opts, args = getopt.getopt(sys.argv[1:], ':o:t:d:g:necf')
# print opts
# print args
password = args[0].lower()

outputFile = ''
target = '' 
data = ''
text = ''
numbersFlag = False
copyFlag = False
fullFlag = False
requestFlag = False

for opt, arg in opts:
	if opt == "-o": #output file
		outputFile = arg
	if opt == "-f": #generate full password list
		fullFlag = True 
	elif opt == "-t": #target of the POST request
		requestFlag = True
		target = arg
	elif opt == "-d": #data for the POST requet
		data = arg
	elif opt == "-c": #copy output to the clipboard
		copyFlag = True
	elif opt == "-g": #text to be searched for in POST response
		text = arg
	# elif opt == "-e": #append extra character
	# 	letters.append(dummyCharacters)
	elif opt == "-n": #append numbers to end
		numbersFlag = True
		print "append all 4 digit combinations of the number list"

#load full or basic password list based on arguments passed in
passwords = fullSub(password) if fullFlag else basicSub(password)
if fullFlag:
	passwords = fullSub(password)
elif numbersFlag:
	passwords = appendNumbers(password)
else:
	passwords = basicSub(password)

#save passwords to file
if outputFile != '':
	f = open(outputFile, 'w')
	for password in passwords:
		f.write("".join(password) + '\n')
	f.close()
#copy passwords to clipboard
elif copyFlag:
	pwList = ''
	i=0
	for password in passwords:
		i+=1
 		pwList += "".join(password) + '\n'
 	print `i` + " passwords copied to the clipboard."
	pyperclip.copy(pwList)
#make request using passwords
elif requestFlag:
	print "Error - make request not implemented"

	payload = {'key1': 'value1', 'key2': 'value2'}
	print target, data, text
	makeRequests(target, data, passwords,text)
else:
	i = 0
	for password in passwords:
		i+=1
		print "".join(password)
	print `i` + " passwords generated."


