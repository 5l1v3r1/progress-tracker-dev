from burp import IHttpRequestResponse
from email.utils import formatdate

import json

# internal imports
from infrastructure.burp.burp_callbacks import BurpCallbacks
from infrastructure.burp.burp_helpers import BurpHelpers
from infrastructure.burp.http_request_response import HttpRequestResponse


class ValueRepository(IHttpRequestResponse):
    _HOST = 'progress-plugin-storage-f2a8e0dd-7b23-4617-b556-c3b88edf6895'
    _PORT = 443
    _PROTOCOL = 'https'

    def __init__(self):
        self._burp_callbacks = BurpCallbacks.get_instance()
        self._burp_helpers = BurpHelpers.get_instance()

    def get(self, key, default_value):
        http_request_responses = self._burp_callbacks.getSiteMap(self._prepare_prefix(key))
        if len(http_request_responses) == 1:
            response = http_request_responses[0].getResponse()
            response_info = self._burp_helpers.analyzeResponse(response)
            return json.loads(self._burp_helpers.bytesToString(response[response_info.getBodyOffset():]))
        return default_value

    def set(self, key, value):
        self._burp_callbacks.addToSiteMap(
            HttpRequestResponse(
                self._burp_helpers.buildHttpService(self._HOST, self._PORT, self._PROTOCOL),
                self._prepare_request(key),
                self._prepare_response(json.dumps(value))
            )
        )

    def _prepare_prefix(self, key):
        return '%s://%s/%s' % (self._PROTOCOL, self._HOST, key)

    def _prepare_request(self, key):
        request  = 'GET /%s HTTP/1.1\r\n' % key
        request += 'Host: %s\r\n' % self._HOST
        request += '\r\n'
        return self._burp_helpers.stringToBytes(request)

    def _prepare_response(self, value):
        date = formatdate(timeval=None, localtime=False, usegmt=True)
        response  = 'HTTP/1.1 200 OK\r\n'
        response += 'Date: %s\r\n' % date
        response += 'Last-Modified: %s\r\n' % date
        response += 'Content-Type: text/plain\r\n'
        response += 'Content-Length: %d\r\n' % len(value)
        response += '\r\n'
        response += value
        return self._burp_helpers.stringToBytes(response)
