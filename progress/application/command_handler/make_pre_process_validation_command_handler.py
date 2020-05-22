class MakePreProcessValidationCommandHandler(object):
    def __init__(self, pre_process_validator):
        self._pre_process_validator = pre_process_validator

    def handle(self, command):
        return self._pre_process_validator.validate(
            command.extension,
            command.is_in_scope,
            command.status_code
        )
