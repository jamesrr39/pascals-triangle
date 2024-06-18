import unittest
import triangle


class MyTestCase(unittest.TestCase):
    def test_get_next_row(self):
        self.assertListEqual([1, 1], triangle.get_next_row([1]), "the second row should be [1,1]")
        self.assertListEqual([1, 6, 15, 20, 15, 6, 1], triangle.get_next_row([1, 5, 10, 10, 5, 1]), "the 6th row should have the correct values")

if __name__ == '__main__':
    unittest.main()
