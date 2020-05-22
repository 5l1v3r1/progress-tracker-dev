from javax.swing import JLabel
from javax.swing import JTable
from javax.swing.table import DefaultTableCellRenderer

# internal imports
from application.application import Application
from application.command.set_domain_dict_value_command import SetDomainDictValueCommand

from infrastructure.event_bus import EventBus
from infrastructure.repository.value_repository import ValueRepository


class Table(JTable):
    @staticmethod
    def _create_cell_renderer(column_name):
        pass

    def __init__(self):
        super(Table, self).__init__()
        self._model = self._create_model()
        self._prev_main_selected_object_id = None
        self._value_repository = ValueRepository()
        self.setModel(self._model)
        self.setAutoCreateRowSorter(True)
        self.setComponentPopupMenu(self._create_popup_menu())
        self._prepare_cell_renderers()
        self._restore_column_widths()
        EventBus().add_observer(self, [EventBus.EVENT_EXTENSION_UNLOADED])

    # JTable
    def valueChanged(self, event):
        super(Table, self).valueChanged(event)
        if not event.getValueIsAdjusting():
            self._execute_select_objects_command()
            self._execute_select_main_object_command()

    # Events
    def on_event(self, event_code, value):
        if event_code == EventBus.EVENT_EXTENSION_UNLOADED:
            self._save_column_widths()

    def _execute_select_objects_command(self):
        Application.get_instance().execute(
            SetDomainDictValueCommand(
                self._get_domain_dict_type(),
                'object_ids',
                self._model.map_object_indexes_to_ids(
                    [self.convertRowIndexToModel(i) for i in self.getSelectedRows()]
                )
            )
        )

    def _execute_select_main_object_command(self):
        main_object_id = None
        main_object_index = self.getSelectedRow()
        if main_object_index != -1:
            main_object_id = self._model.map_object_indexes_to_ids([self.convertRowIndexToModel(main_object_index)])[0]
        if main_object_id != self._prev_main_selected_object_id:
            Application.get_instance().execute(SetDomainDictValueCommand(
                self._get_domain_dict_type(),
                'main_object_id',
                main_object_id
            ))
            self._prev_main_selected_object_id = main_object_id

    def _prepare_cell_renderers(self):
        default_cell_renderer = DefaultTableCellRenderer()
        default_cell_renderer.setHorizontalAlignment(JLabel.LEFT)
        for column_name, column in self._get_columns():
            cell_renderer = self._create_cell_renderer(column_name)
            if cell_renderer is None:
                cell_renderer = default_cell_renderer
            column.setCellRenderer(cell_renderer)

    def _restore_column_widths(self):
        column_widths = self._value_repository.get(self._get_storage_key(), None)
        if column_widths:
            for column_name, column in self._get_columns():
                column.setPreferredWidth(column_widths[column_name])

    def _save_column_widths(self):
        column_widths = {}
        for column_name, column in self._get_columns():
            column_widths[column_name] = column.getWidth()
        self._value_repository.set(self._get_storage_key(), column_widths)

    def _get_columns(self):
        for i in range(self.getColumnModel().getColumnCount()):
            yield self.getColumnName(i), self.getColumnModel().getColumn(i)

    def _get_storage_key(self):
        return self.__class__.__name__
