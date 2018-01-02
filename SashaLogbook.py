import logbook
import sys

logbook.StreamHandler(sys.stdout,
                      level=logbook.ERROR).push_application()
log = logbook.Logger("Sasha Logbook")

log.debug("Debug message")
log.warning("Warning message")
log.error("Error message")
