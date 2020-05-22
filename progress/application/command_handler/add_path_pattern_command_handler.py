class AddPathPatternCommandHandler(object):
    def __init__(
        self,
        duplicate_items,
        duplicate_path_patterns,
        selected_items,
        visible_items,
        visible_path_patterns
    ):
        self._duplicate_items = duplicate_items
        self._duplicate_path_patterns = duplicate_path_patterns
        self._selected_items = selected_items
        self._visible_items = visible_items
        self._visible_path_patterns = visible_path_patterns

    def handle(self, command):
        path_pattern, origin_item = self._selected_items.create_path_pattern_from_main_selected_item()
        if path_pattern:
            if self._duplicate_path_patterns.add_path_pattern(path_pattern):
                self._duplicate_items.delete_duplicate_items_by_path_pattern(path_pattern, origin_item)
                self._visible_items.display()
                self._visible_path_patterns.display()
