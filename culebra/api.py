import os
from . import config


def queue(name):
    if not isinstance(name, basestring):
        raise TypeError()
    return core.queue(name)

def set_home(path):
    if not os.path.isdir(path):
        raise ValueError()
    config.set_home(path)
