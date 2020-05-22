from java.awt import Dimension
from javax.swing import JPanel
from javax.swing import JSeparator

# internal imports
from capturing_panel import CapturingPanel
from status_panel import StatusPanel
from tag_panel import TagPanel
from tag_operator_panel import TagOperatorPanel


class ItemsBar(JPanel):
    def __init__(self):
        super(ItemsBar, self).__init__()
        self.add(StatusPanel())
        self.add(self._prepare_separator())
        self.add(TagPanel())
        self.add(TagOperatorPanel())
        self.add(self._prepare_separator())
        self.add(CapturingPanel())

    def _prepare_separator(self):
        separator = JSeparator(JSeparator.VERTICAL)
        separator.setPreferredSize(Dimension(2, 30))
        return separator
