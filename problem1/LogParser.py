class LogParser:
    def __init__(self, file_list, string):
        self._file_list = file_list
        self._string_to_search = string

    def parselog(self):
        for file in self._file_list:
            file_to_read = open(file, 'r')
            file_content=file_to_read.read()
            lines = file_content.split('\n')
            for line in lines:
                if self._string_to_search in line:
                    print(line)
            file_to_read.close()
