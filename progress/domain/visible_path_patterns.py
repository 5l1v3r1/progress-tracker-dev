# internal imports
from visible_objects import VisibleObjects


class VisiblePathPatterns(VisibleObjects):
    def __init__(self, item_repository, ui_services, value_repository):
        super(VisiblePathPatterns, self).__init__(item_repository, ui_services, value_repository)

    @staticmethod
    def _get_filters():
        return []

    @staticmethod
    def _get_object_type():
        return 'path_pattern'
