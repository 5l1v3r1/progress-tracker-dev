# internal imports
from text_field_panel import TextFieldPanel

from application.command.set_domain_dict_value_command import SetDomainDictValueCommand


class ExcludedExtensionsPanel(TextFieldPanel):
    def _get_domain_dict_key(self):
        return 'excluded_extensions'

    def _get_domain_dict_type(self):
        return SetDomainDictValueCommand.TYPE_PRE_PROCESS_VALIDATOR
