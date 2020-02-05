import unittest

from .solution import solve


class SolutionTestCase(unittest.TestCase):
    def test_solve(self):
        solution = solve([
            "AbsentNameResolver",
            "AntiBlueStrStrangeName",
            "AbAbsolutelyRandomManager",
            "MyAngularBiStreamAndAnomalyDetector",
        ], "abstranam")

        self.assertListEqual(solution, [
            "AntiBlueStrStrangeName",
            "MyAngularBiStreamAndAnomalyDetector",
        ])


if __name__ == '__main__':
    unittest.main()
