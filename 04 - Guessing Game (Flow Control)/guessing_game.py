import random
# Explain the game
print("Let's play a game....")
print("I will pick a number, 1 - 100, and you have to guess it. Now let's play!")
# Get a random integer
answer = random.randint(1, 100)
# Initialize guess to 0
guess = 0
# Ask for the first guess and start the counter at 1
print("Now guess a number between 1 and 100")
i = 1
# Start the game(while loop)
while guess != answer:
    # Take whatever the user inputs in the loop and store it in guess.
    guess = input()
    # Initially assume an integer
    isInt = True
    for char in guess:
        # if each char in guess is number, just continue
        if char in "0123456789":
            continue
        else:
            # if we find a non-int, inform the user to only use ints
            print("Please enter an integer")
            # set as not an int
            isInt = False
            # break out of loop
            break
    # Check if the guess is an int
    if isInt:
        # Turn guess into an integer
        guess = int(guess)
        # Check if guess is between 1 and 100
        if 1 <= guess and guess <= 100:
            # Check if the guess is correct
            if guess == answer:
                print("Well well, congratulations. You got it in {} guesses".format(i))
            elif guess < answer:
                print("Nope! Guess higher next time...")
                i += 1
            elif guess > answer:
                print("Nope! Guess lower next time...")
                i += 1
        else:
            print("Please enter a number that is 1 or greater and 100 or less.")




