class MakePreProcessValidationCommand(object):
    def __init__(self, extension, is_in_scope, status_code):
        self.extension = extension
        self.is_in_scope = is_in_scope
        self.status_code = status_code
