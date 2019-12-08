import random 

## code is the computer generated 4digit code
code = []
for a in range(4):
    b = random.randint(0,9)
    code.append(b)
    a += 1
    
## function for guess digits from user input 
guess = []
print("Please guess the 4 digit code")
def usrGuess():
    guess.clear()
    print("Type one number 0-9 then Enter")
    x = 0
    for x in range(4):
        i = int(input(f"Guess #{x+1}: "))
        guess.append(i)
        x += 1
    return guess


##function to compare comp code vs guessed code number by number
def compareResult():
    i = 0
    for i in range(len(code)):
        if code[i] == guess[i]:
            print (f"Guess #{i+1} is correct")
        else: print (f"Guess #{i+1} is incorrect")
        print("\n")
        
##function to check if guessed number exists in computer code                     
def compareNums():
    i = 0
    while i <= 3:
        nums = guess[i] in code
        print (f"Guess #{i+1} is", nums)
        i += 1              
        
        
    


    
guesses = 0
while guesses < 4:
    usrGuess()
    compareResult()
    compareNums()
    guesses += 1

