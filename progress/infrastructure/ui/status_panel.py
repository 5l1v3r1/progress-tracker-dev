from java.awt.event import ItemListener
from javax.swing import JCheckBox
from javax.swing import JLabel
from javax.swing import JPanel

# internal imports
from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from common.singleton import Singleton


class StatusPanel(JPanel, ItemListener):
    __metaclass__ = Singleton

    def __init__(self):
        super(StatusPanel, self).__init__()
        self._check_boxes = []

    def itemStateChanged(self, event):
        statuses = []
        for check_box in self._check_boxes:
            if check_box.isSelected():
                statuses.append(check_box.getLabel())
        Application.get_instance().execute(SetDomainDictValueCommand(
            SetDomainDictValueCommand.TYPE_VISIBLE_ITEMS,
            'statuses',
            statuses
        ))

    def display(self, values):
        self.add(JLabel('<html><b>Statuses:</b></html>'))
        for status in Application.ITEM_STATUSES:
            check_box = JCheckBox(status)
            check_box.setSelected(status in values['statuses'])
            check_box.addItemListener(self)
            self._check_boxes.append(check_box)
            self.add(check_box)
