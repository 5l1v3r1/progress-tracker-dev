from burp import ITab
from javax.swing import JScrollPane
from javax.swing import JTabbedPane

# internal imports
from burp_callbacks import BurpCallbacks

from infrastructure.ui.items_panel import ItemsPanel
from infrastructure.ui.options_panel import OptionsPanel
from infrastructure.ui.path_patterns_panel import PathPatternsPanel


class ProgressTab(ITab):
    def __init__(self):
        self._ui_component = JTabbedPane()
        self._ui_component.addTab('Items', ItemsPanel())
        self._ui_component.addTab('Path patterns', PathPatternsPanel())
        self._ui_component.addTab('Options', JScrollPane(OptionsPanel()))
        BurpCallbacks.get_instance().customizeUiComponent(self._ui_component)

    def getTabCaption(self):
        return 'Progress'

    def getUiComponent(self):
        return self._ui_component
