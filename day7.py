# day 7 of 100 days python

# hangman challenge
import random

word_list = ["tiger","lion","zebra","monkey"]



# user_guess_letter = input("Please enter your guess letter: ")
chosen_word = random.choice(word_list)
match_letters = ['_'] * len(chosen_word)
print(match_letters)
life = len(chosen_word)

while '_' in match_letters and life > 0:
    user_guess_letter = input("Please enter your guess letter: ").lower()

    # for position in range(len(chosen_word)):
    #     letter = chosen_word[position]
    #     if user_guess_letter == letter:
    #         match_letters[position] = user_guess_letter
    #         word_progress = "".join(match_letters)
    #         print(word_progress)
    #     else:
    #         word_progress = "".join(match_letters)
    #         print(word_progress)
    #         life -= 1
    if user_guess_letter in chosen_word:
        idx = chosen_word.index(user_guess_letter)
        match_letters[idx] = user_guess_letter
        word_progress = "".join(match_letters)
        if user_guess_letter in match_letters:
            life -= 1
        print(word_progress)
    else:
        word_progress = "".join(match_letters)
        print(word_progress)
        life -= 1
print("The correct word was",chosen_word)
if '_' not in match_letters and life > 0:
    print("Oww, You win!")
else:
    print("Ohh, You loss!")

word_progress = "".join(match_letters)
print(word_progress)