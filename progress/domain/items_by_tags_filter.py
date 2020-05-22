class ItemsByTagsFilter(object):
    def __init__(self, tags, operator):
        self._tags = set(tags)
        self._operator = operator

    def __call__(self, *args, **kwargs):
        item = args[0]
        if self._operator == 'AND':
            return item.has_all_tags_of(self._tags)
        return item.has_any_tag_of(self._tags)
