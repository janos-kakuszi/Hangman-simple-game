import sys
import os
import time
import random

word = []

class Hangman():
   def __init__(self):
       print("Welcome to Hangman, are you ready?")
       print("(1)Yes, I am already dead.\n(2)No, I want to live!")
       user_choice_1 = input("->")

       if user_choice_1 == '1':
           print("\nLoading files, please wait...")
           time.sleep(2)
           os.system('clear')
           self.start_game()
       elif user_choice_1 == '2':
           print("\nBye now...")
           exit()
       else:
           print("\n Invalid input, please repeat your choice in correct form\n")
           self.__init__()

   def start_game(self):
       self.core_game()

   def core_game(self):

       guesses = 0
       letters_used = ""
       lang = input("What language do you want?\n"
                    "If Hungarian, please enter hun, if english enter eng.")

       if lang == "hun" or lang == "Hun":
           the_word = (random.choice(open("for_game_hungarian.md", 'r').readlines()))
           word.append(the_word)
           print(the_word)
       elif lang == "eng" or lang == "Eng":
           the_word = (random.choice(open("for_game_english.md", 'r').readlines()))
           word.append(the_word)
           print(the_word)
       else:
            print("\nInvalid input, please repeat your choice in correct form\n")
            self.core_game()

       progress = ["_", "_", "_", "_", "_"]

       while guesses < 6:
           guess = input("Guess a letter ->")
           if guess in the_word and guess not in letters_used:
               print("RIGHT!")
               letters_used += "," + guess
               self.hangman_graphic(guesses)
               print("Progress: " +
                     self.progress_updater(guess, the_word, progress))
               print("Letter used: " + letters_used)
           elif guess not in the_word and guess not in letters_used:
               guesses += 1
               print("WRONG!")
               letters_used += "," + guess
               self.hangman_graphic(guesses)
               print("Progress: " + "".join(progress))
               print("Letter used: " + letters_used)
           else:
               print("That's the wrong letter")
               print("Try again!")

   def hangman_graphic(self, guesses):
       if guesses == 0:
           print("________      ")
           print("|      |      ")
           print("|             ")
           print("|             ")
           print("|             ")
           print("|             ")
       elif guesses == 1:
           print("________      ")
           print("|      |      ")
           print("|      0      ")
           print("|             ")
           print("|             ")
           print("|             ")
       elif guesses == 2:
           print("________      ")
           print("|      |      ")
           print("|      0      ")
           print("|     /       ")
           print("|             ")
           print("|             ")
       elif guesses == 3:
           print("________      ")
           print("|      |      ")
           print("|      0      ")
           print("|     /|      ")
           print("|             ")
           print("|             ")
       elif guesses == 4:
           print("________      ")
           print("|      |      ")
           print("|      0      ")
           print("|     /|\     ")
           print("|             ")
           print("|             ")
       elif guesses == 5:
           print("________      ")
           print("|      |      ")
           print("|      0      ")
           print("|     /|\     ")
           print("|     /       ")
           print("|             ")
       else:
           print("________      ")
           print("|      |      ")
           print("|      0      ")
           print("|     /|\     ")
           print("|     / \     ")
           print("|             ")
           print("GAME OVER!")
           print("The word was:", word)

           self.__init__() # to retry

   def progress_updater(self, guess, the_word, progress):
       i = 0
       while i < len(the_word):
           if guess == the_word[i]:
               progress[i] = guess
               i += 1
           else:
               i += 1

       return "".join(progress)
word = []
game = Hangman()
