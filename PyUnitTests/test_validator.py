import unittest

from classes.Validator import Validator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_long_username_reject(self):
        ## Assume
        username = 'InValidTooLong'

        ## Action
        result = self.validator.user_name_isValid(username)

        ## Assertion
        self.assertFalse(result, 'username is too long')

    def test_username_space_reject(self):
        ## Assume
        username = 'InValidhave '

        ## Action
        result = self.validator.user_name_isValid(username)

        ## Assertion
        self.assertFalse(result, 'username has space')

    def test_username_allLower_reject(self):
        ## Assume
        username = 'invalid'

        ## Action
        result = self.validator.user_name_isValid(username)

        ## Assertion
        self.assertFalse(result, 'username has all small characters')

    def test_pwd_longpass_reject(self):
        ## Assume
        pwd = 'blablablablablablablablablabla'

        ##Action
        result = self.validator.password_isValid(pwd)

        ## Assertion
        self.assertFalse(result)

    def test_pwd_specialpwd_reject(self):
        ## Assume
        pwd = 'bla@blablabla'

        ##Action
        result = self.validator.password_isValid_SpecialChar(pwd)

        ## Assertion
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
