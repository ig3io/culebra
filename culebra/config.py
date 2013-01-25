import os

_QUEUE_HOME = os.getcwd()

def home():
    return _QUEUE_HOME

def set_home(home):
    global _QUEUE_HOME
    _QUEUE_HOME = home