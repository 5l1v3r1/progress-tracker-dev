# internal imports
from domain_dict import DomainDict
from items_by_path_patterns_filter import ItemsByPathPatternsFilter
from path_patterns_by_item_filter import PathPatternsByItemFilter


class DuplicateItems(DomainDict):
    def __init__(self, item_repository, path_pattern_repository, value_repository):
        super(DuplicateItems, self).__init__(value_repository)
        self._item_repository = item_repository
        self._path_pattern_repository = path_pattern_repository

    # DomainDict
    def _get_default_values(self):
        return {
            'overwrite_duplicate_items': True,
        }

    # business logic
    def add_item(self, item):
        duplicate_items = self._find_duplicate_items(item)
        if duplicate_items:
            if self._values['overwrite_duplicate_items']:
                self._overwrite_duplicate_items(duplicate_items, item)
        else:
            self._add_item(item)

    def delete_duplicate_items_by_path_pattern(self, path_pattern, origin_item):
        duplicate_items = self._item_repository.find_by_filters([
            ItemsByPathPatternsFilter([path_pattern])
        ])
        if origin_item in duplicate_items:
            duplicate_items.remove(origin_item)
        self._item_repository.delete_by_list(duplicate_items)

    def _add_item(self, item):
        self._item_repository.add(item)

    def _find_duplicate_items(self, item):
        duplicate_items = self._item_repository.find_by_unique_key(item.get_unique_key())
        if not duplicate_items:
            path_patterns = self._path_pattern_repository.find_by_filters([PathPatternsByItemFilter(item)])
            duplicate_items = self._item_repository.find_by_filters([ItemsByPathPatternsFilter(path_patterns)])
        return duplicate_items

    def _overwrite_duplicate_items(self, duplicate_items, item):
        item.copy_state_from(duplicate_items[-1])
        self._item_repository.delete_by_list(duplicate_items)
        self._add_item(item)
