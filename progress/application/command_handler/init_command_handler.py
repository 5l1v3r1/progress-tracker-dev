class InitCommandHandler(object):
    def __init__(
            self,
            duplicate_items,
            persistence,
            pre_analyze_validator,
            pre_process_validator,
            selected_items,
            ui_services,
            visible_items,
            visible_path_patterns
    ):
        self._domain_dicts = [
            duplicate_items,
            persistence,
            pre_analyze_validator,
            pre_process_validator,
            selected_items,
            visible_items
        ]
        self._ui_services = ui_services
        self._visible_objects_handlers = [
            visible_items,
            visible_path_patterns,
        ]

    def handle(self, command):
        values = {}
        for domain_dict in self._domain_dicts:
            values.update(domain_dict.get_values())
        self._ui_services.display_panels(values)
        for visible_objects_handler in self._visible_objects_handlers:
            visible_objects_handler.display()
