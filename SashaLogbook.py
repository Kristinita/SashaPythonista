import logbook
import sys

# Clize — command line arguments for Python applications
# https://clize.readthedocs.io/en/stable/index.html
from clize import run

log = logbook.Logger("Sasha Logbook")

# «*» symbol needs for correct Clize working, see
# https://github.com/epsy/clize/issues/33#issuecomment-354798817


def clize_log_level(*, logbook_level: 'll'="NOTICE"):
    """Change log levels via command line.

    User select, which logging messages to see. See about 6 log levels here:
    https://logbook.readthedocs.io/en/stable/quickstart.html

    :param logbook_level: user select logging level
    """
    print(logbook_level)

    if logbook_level == "DEBUG":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.DEBUG).push_application()
    elif logbook_level == "INFO":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.INFO).push_application()
    elif logbook_level == "NOTICE":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.NOTICE).push_application()
    elif logbook_level == "WARNING":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.WARNING).push_application()
    elif logbook_level == "ERROR":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.ERROR).push_application()
    elif logbook_level == "CRITICAL":
        logbook.StreamHandler(sys.stdout,
                              level=logbook.CRITICAL).push_application()
    else:
        logbook.StreamHandler(sys.stdout,
                              level=logbook.NOTICE).push_application()

    log.debug("Debug message")
    log.warning("Warning message")
    log.error("Error message")


# Needs, that Clize don't exit, see
# https://github.com/epsy/clize/issues/33#issuecomment-354849918
run(clize_log_level, exit=False)
