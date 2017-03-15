import re

class WordCounter:
    def __init__(self, file_list):
        self.all_word_count = []
        self._file_list = file_list

    def returning_count_of_words(self):
        iterator=0
        for file in self._file_list:
            iterator=iterator+1
            file_to_read = open(file, 'r')
            file_content = file_to_read.read()
            counter=0
            for line in file_content:
                each_wordlist=line.split(" ")
                for each_word in each_wordlist:
                    if re.match("[A-Za-z]",each_word):
                        counter = counter+1
            self.all_word_count.append(counter)
            file_to_read.close()
        print(self.all_word_count)
    def get_list_of_amount(self):
        return self.all_word_count