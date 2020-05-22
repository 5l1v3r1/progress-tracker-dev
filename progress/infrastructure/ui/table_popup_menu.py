from java.awt.event import ActionListener
from javax.swing import JMenu
from javax.swing import JMenuItem
from javax.swing import JPopupMenu

# internal imports
from application.application import Application


class TablePopupMenu(JPopupMenu, ActionListener):
    def __init__(self):
        super(TablePopupMenu, self).__init__()
        self._labels = self._prepare_labels()
        self._prepare_menu(self._labels, self)

    # ActionListener
    def actionPerformed(self, event):
        Application.get_instance().execute(self._create_application_command(
            event.getActionCommand()
        ))

    def _prepare_menu(self, labels, parent):
        for label in sorted(labels.keys()):
            if labels[label]:
                menu_item = JMenu(label)
                self._prepare_menu(labels[label], menu_item)
            else:
                menu_item = JMenuItem(label)
                menu_item.addActionListener(self)
            parent.add(menu_item)
