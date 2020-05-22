from java.awt.event import FocusListener
from javax.swing import GroupLayout
from javax.swing import JLabel
from javax.swing import JPanel
from javax.swing import JTextField

# internal imports
from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from common.singleton import Singleton

from infrastructure.infrastructure_helpers import InfrastructureHelpers


class TextFieldPanel(JPanel, FocusListener):
    __metaclass__ = Singleton

    def __init__(self):
        super(TextFieldPanel, self).__init__()
        self._text_field = None

    def focusGained(self, event):
        pass

    def focusLost(self, event):
        Application.get_instance().execute(SetDomainDictValueCommand(
            self._get_domain_dict_type(),
            self._get_domain_dict_key(),
            InfrastructureHelpers.split(self._text_field.getText())
        ))

    def display(self, values):
        self._prepare_components(values)

    def _prepare_components(self, values):
        self._text_field = JTextField()
        self._text_field.setColumns(30)
        self._text_field.setEditable(True)
        self._text_field.setText(InfrastructureHelpers.join(values[self._get_domain_dict_key()]))
        self._text_field.addFocusListener(self)
        self.add(self._text_field)
