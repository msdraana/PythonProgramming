import random
import hangman_art

print(hangman_art.logo)
word_list = ['bangla', 'english', 'physics', 'chemistry', 'math']
chosen_word = random.choice(word_list)
print(f"Guess word is: {chosen_word}")

display = []
word_len = len(chosen_word)
for char in range(word_len):
    display += '_'
print(display)

end_of_game = False
lives = 0
while not end_of_game:
    guess = input("Guess a Letter: ").lower()

    if guess in display:
        print(f"You\'ve already guessed: {guess}")
    for positon in range(word_len):
        letter = chosen_word[positon]
        if letter == guess:
            display[positon] = letter
    
    if guess not in chosen_word:
        print(f"You guessed: {guess}, that\'s not in the word. You lose a life.")
        lives += 1
        if lives == 6:
            end_of_game = True
            print("You Lose.")

    if '_' not in display:
        end_of_game = True
        print("You Win.")
    print(display)
            
    print(hangman_art.stages[lives])


# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Worng")