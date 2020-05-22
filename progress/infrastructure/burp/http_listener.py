from burp import IBurpExtenderCallbacks
from burp import IHttpListener
from datetime import datetime
from javax.swing import SwingUtilities

# internal imports
from application.application import Application
from application.command.make_pre_analyze_validation_command import MakePreAnalyzeValidationCommand
from application.command.make_pre_process_validation_command import MakePreProcessValidationCommand
from application.command.process_http_dialog_command import ProcessHttpDialogCommand

from infrastructure.ui.execute_application_command_in_gui_thread import ExecuteApplicationCommandInGuiThread

from burp_callbacks import BurpCallbacks
from burp_helpers import BurpHelpers


class HttpListener(IHttpListener):
    def __init__(self):
        self._burp_callbacks = BurpCallbacks.get_instance()
        self._burp_helpers = BurpHelpers.get_instance()

    def processHttpMessage(self, tool_flag, message_is_request, message_info):
        if tool_flag not in [
            IBurpExtenderCallbacks.TOOL_PROXY,
            IBurpExtenderCallbacks.TOOL_REPEATER,
            IBurpExtenderCallbacks.TOOL_TARGET,
        ]:
            return
        if message_is_request:
            return
        if not self._is_pre_analyze_validation_pass(tool_flag):
            return
        request_info, response_info = self._analyze_message(message_info)
        if not self._is_pre_process_validation_pass(request_info, response_info):
            return
        SwingUtilities.invokeLater(ExecuteApplicationCommandInGuiThread(
            self._create_process_http_dialog_command(tool_flag, request_info, message_info)
        ))

    def _analyze_message(self, message_info):
        return \
            self._burp_helpers.analyzeRequest(message_info), \
            self._burp_helpers.analyzeResponse(message_info.getResponse())

    def _create_make_pre_analyze_validation_command(self, tool_flag):
        return MakePreAnalyzeValidationCommand(
            self._burp_callbacks.getToolName(tool_flag)
        )

    def _create_make_pre_process_validation_command(self, request_info, response_info):
        return MakePreProcessValidationCommand(
            request_info.getUrl().getPath().rsplit('.', 1)[-1].lower(),
            self._burp_callbacks.isInScope(request_info.getUrl()),
            str(response_info.getStatusCode())
        )

    def _create_process_http_dialog_command(self, tool_flag, request_info, message_info):
        return ProcessHttpDialogCommand(
            request_info.getMethod(),
            self._save_to_temp_file(message_info.getRequest()),
            self._save_to_temp_file(message_info.getResponse()),
            datetime.now().strftime('%H:%M:%S %d %b %Y'),
            self._burp_callbacks.getToolName(tool_flag),
            request_info.getUrl()
        )

    def _save_to_temp_file(self, data):
        return self._burp_callbacks.saveToTempFile(data)

    def _is_pre_analyze_validation_pass(self, tool_flag):
        return Application.get_instance().execute(
            self._create_make_pre_analyze_validation_command(tool_flag)
        )

    def _is_pre_process_validation_pass(self, request_info, response_info):
        return Application.get_instance().execute(
            self._create_make_pre_process_validation_command(request_info, response_info)
        )
