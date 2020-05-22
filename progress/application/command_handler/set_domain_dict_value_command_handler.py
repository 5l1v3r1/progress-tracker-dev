# internal imports
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand


class SetDomainDictValueCommandHandler(object):
    def __init__(
            self,
            duplicate_items,
            persistence,
            pre_analyze_validator,
            pre_process_validator,
            selected_items,
            selected_path_patterns,
            visible_items
    ):
        self._domain_dicts = {
            SetDomainDictValueCommand.TYPE_DUPLICATE_ITEMS: duplicate_items,
            SetDomainDictValueCommand.TYPE_PERSISTENCE: persistence,
            SetDomainDictValueCommand.TYPE_PRE_ANALYZE_VALIDATOR: pre_analyze_validator,
            SetDomainDictValueCommand.TYPE_PRE_PROCESS_VALIDATOR: pre_process_validator,
            SetDomainDictValueCommand.TYPE_SELECTED_ITEMS: selected_items,
            SetDomainDictValueCommand.TYPE_SELECTED_PATH_PATTERNS: selected_path_patterns,
            SetDomainDictValueCommand.TYPE_VISIBLE_ITEMS: visible_items
        }

    def handle(self, command):
        return self._domain_dicts[command.type].set_value(command.key, command.value)
