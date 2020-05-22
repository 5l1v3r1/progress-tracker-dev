from javax.swing.table import AbstractTableModel

# internal imports
from application.application import Application

from common.singleton import Singleton

from infrastructure.infrastructure_helpers import InfrastructureHelpers


class TableModel(AbstractTableModel):
    __metaclass__ = Singleton

    def __init__(self):
        super(TableModel, self).__init__()
        self._column_model = self._create_column_model()
        self._objects = []

    # AbstractTableModel
    def getColumnClass(self, column_index):
        return self._column_model.get_class(column_index)

    def getColumnCount(self):
        return self._column_model.get_count()

    def getColumnName(self, column_index):
        return self._column_model.get_name(column_index)

    def getRowCount(self):
        return len(self._objects)

    def getValueAt(self, row_index, column_index):
        property = self._get_property_name(column_index)
        value = getattr(self._objects[row_index], 'get_%s' % property)()
        return InfrastructureHelpers.join(value) if self._column_model.is_array(column_index) else value

    def isCellEditable(self, _, column_index):
        return self._column_model.is_editable(column_index)

    def setValueAt(self, value, row_index, column_index):
        property = self.getColumnName(column_index).lower()
        if self._column_model.is_array(column_index):
            value = InfrastructureHelpers.split(value)
        Application.get_instance().execute(self._create_set_object_property_application_command(
            self._objects[row_index].get_id(),
            property,
            value
        ))

    def map_object_indexes_to_ids(self, object_indexes):
        return [self._objects[i].get_id() for i in object_indexes]

    def display(self, objects):
        self._objects = objects
        self.fireTableDataChanged()

    def _get_property_name(self, column_index):
        return self.getColumnName(column_index).lower().replace(' ', '_')
