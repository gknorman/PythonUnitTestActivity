import unittest
import sys
import os


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from classes.validator import Validator

class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_it_will_reject_username_if_too_long(self):
        # Assume
        username = 'InvalidTooLong'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_white_space_present(self):
        # Assume
        username = 'Rev al'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_there_is_no_uppercase_characters(self):
        # Assume
        username = 'reval'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_accept_a_valid_username(self):
        # Assume
        username = 'Reval'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertTrue(result)
        
    def test_it_will_reject_username_if_there_is_a_special_character(self):
        # Assume
        username = 'Reval$%^&*()#@'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)