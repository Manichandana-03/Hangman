import random
from hangman_art import stages
from hangman_words import logo,word_list

lives=6

chosen_word=random.choice(word_list)

print(f"Secret the chosen word is: {chosen_word}" )

word_length=len(chosen_word)

display=[]
for letter in range(word_length):
    display += "_"
print(display)

end_of_game=False

while  not end_of_game:
    guess=input("Guess a letter:  ").lower()
    if guess in display:
        print(f"You've already guessed { guess}")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if guess==letter:
            display[position]=letter
            print(f"")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.You lose a life")
        lives -=1
        if lives==0:
            end_of_game=True
            print("you lose")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You won")
    print(stages[lives])


