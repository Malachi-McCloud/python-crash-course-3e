# Multiples of Ten

# Ask for a number and report back whether that number is a multiple of 10

user_number = input("Please enter a number to find out if it is a multiple of 10")


# Cast it to number
user_number = int(user_number)

outcome = user_number % 10

if outcome == 0:
    print("The number is divisble by 10 \n")

else:
    print("The number was not divisible by 10")