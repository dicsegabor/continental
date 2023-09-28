import json
import yaml


class Log(object):
    def __init__(self, path):
        with open(path, "r") as f:
            data = json.load(f)

        self.Timestamp = data["Timestamp"]
        self.Actual_Vehicle_Speed = data["Actual_Vehicle_Speed"]
        self.Sensor_Input_Ok = data["Sensor_Input_Ok"]
        self.Vehicle_State = data["Vehicle_State"]
        self.CAF_Is_Active = data["CAF_Is_Active"]
        self.CAF_Is_Off_Alert = data["CAF_Is_Off_Alert"]

def open_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)
