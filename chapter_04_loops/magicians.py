# Chapter 4 beginning

# Initialize and Set the list
magicians = ['alice', 'david', 'carolina']

# Loop for each magician in magicians 
for magician in magicians:
    # Print each magician
    print(magician)

# Once loop ends we go into more within loops
for magician in magicians:
    # Print the magician + statement for each magician iterated
    print(f"{magician.title()} has a great trick to show us!")

# Something after the loop INDENTATION IS IMPORTANT
print("Thank you for watching the great tricks")
