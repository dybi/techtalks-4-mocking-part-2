from data_source import introduce_myself


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = Pet()

    def make_freinds(self):
        return introduce_myself(self.name)


class Pet(object):
    def make_noise(self):
        return "Woof!"
