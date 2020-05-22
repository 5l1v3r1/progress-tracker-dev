class SetSelectedItemPropertiesCommandHandler(object):
    def __init__(self, selected_items, visible_items):
        self._selected_items = selected_items
        self._visible_items = visible_items

    def handle(self, command):
        self._selected_items.set_selected_item_properties(command.property, command.value)
        self._visible_items.display()
