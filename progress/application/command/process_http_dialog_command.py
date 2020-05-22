class ProcessHttpDialogCommand(object):
    def __init__(self, method, request, response, time, tool, url):
        self.method = method
        self.request = request
        self.response = response
        self.time = time
        self.tool = tool
        self.url = url
