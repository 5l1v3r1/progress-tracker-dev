# internal imports
from capturing_panel import CapturingPanel
from database_panel import DatabasePanel
from excluded_extensions_panel import ExcludedExtensionsPanel
from excluded_status_codes_panel import ExcludedStatusCodesPanel
from items_model import ItemsModel
from overwrite_duplicate_items_panel import OverwriteDuplicateItemsPanel
from path_patterns_model import PathPatternsModel
from process_only_in_scope_requests_panel import ProcessOnlyInScopeRequestsPanel
from scope_tools_panel import ScopeToolsPanel
from status_panel import StatusPanel
from set_in_progress_status_when_sending_item_to_tool_panel import SetInProgressStatusWhenSendingItemToToolPanel
from tag_panel import TagPanel
from tag_operator_panel import TagOperatorPanel
from ui_helpers import UIHelpers

from infrastructure.burp.http_dialog_editor import HttpDialogEditor


class UIServices(object):
    def __init__(self):
        self._http_dialog_editor = HttpDialogEditor()
        self._models = {
            'item': ItemsModel(),
            'path_pattern': PathPatternsModel(),
        }
        self._panels_to_display = [
            CapturingPanel(),
            DatabasePanel(),
            ExcludedExtensionsPanel(),
            ExcludedStatusCodesPanel(),
            OverwriteDuplicateItemsPanel(),
            ProcessOnlyInScopeRequestsPanel(),
            ScopeToolsPanel(),
            SetInProgressStatusWhenSendingItemToToolPanel(),
            StatusPanel(),
            TagPanel(),
            TagOperatorPanel(),
        ]

    @staticmethod
    def ask_for_value(title, message, initial_value, is_value_array):
        return UIHelpers.ask_for_value(title, message, initial_value, is_value_array)

    @staticmethod
    def confirm(question):
        return UIHelpers.confirm(question)

    @staticmethod
    def display_error(message):
        UIHelpers.display_error(message)

    def display_http_dialog(self, item):
        self._http_dialog_editor.display(item)

    def display_objects(self, type, objects):
        self._models[type].display(objects)

    def display_panels(self, values):
        for panel_to_display in self._panels_to_display:
            panel_to_display.display(values)
