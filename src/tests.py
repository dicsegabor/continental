import os
import unittest
from parameterized import parameterized, parameterized_class

from utils import log_to_records, open_json
import HTMLTestRunner


# Naming the generated test classes afer the projects
def get_class_name(cls, _, params):
    return "%s_%s" % (
        cls.__name__,
        parameterized.to_safe_name(params["project_name"]),
    )


@parameterized_class(
    open_json("../project_parameters.json"),
    class_name_func=get_class_name,
)
class TestCAF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # setting up project specific variables
        cls.project_name: str
        cls.CAF_Vehicle_Speed_Limit: int
        cls.CAF_TimeOut: int

        cls.log_dir = "../logs/" + cls.project_name + "/"

        cls.generate_test_data()

    # Maybe for test data generation based on the project settings
    @classmethod
    def generate_test_data(cls):
        pass

    def test_caf_activation(self):
        case_logs_path = self.log_dir + "caf_activation"
        for filename in os.listdir(case_logs_path):
            filename = os.path.join(case_logs_path, filename)
            log = log_to_records(filename)

            r = log.pop(0)
            self.assertLessEqual(r.Actual_Vehicle_Speed, self.CAF_Vehicle_Speed_Limit)
            self.assertTrue(r.Sensor_Input_Ok)
            self.assertEqual(1, r.Vehicle_State)

            r = log.pop(0)
            self.assertTrue(r.CAF_Is_Active)

    def test_caf_false_activation_veichle_speed(self):
        log = log_to_records(
            self.log_dir + "caf_false_activation/case_veichle_speed_log.json"
        )

        for r in log:
            self.assertGreater(r.Actual_Vehicle_Speed, self.CAF_Vehicle_Speed_Limit)
            self.assertFalse(r.CAF_Is_Active)


# needed for report generation
if __name__ == "__main__":
    HTMLTestRunner.main()
