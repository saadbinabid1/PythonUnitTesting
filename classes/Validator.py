class Validator:

    def user_name_isValid(self, username):

        if len(username) > 10:
            return False

        if ' ' in username:
            return False

        if username.islower():
            return False

        return True

    def password_isValid(self,password):
        if len(password) > 15:
            return False
        return True

    def password_isValid_SpecialChar(self, password):
        special_character = "!@#$%&_="
        if any(char in special_character for char in password):
            return False
        return True
