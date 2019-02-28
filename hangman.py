# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:46:11 2018

@author: ASP
"""

# Simple hangman game:  solution to challenge 26


def hangman():
    pics = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
    guessed = []
    answer = input(str("Please type one word\n"))
    newList = ['_' for i in range(len(answer))]

    print('\n'*300)
    i = 1         # counter for guesses

    while i <= 12:          # 12 total guesses before lost
        print(len(ansList), 'letters', newList)

        # request input from player = 1 alpha char
        guess = input(str(f"Guess #{i} "))
        guessed.append(guess)

        if guess in ansList:

            if ansList.count(guess) == 1:
                # print the position of the letter
                guessIndex = ansList.index(guess)
                print("letter exists at position", guessIndex + 1)
                newList[guessIndex] = guess

            else:


            if newList == ansList:
                print("player 2 wins \n\n")
                print('Congrats! \n\n')

                return
        else:
            print(pics[i])
            print('Incorrect guess')
        i = i+1


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

guesses()
