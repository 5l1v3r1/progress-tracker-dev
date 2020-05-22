import re

# internal imports
from path_pattern import PathPattern
from selected_objects import SelectedObjects


class SelectedItems(SelectedObjects):
    def __init__(self, burp_services, item_repository, ui_services, value_repository):
        super(SelectedItems, self).__init__(item_repository, ui_services, value_repository)
        self._burp_services = burp_services
        self._item_repository = item_repository
        self._ui_services = ui_services

    # DomainDict
    def _get_default_values(self):
        default_values = super(SelectedItems, self)._get_default_values()
        default_values.update({
            'set_in_progress_status_when_sending_item_to_tool': True,
        })
        return default_values

    # business logic
    def set_value(self, key, value):
        super(SelectedItems, self).set_value(key, value)
        if key == 'main_object_id':
            self._display_main_selected_item()

    def create_path_pattern_from_main_selected_item(self):
        main_selected_item = self._find_main_selected_item()
        return self._create_path_pattern(main_selected_item), main_selected_item

    def send_selected_items_to_tool(self, tool_name):
        self._burp_services.send_items_to_tool(self._find_selected_items(), tool_name)
        if self._values['set_in_progress_status_when_sending_item_to_tool']:
            self.set_selected_item_properties('status', 'In progress')

    def set_selected_item_properties(self, property, value):
        if value is None:
            value = self._ask_for_property(property)
        if value is not None:
            self._item_repository.update_property_by_ids(property, value, self._values['object_ids'])

    def _ask_for_path_regexp(self, path):
        path_regexp = self._ui_services.ask_for_value(
            'Path pattern',
            r'Enter path regexp (e.g. /article/\d+/comments)',
            path,
            False
        )
        if path_regexp:
            try:
                re.compile(path_regexp)
                return path_regexp
            except re.error:
                self._ui_services.display_error('Invalid regular expression')

    def _ask_for_property(self, property):
        title = property.title()
        message = 'Enter %s' % property
        is_value_array = False
        if property == 'tags':
            message = 'Enter comma separated tags (e.g. auth,registration)'
            is_value_array = True
        return self._ui_services.ask_for_value(
            title,
            message,
            self._get_main_selected_item_property(property),
            is_value_array
        )

    def _create_path_pattern(self, main_selected_item):
        if main_selected_item:
            path_regexp = self._ask_for_path_regexp(main_selected_item.get_path())
            if path_regexp:
                return PathPattern(
                    None,
                    main_selected_item.get_method(),
                    path_regexp,
                    main_selected_item.get_target()
                )

    def _display_main_selected_item(self):
        self._ui_services.display_http_dialog(
            self._find_main_selected_item()
        )

    def _find_main_selected_item(self):
        if self._values['main_object_id']:
            return self._item_repository.find_by_id(self._values['main_object_id'])

    def _find_selected_items(self):
        return self._item_repository.find_by_ids(self._values['object_ids'])

    def _get_main_selected_item_property(self, property):
        item = self._find_main_selected_item()
        if item:
            return getattr(item, 'get_%s' % property)()

    def _get_object_plural_name(self):
        return 'items'
