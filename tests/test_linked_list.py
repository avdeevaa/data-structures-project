"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_beginning(self):
        self.linked_list.insert_beginning({'id': 1})
        self.assertNotEqual(self.linked_list.insert_beginning({'id': 1}), {'id': 2})
        self.assertEqual(self.linked_list.insert_beginning({'id': 1}), None)

    def test_insert_at_end(self):
        self.linked_list.insert_at_end({'id': 2})
        self.assertEqual(self.linked_list.insert_at_end({'id': 2}), None)
        self.assertNotEqual(self.linked_list.insert_at_end({'id': 2}), {'id': 1})

    def test_str(self):
        self.assertEqual(self.linked_list.__str__(), "None")

    def test_get_data_by_id(self):
        self.assertEqual(self.linked_list.get_data_by_id(2),None)

    def test_to_list(self):
        self.linked_list.insert_beginning({'id': 1})
        self.assertEqual(self.linked_list.to_list(), [{'id': 1}])