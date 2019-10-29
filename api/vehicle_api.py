from typing import Union, List

from core.api_manager import APIManager
from core.constants import GET_VEHICLES_URL, GET_GPS_INFO_URL
from models.vehicle_models import VehicleModel, VehicleGPSModel


class VehicleAPI(APIManager):
    def __init__(self, user_id: str):
        super().__init__(user_id=user_id)

    def get_vehicles(self) -> Union[List, VehicleModel]:
        data = []

        url = GET_VEHICLES_URL

        result = self.execute(url=url, payload={})
        if result.json().get('ErrorCode', None) == '0':
            try:
                vehicle_data = result.json().get('Content').get('GroupData')[0].get('VehicleData')
            except IndexError:
                vehicle_data = []
            except KeyError:
                vehicle_data = []
            except AttributeError:
                vehicle_data = []

            for item in vehicle_data:
                vehicle = VehicleModel()
                for key, field in VehicleModel.Meta.fields.items():
                    setattr(vehicle, field, item.get(key, ''))
                data.append(vehicle)

        return data

    def get_gps_data(self):
        data = []

        url = GET_GPS_INFO_URL
        result = self.execute(url=url, payload={})
        if result.json().get('ErrorCode', None) == '0':
            try:
                gps_data = result.json().get('Content')
            except KeyError:
                gps_data = []
            except AttributeError:
                gps_data = []

            for item in gps_data:
                vehicle_gps = VehicleGPSModel()
                for key, field in VehicleGPSModel.Meta.fields.items():
                    setattr(vehicle_gps, field, item.get(key, ''))
                data.append(vehicle_gps)

        return data
