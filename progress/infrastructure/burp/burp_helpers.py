class BurpHelpers(object):
    _instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        return BurpHelpers._instance

    @staticmethod
    def set_instance(instance):
        BurpHelpers._instance = instance
