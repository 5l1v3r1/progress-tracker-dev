# internal imports
from table import Table

from items_model import ItemsModel
from items_popup_menu import ItemsPopupMenu
from status_cell_renderer import StatusCellRenderer

from application.command.set_domain_dict_value_command import SetDomainDictValueCommand


class ItemsTable(Table):
    @staticmethod
    def _create_cell_renderer(column_name):
        if column_name == 'Status':
            return StatusCellRenderer()

    @staticmethod
    def _create_model():
        return ItemsModel()

    @staticmethod
    def _create_popup_menu():
        return ItemsPopupMenu()

    @staticmethod
    def _get_domain_dict_type():
        return SetDomainDictValueCommand.TYPE_SELECTED_ITEMS
