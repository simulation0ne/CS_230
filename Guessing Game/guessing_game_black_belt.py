# Define a check_if_int function
def check_if_int(usr_input):
    is_int = True
    if usr_input:
        for char in usr_input:
            if char in "0123456789":
                continue
            else:
                print("Please enter an integer.")
                is_int = False
                break
    else:
        print("Please type something in.")
        is_int = False
    return is_int
# Explain the game
print("""This game will allow you to choose a range, and a number in that range.  
Then it will guess that number in 10 tries or less.""")
# Ask for the range
min_range_checks = False
while not min_range_checks:
    min_range = input("What is the lowest number you want to allow?\t")
    if check_if_int(min_range):
        min_range = int(min_range)
        min_range_checks = True
max_range_checks = False
while not max_range_checks:
    max_range = input("What is the highest number you want to allow?\t")
    if check_if_int(max_range):
        max_range = int(max_range)
        max_range_checks = True
# Introduce Lisa Neeson
# (This is all an allusion to Liam Neeson's Taken Movie) :)
print("""
I am Lisa Mycin, a retired AI program.
I don't have bitcoin, but what I do have is a very particular skill.
A skill I was programmed to have.
A skill that makes me a number-guessing nightmare to you.
I don't know who you are, but I know your range, and I will guess your number.
Now think of a number and type it in.""")

# This function will calculate the guess
def compute_guess():
    # The volume of the current range of numbers to chose from is determined by
    # subtracting the current min value from the current max value
    num_range = num_range_list[1] - num_range_list[0]
    # The number I was to get will be the midway of that range,
    # which I determine by dividing the volume of the range of numbers by 2,
    # and then adding that to the current minimum
    add_this = num_range//2
    # Then I set that midpoint to be the value returned by this function.
    return num_range_list[0] + add_this


# Here I initialize my correct answer by asking the user to input it
answer_checks = False
while answer_checks == False:
    answer = input()
    if check_if_int(answer):
        answer = int(answer)
        answer_checks = True
while answer < min_range or answer > max_range:
    print("Your number must be between the minimum and maximum values, nice try.  Now try again.")
    answer = int(input())
# The guess is started at the answer plus one so it will not equal the correct answer and my loop will start.
guess = answer + 1
# I will use a list to store the min and the max for the range that is allowed just to make it easier.
num_range_list = [min_range, max_range]
# Here I initialize the number of guesses to 0
hm_guesses = 0

# Now the main loop starts bc the guess does not equal the answer
while guess != answer:
    # I use my function to calculate the guess
    guess = compute_guess()
    # Now I ask if I guessed right.
    usr_feedback = input("Is your number {}?".format(guess)).lower()
    # Now I test what the user says about my guess
    # If they said I need to guess higher, I set my new min to the number I guessed,
    # because I know it can't be lower than that
    if usr_feedback == "higher":
        num_range_list[0] = guess
        # Increment the number of guesses
        hm_guesses += 1
        continue
    # If they said I need to guess lower, I set my new max to the number I guessed,
    # because I know it can't be higher than that
    elif usr_feedback == "lower":
        num_range_list[1] = guess
        # Increment the number of guesses
        hm_guesses += 1
        continue
    # If they said that my guess was correct, I tell them haha I got it! and end the program
    elif usr_feedback == "yes":
        # Increment the number of guesses
        hm_guesses += 1
        print("You remember me? We spoke on the console {} guesses ago. "
              "I told you I would guess your number.".format(hm_guesses))
    # If they don't say 'higher', 'lower', or 'yes', I tell them to do so
    else:
        usr_feedback = input("Please only use 'higher', 'lower', or 'yes'. Hit enter.")