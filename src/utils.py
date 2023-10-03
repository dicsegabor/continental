from json import load, dumps
from typing import Self


def open_json(path: str):
    with open(path, "r") as f:
        return load(f)


class Record:
    def __init__(
        self,
        timestamp: int,
        actual_vehicle_speed: int,
        sensor_input_ok: bool,
        vehicle_state: int,
        caf_is_active: bool,
        caf_is_off_alert: int,
    ) -> None:
        self.Timestamp = timestamp
        self.Actual_Vehicle_Speed = actual_vehicle_speed
        self.Sensor_Input_Ok = sensor_input_ok
        self.Vehicle_State = vehicle_state
        self.CAF_Is_Active = caf_is_active
        self.CAF_Is_Off_Alert = caf_is_off_alert

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(
            data["Timestamp"],
            data["Actual_Vehicle_Speed"],
            data["Sensor_Input_Ok"],
            data["Vehicle_State"],
            data["CAF_Is_Active"],
            data["CAF_Is_Off_Alert"],
        )


def log_to_records(path: str) -> list[Record]:
    data = open_json(path)
    return [Record.from_dict(r) for r in data]


# wanted to use this for data generation, then I understood the assignment
def records_to_json(log: list[Record]) -> str:
    return dumps([r.__dict__ for r in log])
