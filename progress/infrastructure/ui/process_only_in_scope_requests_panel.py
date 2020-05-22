# internal imports
from check_box_panel import CheckBoxPanel

from application.command.set_domain_dict_value_command import SetDomainDictValueCommand


class ProcessOnlyInScopeRequestsPanel(CheckBoxPanel):
    def _get_domain_dict_key(self):
        return 'process_only_in_scope_requests'

    def _get_domain_dict_type(self):
        return SetDomainDictValueCommand.TYPE_PRE_PROCESS_VALIDATOR

    def _get_label(self):
        return 'Process only in-scope requests'
