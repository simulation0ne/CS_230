# Create a variable called name, and use this to store the input the user gives as their name.
# Use the input function to ask the user for their name.
name = input("Hi there, what is your name?\n")
# Use the name variable from now on to refer to the user.

# Ask the user if they want to hear a knock knock joke.
# Use the name variable to refer to the user
print("Hi {}, want to hear a knock-knock joke?".format(name))
# No matter what they say, tell them the joke.
# Even if all they do is hit enter
input()
# Start the joke by printing out knock-knock
print("Knock-knock")
# Again, no matter what they say, proceed with the joke
input()
# Tell them it is Michael Ellis (From the Monty Python sketches)
print("Michael Ellis")
# Once more, no matter what they use says, continue with the joke
input()
# Once they ask Michael Ellis who, realize they don't know Michael Ellis and then clam up about who he is.
print("Oh... Um, no never mind, no you wouldn't know him")


