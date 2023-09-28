import unittest
from utils import Log, open_json
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

    @parameterized.expand(
        [
            (
                "Normal behaviour",
                "../logs/tca_1_log.json",
                [False, True],
            ),
        ],
    )
    def test_caf_activation(self, _, log_path, outcomes):
        for i, data in enumerate(open_json(log_path)):
            log = Log(data)
            self.assertEqual(outcomes[i], log.CAF_Is_Active)
