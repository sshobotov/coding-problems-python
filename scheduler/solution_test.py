import unittest
from .solution import Scheduler


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.was_executed = False

        def fn1():
            self.was_executed = False

        def fn2():
            self.was_executed = True

        instance = Scheduler()
        instance.schedule(fn1, 50)
        instance.schedule(fn2, 150)
        instance.schedule(fn1, 100)
        instance.run()

        self.assertEqual(True, self.was_executed)


if __name__ == '__main__':
    unittest.main()
