#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import unittest

from scripts.preprocessing import run_preprocessing

log = logging.getLogger(__name__)


class TestCase(unittest.TestCase):
    def test_something(self):
        run_preprocessing()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
