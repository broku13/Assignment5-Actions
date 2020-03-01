import unittest
import task
import random
import math


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        radius = random.randint(1, 10)
        expected = radius * radius * math.pi
        self.assertEqual(expected, task.circle_area(radius))


if __name__ == '__main__':
    unittest.main()