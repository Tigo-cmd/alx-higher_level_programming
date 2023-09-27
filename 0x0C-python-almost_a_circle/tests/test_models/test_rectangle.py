#!/usr/bin/python3
"""This module uses the unittest to test the rectangle class"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

if __name__ == '__main__':
    class TestRectangle_Class(unittest.TestCase):
        def test_new_rect_instance(self):
            r = Rectangle(2, 6)
            self.assertEqual(r.width, 2)
            self.assertEqual(r.height, 6)
            self.assertEqual(r.x, 0)
            self.assertEqual(r.y, 0)
            self.assertEqual(r.id, 1)

        def test_new_rect_with_custom_id(self):
            r = Rectangle(5, 10, 0, 0, 100)
            self.assertEqual(r.id, 100)

        def test_new_rect_with_negative_width(self):
            with self.assertRaises(ValueError):
                Rectangle(-5, 10)

        def test_new_rectan_with_negative_height(self):
            with self.assertRaises(ValueError):
                Rectangle(5, -10)

        def test_create_new_rectangle_with_negative_x(self):
            with self.assertRaises(ValueError):
                Rectangle(5, 10, -2)

        def test_create_new_rectangle_with_negative_y(self):
            with self.assertRaises(ValueError):
                Rectangle(5, 10, 0, -3)

        def test_area_method(self):
            r = Rectangle(5, 10)
            self.assertEqual(r.area(), 50)

        def test_update_with_args(self):
            r = Rectangle(5, 10)
            r.update(10)
            self.assertEqual(r.id, 10)

        def test_update_with_kwargs(self):
            r = Rectangle(5, 10)
            r.update(width=20, height=30, x=2, y=3)
            self.assertEqual(r.width, 20)
            self.assertEqual(r.height, 30)
            self.assertEqual(r.x, 2)
            self.assertEqual(r.y, 3)

        def test_to_dictionary_method(self):
            r = Rectangle(5, 10, 2, 3, 100)
            expected_dict = {'id': 100, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
            self.assertDictEqual(r.to_dictionary(), expected_dict)


    class TestRectangle_stdout(unittest.TestCase):
        @staticmethod
        def capture_stdout(rect, method):
            """returns text printed to  output.
            """
            capture = io.StringIO()
            sys.stdout = capture
            if method == "print":
                print(rect)
            else:
                rect.display()
            sys.stdout = sys.__stdout__
            return capture

        def test_str_method_print_width_height(self):
            r = Rectangle(4, 6)
            capture = TestRectangle_stdout.capture_stdout(r, "print")
            correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
            self.assertEqual(correct, capture.getvalue())

        def test_display_width_height(self):
            r = Rectangle(2, 3, 0, 0, 0)
            capture = TestRectangle_stdout.capture_stdout(r, "display")
            self.assertEqual("##\n##\n##\n", capture.getvalue())
