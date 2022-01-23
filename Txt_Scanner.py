import pathlib, uuid, os
from uuid import UUID


class UserInterface:
    def get_root_and_special_word():
        _user_root = input("\nWelcome to scanner \nPleaase enter the root you want to begin the search with \n") 
        _special_word = input("\nPlease enter the special word you would like to find in the .txt files\n")
        return _user_root, _special_word 



class InputValidation:
    def check_input(_test_path):
        # Test if the given root is valid
        if os.path.isdir(_test_path):
            return True
        else:
            print("There is an Error in your input\nMake sure that your input is a valid root")
            return False



class FilesProcess:
    def get_all_txt_files(success_path):
        all_txt_roots = []
        # Get all roots of .txt fiels.
        for root in pathlib.Path(success_path).glob('**/*.txt'):
            all_txt_roots.append(str(root))  # Convert them to string
        all_txt_roots
        return all_txt_roots

    def process_files(all_txt_roots, special_word):
        for file in all_txt_roots:
            # Sending every txt root we found to the scanner.
            OpenFile.open_file(file, special_word)



class OpenFile:
    def open_file(my_file, special_word):
        with open(my_file) as file:
            # Safety if a very big file dont load it all to memory -> process line by line
            line_number = 0
            file_name = os.path.basename(my_file)
            for line in file:
                line_number += 1
                CheckLine(special_word).check_line(line.strip(), line_number, file_name.capitalize() )



class CheckLine:
    def __init__(self, special_word):
        self._special_word = special_word
        self._word_to_find = ["password", "token"]

    def is_valid_uuid(word, version=4):
        try:
            # Test if string in the .txt is a valid UUID.
            uuid_obj = UUID(uuid.UUID(word).hex, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == word

    def check_line(self, line, line_number, file_name):
        
        if "user" in line and "pass" in line and line.index('user') < line.index('pass'):
            print(f"\n{file_name} \nLine {line_number} contain the word user and pass \n{line}")
        for word in line.split():
            word = word.lower()

            if word in self._word_to_find:
                print(f"\n{file_name} \nLine {line_number} contain the word {word} in it:\n{line}")

            elif CheckLine.is_valid_uuid(word):
                print(f"\n{file_name} \nLine {line_number} {word} is a valid UUID:\n{line}")

            elif word == self._special_word:
                print(f"\n{file_name} \nLine {line_number} contain the special word {word} in it:\n{line}")

            elif len(word) > 80:
                print(f"\n{file_name} \nLine {line_number} the word {word} contain more then 80 charcter:\n{line}")


def main():
        user_root, BC_SPECIAL_WORD = UserInterface.get_root_and_special_word()

        if InputValidation.check_input(user_root):
            txt_file = FilesProcess.get_all_txt_files(user_root)
            if len(txt_file) != 0:
                FilesProcess.process_files(txt_file, BC_SPECIAL_WORD)
            else:
                print("There are no txt files in the root you entered")
            

if __name__ == '__main__':
    main()
