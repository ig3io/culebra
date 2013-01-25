import os

_QUEUE_HOME = os.getcwd()
_EXTENSION = '.clbr'

def home():
    return _QUEUE_HOME

def extension():
    return _EXTENSION

def set_home(home):
    global _QUEUE_HOME
    _QUEUE_HOME = home

def set_extension(extension):
    global _EXTENSION
    _EXTENSION = extension
