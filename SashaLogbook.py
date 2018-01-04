import logbook

from clize import run

log = logbook.Logger("Sasha Logbook")


def test(*, level_logger: 'll'="logbook.StreamHandler(sys.stdout, level=logbook.ERROR).push_application()"):
    print(level_logger)


log.debug("Debug message")
log.warning("Warning message")
log.error("Error message")

run(test, exit=False)
