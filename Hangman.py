from random import *

word ="alphabet"

guesses = [7]
maxfails = 9
x=0
list=[]
for i in range(len(word)):
    list.append("_")


while x == 0:
    guess = input("Guess a letter: ")
    while(guess.isalpha() == False):
        print("That's not a letter")

    if guess in word:
        print ("Good, now the next letter.")
        for i in range(len(word)):
            if guess == word[i]:
                list[i] = guess
        

    elif guess not in word:
        print ("Try Again")
        maxfails = maxfails - 1
    if maxfails == 0:
        x=1
    if len(list) == len(word):
        x = 1
    








##len(guess)==1


##input("Type a word for someone to guess: ")

### Converts the word to lowercase
##list = list.lower()
##
### Checks if only letters are present
##while(list.isalpha() == False):
##	print("That's not a word!")
