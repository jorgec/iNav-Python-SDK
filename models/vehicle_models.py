from typing import List

from models.datamodel import DataModel


class VehicleModel(DataModel):
    simcode: str = ""
    vehicle_id: str = ""
    vehicle_name: str = ""
    driver_name: str = ""
    track_type: str = ""
    track_id: str = ""

    class Meta:
        fields = {
            "SIMCode": "simcode",
            "VehicleID": "vehicle_id",
            "VehicleName": "vehicle_name",
            "DriverName": "driver_name",
            "TrackType": "track_type",
            "TrackID": "track_id",
        }

    def __str__(self):
        return self.vehicle_name


class VehicleGPSModel(DataModel):
    simcode: str = ""
    lat: str = "0.0"
    lon: str = "0.0"
    acc: str = ""
    camera_url: str = ""
    vehicle_name: str = ""
    track_type: str = ""
    camera_time: str = ""
    direction: str = ""
    status_jt: str = ""
    today_mileage: str = ""
    status: str = ""
    fuel_percent: str = ""
    temperature: str = ""
    fuel_liter: str = ""
    valid: str = ""
    track_id: str = ""
    gps_time: str = ""
    addr: str = ""
    extends: List = list
    gps_last_located_time: str = ""
    speed: str = ""
    online: str = ""
    gps_time_desc: str = ""

    class Meta:
        fields = {
            "SIMCode": "simcode",
            "Lng": "lat",
            "Lat": "lon",
            "ACC": "acc",
            "CameraUrl": "camera_url",
            "VehicleName": "vehicle_name",
            "TrackType": "track_type",
            "CameraTime": "camera_time",
            "Direction": "direction",
            "StatusJT": "status_jt",
            "TodayMileage": "today_mileage",
            "Status": "status",
            "FuelPercent": "fuel_percent",
            "Mileage": "temperature",
            "Temperature": "fuel_liter",
            "FuelLiter": "valid",
            "Valid": "track_id",
            "TrackID": "gps_time",
            "GPSTime": "addr",
            "Addr": "extends",
            "Extends": "gps_last_located_time",
            "GPSLastLocatedTime": "speed",
            "Speed": "online",
            "usageTime": "gps_time_desc",
        }

    def __str__(self):
        return self.vehicle_name
