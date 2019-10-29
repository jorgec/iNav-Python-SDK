import unittest
from .keys import username, password, user_id
from models.user_models import UserModel
from faker import Faker

from inav_sdk import INavSDK


class AuthTest(unittest.TestCase):
    def test_auth(self):
        inav = INavSDK()

        auth = inav.auth().login(username=username, password=password)

        assert auth.username == username
        assert auth.password == password
