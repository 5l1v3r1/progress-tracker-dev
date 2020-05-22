# internal imports
from check_box_panel import CheckBoxPanel

from application.command.set_domain_dict_value_command import SetDomainDictValueCommand


class OverwriteDuplicateItemsPanel(CheckBoxPanel):
    def _get_domain_dict_key(self):
        return 'overwrite_duplicate_items'

    def _get_domain_dict_type(self):
        return SetDomainDictValueCommand.TYPE_DUPLICATE_ITEMS

    def _get_label(self):
        return 'Overwrite duplicate items'
