from java.lang import Integer
from java.lang import String

# internal imports
from table_column_model import TableColumnModel


class PathPatternsColumnModel(TableColumnModel):
    @staticmethod
    def _prepare_columns():
        return [
            # name, class, is array?, is editable?
            ('Id', Integer, False, False),
            ('Path regexp', String, False, False),
            ('Method', String, False, False),
            ('Target', String, False, False),
        ]
