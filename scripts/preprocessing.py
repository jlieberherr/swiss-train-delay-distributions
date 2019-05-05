#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from settings import init_logging, get_path_to_output

log = logging.getLogger(__name__)


def run_preprocessing():
    init_logging(get_path_to_output(), "preprocessing.log")
    log.info("log something")
    return 3


if __name__ == "__main__":
    run_preprocessing()
