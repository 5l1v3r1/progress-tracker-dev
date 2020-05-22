class Repository(object):
    def __init__(self, database):
        self._database = database
        self._last_object_id = 0
        self._objects = []

    def add(self, object):
        object.set_id(self._get_next_id())
        self._objects.append(object)
        if self._database.is_connected():
            self._insert_object(object)

    def delete_by_ids(self, ids):
        self.delete_by_list(
            self.find_by_ids(ids)
        )

    def delete_by_list(self, objects):
        ids = []
        for object in objects:
            ids.append(object.get_id())
            self._objects.remove(object)
        if self._database.is_connected():
            self._delete_objects(ids)

    def find_all(self):
        return self._objects

    def find_by_filters(self, filters):
        return filter(lambda object: all(f(object) for f in filters), self._objects)

    def find_by_id(self, id):
        return self.find_by_ids([id])[0]

    def find_by_ids(self, ids):
        return filter(lambda object: object.get_id() in ids, self._objects)

    def find_by_unique_key(self, unique_key):
        return filter(lambda object: object.get_unique_key() == unique_key, self._objects)

    def update_property_by_id(self, property, value, id):
        self.update_property_by_ids(property, value, [id])

    def update_property_by_ids(self, property, value, ids):
        setter_name = 'set_%s' % property
        map(lambda object: getattr(object, setter_name)(value), self.find_by_ids(ids))
        if self._database.is_connected():
            self._update_objects(property, value, ids)

    def _get_next_id(self):
        self._last_object_id += 1
        return self._last_object_id

    # persistence
    def init_persistence(self):
        if self._database.is_connected():
            self._create_table()
            for object in self._objects:
                self._insert_object(object)

    def load(self):
        if self._database.is_connected():
            self._objects = self._get_all_objects()
            if self._objects:
                self._last_object_id = self._objects[-1].get_id()

    # persistence (repository interface)
    def _create_table(self):
        pass

    def _delete_objects(self, ids):
        pass

    def _get_all_objects(self):
        return []

    def _insert_object(self, object):
        pass

    def _update_objects(self, property, value, ids):
        pass
