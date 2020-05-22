from java.awt import Frame
from javax.swing import JFileChooser
from javax.swing import JOptionPane

# internal imports
from infrastructure.infrastructure_helpers import InfrastructureHelpers


class UIHelpers(object):
    @staticmethod
    def ask_for_value(title, message, initial_value, is_value_array):
        value = JOptionPane.showInputDialog(
            UIHelpers._get_parent_frame(),
            message,
            title,
            JOptionPane.PLAIN_MESSAGE,
            None,
            None,
            InfrastructureHelpers.join(initial_value) if is_value_array else initial_value
        )
        if value is not None and is_value_array:
            return InfrastructureHelpers.split(value)
        return value

    @staticmethod
    def choose_file():
        file_chooser = JFileChooser()
        if file_chooser.showSaveDialog(UIHelpers._get_parent_frame()) == JFileChooser.APPROVE_OPTION:
            return str(file_chooser.getSelectedFile())

    @staticmethod
    def confirm(question):
        chosen_option = JOptionPane.showConfirmDialog(
            UIHelpers._get_parent_frame(),
            question,
            'Confirm',
            JOptionPane.YES_NO_OPTION,
            JOptionPane.WARNING_MESSAGE
        )
        return chosen_option == JOptionPane.YES_OPTION

    @staticmethod
    def display_error(message):
        JOptionPane.showMessageDialog(
            UIHelpers._get_parent_frame(),
            message,
            'Error',
            JOptionPane.ERROR_MESSAGE
        )

    @staticmethod
    def _get_parent_frame():
        for frame in Frame.getFrames():
            if 'burp suite' in frame.getTitle().lower():
                return frame
