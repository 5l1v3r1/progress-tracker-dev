# internal imports
from domain_dict_with_lock import DomainDictWithLock


class PreAnalyzeValidator(DomainDictWithLock):
    def __init__(self, value_repository):
        super(PreAnalyzeValidator, self).__init__(value_repository)

    # DomainDict
    def _get_default_values(self):
        return {
            'scope_tools': ['Proxy'],
            'capturing': 'On'
        }

    # business logic
    def validate(self, source_tool):
        with self._lock:
            return \
                self._values['capturing'] == 'On' and \
                source_tool in self._values['scope_tools']
