from java.awt import Component
from javax.swing import BoxLayout
from javax.swing import JLabel
from javax.swing import JPanel

# internal imports
from database_panel import DatabasePanel
from excluded_extensions_panel import ExcludedExtensionsPanel
from excluded_status_codes_panel import ExcludedStatusCodesPanel
from overwrite_duplicate_items_panel import OverwriteDuplicateItemsPanel
from process_only_in_scope_requests_panel import ProcessOnlyInScopeRequestsPanel
from scope_tools_panel import ScopeToolsPanel
from set_in_progress_status_when_sending_item_to_tool_panel import SetInProgressStatusWhenSendingItemToToolPanel


class OptionsPanel(JPanel):
    def __init__(self):
        super(OptionsPanel, self).__init__()
        self.setLayout(BoxLayout(self, BoxLayout.Y_AXIS))
        self._add_label('Database')
        self._add_panel(DatabasePanel())
        self._add_label('Scope tools')
        self._add_panel(ScopeToolsPanel())
        self._add_label('Excluded extensions')
        self._add_panel(ExcludedExtensionsPanel())
        self._add_label('Excluded status codes')
        self._add_panel(ExcludedStatusCodesPanel())
        self._add_label('Misc')
        self._add_panel(OverwriteDuplicateItemsPanel())
        self._add_panel(ProcessOnlyInScopeRequestsPanel())
        self._add_panel(SetInProgressStatusWhenSendingItemToToolPanel())

    def _add_label(self, label):
        panel = JPanel()
        panel.add(JLabel('<html><h2>%s</h2></html>' % label))
        self._add_panel(panel)

    def _add_panel(self, panel):
        panel.setMaximumSize(panel.getPreferredSize())
        panel.setAlignmentX(Component.LEFT_ALIGNMENT)
        self.add(panel)
