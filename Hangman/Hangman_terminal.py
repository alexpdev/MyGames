# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:46:11 2018

@author: ASP
"""

# Simple hangman game:  solution to challenge 26




p1 = """                                    \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""
p2 = """                                    \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""
p3 = """                                    \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
             |                  |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""
p4 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
           --|                  |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""
p5 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
           --|--                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""


p6 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
          o--|--                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""

p7 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
          o--|--o               |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""

p8 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
          o--|--o               |            \n
             |                  |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""
p9 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
          o--|--o               |            \n
             |                  |            \n
            /                   |            \n
           /                    |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""

p10 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
          o--|--o               |            \n
             |                  |            \n
            /\                  |            \n
           /  \                 |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""
p11 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
          o--|--o               |            \n
             |                  |            \n
            /\                  |            \n
          _/  \                 |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""
p12 = """                                     \n
             |------------------|            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
             |                  |            \n
            )@(                 |            \n
          o--|--o               |            \n
             |                  |            \n
            /\                  |            \n
          _/  \_                |            \n
                                |            \n
                                |            \n
                                |            \n
--------------------------------------------"""


def main(figures):
    print("Hangman 2 Player")
    print("\n" * 3)
    total_guesses = 12
    answer,blanks = player_1()
    final = player_2(answer,blanks,figures,total_guesses)
    if final:
        print("congratulations... player2 won!")

def player_1():
    answer = input(str("Player 1: Enter word to begin the game.\n"))
    lst = ['_' for i in range(len(answer))]
    print('\n'* 50)
    return answer,lst

def player_2(answer,blanks,figures,total_guesses):
    guessed = []
    num_wrong = 0
    while num_wrong < total_guesses:
        if not [i for i in answer if i not in guessed]:
            return True
        guess = get_guess(blanks,num_wrong,guessed,answer)
        if guess_is_valid(guess,guessed):
            guessed.append(guess)
            if guess_in_answer(guess,answer):
                print("congratulations you guessed correctly")
                blanks = ["_" if i not in guessed else i for i in answer]
            else:
                print("Sorry that guess was incorrect \n")
                num_wrong += 1
                print(figures[num_wrong])
        else:
            print("Invalid input. Try again.")
    print("game over, player 2 lost")
    print(answer)
    return False


def guess_in_answer(guess,answer):
    if guess in answer:
        return True
    return False

def guess_is_valid(guess,guessed):
    if len(guess) == 1 and guess.isalpha():
        if guess not in guessed:
            return True
    return False

def get_guess(blanks,num_wrong,guessed,answer):
    print("Already Guessed:", ",".join(guessed))
    print("Word:", ''.join(blanks))
    guess = input(str(num_wrong) + " wrong out of 12.  Guess: ")
    print("\n"*2)
    return guess

if __name__ == "__main__":
    figures = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
    main(figures)
