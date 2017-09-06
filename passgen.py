import sys
import requests
import getopt
import pyperclip
from substitute import fullSub
from substitute import basicSub
from substitute import appendNumbers
import argparse


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

parser = argparse.ArgumentParser()

if __name__ == '__main__':
	parser.add_argument("-o", "--outputFile", help="The file that the password list will be written to.")
	parser.add_argument("-f", "--full", help="Full password list flag.  This can generate a very large password", action="store_true")
	parser.add_argument("-c", "--copy", help="Copy password list result to the clipboard.", action="store_true")
	parser.add_argument("-n", "--numbers", help="Append numbers flag.", action="store_true")
	parser.add_argument("-t", "--target", help="The target of the HTTP POST request.")
	parser.add_argument("-d", "--data", help="The data for the post request.")
	parser.add_argument("-g", "--search", help="The text to search for in POST respose that will indicate a successful login.")
	parser.add_argument("password",nargs="*")
	args = parser.parse_args()

	print('args.outputFile',args.outputFile)
	print('args.full',args.full)
	print('args.copy',args.copy)
	print('args.numbers',args.numbers)
	print('args.target',args.target)
	print('args.data',args.data)
	print('args.search',args.search)
	print('args.password',args.password)

	#get the password and options from the command line
	password = args.password[0]

	#load full or basic password list based on arguments passed in
	if args.full:
		passwords = fullSub(password)
	elif args.numbers:
		passwords = appendNumbers(password)
	else:
		passwords = basicSub(password)

	#save passwords to file
	if args.outputFile != None:
		writePasswordsToFile(args.outputFile, passwords)
	#copy passwords to clipboard
	elif args.copy:
		writePasswordsToClipboard(passwords)
	#make request using passwords
	elif args.target != None:
		#make sure all required values were passed in
		if args.data == None:
			print 'You must provide data in order to make a HTTP request.  Example: -d email=test@test.com&password={0}'
			sys.exit()
		elif args.search == None:
			print 'You must specify what text to search for in the response in order to make a HTTP request. Example: -g success:true'
			sys.exit()
		elif args.target == None:
			print 'You must specify a target URL in order to make a HTTP request'
			sys.exit()
		makeRequests(args.target, args.data, passwords,args.search)
	else:
		printPasswords(passwords)
