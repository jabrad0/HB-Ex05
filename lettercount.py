from sys import argv
import string

script, filename = argv

def main():
    # Initialize a list letters in the alphabet
    alphabet = string.lowercase
    list_alpha = list(alphabet)

    
    open_file = open(filename)
    file_lowertext = open_file.read().lower()
    list_file_lowertext = list(file_lowertext)
    

    for letter in list_alpha:
        count_letters = list_file_lowertext.count(letter)
        if count_letters != 0:
            print letter, count_letters

    open_file.close()



if __name__ == '__main__':
    main()