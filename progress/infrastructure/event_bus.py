# internal imports
from common.singleton import Singleton


class EventBus(object):
    __metaclass__ = Singleton

    EVENT_EXTENSION_UNLOADED = 1

    def __init__(self):
        self._observers = {}

    def add_observer(self, observer, event_codes):
        for event_code in event_codes:
            if event_code not in self._observers:
                self._observers[event_code] = []
            self._observers[event_code].append(observer)

    def notify(self, event_code, value):
        for observer in self._observers[event_code]:
            observer.on_event(event_code, value)
