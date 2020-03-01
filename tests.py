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

    def test4(self):
        length = random.randint(5, 10)
        temp = []
        first = 0
        last = 0
        for i in range(length):
            randomnum = random.randint(10, 20)
            if i == 0:
                first = randomnum
            elif i == (length - 1):
                last = randomnum
            temp.append(randomnum)
        self.assertEqual((first, last), (task.first_last(temp)))


if __name__ == '__main__':
    unittest.main()
