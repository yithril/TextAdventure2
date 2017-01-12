
class Repository(object):
    def __init__(self, loader, factory):
        self._loader = loader
        self._factory = factory

    def get_by_id(self, id):
        d = self._loader.load(id)
        return self._factory.create(d)



