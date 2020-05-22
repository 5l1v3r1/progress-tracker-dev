# internal imports
from application.command.delete_selected_objects_command import DeleteSelectedObjectsCommand


class DeleteSelectedObjectsCommandHandler(object):
    def __init__(self, selected_items, selected_path_patterns, visible_items, visible_path_patterns):
        self._selected_object_handlers = {
            DeleteSelectedObjectsCommand.TYPE_ITEM: selected_items,
            DeleteSelectedObjectsCommand.TYPE_PATH_PATTERN: selected_path_patterns,
        }
        self._visible_object_handlers = {
            DeleteSelectedObjectsCommand.TYPE_ITEM: visible_items,
            DeleteSelectedObjectsCommand.TYPE_PATH_PATTERN: visible_path_patterns,
        }

    def handle(self, command):
        self._selected_object_handlers[command.type].delete_selected_objects()
        self._visible_object_handlers[command.type].display()
