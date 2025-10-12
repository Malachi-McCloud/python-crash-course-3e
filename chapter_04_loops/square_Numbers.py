# Square Numbers
# print the square numbers for a range(list) of numbers

# Initialize squares as an empty list
squares = []

# loop for a range of values
for value in range(1,11):
    # Inside the loop for each value 1-10
    square = value ** 2 # We pow^2 each number then add it to the list we initialized above
    squares.append(square) # Adding the number

# Print squares full list outside the loop deindented
print(squares)

# Simple Statistics working with squares

# MINIMUM
print(min(squares))

# MAXIMUM
print(max(squares))

# SUM
print(sum(squares))