class SendSelectedItemsToToolCommandHandler(object):
    def __init__(self, selected_items, visible_items):
        self._selected_items = selected_items
        self._visible_items = visible_items

    def handle(self, command):
        self._selected_items.send_selected_items_to_tool(command.tool_name)
        self._visible_items.display()
