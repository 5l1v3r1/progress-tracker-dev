class BurpCallbacks(object):
    _instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        return BurpCallbacks._instance

    @staticmethod
    def set_instance(instance):
        BurpCallbacks._instance = instance
