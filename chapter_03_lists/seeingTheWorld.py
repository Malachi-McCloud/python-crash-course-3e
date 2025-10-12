# Exercise 3-8 Seeing the world 
# Think of atleast 5 places you would like to visit
# Store them in a list, print the list in original order, 
# use sorted to store them in reverse alphabetical order
# print it again then use reverse() to change it again then reverse again to change it back
# use sort() to do alphabetical again

# Skipped 3-10

# Initialize and set values to the list
locations = ['France', 'Germany', 'Italy', 'Scotland', 'England']

# Print the original list
print(locations)

# Sort the list
locations = sorted(locations)

# Print the sorted list
print(locations)

# print with the list sorted in reverse alphabetical order 
locations.reverse()

# print locations.reverse
print(locations)


# Incorporating 3-9 into this it supposed to be dinner guest to see the length
print(len(locations))