from javax.swing import JLabel
from javax.swing import JPanel
from javax.swing import JTextField
from javax.swing.event import DocumentListener

# internal imports
from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from common.singleton import Singleton

from infrastructure.infrastructure_helpers import InfrastructureHelpers


class TagPanel(JPanel, DocumentListener):
    __metaclass__ = Singleton

    def __init__(self):
        super(TagPanel, self).__init__()
        self._text_field = None

    def changeUpdate(self, event):
        self._update()

    def insertUpdate(self, event):
        self._update()

    def removeUpdate(self, event):
        self._update()

    def display(self, values):
        self.add(JLabel('<html><b>Tags:</b></html>'))
        self._text_field = JTextField()
        self._text_field.setColumns(20)
        self._text_field.setEditable(True)
        self._text_field.setText(InfrastructureHelpers.join(values['tags']))
        self._text_field.getDocument().addDocumentListener(self)
        self.add(self._text_field)

    def _update(self):
        Application.get_instance().execute(SetDomainDictValueCommand(
            SetDomainDictValueCommand.TYPE_VISIBLE_ITEMS,
            'tags',
            InfrastructureHelpers.split(self._text_field.getText())
        ))
