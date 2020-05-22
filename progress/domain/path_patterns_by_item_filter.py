class PathPatternsByItemFilter(object):
    def __init__(self, item):
        self._item = item

    def __call__(self, *args, **kwargs):
        return args[0].is_item_matched(self._item)
