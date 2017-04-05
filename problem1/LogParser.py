class LogParser:
    def __init__(self, file_list, string):
        self._file_list = file_list
        self._string_to_search = string

    def parselog(self):
        string = []
        for file in self._file_list:
            file_to_read = open(file, 'r')
            file_content=file_to_read.read()
            lines = file_content.split('\n')
            for line in lines:
                if self._string_to_search in line:
                    if "****" in line:
                        continue
                    string.append(line.split())
            file_to_read.close()
        for x in range(0, len(string)):
            del string[x][0:2]
        for x in range(0, len(string)):
            del string[x][1:2]
        for x in range(0, len(string)):
            del string[x][2:]
        new_string=[x for x in string if len(x)>0]

        return new_string
