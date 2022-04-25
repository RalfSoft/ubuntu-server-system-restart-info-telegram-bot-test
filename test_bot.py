import unittest
from bot import test

class TestStringMethods(unittest.TestCase):

    def test1(self):
        testString = test()
        self.assertEqual(testString, 'test')

if __name__ == '__main__':
    unittest.main()