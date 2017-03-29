from InputFileValidator import InputFileValidator
from LogParser import LogParser
import argparse

parser = argparse.ArgumentParser(description='This is a Python version of grep function.')
parser.add_argument('name_of_file', type=str,
                    help='an name of the file to check')
parser.add_argument('string_to_search', type=str,
                    help='full phrase to search in the file')
args = parser.parse_args()
name_of_file = args.name_of_file
string_to_search = args.string_to_search
file_validator = InputFileValidator(name_of_file)
if file_validator.validate():
    log_parser = LogParser(file_validator.get_list_of_files(), string_to_search)
    log_parser.parselog()







