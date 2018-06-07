from data_source import introduce_myself


class Person(object):
    def __init__(self, name):
        self.name = name

    def make_freinds(self):
        return introduce_myself(self.name)
