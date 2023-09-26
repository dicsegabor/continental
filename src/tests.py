import unittest
from utils import Log
from parameterized import parameterized


class TestCAF(unittest.TestCase):
    @parameterized.expand(
        [
            ("../logs/tca_1_log.json", True),
            ("../logs/tca_2_log.json", False),
        ]
    )
    def test_caf_activation(self, log_path, outcome):
        log = Log(log_path)
        self.assertEqual(outcome, log.CAF_Is_Active)
