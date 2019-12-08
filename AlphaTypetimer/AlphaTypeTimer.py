from datetime import datetime

print("Type the full alphabet as fast as you can.  Must be 100% accurate.")
input("press enter when ready, and press enter when finished")
a = datetime.now()
alpha = str(input())
input()
b = datetime.now()
alphabet = "abcdefghijklmnopqrstuvwxyz"
c = b - a

if alphabet == alpha:
    print(c)
else: print("sorry there was an error in your input. try again")



