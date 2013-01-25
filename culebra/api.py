import os
from . import config
from . import core


def queue(name):
    if not isinstance(name, basestring):
        raise TypeError()
    return core.queue(name)

def set_home(path):
    if not os.path.isdir(path):
        raise ValueError()
    config.set_home(path)

def set_extension(ext):
    if not isinstance(ext, basestring):
        raise TypeError()
    if not ext.startswith('.'):
        raise ValueError()
    config.set_extension(ext)