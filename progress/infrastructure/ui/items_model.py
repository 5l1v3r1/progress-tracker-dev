# internal imports
from items_column_model import ItemsColumnModel
from table_model import TableModel

from application.command.set_item_property_command import SetItemPropertyCommand


class ItemsModel(TableModel):
    @staticmethod
    def _create_column_model():
        return ItemsColumnModel()

    @staticmethod
    def _create_set_object_property_application_command(id, property, value):
        return SetItemPropertyCommand(id, property, value)
