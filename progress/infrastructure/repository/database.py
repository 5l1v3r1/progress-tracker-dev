from java.lang import Class
from java.lang import ClassNotFoundException
from java.sql import DriverManager
from java.sql import SQLException
from java.sql import Statement
from java.sql import Types

# internal imports
from infrastructure.event_bus import EventBus


class Database(object):
    @staticmethod
    def get_driver_name():
        return 'SQLite'

    @staticmethod
    def is_driver_loaded():
        try:
            Class.forName('org.sqlite.JDBC')
            return True
        except ClassNotFoundException:
            return False

    def __init__(self, logger):
        self._connection = None
        self._logger = logger
        EventBus().add_observer(self, [EventBus.EVENT_EXTENSION_UNLOADED])

    # Events
    def on_event(self, event_code, value):
        if event_code == EventBus.EVENT_EXTENSION_UNLOADED:
            if self.is_connected():
                self.disconnect()

    def connect(self, database_path):
        try:
            Class.forName('org.sqlite.JDBC')
            self._connection = DriverManager.getConnection('jdbc:sqlite:%s' % database_path)
            self._connection.setAutoCommit(True)
        except ClassNotFoundException as e:
            self._log_error(e.getMessage())
        except SQLException as e:
            self._log_error(e.getMessage())

    def disconnect(self):
        try:
            self._connection.close()
        except SQLException as e:
            self._log_error(e.getMessage())

    def is_connected(self):
        return self._connection is not None

    # queries
    def delete(self, query, params=()):
        self._execute_update(query, params)

    def execute(self, query, params=()):
        try:
            statement = self._prepare_statement(query, params)
            statement.execute()
            statement.close()
        except SQLException as e:
            self._log_error(e.getMessage())

    def insert(self, query, params=()):
        self._execute_update(query, params)

    def select(self, query, params=()):
        try:
            statement = self._prepare_statement(query, params)
            result_set = statement.executeQuery()
            meta_data = result_set.getMetaData()
            column_count = meta_data.getColumnCount()
            column_types = [meta_data.getColumnType(i+1) for i in range(column_count)]
            while result_set.next():
                row = []
                for i in range(column_count):
                    column_index = i + 1
                    if column_types[i] == Types.INTEGER:
                        value = result_set.getLong(column_index)
                    else:
                        value = result_set.getString(column_index)
                    row.append(value)
                yield row
            statement.close()
        except SQLException as e:
            self._log_error(e.getMessage())

    def update(self, query, params=()):
        self._execute_update(query, params)

    def _execute_update(self, query, params):
        try:
            statement = self._prepare_statement(query, params)
            statement.executeUpdate()
            statement.close()
        except SQLException as e:
            self._log_error(e.getMessage())

    def _prepare_statement(self, query, params):
        statement = self._connection.prepareStatement(query, Statement.NO_GENERATED_KEYS)
        i = 1
        for param in params:
            if isinstance(param, (int, long)):
                statement.setLong(i, param)
            else:
                statement.setString(i, param)
            i += 1
        return statement

    def _log_error(self, message):
        self._logger.error('Database error: ' + message)
