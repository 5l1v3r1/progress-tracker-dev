# internal imports
from burp_callbacks import BurpCallbacks


class Logger(object):
    def __init__(self):
        self._burp_callbacks = BurpCallbacks.get_instance()

    def error(self, message):
        self._burp_callbacks.printError(message)
