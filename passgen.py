import sys
import itertools
import getopt
import requests
import pyperclip

#dictionary containing substitutions
subDict = {
	'a': ['a','A','@','4'],
	'b': ['b','B','8','6'],
	'c': ['c','C','[','{','(','<'], 
	'd': ['d','D',], 
	'e': ['e','E','3'], 
	'f': ['f','F'], 
	'g': ['g','G','6','9'], 
	'h': ['h','H','#'], 
	'i': ['i','I','1','l','L','|','!'], 
	'j': ['j','J'], 
	'k': ['k','K'], 
	'l': ['l','L','i','I','|','!','1'], 
	'm': ['m','M'], 
	'n': ['n','N'], 
	'o': ['o','O','0','Q'], 
	'p': ['p','P'], 
	'q': ['q','Q','9','0','O'], 
	'r': ['r','R'], 
	's': ['s','S','$','5'], 
	't': ['t','T','+','7'], 
	'u': ['u','U','v','V'], 
	'v': ['v','V','u','U'], 
	'w': ['w','W'], 
	'x': ['x','X','+'], 
	'y': ['y','Y'], 
	'z': ['z','Z','2'], 
}
#characters commonly appended to passwords to meet complexity requirements
dummyCharacters = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','?']

#used to generate 4 digit number to append to passwords
numbersOnly = ['1','2','3','4','5','6','7','8','9','0']

#get the password and options from the command line
opts, args = getopt.getopt(sys.argv[1:], ':o:t:d:nec')
# print opts
# print args
password = args[0]

#place substitution sets into the letters array
letters = []
for i,val in enumerate(password):
	if val in subDict.keys():
		letters.append(subDict[val])
	else:
		letters.append(val)

outputFile = ''
target = '' 
data = ''
appendNumbers = False
copy = False

for opt, arg in opts:
	if opt == "-o": #output file
		outputFile = arg
	elif opt == "-t": #target of the POST request
		target = arg
	elif opt == "-d": #data for the POST requet
		data = arg
	elif opt == "-c": #copy output to the clipboard
		copy = True
	elif opt == "-e": #append extra character
		letters.append(dummyCharacters)
	elif opt == "-n": #append 4 digit numbers to end
		numberCombinations = itertools.product(numbersOnly, numbersOnly, numbersOnly, numbersOnly)
		print "append all 4 digit combinations of the number list"
print outputFile, target, data, appendNumbers

#pass the letters array of arrays to get the cartesian product
passwords = itertools.product(*letters)

#save passwords to file
if outputFile != '':
	f = open(outputFile, 'w')
	for password in passwords:
		f.write("".join(password) + '\n')
	f.close()
#copy passwords to clipboard
elif copy:
	pwList = ''
	i=0
	for password in passwords:
		i+=1
 		pwList += "".join(password) + '\n'
 	print `i` + " passwords copied to the clipboard."
	pyperclip.copy(pwList)
#make request using passwords
elif target != '' and data != '':
	print "Error - make request not implemented"
	# r = requests.post(target)
else:
	i = 0
	for password in passwords:
		i+=1
		print "".join(password)
	print `i` + " passwords generated."


