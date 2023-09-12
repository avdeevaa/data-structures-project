import unittest

from src.stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push('data1')
        self.assertIsNone(self.stack.push('data2'))

    def test_pop(self):
        self.stack.push('data1')
        self.assertEqual(self.stack.pop(), "data1")

    def test_str(self):
        self.assertEqual(self.stack.__str__(), None)


if __name__ == '__main__':
    unittest.main()
