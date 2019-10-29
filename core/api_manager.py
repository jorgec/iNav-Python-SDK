import base64
from typing import Dict

import requests

from core.http_config import HTTP_GET, HTTPConfig, HTTP_POST
from core.http_connection import HTTPConnection


class APIManager:
    user_id: str = None
    http_headers: Dict = None
    encoded_key: str = None
    payload: Dict = {}

    def __init__(
        self,
        user_id: str = None,
    ):
        if user_id:
            self.user_id = user_id
        self.http_headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def auth_with_user_id(self):
        self.payload['UserID'] = self.user_id

    def execute(
        self, url: str, method: str = HTTP_POST, payload: Dict = dict, auth: bool = True
    ) -> requests.Response:
        if auth:
            self.auth_with_user_id()

        if payload:
            data = {**self.payload, **payload}
        else:
            data = self.payload

        http_config = HTTPConfig(url=url, method=method, headers=self.http_headers)
        http_connection = HTTPConnection(config=http_config)

        return http_connection.execute(data=data)
