import unittest
from utils import log_to_records, open_json
from parameterized import parameterized, parameterized_class


# Naming the generated test classes afer the projects
def get_class_name(cls, _, params):
    return "%s_%s" % (
        cls.__name__,
        parameterized.to_safe_name(params["name"]),
    )


@parameterized_class(
    open_json("../project_parameters.json"),
    class_name_func=get_class_name,
)
class TestCAF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.CAF_Vehicle_Speed_Limit: int
        cls.CAF_TimeOut: int

    def test_correct_behaviour(self):
        log = log_to_records("../logs/correct_behaviour_log.json")

        r = log[0]
        self.assertLessEqual(r.Actual_Vehicle_Speed, self.CAF_Vehicle_Speed_Limit)
        self.assertTrue(r.Sensor_Input_Ok)
        self.assertEqual(1, r.Vehicle_State)

        r = log[1]
        self.assertTrue(r.CAF_Is_Active)
