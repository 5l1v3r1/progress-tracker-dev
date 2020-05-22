class MakePreAnalyzeValidationCommandHandler(object):
    def __init__(self, pre_analyze_validator):
        self._pre_analyze_validator = pre_analyze_validator

    def handle(self, command):
        return self._pre_analyze_validator.validate(command.source_tool)
