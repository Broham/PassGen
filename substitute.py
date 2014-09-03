from itertools import product
from lists import subDict
from lists import dummyCharacters
from lists import numbersOnly

#returns the cartesian product of all replaceable characters 
def fullSub(password):
	letters = []
	#place substitution sets into the letters array
	for i,val in enumerate(password):
		if val in subDict.keys():
			letters.append(subDict[val])
		else:
			letters.append(val)
	return product(*letters)

#returns a list of possible passwords by replacing the first letter with common substitutions and appending numbers and letters to the end
def basicSub(password):
	passwords = []
	middle = password[1:]
	replacements = product(subDict[password[0]], dummyCharacters)
	for val in replacements:
		passwords.append(val[0] + middle + val[1])
	return passwords

#same as basic substitution, but appends 0-9999 to the end 
def appendNumbers(password):
	passwords = []
	middle = password[1:]
	#creates a list of numbers from 0-9999 including values like 0, 00, 000, and 0000
	numCombos = [''.join(p) for n in range(1,5) for p in product(numbersOnly, repeat=n)]
	# print "numbers", numCombos
	replacements = product(subDict[password[0]], numCombos)
	for val in replacements:
		passwords.append(val[0] + middle + val[1])
	return passwords
