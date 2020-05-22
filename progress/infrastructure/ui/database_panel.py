from java.awt.event import ActionListener
from javax.swing import JButton
from javax.swing import JPanel
from javax.swing import JTextField

# internal imports
from ui_helpers import UIHelpers

from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from common.singleton import Singleton


class DatabasePanel(JPanel, ActionListener):
    __metaclass__ = Singleton

    def __init__(self):
        super(DatabasePanel, self).__init__()
        self._button = None
        self._text_field = None

    def actionPerformed(self, event):
        database_path = UIHelpers.choose_file()
        if database_path:
            if Application.get_instance().execute(SetDomainDictValueCommand(
                SetDomainDictValueCommand.TYPE_PERSISTENCE,
                'database_path',
                database_path
            )):
                self._text_field.setText(database_path)

    def display(self, values):
        self._prepare_components(values)

    def _prepare_components(self, values):
        self._text_field = JTextField()
        self._text_field.setColumns(30)
        self._text_field.setEditable(False)
        self._text_field.setText(values['database_path'])
        self.add(self._text_field)
        button = JButton('Save as...')
        button.addActionListener(self)
        self.add(button)
