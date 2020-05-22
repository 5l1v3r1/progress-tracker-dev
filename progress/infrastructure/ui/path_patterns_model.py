# internal imports
from path_patterns_column_model import PathPatternsColumnModel
from table_model import TableModel


class PathPatternsModel(TableModel):
    @staticmethod
    def _create_column_model():
        return PathPatternsColumnModel()

    @staticmethod
    def _create_set_object_property_application_command(id, property, value):
        pass
