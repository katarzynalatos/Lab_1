import argparse
from InputFileValidator import InputFileValidator
from WordCounter import WordCounter

parser = argparse.ArgumentParser(description='This is a Python version of grep function.')
parser.add_argument('name_of_file', type=str,
                    help='an name of the file to check')
args = parser.parse_args()
name_of_file = args.name_of_file
word_searcher = InputFileValidator(name_of_file)
if word_searcher.validate():
    To_count_all_word = WordCounter(word_searcher.get_list_of_files())
    To_count_all_word.returning_count_of_words()
    list = To_count_all_word.get_list_of_amount()
    print(list)