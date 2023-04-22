#!/usr/bin/python3

"""defines unittest for base.py
   
   Unittest classes
     TestBase_instance
     TestBase_save_to_file
     TestBase_from_json_to_string
     TestBase_create
     TestBase_load_from_file
     TestBase_save_to_file
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instance(unittest.TestCase):
    """unittest to test instance of:
       Base class
    """

    def test_num_arg(self):
        Ba = Base()
        Bb = Base()
        self.assertEqual(Ba.id, Bb.id - 1)

    def test_more_bases(self):
        Ba = Base()
        Bb = Base()
        Bc = Base()
        self.assertEqual(Ba.id, Bc.id - 2)

    def test_special_id(self):
        self.assertEqual(6, Base(6).id)

    def test_str_id(self):
        self.assertEqual("string", Base("string").id)

class TestBase_to_json_string(unnittest.TestCase):
    """unittestfor json to string method;
      Base class
    """

    def test_json_string_square_type(self0:
            s = square(10, 2, 4, 8)
            self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])) == 39)
