from models.base import Base
import unittest


class Test_BaseCase(unittest.TestCase):
    """this tests the base.py cases for adequate functionalities"""
    def test_init(self):
        """test the initializing function"""
        start = Base()
        test = Base(2)
        self.assertIsInstance(start, Base)
        self.assertTrue(isinstance(test, Base))
        self.assertEqual(test.id, 2)
        self.assertEqual(start.id, 1)


if __name__ == '__main__':
    unittest.main()
