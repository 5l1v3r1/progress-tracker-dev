import os.path

# internal imports
from domain_dict import DomainDict


class Persistence(DomainDict):
    def __init__(self, database, item_repository, path_pattern_repository, ui_services, value_repository):
        super(Persistence, self).__init__(value_repository)
        self._database = database
        self._repositories = [
            item_repository,
            path_pattern_repository,
        ]
        self._ui_services = ui_services
        self._load()

    # DomainDict
    def _get_default_values(self):
        return {
            'database_path': '',
        }

    # business logic
    def set_value(self, key, value):
        if self._persist(value):
            super(Persistence, self).set_value(key, value)
            return True
        return False

    def _load(self):
        if self._values['database_path']:
            self._database.connect(self._values['database_path'])
            for repository in self._repositories:
                repository.load()

    def _persist(self, database_path):
        if (
            self._is_driver_loaded() and
            self._prepare_database_file(database_path) and
            self._persist_repositories(database_path)
        ):
            return True
        return False

    def _is_driver_loaded(self):
        if not self._database.is_driver_loaded():
            self._ui_services.display_error(
                '%s driver not found (see "Requirements" on https://github.com/dariusztytko/progress-burp)' % self._database.get_driver_name())
            return False
        return True

    def _prepare_database_file(self, database_path):
        try:
            if os.path.exists(database_path):
                if not self._ui_services.confirm('File already exists. Are you sure you want to replace it?'):
                    return False
            with open(database_path, 'ab') as f:
                f.truncate(0)
            return True
        except IOError as e:
            self._ui_services.display_error(str(e))

    def _persist_repositories(self, database_path):
        if self._database.is_connected():
            self._database.disconnect()
        self._database.connect(database_path)
        for repository in self._repositories:
            repository.init_persistence()
        return True
