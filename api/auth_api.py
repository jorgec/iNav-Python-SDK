from core.api_manager import APIManager
from core.constants import LOGIN_URL
from models.user_models import UserModel


class AuthAPI(APIManager):
    user_data: UserModel = None

    def __init__(self):
        super().__init__()
        self.user_data = UserModel()

    def login(self, username: str, password: str) -> UserModel:
        url = LOGIN_URL
        payload = {
            "UserName": username,
            "Password": password
        }

        result = self.execute(url=url, payload=payload, auth=False)

        if result.json().get('ErrorCode', None) == '0':
            login_user = result.json().get('Content').get('LoginUser')
            for key, field in UserModel.Meta.fields.items():
                setattr(self.user_data, field, login_user.get(key, ''))

        return self.user_data
