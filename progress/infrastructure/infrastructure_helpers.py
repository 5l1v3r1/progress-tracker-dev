class InfrastructureHelpers(object):
    @staticmethod
    def join(values):
        return ','.join(values)

    @staticmethod
    def split(value):
        return value.replace(',', ' ').split()
