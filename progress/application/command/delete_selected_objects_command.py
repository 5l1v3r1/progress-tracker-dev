class DeleteSelectedObjectsCommand(object):
    TYPE_ITEM = 1
    TYPE_PATH_PATTERN = 2

    def __init__(self, type):
        self.type = type
