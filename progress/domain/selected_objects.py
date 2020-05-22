# internal imports
from domain_dict import DomainDict


class SelectedObjects(DomainDict):
    def __init__(self, object_repository, ui_services, value_repository):
        super(SelectedObjects, self).__init__(value_repository)
        self._object_repository = object_repository
        self._ui_services = ui_services

    # DomainDict
    def _get_default_values(self):
        return {
            'main_object_id': None,
            'object_ids': [],
        }

    def _get_keys_excluded_from_storing(self):
        return ['main_object_id', 'object_ids']

    # business logic
    def delete_selected_objects(self):
        if self._ui_services.confirm(
            'Are you sure you want to delete the selected %s?' % self._get_object_plural_name()
        ):
            self._object_repository.delete_by_ids(self._values['object_ids'])

    def _get_object_plural_name(self):
        pass
