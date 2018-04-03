# Ask the user how much their items cost
cost = float(input("How much do your items cost?"))
# Ask how much money they have
tendered = float(input("How much do you have to pay for that?"))
# Print how much they have(tendered) and how much they owe(cost of item)
print("\nAmount tendered: \t{0:>6.2f}".format(tendered))
print("Price of items: \t{0:>6.2f}".format(cost))

# Print a nice separator
print("\t\t\t\t-_________")

# Change will equal what they have minus what they owe
change = tendered - cost
# Print change in decimal
print("Change: \t\t\t{0:>6.2f}".format(change))
# To calculate we will convert to all pennies
# To do this, change will be multiplied by 100
change = int(round(change * 100))
# Print that new value out as change left in pennies
print("Change left: \t\t{:>6.0f}\n".format(change))

# The number of twenties will be the change divided by 2000($20) with no remainder
# $20's
twenties = change // 2000
# Print the number of twenties to be returned
print("Twenties: \t{0:.0f}".format(twenties))

# Then change will be updated to be the remainder(mod) of that
change %= 2000
# Now we will just repeat this for all other bills and coins
# ($10's = change // 1000, change %= 1000, $5's = change // 500, change %= 500, etc)


# Repeat for each denomination of currency:
# $10's
tens = change // 1000
print("Tens: \t\t{0:.0f}".format(tens, twenties))
change %= 1000
# $5's
fives = change // 500
print("Fives: \t\t{0:.0f}".format(fives))
change %= 500
# $1's
ones = change // 100
print("Ones: \t\t{0:.0f}".format(ones))
change %= 100
# $.25's
quarters = change // 25
print("Quarters: \t{0:.0f}".format(quarters))
change %= 25
# $.10's
dimes = change // 10
print("Dimes: \t\t{0:.0f}".format(dimes))
change %= 10
# $.05's
nickles = change // 5
print("Nickles: \t{0:.0f}".format(nickles))
change %= 5
# $.01's
pennies = change // 1
print("Pennies: \t{0:.0f}".format(pennies))
change %= 1
