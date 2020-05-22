# internal imports
from domain_dict_with_lock import DomainDictWithLock


class PreProcessValidator(DomainDictWithLock):
    def __init__(self, value_repository):
        super(PreProcessValidator, self).__init__(value_repository)

    # DomainDict
    def _get_default_values(self):
        return {
            'excluded_extensions': ['css', 'js', 'gif', 'ico', 'jpg', 'jpeg', 'png', 'svg', 'woff', 'woff2'],
            'excluded_status_codes': ['404'],
            'process_only_in_scope_requests': True,
        }

    # business logic
    def validate(self, extension, is_in_scope, status_code):
        with self._lock:
            return \
                self._validate_extension(extension) and \
                self._validate_scope(is_in_scope) and \
                self._validate_status_code(status_code)

    def _validate_extension(self, extension):
        return extension not in self._values['excluded_extensions']

    def _validate_scope(self, is_in_scope):
        if self._values['process_only_in_scope_requests']:
            return is_in_scope
        return True

    def _validate_status_code(self, status_code):
        return status_code not in self._values['excluded_status_codes']
