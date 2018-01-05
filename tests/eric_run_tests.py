# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2018-01-03 18:23:31
# @Last Modified time: 2018-01-05 14:51:15
"""Run tests.

File for running all tests.
"""
from eric_config import log
# Pyfancy — output color highighting
# Disabled green background, because bad color in AppVeyor
# https://github.com/appveyor/ci/issues/1138#issuecomment-355525721
from pyfancy import pyfancy
# If I import variables, Python run all tests.
# I one of tests is false, Python run all tests → exit with code 1. Not
# exit after each error.
# a_encoding, not encoding, because encoding test need to run before the rest
from eric_a_encoding import encoding_failure_tests
from eric_asterisks import asterisks_failure_tests
from eric_body import body_failure_tests
from eric_head import head_failure_tests
# [Bug] Disable, because check as errors all latin symbols,
# see: https://github.com/myint/language-check/issues/50
# from eric_languagetool import languagetool_failure_tests


if encoding_failure_tests or body_failure_tests \
        or head_failure_tests or asterisks_failure_tests is True:
    exit(1)
else:
    log.notice(pyfancy().green().bold(
        "Congratulations! You haven't errors in your packages!"))
