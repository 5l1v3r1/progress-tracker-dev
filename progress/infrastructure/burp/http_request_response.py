from burp import IHttpRequestResponse


class HttpRequestResponse(IHttpRequestResponse):
    def __init__(self, http_service, request, response):
        self._http_service = http_service
        self._request = request
        self._response = response

    def getComment(self):
        pass

    def getHighlight(self):
        pass

    def getHttpService(self):
        return self._http_service

    def getRequest(self):
        return self._request

    def getResponse(self):
        return self._response

    def setComment(self, comment):
        pass

    def setHighlight(self, color):
        pass

    def setHttpService(self, http_service):
        pass

    def setRequest(self, message):
        pass

    def setResponse(self, message):
        pass
