import os
from . import config
from .queue import Queue

def queue(name):
    path = os.path.join(config.home(), name + config.extension())
    return Queue(name, path)