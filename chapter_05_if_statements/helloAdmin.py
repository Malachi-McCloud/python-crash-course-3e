# Hello Admin Exercise 5-8, 5-9

# 5-8 Make a list of 5 or more usernames including admin that will print a list after they log into a website

# if the user is admin print a special greeting otherwise its generic

# original list not normalized
user_list = ['DanTheMan', 'FrogTheLog', 'Admin', 'Jumpman101', 'ZergBuster1000']

# normalized lower list
user_list_lower = [user.lower() for user in user_list]

# Check if there are any users 5-9
if len(user_list) == 0:
    print("There are no users in the list")
# For each user in the normalized list 
else:
    for user in user_list_lower:
        # We check the equals for each one
        if user == 'admin':
            # Special message for admin
            print("Welcome Admin the admin panel is available through the button on the top right")
        else:
            # Plain jane message
            print(f"Welcome {user}")