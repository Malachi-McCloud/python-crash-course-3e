# Lists Begin here

# We initialize the list and set a value of the 4 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# We print the whole list the exact same way it is type in the code
print(bicycles)

# Now we want to print the first bicycle
print(bicycles[0]) # This time we only get the "trek" bike

# We can add more the the value as we do this
print(bicycles[0].capitalize()) # upper cases Trek

# We can use lists entries the same as strings in a print message
print(f"My favorite bicycle brand is {bicycles[1].capitalize()}")

# Lets change the value in the list
bicycles[1] = "mongoose"

# Print the same message
print(f"My favorite bicycle brand is {bicycles[1].capitalize()}")

# Lets say we need the last item from the list
print(bicycles[-1])

# Second to last
print(bicycles[-2])

# Add a last item then reprint the last item this time
bicycles.append('electric')

# Last item from list prints our variable added above
print(bicycles[-1])

# Now to to put 1 at the front
bicycles.insert(0, 'BMX') # insert allows you to pick where oyu want it to go index wise
print(bicycles[0])

# Now we remove an item
print(bicycles)

# Delete
del bicycles[0]

# now we see the result
print(bicycles)