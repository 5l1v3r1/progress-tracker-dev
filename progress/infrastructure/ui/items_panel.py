from java.awt import BorderLayout
from javax.swing import JPanel

# internal imports
from items_bar import ItemsBar
from items_view import ItemsView


class ItemsPanel(JPanel):
    def __init__(self):
        super(ItemsPanel, self).__init__()
        self.setLayout(BorderLayout())
        self.add(ItemsBar(), BorderLayout.PAGE_START)
        self.add(ItemsView(), BorderLayout.CENTER)
