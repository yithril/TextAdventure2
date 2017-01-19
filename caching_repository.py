
class Caching_Repository(object):
    def __init__(self, repository, cache = {}):
        self._repository = repository
        self._cache = cache

    def get_by_id(self,id):
        if id not in self._cache:
            self._cache[id] = self._repository.get_by_id(id)
        return self._cache[id]
