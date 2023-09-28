from json import load


def open_json(path: str):
    with open(path, "r") as f:
        return load(f)


class Record:
    def __init__(self, data: dict) -> None:
        self.Timestamp = data["Timestamp"]
        self.Actual_Vehicle_Speed = data["Actual_Vehicle_Speed"]
        self.Sensor_Input_Ok = data["Sensor_Input_Ok"]
        self.Vehicle_State = data["Vehicle_State"]
        self.CAF_Is_Active = data["CAF_Is_Active"]
        self.CAF_Is_Off_Alert = data["CAF_Is_Off_Alert"]


def log_to_records(path: str) -> list[Record]:
    data = open_json(path)
    return [Record(r) for r in data]
