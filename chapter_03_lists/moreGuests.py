# 3-6 More Guests
# You found a bigger dinner table so now you need to think of three more guests to invite

# Start the same as 3-5 initialize and set the variables in the list
attending = ['Tom', 'Bob', 'Mike', 'Dave', 'Mark']

# Declare what we are doing
print("We receive a call we have a larger table now sir.\nPlease make sure to update the list of guests.")

# Show who was attending
print(f"Previous list: {attending}")

# Now we add
attending.append("Jackie")
attending.append("Viktor")
attending.append("Doug")

# Show who is now attending
print(f"Current list: {attending}")