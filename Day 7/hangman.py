import random
import hangman_art
import hangman_words
#Step 1 

def create_blanks(chosen_word):
    blanks = []
    for _ in range(len_chosen_word):
        blanks.append('_')
    return blanks

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
len_chosen_word=len(chosen_word)
blanks = create_blanks(chosen_word=chosen_word)
dead=False
win = False
lives = 6

while win==False and not dead==True:
    letter_found = False
    guess = input("Guess a letter. ").lower()
    if guess in blanks:
        print(f"You've already guessed {guess}")

  
    for position in range(len_chosen_word):
        letter = chosen_word[position]
        if guess == letter:
            blanks[position] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        print(hangman_art.stages[lives])
        if lives == 0:
            dead=True
            print(f"You lose! The word was {chosen_word}")

    print(f"{' '.join(blanks)}")

    if not '_' in blanks:
        win = True
        print("You win!")

