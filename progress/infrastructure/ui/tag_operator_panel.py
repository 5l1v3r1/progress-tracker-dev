from java.awt.event import ItemListener
from javax.swing import ButtonGroup
from javax.swing import JPanel
from javax.swing import JRadioButton

# internal imports
from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from common.singleton import Singleton


class TagOperatorPanel(JPanel, ItemListener):
    __metaclass__ = Singleton

    _OPERATORS = ['AND', 'OR']

    def __init__(self):
        super(TagOperatorPanel, self).__init__()
        self._buttons = []

    def display(self, values):
        button_group = ButtonGroup()
        for operator in self._OPERATORS:
            button = JRadioButton(operator)
            button.setSelected(operator == values['tags_operator'])
            button.addItemListener(self)
            button_group.add(button)
            self._buttons.append(button)
            self.add(button)

    def itemStateChanged(self, event):
        for button in self._buttons:
            if button.isSelected():
                Application.get_instance().execute(SetDomainDictValueCommand(
                    SetDomainDictValueCommand.TYPE_VISIBLE_ITEMS,
                    'tags_operator',
                    button.getLabel()
                ))
                break
