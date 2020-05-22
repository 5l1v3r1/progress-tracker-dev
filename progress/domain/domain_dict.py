class DomainDict(object):
    def __init__(self, value_repository):
        self._value_repository = value_repository
        self._values = value_repository.get(
            self._get_storage_key(),
            self._get_default_values()
        )

    def get_values(self):
        return self._values

    def set_value(self, key, value):
        self._values[key] = value
        if key not in self._get_keys_excluded_from_storing():
            self._value_repository.set(self._get_storage_key(), self._values)

    def _get_default_values(self):
        return {}

    def _get_keys_excluded_from_storing(self):
        return []

    def _get_storage_key(self):
        return self.__class__.__name__
