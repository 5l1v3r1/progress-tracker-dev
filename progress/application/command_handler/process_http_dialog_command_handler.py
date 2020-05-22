# internal imports
from domain.item import Item


class ProcessHttpDialogCommandHandler(object):
    def __init__(self, duplicate_items, visible_items):
        self._duplicate_items = duplicate_items
        self._visible_items = visible_items

    def handle(self, command):
        self._duplicate_items.add_item(
            self._create_item(command)
        )
        self._visible_items.display()

    def _create_item(self, command):
        return Item(
            '',
            command.url.getHost(),
            None,
            command.method,
            command.url.getPath(),
            command.url.getPort(),
            command.url.getProtocol(),
            command.request,
            command.response,
            'New',
            [],
            command.time,
            command.tool
        )
