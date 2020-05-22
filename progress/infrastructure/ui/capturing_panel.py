from java.awt.event import ItemListener
from javax.swing import ButtonGroup
from javax.swing import JLabel
from javax.swing import JPanel
from javax.swing import JRadioButton

# internal imports
from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from common.singleton import Singleton


class CapturingPanel(JPanel, ItemListener):
    __metaclass__ = Singleton

    _OPTIONS = ['On', 'Off']

    def __init__(self):
        super(CapturingPanel, self).__init__()
        self._buttons = []

    def display(self, values):
        self.add(JLabel('<html><b>Capturing:</b></html'))
        button_group = ButtonGroup()
        for option in self._OPTIONS:
            button = JRadioButton(option)
            button.setSelected(option == values['capturing'])
            button.addItemListener(self)
            button_group.add(button)
            self._buttons.append(button)
            self.add(button)

    def itemStateChanged(self, event):
        for button in self._buttons:
            if button.isSelected():
                Application.get_instance().execute(SetDomainDictValueCommand(
                    SetDomainDictValueCommand.TYPE_PRE_ANALYZE_VALIDATOR,
                    'capturing',
                    button.getLabel()
                ))
                break
