# Checking User Names : Exercise 5-10

# Make a list of 5 or names called current users
current_users = ['DanTheMan', 'FrogTheLog', 'Admin', 'Jumpman101', 'ZergBuster1000']

# Make another list of 5 users called new users two names need to match from the first list
new_users = ['BenTen', 'ToadTheLoad', 'FrogTheLog', 'HumptyDumpty', 'ZergBuster1000']

# loop throug new users see if each names has been used makes sure the comparison is case insensitive

# Lets normalize the lists to esnure the comparison is case insensitive
current_users_upper = [user.upper() for user in current_users]

# same for the second list
new_users_upper = [user.upper() for user in new_users]

# Now we loop through for each user in new_users_upper our normalized list
for user in new_users_upper:
    if user in current_users_upper:
        print("Sorry that user name is taken. Please try another")
    else:
        print("Your user account has been created.")

# Success on this one!

# Skipping 5-11 Oridinal Number

# 5-12 just talks about the styling of your if statements and how you write them 1 > 5 no 1>5
# 5-13 Ask us our idea my idea is to get back to the meat and potatos of the book to be able to really grasp the wheel and be ready for January.