from threading import Lock

# internal imports
from domain_dict import DomainDict


class DomainDictWithLock(DomainDict):
    def __init__(self, value_repository):
        super(DomainDictWithLock, self).__init__(value_repository)
        self._lock = Lock()

    def set_value(self, key, value):
        with self._lock:
            super(DomainDictWithLock, self).set_value(key, value)
