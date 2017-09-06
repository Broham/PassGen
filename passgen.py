import sys
import requests
import getopt
import pyperclip
from substitute import fullSub
from substitute import basicSub
from substitute import appendNumbers

def printPasswords(passwords):
	for password in passwords:
		print password
	print '%s passwords generated.' % len(passwords)

def writePasswordsToClipboard(passwords):
	pwList = '\n'.join(passwords)
	print '%s passwords copied to the clipboard.' % (len(passwords))
	pyperclip.copy(pwList)

def writePasswordsToFile(outputFile, passwords):
	with open(outputFile, 'w') as f:
		f.write('\n'.join(passwords))
	print '%s passwords written to %s' % (len(passwords), outputFile)
	f.close()

def makeRequests(target, data, passwords, findText):
	print("testing passwords... this may take a while.")
	for password in passwords:
		r = requests.post(target + "?" + data.format(password))
		if findText in r.text:
			print "Match found for password: ", password
			return
	print "No matches found for passwords."

if __name__ == '__main__':

	#get the password and options from the command line
	opts, args = getopt.getopt(sys.argv[1:], ':o:t:d:g:necf')
	print 'opts', opts
	print 'args', args
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
		if opt == '-o': #output file
			outputFile = arg
		if opt == '-f': #generate full password list
			fullFlag = True 
		elif opt == '-t': #target of the POST request
			requestFlag = True
			target = arg
		elif opt == '-d': #data for the POST requet
			requestFlag = True
			data = arg
		elif opt == '-c': #copy output to the clipboard
			copyFlag = True
		elif opt == '-g': #text to be searched for in POST response
			requestFlag = True
			text = arg
		# elif opt == '-e': #append extra character
		# 	letters.append(dummyCharacters)
		elif opt == '-n': #append numbers to end
			numbersFlag = True

	#load full or basic password list based on arguments passed in
	if fullFlag:
		passwords = fullSub(password)
	elif numbersFlag:
		passwords = appendNumbers(password)
	else:
		passwords = basicSub(password)

	#save passwords to file
	if outputFile != '':
		writePasswordsToFile(outputFile, passwords)
	#copy passwords to clipboard
	elif copyFlag:
		writePasswordsToClipboard(passwords)
	#make request using passwords
	elif requestFlag:
		#make sure all required values were passed in
		if data == '':
			print 'You must provide data in order to make a HTTP request.  Example: -d email=test@test.com&password={0}'
			sys.exit()
		elif text == '':
			print 'You must specify what text to search for in the response in order to make a HTTP request. Example: -g success:true'
			sys.exit()
		elif target == '':
			print 'You must specify a target URL in order to make a HTTP request'
			sys.exit()
		makeRequests(target, data, passwords,text)
	else:
		printPasswords(passwords)
