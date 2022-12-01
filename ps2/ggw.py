def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ("_ " * len(secret_word)).split() #initialize guess
    print(guessed_word)
    for letter in letters_guessed:
        for ind in range(0,len(secret_word)):
            if letter == secret_word[ind]:
                print(ind)
                guessed_word[ind] = letter
    return "".join(guessed_word)

secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
letters_guessed.pop()
print(letters_guessed)
print(get_guessed_word(secret_word, letters_guessed))
