from java.lang import Integer
from java.lang import String

# internal imports
from table_column_model import TableColumnModel


class ItemsColumnModel(TableColumnModel):
    @staticmethod
    def _prepare_columns():
        return [
            # name, class, is array?, is editable?
            ('Id', Integer, False, False),
            ('Path', String, False, False),
            ('Method', String, False, False),
            ('Status', String, False, False),
            ('Tags', String, True, True),
            ('Comment', String, False, True),
            ('Target', String, False, False),
            ('Tool', String, False, False),
            ('Time', String, False, False),
        ]
