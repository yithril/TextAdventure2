from glob import glob
import os.path
import json

class File_Loader(object):
    def __init__(self, path):
        self._path = path

    def load(self, id):
        globpattern = os.path.join(self._path, "%d_*.json"%id)
        file_path = glob(globpattern)[0]
        with open(file_path) as json_data:
             return json.load(json_data)

