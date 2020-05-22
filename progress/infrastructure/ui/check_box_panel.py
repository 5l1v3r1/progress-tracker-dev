from java.awt.event import ItemListener
from javax.swing import JCheckBox
from javax.swing import JPanel

# internal imports
from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from common.singleton import Singleton


class CheckBoxPanel(JPanel, ItemListener):
    __metaclass__ = Singleton

    def __init__(self):
        super(CheckBoxPanel, self).__init__()
        self._check_box = None

    def itemStateChanged(self, event):
        Application.get_instance().execute(SetDomainDictValueCommand(
            self._get_domain_dict_type(),
            self._get_domain_dict_key(),
            self._check_box.isSelected()
        ))

    def display(self, values):
        self._check_box = JCheckBox(self._get_label())
        self._check_box.setSelected(values[self._get_domain_dict_key()])
        self._check_box.addItemListener(self)
        self.add(self._check_box)
