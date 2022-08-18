from unittest import TestCase

from project.src.entities.User import User

SURNAME_2 = "Surname2"

S = "surname1"

PASSWORD = "Pwd"
SURNAME_1 = "Surname1"
NAME = "Name"
USER_CODE = "Test"


def create_user():
    user = User(USER_CODE, NAME, SURNAME_1, PASSWORD)
    return user


class TestUser(TestCase):
    """
    Unit test class for user object
    """

    def test_getters(self):
        user = create_user()

        self.assertEqual(user.get_user_code(), USER_CODE)
        self.assertEqual(user.get_name(), NAME)
        self.assertEqual(user.get_user_code(), USER_CODE)
        self.assertEqual(user.get_user_code(), USER_CODE)

    def test_set_user_code(self):
        new_user_code = "NewUserCode"

        user = create_user()
        user.set_user_code(new_user_code)

        self.assertEqual(user.get_user_code(), new_user_code)

    def test_set_surnames_with_only_one_surname(self):
        user = create_user()
        user.set_surnames(SURNAME_1 + "1")

        self.assertEqual(user.get_surnames(), SURNAME_1 + "1")

    def test_set_surnames_with_two_surname(self):
        user = create_user()
        user.set_surnames(SURNAME_1 + "1", SURNAME_2)

        self.assertEqual(user.get_surnames(), SURNAME_1 + "1 " + SURNAME_2)

    def test_set_surnames_with_two_surname_but_second_empty(self):
        user = create_user()
        user.set_surnames(SURNAME_1 + "1", "")

        self.assertEqual(user.get_surnames(), SURNAME_1 + "1")

    def test_set_pwd(self):
        new_pwd = "NewPwd"

        user = create_user()
        user.set_pwd(new_pwd)

        self.assertEqual(user.get_pwd(), new_pwd)

    def test_set_name(self):
        new_name = "NewName"

        user = create_user()
        user.set_name(new_name)

        self.assertEqual(user.get_name(), new_name)
