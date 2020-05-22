# internal imports
from path_patterns_model import PathPatternsModel
from path_patterns_popup_menu import PathPatternsPopupMenu
from table import Table

from application.command.set_domain_dict_value_command import SetDomainDictValueCommand


class PathPatternsTable(Table):
    @staticmethod
    def _create_model():
        return PathPatternsModel()

    @staticmethod
    def _create_popup_menu():
        return PathPatternsPopupMenu()

    @staticmethod
    def _get_domain_dict_type():
        return SetDomainDictValueCommand.TYPE_SELECTED_PATH_PATTERNS
