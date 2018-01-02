from clize import run


def echo(*, prefix='f'):
    """Echoes prefix parameter

    :param prefix: Print specified letter
    """
    print(prefix)


run(echo)
