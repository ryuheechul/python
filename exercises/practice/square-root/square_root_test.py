# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/square-root/canonical-data.json
# File last updated on 2023-07-16

import unittest

from square_root import (
    square_root,
)


class SquareRootTest(unittest.TestCase):
    def test_root_of_1(self):
        self.assertEqual(square_root(1), 1)

    def test_root_of_4(self):
        self.assertEqual(square_root(4), 2)

    def test_root_of_25(self):
        self.assertEqual(square_root(25), 5)

    def test_root_of_81(self):
        self.assertEqual(square_root(81), 9)

    def test_root_of_196(self):
        self.assertEqual(square_root(196), 14)

    def test_root_of_65025(self):
        self.assertEqual(square_root(65025), 255)
