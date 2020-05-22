from burp import IBurpExtender
from burp import IExtensionStateListener

# internal imports
from application.application import Application

from infrastructure.event_bus import EventBus
from infrastructure.repository.database import Database
from infrastructure.repository.item_repository import ItemRepository
from infrastructure.repository.path_pattern_repository import PathPatternRepository
from infrastructure.repository.value_repository import ValueRepository
from infrastructure.ui.ui_services import UIServices

from burp_callbacks import BurpCallbacks
from burp_helpers import BurpHelpers
from burp_services import BurpServices
from http_listener import HttpListener
from logger import Logger
from progress_tab import ProgressTab


class BurpExtender(IBurpExtender, IExtensionStateListener):
    def registerExtenderCallbacks(self, callbacks):
        BurpCallbacks.set_instance(callbacks)
        BurpHelpers.set_instance(callbacks.getHelpers())
        self._prepare_application()
        callbacks.addSuiteTab(ProgressTab())
        callbacks.registerExtensionStateListener(self)
        callbacks.registerHttpListener(HttpListener())
        callbacks.setExtensionName('Progress v1.1')

    def extensionUnloaded(self):
        EventBus().notify(EventBus.EVENT_EXTENSION_UNLOADED, None)

    def _prepare_application(self):
        database = Database(Logger())
        Application.set_instance(Application(
            BurpServices(),
            database,
            ItemRepository(database),
            PathPatternRepository(database),
            UIServices(),
            ValueRepository()
        ))
