import string

def get_available_letters(letters_guessed):
    available_letters = list(string.ascii_lowercase)
    print (available_letters)
    for letter in letters_guessed:
        if letter in available_letters:
            print(letter)
            available_letters.pop(available_letters.index(letter))
    return "".join(available_letters)

letters_guessed = ['e', 'i', 'k', 'p', 'r', 's','z']
print(get_available_letters(letters_guessed))
