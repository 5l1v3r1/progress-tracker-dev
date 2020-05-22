# internal imports
from burp_callbacks import BurpCallbacks


class BurpServices(object):
    def __init__(self):
        self._burp_callbacks = BurpCallbacks.get_instance()

    def send_items_to_tool(self, items, tool_name):
        for item in items:
            params = [
                item.get_host(),
                item.get_port(),
                item.get_protocol() == 'https',
                item.get_request().getBuffer()
            ]
            if tool_name == 'Repeater':
                params.append(None)
                self._burp_callbacks.sendToRepeater(*params)
            elif tool_name == 'Intruder':
                self._burp_callbacks.sendToIntruder(*params)
            elif tool_name == 'Scanner':
                self._burp_callbacks.doActiveScan(*params)
