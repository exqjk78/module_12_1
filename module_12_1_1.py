import module_12_1 as runn
import unittest
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = runn.Runner('78')
        for walk in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = runn.Runner('37')
        for run_ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = runn.Runner('Макар')
        runner_4 = runn.Runner('Вика')
        for run_ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)