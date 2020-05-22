from javax.swing import JScrollPane
from javax.swing import JSplitPane
from javax.swing import JTabbedPane

# internal imports
from items_table import ItemsTable

from infrastructure.burp.http_dialog_editor import HttpDialogEditor


class ItemsView(JSplitPane):
    def __init__(self):
        super(ItemsView, self).__init__(JSplitPane.VERTICAL_SPLIT)
        self._prepare_table_view()
        self._prepare_http_dialog_editor_view()

    def _prepare_table_view(self):
        self.setTopComponent(JScrollPane(ItemsTable()))

    def _prepare_http_dialog_editor_view(self):
        editor = HttpDialogEditor()
        editor_view = JTabbedPane()
        editor_view.addTab('Request', editor.get_request_editor_component())
        editor_view.addTab('Response', editor.get_response_editor_component())
        self.setBottomComponent(editor_view)
