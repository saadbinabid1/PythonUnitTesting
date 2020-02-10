import unittest

from classes.Validator import Validator


class MyTestCase(unittest.TestCase):
    def test_long_username_reject(self):
        ## Assume
        username = 'InValidTooLong'
        validator = Validator()

        ## Action
        result = validator.user_name_isValid(username)

        ## Assertion
        self.assertFalse(result, 'username is too long')

    def test_username_space_reject(self):
        ## Assume
        username = 'InValidhave '
        validator = Validator()

        ## Action
        result = validator.user_name_isValid(username)

        ## Assertion
        self.assertFalse(result, 'username has space')

    def test_username_allLower_reject(self):
        ## Assume
        username = 'invalid'
        validator = Validator()

        ## Action
        result = validator.user_name_isValid(username)

        ## Assertion
        self.assertFalse(result, 'username has all small characters')


if __name__ == '__main__':
    unittest.main()
