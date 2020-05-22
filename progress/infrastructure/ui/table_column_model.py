class TableColumnModel(object):
    def __init__(self):
        self._columns = self._prepare_columns()

    def get_class(self, column_index):
        return self._columns[column_index][1]

    def get_count(self):
        return len(self._columns)

    def get_name(self, column_index):
        return self._columns[column_index][0]

    def is_array(self, column_index):
        return self._columns[column_index][2]

    def is_editable(self, column_index):
        return self._columns[column_index][3]
