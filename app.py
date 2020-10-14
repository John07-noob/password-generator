# This Password-Generator created by John07-noob
# Sep/7/2020

import random

# Variables
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
super = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%()[]~'"

print("Welcome to Password Generator")
print("You want only alphabet, number or super?")
while True:
    # Ask user input for alpha/num/super
    ask_user = input("Please insert here (alpha/num/super): ")
    if ask_user == "alpha":
        # Ask user how long password should be
        password_range = int(input("How long you want: "))
        # Choose random chars in alpha variable and range for the password should be (password_range)
        x = "".join(random.choice(alpha) for i in range(password_range))
        print("The result:", x)
        # After print the result, this code out of loop
        break
    elif ask_user == "num":
        password_range = int(input("How long you want: "))
        # Choose random chars in num variable and range for the password should be (password_range)
        x = "".join(random.choice(num) for i in range(password_range))
        print("The result:", x)
        break
    elif ask_user == "super":
        password_range = int(input("How long you want: "))
        # Choose random chars in super variable and range for the password should be (password_range)
        x = "".join(random.choice(super) for i in range(password_range))
        print("The result:", x)
        break
    else:
        print("Please insert the valid answer")
