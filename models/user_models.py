from models.datamodel import DataModel


class UserModel(DataModel):
    user_level: str = ""
    device_token: str = ""
    expire_time_desc: str = ""
    password: str = ""
    expire_time: str = ""
    client_id: str = ""
    client_name: str = ""
    username: str = ""
    user_id: str = ""
    login_token: str = ""

    class Meta:
        fields = {
            "UserLevel": 'user_level',
            "DeviceToken": 'device_token',
            "ExpireTimeDesc": 'expire_time_desc',
            "Password": 'password',
            "ExpireTime": 'expire_time',
            "ClientID": 'client_id',
            "ClientName": 'client_name',
            "UserName": 'username',
            "UserID": 'user_id',
            "LoginToken": 'login_token',
        }
