from time import sleep as pause
# Define a get_input function
def get_int_input():
    usr_input = input()
    # Take out any spaces or non-numbers, and turn it into an int
    usr_input = clean_int_input(usr_input)
    # If the input was a decimal, tell the user not to use a decimal
    if usr_input == "is_decimal":
        print("Please do not enter a decimal, agent. Try again.")
        usr_input = get_int_input()
    # If the input was just non-integers, tell the user to use a number
    elif usr_input == "":
        print("Please enter a number, agent. Try again")
        usr_input = get_int_input()
    # Now the input should safely be a number and we can turn it into an int
    usr_input = int(usr_input)
    # Return this cleaned integer to the program
    return usr_input


# Define a clean_input function
def clean_int_input(unclean_input):
    # Initialize the cleaned input to an empty string
    cleaned_int_input = ""
    # Iterate through each character and check it is a number
    for char in unclean_input:
        # If we find a '.', tell the user we do not allow decimals
        if char == ".":
            return "is_decimal"
        # Else, test if the character is a number, and add it to the cleaned input if it is.
        elif char in "0123456789":
            cleaned_int_input += char
        # Else, ignore that character, and continue the loop
        else:
            continue
    # If at the end, there were no int's in the input, return a empty string
    if cleaned_int_input == "":
        return ""
    else:
        # Return the cleaned input to the program
        return cleaned_int_input


# Define a encode_message function
def encode_message():
    message = input("Please enter your secret message to be encoded.\n").lower()
    if message:
        encoded_message = ""
        for char in message:
            char_index = decoding_key.index(char)
            encoded_message += encoding_key[char_index]
        print("Here is your encoded message: " + encoded_message)
        pause(1)
    else:
        print("You cannot enter a blank text, agent. Try again.")
        encode_message()


# Define a decode_message function
def decode_message():
    message = input("Please enter your secret message to be decoded.\n").lower()
    if message:
        decoded_message = ""
        for char in message:
            char_index = encoding_key.index(char)
            decoded_message += decoding_key[char_index]
        print("Here is your decoded message: " + decoded_message.capitalize())
        pause(1)
    else:
        print("You cannot enter a blank text, agent. Try again.")
        decode_message()


# Define a test_selected function
def test_selected(val):
    # If the selected option was 0, wish the agent good luck and quit the program
    if val == 0:
        print("Good luck out there agent.")
        quit()
    # If the selected option was 1, help the agent encode a message
    elif val == 1:
        encode_message()
    # If the selected option was 2, help the agent decode a message
    elif val == 2:
        decode_message()
# This is the randomized key for encoding and decoding messages.
encoding_key = """ukle9.,bh!wx:34fa"stgz 01y278nrv'?p;$mqoij56cd%-/"""
decoding_key = """abcdefghijklmnopqrstuvwxyz 0123456789.?!:;'"$%-,/"""

selected = -1
# Start a while loop so the agent can do this any many times as he wants before quitting
while selected != 0:
    # First we will display the menu.
    print("\nWelcome back agent, choose an option from the menu below.")
    print("""0.) Quit
1.) Encode a Secret Message
2.) Decode a Secret Message""")
    # Ask for the input that will be an int
    selected = get_int_input()
    while selected not in [0, 1, 2]:
        print("Please only select one of the available options, agent. Try again.")
        selected = get_int_input()
    test_selected(selected)