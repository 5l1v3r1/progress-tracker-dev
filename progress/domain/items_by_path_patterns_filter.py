class ItemsByPathPatternsFilter(object):
    def __init__(self, path_patterns):
        self._path_patterns = path_patterns

    def __call__(self, *args, **kwargs):
        for path_pattern in self._path_patterns:
            if path_pattern.is_item_matched(args[0]):
                return True
        return False
