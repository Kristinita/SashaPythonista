# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-03 18:23:31
# @Last Modified time: 2018-01-04 16:21:39
"""Run tests.

File for running all tests.
"""

from eric_config import log
# If I import variables, Python run all tests.
# I one of tests is false, Python run all tests → exit with code 1. Not
# exit after each error.
from eric_asterisks import asterisks_failure_tests
from eric_body import body_failure_tests
from eric_head import head_failure_tests
# [Bug] Disable, because check as errors all latin symbols,
# see: https://github.com/myint/language-check/issues/50
# from eric_languagetool import languagetool_failure_tests


if body_failure_tests or head_failure_tests \
        or asterisks_failure_tests is True:
    exit(1)
else:
    log.notice("Congratulations! You haven't errors in your packages!")
