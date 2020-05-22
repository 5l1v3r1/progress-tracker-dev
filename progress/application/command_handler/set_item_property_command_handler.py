class SetItemPropertyCommandHandler(object):
    def __init__(self, item_repository, visible_items):
        self._item_repository = item_repository
        self._visible_items = visible_items

    def handle(self, command):
        self._item_repository.update_property_by_id(command.property, command.value, command.item_id)
        self._visible_items.display()
