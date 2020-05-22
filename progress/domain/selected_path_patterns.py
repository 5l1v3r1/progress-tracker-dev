# internal imports
from selected_objects import SelectedObjects


class SelectedPathPatterns(SelectedObjects):
    def __init__(self, path_pattern_repository, ui_services, value_repository):
        super(SelectedPathPatterns, self).__init__(path_pattern_repository, ui_services, value_repository)

    def _get_object_plural_name(self):
        return 'path patterns'
