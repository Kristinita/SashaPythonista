import logbook

from clize import parser
from clize import run
from clize import util
from sigtools import wrappers

log = logbook.Logger("Sasha Logbook")

levels = {
    'CRITICAL': log.critical,
    'ERROR': log.error,
    'WARNING': log.warning,
    'INFO': log.info,
    'DEBUG': log.debug,
}


@parser.value_converter
def loglevel(arg):
    try:
        return int(arg)
    except ValueError:
        try:
            return levels[arg.upper()]
        except KeyError:
            raise ValueError(arg)


class LogLevelParameter(parser.FlagParameter):

    def __init__(self, conv, value=log.info, **kwargs):
        super(LogLevelParameter, self).__init__(
            conv=loglevel, value=value, **kwargs)

    def help_parens(self):
        if self.default is not util.UNSET:
            for k, v in levels.items():
                if v == self.default:
                    default = k
                    break
            else:
                default = self.default
            yield 'default: {0}'.format(default)


log_level = parser.use_class(named=LogLevelParameter)


def try_log(logger):
    logger.debug("Debug")
    logger.info("Info")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical")


@wrappers.decorator
def with_logger(wrapped, *args, log: log_level=log.critical, **kwargs):
    """
    log options:

    :param log: The desired log level"""
    logger = log.getLogger('myapp')
    logger.setLevel(log)
    logger.addHandler(log.StreamHandler())
    return wrapped(*args, logger=logger, **kwargs)


@with_logger
def main(*, logger):
    """Tries out the log system"""
    try_log(logger)


run(main)
