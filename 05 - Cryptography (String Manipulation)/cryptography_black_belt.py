"""
This programs uses a 3-character base key to create a more complex key that can be used to encrypt and decrypt anything.
You and your recipient both have to have the program and that 3-character base key in order to encode/decode messages.
If you try to decode a message with the wrong base key, it will give you incorrect output and not reveal the secret message!

For an example, try to decrypt this:
!d$kyp;ks5vk!yp;ks$xkle$9!$6;5ekgk95(k!d$k3'g?mk86y(vk,ybkj's0ky%$6k!d$kp5hek;ya)l
with the key: 3ef
"""


from time import sleep as pause
from random import randint

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
def get_base_key(next_step):
    print("Do you have a unique key for this message?")
    getting_unique_key = True
    while getting_unique_key:
        has_unique_key = input().lower()
        if has_unique_key == "yes":
            getting_unique_key = False
            is_valid = False
            while not is_valid:
                key = input("Please enter your unique key:\t").lower()
                is_valid = True
                if len(key) == 3:
                    for char in key:
                        if char in "0123456789abcdef":
                            continue
                        else:
                            print("That key is not valid, make sure to enter a valid key")
                            is_valid = False
                            break
                else:
                    print("Please enter a valid 3-character key")
                    is_valid = False
            if is_valid:
                if next_step == "encrypt":
                    encode_message(key)
                if next_step == "decrypt":
                    decode_message(key)
        elif has_unique_key == "no":
            getting_unique_key = False
            if next_step == "decrypt":
                print("You cannot decrypt a message without that message's base key, agent. Try again.")
                return
            else:
                key = new_base_key()
                print("Your key for this message will be {}".format(key))
                if next_step == "encrypt":
                    encode_message(key)
                if next_step == "decrypt":
                    decode_message(key)
        else:
            print("Please only answer 'yes' or 'no'. Try again.")



def new_base_key():
    # define a base to pull the key out of
    base = "0123456789abcdef"
    # get three of the indexes in the base
    num1 = get_randint(base)
    num2 = get_randint(base)
    num3 = get_randint(base)
    # set the characters of the base key by getting the char from that slice of the base
    char1 = base[num1]
    char2 = base[num2]
    char3 = base[num3]
    # return the three chars as one string
    return str(char1 + char2 + char3)


def encode_message(base_key):
    # Use the generate encryption pattern function to get the particular pattern based on the given key
    encryption_pattern, init_key = generate_encryption_pattern(base_key)
    # Ask for the message from the user
    message = input("What is the message you would like to encrypt?").lower()
    new_message = ""
    for char in message:
        # Get the index of each char in the init pattern
        init_index = init_key.index(char)
        # Set a new character as the character from that slice of the encryption pattern
        new_char = encryption_pattern[init_index]
        # Concatenate the new message with each new char
        new_message += new_char
    # Print out the new message
    print("Your encrypted message is:\t{}".format(new_message))
    # Print out the key used for creating this message
    print("Your unique key for this message is:\t{}".format(base_key))


def generate_encryption_pattern(base_key):
    # This is the initial pattern for creating encryption patterns.
    init_key = """abcdefghijklmnopqrstuvwxyz 0123456789.?!:;'"$%-,()"""
    # set a length variable to the length of that initial pattern
    length = len(init_key)
    # set the start point as the result of the base key calculation
    start = calc_base_key(base_key)
    # Use a skip of three
    skip = 3
    # start an empty index list to store an index pattern in
    index_list = []
    # set the start back by three so I can add it again to start the loop
    index_to_use = start - skip
    # start the while loop to fill the index list
    while len(index_list) < length:
        # add the skip to the last used position
        index_to_use += skip
        # test if the index is out of range and if it is, send it back to the beginning
        if index_to_use < length:
            index_list.append(init_key[index_to_use])
        # send the index back to the beginning
        else:
            index_to_use -= length
            index_list.append(init_key[index_to_use])
    # turn the list into a pattern for encrypting and decrypting
    encryption_pattern = "".join(index_list)
    # return both the pattern and the init key to the calling functions
    return encryption_pattern, init_key


def calc_base_key(base_key):
    # This is a base used to create the original base key
    base = "0123456789abcdef"
    # start the count at 0
    total = 0
    for char in base_key:
        # for each char in the base_key, get its index number and add that to the total
        for char in base_key:
            total += base.index(char)
        # return that total to the calling function
        return total



# Define a decode_message function
def decode_message(base_key):
    # Get the encryption pattern and initial pattern
    encryption_pattern, init_key = generate_encryption_pattern(base_key)
    # Ask for the message to decrypt
    message = input("What is the message you would like to decrypt?").lower()
    new_message = ""
    for char in message:
        # for each character, find its index in the encryption pattern
        encrypt_index = encryption_pattern.index(char)
        # use that index to find the corresponding character in the initial pattern
        new_char = init_key[encrypt_index]
        # add each new character to the decrypted message
        new_message += new_char
    # print out the decrypted message
    print("Your decrypted message is:\t{}".format(new_message))


# Define a get_randint function
def get_randint(string):
    # get a random string based on the length of a passed in string
    # (used to select random indexes of strings)
    ri = randint(0, (len(string) - 1))
    # return that random integer to the calling function
    return ri


# Define a generate_key function
def generate_key():
    # A user-used function that just calls the new base key function and prints out the result
    key = new_base_key()
    # print out the new key for the user to look at
    print("Your newly generated key is:\t{}".format(key))


# Define a test_selected function
def test_selected(val):
    # If the selected option was 0, wish the agent good luck and quit the program
    if val == 0:
        print("Good luck out there agent.")
        quit()
    # If the selected option was 1, help the agent encode a message
    elif val == 1:
        get_base_key("encrypt")
    # If the selected option was 2, help the agent decode a message
    elif val == 2:
        get_base_key("decrypt")
    # If the selected option was 3, generate a new key for the agent
    elif val == 3:
        generate_key()

wait_time = 2
print("Welcome agent!")
pause(wait_time)
print("This is the Pynigma Machine.")
pause(wait_time)
print("Use this to encrypt and decrypt secret messages from other agents in the field.")
pause(wait_time+2)
print("Remember, you must have the same code used to encrypt a message in order to correctly decrypt it, "
      "so keep that key handy.")
pause(wait_time+3)
selected = -1
# Start a while loop so the agent can do this any many times as he wants before quitting
while selected != 0:
    # First we will display the menu.
    print("\nWelcome back agent, choose an option from the menu below.")
    print("""0.) Quit
1.) Encode a Secret Message
2.) Decode a Secret Message
3.) Generate a New Key""")
    # Ask for the input that will be an int
    selected = get_int_input()
    while selected not in range(0,4):
        print("Please only select one of the available options, agent. Try again.")
        selected = get_int_input()
    test_selected(selected)