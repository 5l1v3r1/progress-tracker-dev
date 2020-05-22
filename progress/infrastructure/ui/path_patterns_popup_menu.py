# internal imports
from table_popup_menu import TablePopupMenu

from application.command.delete_selected_objects_command import DeleteSelectedObjectsCommand


class PathPatternsPopupMenu(TablePopupMenu):
    def __init__(self):
        super(PathPatternsPopupMenu, self).__init__()

    @staticmethod
    def _create_application_command(command):
        if command == 'Delete':
            return DeleteSelectedObjectsCommand(DeleteSelectedObjectsCommand.TYPE_PATH_PATTERN)

    @staticmethod
    def _prepare_labels():
        return {
            'Delete': {}
        }
