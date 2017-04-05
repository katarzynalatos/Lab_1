from AbstractValidator import AbstractValidator
from os.path import isfile
from os.path import isdir
from os import listdir



class InputFileValidator(AbstractValidator):
    def __init__(self, name):
        self._name=name
        self._files = []

    def validate(self):
        if isfile(self._name):
            self._files.append(self._name)
            return True
        elif isdir(self._name):
            self._files = [self._name+"/"+files for files in listdir(self._name) if isfile(self._name+"/"+files)]
            if len(self._files) > 0:
                return True
            else:
                return False
        else:
            return False

    def get_list_of_files(self):
        return self._files
