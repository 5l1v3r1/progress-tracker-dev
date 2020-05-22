class SetDomainDictValueCommand(object):
    TYPE_DUPLICATE_ITEMS = 1
    TYPE_PERSISTENCE = 2
    TYPE_PRE_ANALYZE_VALIDATOR = 3
    TYPE_PRE_PROCESS_VALIDATOR = 4
    TYPE_SELECTED_ITEMS = 5
    TYPE_SELECTED_PATH_PATTERNS = 6
    TYPE_VISIBLE_ITEMS = 7

    def __init__(self, type, key, value):
        self.type = type
        self.key = key
        self.value = value
