from java.lang import Runnable

# internal imports
from application.application import Application


class ExecuteApplicationCommandInGuiThread(Runnable):
    def __init__(self, command):
        self.command = command

    def run(self):
        Application.get_instance().execute(self.command)
