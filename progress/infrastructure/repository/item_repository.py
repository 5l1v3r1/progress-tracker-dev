# internal imports
from repository import Repository

from domain.item import Item

from infrastructure.infrastructure_helpers import InfrastructureHelpers
from infrastructure.burp.burp_callbacks import BurpCallbacks
from infrastructure.burp.burp_helpers import BurpHelpers


class ItemRepository(Repository):
    def __init__(self, database):
        super(ItemRepository, self).__init__(database)
        self._burp_callbacks = BurpCallbacks.get_instance()
        self._burp_helpers = BurpHelpers.get_instance()

    # persistence
    def _create_table(self):
        self._database.execute(
            'CREATE TABLE items('
            'comment TEXT NOT NULL,'
            'host TEXT NOT NULL,'
            'id INTEGER PRIMARY KEY,'
            'method TEXT NOT NULL,'
            'path TEXT NOT NULL,'
            'port INTEGER NOT NULL,'
            'protocol TEXT NOT NULL,'
            'request TEXT NOT NULL,'
            'response TEXT NOT NULL,'
            'status TEXT NOT NULL,'
            'tags TEXT NOT NULL,'
            'time TEXT NOT NULL,'
            'tool TEXT NOT NULL,'
            'UNIQUE(protocol, host, port, method, path) ON CONFLICT IGNORE)'
        )

    def _delete_objects(self, ids):
        self._database.delete('DELETE FROM items WHERE id in (%s)' % ','.join(map(str, ids)))

    def _get_all_objects(self):
        items = []
        for row in self._database.select(
                'SELECT '
                'comment, host, id, method, path, port, protocol, request, response, status, tags, time, tool '
                'FROM items '
                'ORDER BY id'
        ):
            row[7] = self._decode_data(row[7])
            row[8] = self._decode_data(row[8])
            row[10] = InfrastructureHelpers.split(row[10])
            items.append(Item(*row))
        return items

    def _insert_object(self, item):
        self._database.insert(
            'INSERT INTO '
            'items(comment, host, id, method, path, port, protocol, request, response, status, tags, time, tool) '
            'values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (
                item.get_comment(),
                item.get_host(),
                item.get_id(),
                item.get_method(),
                item.get_path(),
                item.get_port(),
                item.get_protocol(),
                self._encode_data(item.get_request()),
                self._encode_data(item.get_response()),
                item.get_status(),
                InfrastructureHelpers.join(item.get_tags()),
                item.get_time(),
                item.get_tool(),
            )
        )

    def _update_objects(self, property, value, ids):
        if property == 'tags':
            value = InfrastructureHelpers.join(value)
        self._database.update(
            'UPDATE items SET %s = ? WHERE id in (%s)' % (property, ','.join(map(str, ids))),
            (value, )
        )

    def _decode_data(self, data):
        return self._burp_callbacks.saveToTempFile(self._burp_helpers.base64Decode(data))

    def _encode_data(self, data):
        return self._burp_helpers.base64Encode(data.getBuffer())
