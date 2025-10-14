# Dimensions
# Starts the usage and difference between lists and tuples

# Tuple is just like a list but, we use paranthes

# Initialize and set dimensions
dimensions = (200,0)

# Print both values individually
print(dimensions[0])
print(dimensions[1])

# Now we try to reassign a value
# dimensions[0] = 250 Causes Break

# Now we loop for each value
for dimension in dimensions:
    print(dimension)

# Tuples are distinct because we can use the individual assignment to modify a tuple but, we can write over a tuple and reassign the whole thing

dimensions = (400, 100) # doesn't break our code
for dimension in dimensions: # Loops again same way
    print(dimension) # prints the new values

# END CHAPTER 4