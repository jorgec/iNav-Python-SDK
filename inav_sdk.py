from api import AuthAPI, VehicleAPI


class INavSDK:
    api = None
    user_id: str = None

    def set_keys(self, user_id: str) -> None:
        self.user_id = user_id

    def auth(self) -> AuthAPI:
        self.api = AuthAPI()
        return self.api

    def vehicle(self) -> VehicleAPI:
        self.api = VehicleAPI(user_id=self.user_id)
        return self.api
