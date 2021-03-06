#!/usr/bin/python3
'''UnitTesting  the base module'''


import unittest
import pycodestyle
import os
import inspect
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''this class for testing the base class'''

    def test_pep_style(self):
        '''testing pycodestyle in class Base'''
        style = pycodestyle.StyleGuide()
        check = style.check_files(
            [os.path.abspath(inspect.getsourcefile(Base))])
        self.assertEqual(check.total_errors, 0,
                         'PEP8 style errors: %d' % check.total_errors)

    def test_init_base_obj_1(self):
        '''creating an instance of the class Base with out passing the id'''
        obj = Base()
        obj2 = Base()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_init_base_obj_2(self):
        '''creating an instance of the class Base with specifying the id'''
        obj = Base(123)
        self.assertEqual(obj.id, 123)

    def test_saving_to_file_empty_list(self):
        """Test saving emplty list and loading from empty file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_saving_to_file_None(self):
        """
        Test passing the save_to_file method None and load it
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))


    def test_to_json_string_AND_from_json_string_rec(self):
        '''test the to_json_string and from_json_string methods with the Rectangle class'''
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    def test_to_json_string_AND_from_json_string_sqr(self):
        '''test the to_json_string and from_json_string methods with the Square class'''
        list_input = [
            {'id': 99, 'size': 10},
            {'id': 9, 'size': 1}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    def test_save_to_file_AND_load_from_file(self):
        '''testing save_to_file and load_from_file methods'''
        # testing for the rectangle class
        r1 = Rectangle(5, 3)
        r2 = Rectangle(6, 2)
        list_rectangles_input = [r1, r2]

        # save a file and check f the file is created and is a file
        Rectangle.save_to_file(list_rectangles_input)
        self.assertTrue(os.path.isfile('Rectangle.json'))
        # check if the file is fnot empty
        with open('Rectangle.json', 'r') as f:
            r_total = sum(1 for _ in f)
        self.assertGreater(r_total, 0)

        # load data from the rectangle json file
        list_rectangles_output = Rectangle.load_from_file()
        #check if the objects in the lists are rectangles
        for rect in list_rectangles_input:
            self.assertIsInstance(rect, Rectangle)

        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)

        # now testing for the square class-----------
        s1 = Square(5, 1, 1)
        s2 = Square(2, 2, 2)
        list_squares_input = [s1, s2]

        # save data to file and check if created and is a file
        Square.save_to_file(list_squares_input)
        self.assertTrue(os.path.isfile('Square.json'))

        # check if file is not empty
        with open('Square.json', 'r') as f:
            s_total = sum(1 for _ in f)
        self.assertGreater(s_total, 0)

        # load data from the square json file
        list_squares_output = Square.load_from_file()

        # check if lists have square objects
        for square in list_squares_input:
            self.assertIsInstance(square, Square)

        for square in list_squares_output:
            self.assertIsInstance(square, Square)
