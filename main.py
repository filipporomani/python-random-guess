from random import choice
import string

alphabet = string.ascii_letters + string.digits + string.punctuation + string.whitespace

to_guess = input('Enter a word to guess: ')

found = [False] * len(to_guess)
reconstructed = ['_'] * len(to_guess)

guesses = []

while False in found:
    guess = choice(alphabet)
    guesses.append(guess)
    print('Guessing', guess)
    for i, letter in enumerate(to_guess):
        if letter == guess:
            found[i] = True
            reconstructed[i] = letter
            
print("\n\n\n")            
print('Found', to_guess, 'in', len(guesses), 'guesses')
print(''.join(reconstructed))
