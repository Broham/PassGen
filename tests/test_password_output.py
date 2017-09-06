import sys
import os
import unittest
import pyperclip
from passgen import writePasswordsToClipboard
from passgen import writePasswordsToFile

class PasswordOutputTest(unittest.TestCase):

  passwords = ['password1', 'password2', 'password3']
  passwordData = 'password1\npassword2\npassword3\n'
  fileName = 'test_passwords.txt'
  def test_write_to_file(self):
    writePasswordsToFile('test_passwords.txt',self.passwords)
    with open('test_passwords.txt', 'r') as myfile:
      data=myfile.read()
      self.assertEqual(data,self.passwordData)

  def test_write_to_clipboard(self):
    writePasswordsToClipboard(self.passwords)
    self.assertEqual(pyperclip.paste(), self.passwordData)

  @classmethod
  def tearDownClass(self):
    os.remove(self.fileName)
