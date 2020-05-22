# internal imports
from domain_dict import DomainDict


class VisibleObjects(DomainDict):
    def __init__(self, object_repository, ui_services, value_repository):
        super(VisibleObjects, self).__init__(value_repository)
        self._object_repository = object_repository
        self._ui_services = ui_services

    def display(self):
        self._ui_services.display_objects(
            self._get_object_type(),
            self._find_visible_objects()
        )

    def set_value(self, key, value):
        super(VisibleObjects, self).set_value(key, value)
        self.display()

    def _find_visible_objects(self):
        return self._object_repository.find_by_filters(self._get_filters())
