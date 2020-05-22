class DuplicatePathPatterns(object):
    def __init__(self, path_pattern_repository):
        self._path_pattern_repository = path_pattern_repository

    def add_path_pattern(self, path_pattern):
        if self._has_duplicate_path_patterns(path_pattern):
            return False
        self._path_pattern_repository.add(path_pattern)
        return True

    def _has_duplicate_path_patterns(self, path_pattern):
        return len(self._path_pattern_repository.find_by_unique_key(path_pattern.get_unique_key())) > 0
