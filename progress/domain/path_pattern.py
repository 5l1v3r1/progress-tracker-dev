import re


class PathPattern(object):
    def __init__(self, id, method, path_regexp, target):
        self._id = id
        self._method = method
        self._path_regexp = path_regexp
        self._path_regexp_compiled = re.compile(path_regexp)
        self._target = target

    def get_id(self):
        return self._id

    def get_method(self):
        return self._method

    def get_path_regexp(self):
        return self._path_regexp

    def get_target(self):
        return self._target

    def set_id(self, id):
        self._id = id

    # business logic
    def get_unique_key(self):
        return self.get_target() + self.get_method() + self.get_path_regexp()

    def is_item_matched(self, item):
        return \
            self._target == item.get_target() and \
            self._method == item.get_method() and \
            self._path_regexp_compiled.match(item.get_path())
