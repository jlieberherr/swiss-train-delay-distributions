#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import unittest

from settings import init_logging, get_path_to_output

log = logging.getLogger(__name__)


class TestCase(unittest.TestCase):
    def test_something(self):
        init_logging(get_path_to_output(), "test.log")
        log.info("a log entry")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
