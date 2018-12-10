import unittest
from src import sample

class TestSample(unittest.TestCase):

    def test_sample(self):
        """test method for sample
        """
        value1 = 2
        value2 = 6
        expected = 8
        actual = sample.plus(value1, value2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()