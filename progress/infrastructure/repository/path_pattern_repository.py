# internal imports
from repository import Repository

from domain.path_pattern import PathPattern


class PathPatternRepository(Repository):
    # persistence
    def _create_table(self):
        self._database.execute(
            'CREATE TABLE path_patterns('
            'id INTEGER PRIMARY KEY,'
            'method TEXT NOT NULL,'
            'path_regexp TEXT NOT NULL,'
            'target TEXT NOT NULL,'
            'UNIQUE(method, path_regexp, target) ON CONFLICT IGNORE)'
        )

    def _delete_objects(self, ids):
        self._database.delete('DELETE FROM path_patterns WHERE id in (%s)' % ','.join(map(str, ids)))

    def _get_all_objects(self):
        path_patterns = []
        for row in self._database.select(
                'SELECT '
                'id, method, path_regexp, target '
                'FROM path_patterns '
                'ORDER BY id'
        ):
            path_patterns.append(PathPattern(*row))
        return path_patterns

    def _insert_object(self, path_pattern):
        self._database.insert(
            'INSERT INTO '
            'path_patterns(id, method, path_regexp, target) '
            'values(?, ?, ?, ?)',
            (
                path_pattern.get_id(),
                path_pattern.get_method(),
                path_pattern.get_path_regexp(),
                path_pattern.get_target()
            )
        )

    def _update_objects(self, property, value, ids):
        pass
