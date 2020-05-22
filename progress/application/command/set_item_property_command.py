class SetItemPropertyCommand(object):
    def __init__(self, item_id, property, value):
        self.item_id = item_id
        self.property = property
        self.value = value
