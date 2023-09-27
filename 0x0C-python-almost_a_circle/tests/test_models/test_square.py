#!/usr/bin/python3
"""This module test the square class using the unitest module"""


import io
import sys
import unittest
from models.base import Base
from models.square import Square


if __name__ == "__main__":
    class TestSquare(unittest.TestCase):

        def test_is_base(self):
            self.assertIsInstance(Square(10), Base)

        def test_is_rectangle(self):
            self.assertIsInstance(Square(10), Square)

        def test_size_private(self):
            with self.assertRaises(AttributeError):
                print(Square(10, 2, 3, 4).__size)

        def test_None_size(self):
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(None)

        def test_str_size(self):
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square("invalid")

        def test_float_size(self):
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(5.5)

        def test_complex_size(self):
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(complex(5))

        def test_negative_size(self):
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Square(-1, 2)

        def test_area(self):
            self.assertEqual(100, Square(10, 0, 0, 1).area())

        def test_update_args(self):
            s = Square(10, 10, 10, 10)
            s.update()
            self.assertEqual("[Square] (10) 10/10 - 10", str(s))

        def test_update_kwargs_one(self):
            s = Square(10, 10, 10, 10)
            s.update(id=1)
            self.assertEqual("[Square] (1) 10/10 - 10", str(s))

        def test_to_dictionary(self):
            s = Square(10, 2, 1, 1)
            correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
            self.assertDictEqual(correct, s.to_dictionary())


    class TestSquare_stdout(unittest.TestCase):
        @staticmethod
        def capture_stdout(sq, method):
            """returns text printed to standard output.
            """
            capture = io.StringIO()
            sys.stdout = capture
            if method == "print":
                print(sq)
            else:
                sq.display()
            sys.stdout = sys.__stdout__
            return capture

        def test_str_method_print_size(self):
            s = Square(4)
            capture = TestSquare_stdout.capture_stdout(s, "print")
            correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
            self.assertEqual(correct, capture.getvalue())

        def test_display_size(self):
            s = Square(2, 0, 0, 9)
            capture = TestSquare_stdout.capture_stdout(s, "display")
            self.assertEqual("##\n##\n", capture.getvalue())
