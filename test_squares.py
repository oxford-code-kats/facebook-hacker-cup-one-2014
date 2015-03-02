import unittest

from squares import parse_inputs, Bounds, get_bounds, is_square, is_filled

class TestSquares(unittest.TestCase):
    
    def test_parse_inputs(self):
        data = ['..##', '..##', '....', '....']
        parsed_data = parse_inputs(data)
        expected_data = [
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(parsed_data, expected_data)

    def test_get_square_bounds(self):
        data = [
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        expected_bounds = Bounds(xmin=2, xmax=3, ymin=0, ymax=1)
        bounds = get_bounds(data)
        self.assertEqual(bounds, expected_bounds)

    def test_is_square(self):
        bounds = Bounds(xmin=2, xmax=3, ymin=0, ymax=1)
        self.assertTrue(is_square(bounds))

    def test_is_not_square(self):
        bounds = Bounds(xmin=1, xmax=3, ymin=0, ymax=1)
        self.assertFalse(is_square(bounds))

    def test_is_square_empty_grid(self):
        bounds = Bounds(xmin=None, xmax=None, ymin=None, ymax=None)
        self.assertFalse(is_square(bounds))

    def test_is_filled(self):
        data = [
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        bounds = Bounds(xmin=2, xmax=3, ymin=0, ymax=1)
        self.assertTrue(is_filled(data, bounds))

    def test_is_filled(self):
        data = [
            [0, 1, 1, 1],
            [0, 1, 0, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 0],
        ]
        bounds = Bounds(xmin=1, xmax=3, ymin=0, ymax=2)
        self.assertFalse(is_filled(data, bounds))