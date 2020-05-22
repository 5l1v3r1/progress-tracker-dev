# internal imports
from table_popup_menu import TablePopupMenu

from application.application import Application
from application.command.add_path_pattern_command import AddPathPatternCommand
from application.command.delete_selected_objects_command import DeleteSelectedObjectsCommand
from application.command.send_selected_items_to_tool_command import SendSelectedItemsToToolCommand
from application.command.set_selected_item_properties_command import SetSelectedItemPropertiesCommand


class ItemsPopupMenu(TablePopupMenu):
    def __init__(self):
        super(ItemsPopupMenu, self).__init__()

    @staticmethod
    def _create_application_command(command):
        if command == 'Add path pattern':
            return AddPathPatternCommand()
        if command == 'Delete':
            return DeleteSelectedObjectsCommand(DeleteSelectedObjectsCommand.TYPE_ITEM)
        if command in Application.ACTION_TOOLS:
            return SendSelectedItemsToToolCommand(command)
        if command == 'Set comment':
            return SetSelectedItemPropertiesCommand('comment', None)
        if command in Application.ITEM_STATUSES:
            return SetSelectedItemPropertiesCommand('status', command)
        if command == 'Set tags':
            return SetSelectedItemPropertiesCommand('tags', None)

    @staticmethod
    def _prepare_labels():
        labels = {
            'Add path pattern': {},
            'Delete': {},
            'Send to': {},
            'Set comment': {},
            'Set status': {},
            'Set tags': {}
        }
        for action_tool in Application.ACTION_TOOLS:
            labels['Send to'][action_tool] = {}
        for item_status in Application.ITEM_STATUSES:
            labels['Set status'][item_status] = {}
        return labels
