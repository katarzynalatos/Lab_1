class WordCounter:
    def __init__(self, file_list):
        self._word_count = []
        self._chars_count = []
        self._line_count = []
        self._file_list = file_list

    def _counting_chars(self, file_to_read):
        file = open(file_to_read, "r")
        file_content= file.read()
        count =len(file_content)
        file.close()
        return count

    def _counting_words(self, file_to_read):
        file = open(file_to_read, "r")
        file_content = file.read()
        count = len(file_content.split())
        file.close()
        return count


    def _counting_lines(self, file_to_read):
        file = open(file_to_read, "r")
        file_content = file.read()
        count = len(file_content.splitlines())
        file.close()
        return count

    def returning_count_of_chars_words_lines_in_every_file(self):
        for file in self._file_list:

            self._chars_count.append(self._counting_chars(file))
            self._word_count.append(self._counting_words(file))
            self._line_count.append(self._counting_lines(file))

    def returning_count_of_all_chars_words_lines_provided(self):
        self.returning_count_of_chars_words_lines_in_every_file()
        count_chars=0
        count_words=0
        count_lines=0
        for count in self._chars_count:
            count_chars+= count
        for count in self._word_count:
            count_words += count
        for count in self._line_count:
            count_lines += count
        print("Chars: {}".format(count_chars))
        print("Words: {}".format(count_words))
        print("Lines: {}".format(count_lines))
