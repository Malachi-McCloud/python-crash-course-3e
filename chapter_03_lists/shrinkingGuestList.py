# 3-7 Shrinking Guest List
# use the pop method to remove guests until you are down to 2 print a message for each guest

# lets make this easy

# initialize and set the list variable
attending = ['Tom', 'Bob', 'Mike', 'Dave', 'Mark']

# send them a message and pop them
popped_guest = attending.pop()

print(f"Sorry we had to revoke your invitation! :  {popped_guest}")

# Second Guest
popped_guest = attending.pop()

print(f"Sorry we had to revoke your invitation! :  {popped_guest}")
