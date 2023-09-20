import unittest

from src.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue('data1')
        self.assertNotEqual(self.queue.enqueue('data1'), 'data1')
        self.assertEqual(self.queue.enqueue('data1'), None)

    def test_str(self):
        self.assertEqual(self.queue.__str__(), "")

    def test_dequeue(self):
        self.queue.enqueue('data1')
        self.assertEqual(self.queue.dequeue(), "data1")
        self.assertNotEqual(self.queue.dequeue(), "data1")


if __name__ == '__main__':
    unittest.main()