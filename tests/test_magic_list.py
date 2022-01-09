
from dataclasses import dataclass
from magic_list.magic_list import MagicList
from unittest import TestCase


class TestMagicList(TestCase):
        
    def test_default_list(self):
        a = MagicList()
        
        # init
        a[0] = 1
        a[1] = 2
        self.assertEqual(a[0], 1)
        self.assertEqual(a[1], 2)
        
        #update
        a[0] = 100
        a[1] = 102
        self.assertEqual(a[0], 100)
        self.assertEqual(a[1], 102)
        
        # index error on get
        with self.assertRaises(IndexError):
            _ = a[100]

        # index error on set
        with self.assertRaises(IndexError):
            a[7] = 100

    def test_custom_type(self):
        
        @dataclass
        class Person:
            age: int = 1

        a = MagicList(cls_type=Person)
        
        # init        
        a[0] = 1
        a[1] = 2
        self.assertEqual(a[0].age, 1)
        self.assertEqual(a[1].age, 2)

        # update
        a[0] = 120
        a[1] = 121
        self.assertEqual(a[0].age, 120)
        self.assertEqual(a[1].age, 121)

        # index error on get
        with self.assertRaises(IndexError):
            _ = a[100].age

        # index error on set
        with self.assertRaises(IndexError):
            a[100] = 100
