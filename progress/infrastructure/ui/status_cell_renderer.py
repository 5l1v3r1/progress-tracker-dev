from java.awt import Color
from javax.swing.table import DefaultTableCellRenderer


class StatusCellRenderer(DefaultTableCellRenderer):
    _LABEL_COLORS = {
        # foreground, background
        'Blocked': [Color(0xf0f0f0), Color(0x1B1C1D)],
        'Done': [Color(0x1B1C1D), Color(0x21BA45)],
        'Ignored': [Color(0x1B1C1D), Color(0x767676)],
        'In progress': [Color(0x1B1C1D), Color(0xFBBD08)],
        'Postponed': [Color(0x1B1C1D), Color(0xF2711C)],
        'New': [Color(0x1B1C1D), Color(0xDB2828)],
    }

    def getTableCellRendererComponent(self, table, value, is_selected, has_focus, row, col):
        cell = super(StatusCellRenderer, self).getTableCellRendererComponent(
            table, value, is_selected, has_focus, row, col
        )
        cell.setForeground(
            table.getSelectionForeground() if is_selected else self._LABEL_COLORS[value][0]
        )
        cell.setBackground(
            table.getSelectionBackground() if is_selected else self._LABEL_COLORS[value][1]
        )
        return cell
