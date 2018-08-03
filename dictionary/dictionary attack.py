#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords


#Write logic to see if the password is in the dictionary file below here:

dictionary = []

for a in f:
    dictionary.append(a.strip())

answer="yes"

while answer == "yes":

    test_password = input("Type in a trial password: ")

    test_password.strip()
    test_password.lower
    test_password.split('_')
    test_password.split('.')
    test_password.split(' ')
    test_password.split('!')
    test_password.split('@')
    test_password.split('#')
    test_password.split('$')
    test_password.split('%')
    test_password.split('^')
    test_password.split('&')
    test_password.split('*')
    test_password.split('(')
    test_password.split(')')
    test_password.split('1')
    test_password.split('2')
    test_password.split('3')
    test_password.split('4')
    test_password.split('5')
    test_password.split('6')
    test_password.split('7')
    test_password.split('8')
    test_password.split('9')
    test_password.split('0')
    
    
    if test_password in dictionary:
        print("That's a weak password.")
    else:
        print("Secure password")


    answer = input("Want to try again? yes or no: ")
            
    














