from burp import IMessageEditorController

# internal imports
from burp_callbacks import BurpCallbacks
from burp_helpers import BurpHelpers

from common.singleton import Singleton


class HttpDialogEditor(IMessageEditorController):
    __metaclass__ = Singleton

    def __init__(self):
        self._burp_callbacks = BurpCallbacks.get_instance()
        self._burp_helpers = BurpHelpers.get_instance()
        self._request_editor = self._burp_callbacks.createMessageEditor(self, False)
        self._response_editor = self._burp_callbacks.createMessageEditor(self, False)
        self._item = None

    # IMessageEditorController
    def getHttpService(self):
        return self._burp_helpers.buildHttpService(
            self._item.get_host(),
            self._item.get_port(),
            self._item.get_protocol()
        )

    def getRequest(self):
        return self._item.get_request().getBuffer()

    def getResponse(self):
        return self._item.get_response().getBuffer()

    def get_request_editor_component(self):
        return self._request_editor.getComponent()

    def get_response_editor_component(self):
        return self._response_editor.getComponent()

    def display(self, item):
        if item is not None:
            self._item = item
            self._request_editor.setMessage(self._item.get_request().getBuffer(), True)
            self._response_editor.setMessage(self._item.get_response().getBuffer(), False)
