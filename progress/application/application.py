# internal imports
from command.add_path_pattern_command import AddPathPatternCommand
from command.delete_selected_objects_command import DeleteSelectedObjectsCommand
from command.init_command import InitCommand
from command.make_pre_analyze_validation_command import MakePreAnalyzeValidationCommand
from command.make_pre_process_validation_command import MakePreProcessValidationCommand
from command.process_http_dialog_command import ProcessHttpDialogCommand
from command.send_selected_items_to_tool_command import SendSelectedItemsToToolCommand
from command.set_domain_dict_value_command import SetDomainDictValueCommand
from command.set_item_property_command import SetItemPropertyCommand
from command.set_selected_item_properties_command import SetSelectedItemPropertiesCommand

from command_handler.add_path_pattern_command_handler import AddPathPatternCommandHandler
from command_handler.delete_selected_objects_command_handler import DeleteSelectedObjectsCommandHandler
from command_handler.init_command_handler import InitCommandHandler
from command_handler.make_pre_analyze_validation_command_handler import MakePreAnalyzeValidationCommandHandler
from command_handler.make_pre_process_validation_command_handler import MakePreProcessValidationCommandHandler
from command_handler.process_http_dialog_command_handler import ProcessHttpDialogCommandHandler
from command_handler.send_selected_items_to_tool_command_handler import SendSelectedItemsToToolCommandHandler
from command_handler.set_domain_dict_value_command_handler import SetDomainDictValueCommandHandler
from command_handler.set_item_property_command_handler import SetItemPropertyCommandHandler
from command_handler.set_selected_item_properties_command_handler import SetSelectedItemPropertiesCommandHandler

from domain.duplicate_items import DuplicateItems
from domain.duplicate_path_patterns import DuplicatePathPatterns
from domain.persistence import Persistence
from domain.pre_process_validator import PreProcessValidator
from domain.pre_analyze_validator import PreAnalyzeValidator
from domain.selected_items import SelectedItems
from domain.selected_path_patterns import SelectedPathPatterns
from domain.visible_items import VisibleItems
from domain.visible_path_patterns import VisiblePathPatterns


class Application(object):
    ACTION_TOOLS = ['Intruder', 'Repeater', 'Scanner']
    ITEM_STATUSES = ['Blocked', 'Done', 'Ignored', 'In progress', 'New', 'Postponed']
    SCOPE_TOOLS = ['Proxy', 'Repeater', 'Target']

    _instance = None

    @staticmethod
    def get_instance():
        return Application._instance

    @staticmethod
    def set_instance(instance):
        Application._instance = instance

    def __init__(
        self,
        burp_services,
        database,
        item_repository,
        path_pattern_repository,
        ui_services,
        value_repository
    ):
        duplicate_items = DuplicateItems(item_repository, path_pattern_repository, value_repository)
        duplicate_path_patterns = DuplicatePathPatterns(path_pattern_repository)
        persistence = Persistence(database, item_repository, path_pattern_repository, ui_services, value_repository)
        pre_analyze_validator = PreAnalyzeValidator(value_repository)
        pre_process_validator = PreProcessValidator(value_repository)
        selected_items = SelectedItems(burp_services, item_repository, ui_services, value_repository)
        selected_path_patterns = SelectedPathPatterns(path_pattern_repository, ui_services, value_repository)
        visible_items = VisibleItems(item_repository, ui_services, value_repository)
        visible_path_patterns = VisiblePathPatterns(path_pattern_repository, ui_services, value_repository)

        self._command_handlers = {
            AddPathPatternCommand.__name__: AddPathPatternCommandHandler(
                duplicate_items,
                duplicate_path_patterns,
                selected_items,
                visible_items,
                visible_path_patterns
            ),
            DeleteSelectedObjectsCommand.__name__: DeleteSelectedObjectsCommandHandler(
                selected_items,
                selected_path_patterns,
                visible_items,
                visible_path_patterns
            ),
            InitCommand.__name__: InitCommandHandler(
                duplicate_items,
                persistence,
                pre_analyze_validator,
                pre_process_validator,
                selected_items,
                ui_services,
                visible_items,
                visible_path_patterns
            ),
            MakePreAnalyzeValidationCommand.__name__: MakePreAnalyzeValidationCommandHandler(
                pre_analyze_validator
            ),
            MakePreProcessValidationCommand.__name__: MakePreProcessValidationCommandHandler(
                pre_process_validator
            ),
            ProcessHttpDialogCommand.__name__: ProcessHttpDialogCommandHandler(
                duplicate_items,
                visible_items
            ),
            SendSelectedItemsToToolCommand.__name__: SendSelectedItemsToToolCommandHandler(
                selected_items,
                visible_items
            ),
            SetDomainDictValueCommand.__name__: SetDomainDictValueCommandHandler(
                duplicate_items,
                persistence,
                pre_analyze_validator,
                pre_process_validator,
                selected_items,
                selected_path_patterns,
                visible_items
            ),
            SetItemPropertyCommand.__name__: SetItemPropertyCommandHandler(
                item_repository,
                visible_items
            ),
            SetSelectedItemPropertiesCommand.__name__: SetSelectedItemPropertiesCommandHandler(
                selected_items,
                visible_items
            )
        }
        self.execute(InitCommand())

    def execute(self, command):
        return (self._command_handlers[command.__class__.__name__]).handle(command)
