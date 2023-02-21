import random
import hangmanArt
import hangmanWords
import os
import time

word_list = hangmanWords.word_list
stages = hangmanArt.stages
display = []
chosen_word = random.choice(word_list)
num_of_lives = 6
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

for letter in chosen_word:
    display.append("_")

while num_of_lives != 0:
    print(hangmanArt.logo)
    incomplete_word = ' '.join(display)
    print(incomplete_word)
    print(stages[num_of_lives])
    # print(chosen_word)
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"\nYou entered the letter '{guess}' more than once.")


    for position in range(0 , len(chosen_word)):
        if chosen_word[position] == guess and display[position] == "_":
            display[position] = guess
            if "_" not in display:
                print(f"\nThe word was: {chosen_word}")
                print("You win!")
                num_of_lives = 0


    if guess in chosen_word:
        print("\nYou were right")


    if guess not in display:
        num_of_lives -= 1
        print(f"\nThe letter '{guess}' isn't in the word. ")
        print(f"Lives: {num_of_lives}")
        

    if num_of_lives != 0:    
        time.sleep(2)    
        clearConsole()


if "_" in display:
    print(f"\nThe word was: {chosen_word}")
    print("You lose!")