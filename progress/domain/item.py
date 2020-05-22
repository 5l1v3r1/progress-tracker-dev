class Item(object):
    def __init__(
            self,
            comment,
            host,
            id,
            method,
            path,
            port,
            protocol,
            request,
            response,
            status,
            tags,
            time,
            tool
    ):
        self._comment = comment
        self._host = host
        self._id = id
        self._method = method
        self._path = path
        self._port = port
        self._protocol = protocol
        self._request = request
        self._response = response
        self._status = status
        self._tags = tags
        self._time = time
        self._tool = tool

    # get & set
    def get_comment(self):
        return self._comment

    def get_host(self):
        return self._host

    def get_id(self):
        return self._id

    def get_method(self):
        return self._method

    def get_path(self):
        return self._path

    def get_port(self):
        return self._port

    def get_protocol(self):
        return self._protocol

    def get_request(self):
        return self._request

    def get_response(self):
        return self._response

    def get_status(self):
        return self._status

    def get_tags(self):
        return self._tags

    def get_time(self):
        return self._time

    def get_tool(self):
        return self._tool

    def set_comment(self, comment):
        self._comment = comment

    def set_id(self, id):
        self._id = id

    def set_status(self, status):
        self._status = status

    def set_tags(self, tags):
        self._tags = tags

    # business logic
    def copy_state_from(self, item):
        self._comment = item.get_comment()
        self._status = item.get_status()
        self._tags = item.get_tags()

    def get_target(self):
        return '%s://%s:%d' % (self._protocol, self._host, self._port)

    def get_unique_key(self):
        return self.get_target() + self.get_method() + self.get_path()

    def has_all_tags_of(self, tags):
        item_tags = set(self._tags)
        return tags.issubset(item_tags)

    def has_any_tag_of(self, tags):
        item_tags = set(self._tags)
        return bool(tags.intersection(item_tags))

    def is_status_one_of(self, statuses):
        return self._status in statuses
