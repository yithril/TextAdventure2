
class ActionRepo(object):
    def __init__(self, cache = {}):
        self._cache = cache

    def add(self,name,action):
        path = "actions/"
        if action not in self._cache:
            self._cache[name] = action

    def get_by_name(self,name):
        return self._cache[name]