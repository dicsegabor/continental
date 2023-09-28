import unittest
from utils import Log, open_json
from parameterized import parameterized, parameterized_class


def get_class_name(cls, _, params):
    return "%s_%s" % (
        cls.__name__,
        parameterized.to_safe_name(params["name"]),
    )


@parameterized_class(
    open_json("../project_parameters.json")["projects"],
    class_name_func=get_class_name,
)
class TestCAF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.CAF_Vehicle_Speed_Limit: int
        cls.CAF_TimeOut: int

    @parameterized.expand(
        [
            (0, "../logs/tca_1_log.json", True),
            (1, "../logs/tca_2_log.json", False),
        ],
    )
    def test_caf_activation(self, _, log_path, outcome):
        log = Log(log_path)
        self.assertEqual(outcome, log.CAF_Is_Active)
