# import time and sys for the laughing at the end
from time import sleep as pause
from sys import stdout

# Ask for the user's name
# Store it in the "name" variable
name = input("Hi what is your name?\n")

# Ask the user if they would like to hear a knock-knock joke
print("Hi {}, would you like to hear a knock-knock joke?".format(name))

# Create a yes_answers list
yes_answers = ["yes", "yeah", "sure", "uh-huh", "of course", "totally", "definitely", "ok"]

# Store their answer in a doJoke variable
do_joke = input().lower()

# Strip the doJoke of all non-alphabetical characters
# Create a new variable to store the do_joke in as we go
new_do_joke = ""
for char in do_joke:
    if char in "abcdefghijklmnopqrstuvwxyz":
        new_do_joke += char
# reassign the do_joke variable to the new one
do_joke = new_do_joke

# Test the user's answer
# if it is some form of yes, do the joke
if do_joke in yes_answers:
    # loop 3 times to ask knock knock
    for i in range(0, 3):
        print("Knock-knock")
        input()
        # Say spam is there each time
        print("Spam")
        input()
    # After that, do it one more time
    print("Knock-knock")
    input()
    # Now say Orange is there
    print("Orange")
    input()
    # Ask them aren't they glad I didn't say spam again
    print("Orange you glad I didn't say spam?")
    # Wait before laughing
    pause(2)
    # Laugh at them now
    for i in range (0, 20):
        # Print "HA" 20 times
        print("HA ", end="", flush=True)
        # pause between each "HA"
        pause(.3)
    # At the end, print out a smile with no new line
    stdout.write(":)")
else:
    print("Oh well, maybe next time. Bye!")

