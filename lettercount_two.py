from sys import argv
import string

script, filename = argv

def main():
    # Initialize a list letters in the alphabet
    letters = []
    alphabet = string.lowercase
    for letter in alphabet:
        letters.append(letter)
    
    count_letters = [0] * 26

    open_file = open(filename)
    file_lowercase_text = open_file.read().lower()
    
    for character in file_lowercase_text:
        if character in letters:
            alphabet_index = letters.index(character)
            count_letters[alphabet_index] += 1
    
    for i in range(26):
        print letters[i], count_letters[i]



if __name__ == '__main__':
    main()