# Exercise 3-5 Changing Guest List
# We take a list of invited guests then replace a guest who cannot make it to the party

attending = ['Tom', 'Bob', 'Mike', 'Dave', 'Mark']

# First run attending
print(attending)

# State they can't make it
print(f"{attending[0]} cannot make the party he will be replaced by Jackie")

# Change the attending list index 0
attending[0] = "Jackie"

# Print the changed list
print(attending)