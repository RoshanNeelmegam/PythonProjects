#importing essentials
import random
from artworks import logo, stages
from wordlist import word_list
import os

#LOGO and dashes
print(logo)
random_Word = random.choice(word_list)
# print(random_Word)
dashes = []
word = []
for letters in random_Word:
    dashes.append("_")
# print(" ".join(dashes))
for letters in random_Word:
    word.append(letters)
#print(word)

#game logic
game_Over = False
danger_Level = 6
while not game_Over:
    print(" ".join(dashes))
    guess = input("Guess a letter: ")
    if guess in word:
         os.system('cls')
         # This will print hangman 
         if danger_Level < 6:
             print(stages[danger_Level])
         position = word.index(guess)
         word[position] = "-"
         dashes[position] = guess
        # This will break out of code if word right
         if '_' not in dashes:
             print("You Won!!!")
             break
        # This will get executed if guess is right
         print("Your guess is right! Guess the next letter.")
    else: 
          os.system('cls')
          print(stages[danger_Level])
          danger_Level -= 1
          # This will stop the game if hangman is fully drawn
          if danger_Level == -1:
            print(f"Game Over!!! You loose. The word is {random_Word}.")
            break
          print("Your guess is wrong! Guess again.")
    

   
        
    
    

