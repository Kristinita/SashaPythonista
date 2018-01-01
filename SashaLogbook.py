"""Test.

Example
"""

import logbook

import sys
logbook.StreamHandler(sys.stdout, level=logbook.CRITICAL).push_application()
log = logbook.Logger("Sasha Logbook")

log.info("This is an informative message")
log.warning("This is a warning message")
log.error("This is an error message")
