import requests
import sys

def makeRequests(target, data, passwords, findText):
	print("testing passwords... this may take a while.")
	for password in passwords:
		r = requests.post(target + "?" + data.format(password))
		if findText in r.text:
			print "Match found for password: ", password
			return
	print "No matches found for passwords."
