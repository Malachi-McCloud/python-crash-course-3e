# Players file working with slicing a list

# initialize and set a value to the list
players =  ['charles', 'martina', 'michael', 'florence', 'eli']

# Returns the players between indices 0-3 so indices 0,1,2
print(players[0:3])

# Returns the players between indices 1-4
print(players[1:4])

# If we do the same but, omit the first number it automatically starts at the beginning
print(players[:4])

# Inversely we can add only the first number omitting the second starts at that point until the end
print(players[2:])

# We can also work with a negative from the other end of the list
print(players[-3:]) # which with 5 names does the same as 2:

# Looping through a slice
print("Here are the first three players on my team!\n")

# Loop through and slice until the 3 player
for player in players[:3]:
    print(player)