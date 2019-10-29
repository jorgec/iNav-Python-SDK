import unittest

from models.vehicle_models import VehicleModel, VehicleGPSModel
from .keys import username, password, user_id

from inav_sdk import INavSDK


class VehicleListTest(unittest.TestCase):
    def test_get_vehicles(self):
        inav = INavSDK()
        inav.set_keys(user_id=user_id)

        vehicles = inav.vehicle().get_vehicles()

        assert len(vehicles) > 0, print(vehicles)
        assert isinstance(vehicles[0], VehicleModel), print(vehicles[0])

    def test_gps(self):
        inav = INavSDK()
        inav.set_keys(user_id=user_id)

        gps_data = inav.vehicle().get_gps_data()

        assert len(gps_data) > 0, print(gps_data)
        assert isinstance(gps_data[0], VehicleGPSModel), print(gps_data[0])
