import unittest
from utils import Log, open_yaml
from parameterized import parameterized, parameterized_class


def get_class_name_single(cls, _, params_dict):
    return "%s_%s" % (cls.__name__, parameterized.to_safe_name(params_dict['project_name']))


@parameterized_class(
    [
        {'project_name': 'StarInTheCircle'},
        {'project_name': 'BlueAndWhiteCircle'},
    ],
    classname_func=get_class_name_single
)
class TestCAF(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.project_name: str

        proj_pars = open_yaml('../project_parameters.yaml')

        cls.CAF_Vehicle_Speed_Limit = proj_pars[cls.project_name]['CAF_Vehicle_Speed_Limit']
        cls.CAF_TimeOut = proj_pars[cls.project_name]['CAF_TimeOut']

    @parameterized.expand(
        [
            ("../logs/tca_1_log.json", True),
            ("../logs/tca_2_log.json", False),
        ]
    )
    def test_caf_activation(self, log_path, outcome):
        log = Log(log_path)
        self.assertEqual(outcome, log.CAF_Is_Active)
