# internal imports
from items_by_statuses_filter import ItemsByStatusesFilter
from items_by_tags_filter import ItemsByTagsFilter
from visible_objects import VisibleObjects


class VisibleItems(VisibleObjects):
    def __init__(self, item_repository, ui_services, value_repository):
        super(VisibleItems, self).__init__(item_repository, ui_services, value_repository)

    # DomainDict
    def _get_default_values(self):
        return {
            'statuses': ['In progress', 'New'],
            'tags': [],
            'tags_operator': 'AND',
        }

    # business logic
    def _get_filters(self):
        filters = [ItemsByStatusesFilter(self._values['statuses'])]
        if self._values['tags']:
            filters.append(ItemsByTagsFilter(self._values['tags'], self._values['tags_operator']))
        return filters

    @staticmethod
    def _get_object_type():
        return 'item'
