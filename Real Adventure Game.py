# Update this text to match your story.
start = '''
You woke up one day to find out that you have become a duck. You find yourself in the middle of nowhere with no one in sight and you're trying to find your way back home.
'''

print(start)

print("Where should I go, left or right? Type 'left' to go left or 'right' to go right.") # Update to match your story. 
user_input = input()
while not (user_input == "left" or user_input == "right"):
	print("Invalid response: Type 'left' to go left or 'right' to go right.")
	user_input= input()

if user_input == "left":
    print("You decide to go left and you end up in the ocean instead of a lake. Wow, I'm still not home. Should I go 'left' or 'right'?") # Update to match your story.
    user_input2= input ()
    while not (user_input2 == "left" or user_input2 == "right"):
        print("Invalid response: Type 'left' to go left or 'right' to go right.")
        user_input2= input()
     
    if user_input2 =="left":
            print ("Octopus appears and says: Hello there! Do you want me to help you? Should I say 'yes' or 'no'?")
            user_input3 = input()
            while not (user_input3 == "yes" or user_input3 == "no"):
                print("Invalid response: Type yes or no.")
                user_input3 = input()

            if user_input3 == "yes":
                print("Octopus leads you to home. You say: Yay, thank you!")
            elif user_input3 == "no":
                print("Octopus leaves. You are stranded and cannot find your way back home:( GAME OVER")
    if user_input2 == "right":
            print ("You meet a starfish and it asks you: Do you want to be friends? Should you say 'yes' or 'no'?")
            user_input4 = input()
            while not (user_input4 == "yes" or user_input4 == "no"):
                print("Invalid response: Type yes or no.")
                user_input4 = input()
            if user_input4 == "yes":
                print ("Starfish says yay, you become friends and you live with him. GAME COMPLETED, YOU WIN")
            if user_input4 == "no":
                print ("Starfish cries and you never go home. YOU LOSE")
                    
                   
elif user_input == "right":
    print("You choose to go right and you end up in city. Do you want cross the road? Type 'yes' or 'no'.")
    user_input5= input()
    while not (user_input5 == "yes" or user_input5 == "no"):
                print("Invalid response: Type yes or no.")
                user_input5 = input()

    if user_input5== "yes":
        print("You get caught by animal rescue. Do you want to try and escape? Type 'yes' or 'no'.")
        user_input6= input()
        while not (user_input6 == "yes" or user_input6 == "no"):
                print("Invalid response: Type yes or no.")
                user_input6 = input()

        if user_input6 == "yes":
            print ("You have escaped, but you get attacked by cats in the alleys. YOU LOSE. GAME OVER")
        if user_input6 == "no":
            print ("You have been taken to a new lake and you have decided that it will be your new home. YOU WIN")
    if user_input5 == "no":
        print("You continue going straight and you get picked up by a family. Do you accept your new life? Type 'yes' or 'no'?")
        user_input7= input()
        while not (user_input7 == "yes" or user_input7 == "no"):
                print("Invalid response: Type yes or no.")
                user_input7 = input()

        if user_input7 == "yes":
            print ("You have been adopted by the family. You now eat like a king. YOU WIN")
        if user_input7 == "no":
            print ("You have managed to escape. You roam the streets and get run over by a semi-truck. YOU LOSE")
            
