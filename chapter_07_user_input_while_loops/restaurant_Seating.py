# Restaurant Seating Exercise 7-2


# Ask how many people they have in their party
party_size = input("How many people were you looking to seat?")

# We need to cast it to an int
party_size = int(party_size)

# if its over 8 they have to wait otherwise follow me to your table
if party_size > 8:
    print("You will have to wait for a table to open.")
else:
    print("Follow me we have a table right here.")