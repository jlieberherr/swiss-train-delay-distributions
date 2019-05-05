#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from scripts.preprocessing import run_preprocessing


class TestCase(unittest.TestCase):
    def test_something(self):
        run_preprocessing()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
