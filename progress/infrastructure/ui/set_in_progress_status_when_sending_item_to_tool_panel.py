# internal imports
from check_box_panel import CheckBoxPanel

from application.command.set_domain_dict_value_command import SetDomainDictValueCommand


class SetInProgressStatusWhenSendingItemToToolPanel(CheckBoxPanel):
    def _get_domain_dict_key(self):
        return 'set_in_progress_status_when_sending_item_to_tool'

    def _get_domain_dict_type(self):
        return SetDomainDictValueCommand.TYPE_SELECTED_ITEMS

    def _get_label(self):
        return '<html>Set <i>In progress</i> status when sending item to tool</html>'
