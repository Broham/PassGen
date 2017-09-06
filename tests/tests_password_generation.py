"""Tests for the password generation functions."""
import unittest
from substitute import fullSub
from substitute import basicSub
from substitute import appendNumbers

class PasswordGenerationTest(unittest.TestCase):
  def test_basic_passwords(self):
    passwords = basicSub('smith')
    self.assertEqual(76, len(passwords))
    self.assertEqual('smith1', passwords[0])
    self.assertEqual('5mith?', passwords[75])

  def test_full_passwords(self):
    passwords = fullSub('smith')
    self.assertEqual(672, len(passwords))
    self.assertEqual('smith', passwords[0])
    self.assertEqual('5M!7#', passwords[671])

  def test_password_with_numbers(self):
    passwords = appendNumbers('smith')
    self.assertEqual(44440, len(passwords))
    self.assertEqual('smith1', passwords[0])
    self.assertEqual('5mith0000', passwords[44439])
