class ItemsByStatusesFilter(object):
    def __init__(self, statuses):
        self._statuses = statuses

    def __call__(self, *args, **kwargs):
        return args[0].is_status_one_of(self._statuses)
