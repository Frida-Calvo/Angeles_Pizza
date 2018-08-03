Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
# Update this text to match your story.
start = '''
Duck: hi, i'm lost. help me find my home :) 
'''

print(start)

print("Where should I go, left or right? Type 'left' to go left or 'right' to go right.") # Update to match your story. 
user_input = input()
while not (user_input == "left" or user_input == "right"):
	print("Invalid response: Type 'left' to go left or 'right' to go right.")
	user_input= input()

if user_input == "left":
    print("You decide to go left. Duck: Wow, I'm still not home. Should I go 'left' or 'right'?") # Update to match your story.
    user_input2= input ()
    # Continue code to finish story.
 
elif user_input == "right":
    print("You choose to go right and ...") # Update to match your story.
    
    # Continue code to finish story.
