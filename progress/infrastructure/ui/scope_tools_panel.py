from java.awt.event import ItemListener
from javax.swing import JCheckBox
from javax.swing import JPanel

# internal imports
from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from common.singleton import Singleton


class ScopeToolsPanel(JPanel, ItemListener):
    __metaclass__ = Singleton

    def __init__(self):
        super(ScopeToolsPanel, self).__init__()
        self._check_boxes = []

    def itemStateChanged(self, event):
        scope_tools = []
        for check_box in self._check_boxes:
            if check_box.isSelected():
                scope_tools.append(check_box.getLabel())
        Application.get_instance().execute(SetDomainDictValueCommand(
            SetDomainDictValueCommand.TYPE_PRE_ANALYZE_VALIDATOR,
            'scope_tools',
            scope_tools
        ))

    def display(self, active_scope_tools):
        self._prepare_components(active_scope_tools)

    def _prepare_components(self, values):
        for scope_tool in Application.SCOPE_TOOLS:
            check_box = JCheckBox(scope_tool)
            check_box.setSelected(scope_tool in values['scope_tools'])
            check_box.addItemListener(self)
            self._check_boxes.append(check_box)
            self.add(check_box)
