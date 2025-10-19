# Greeter Functions chapter 8 beginning


# Original
# # Create a small function called
# def greet_user(username):
#     # Display a smile greeting
#     print(f"Hello, {username}")

# # Must have an arguement if the function isn''t called after being declare nothing  happens for this file running.
# greet_user('Malachi')

# Rebuild while loop
def get_formatted_name(first_name, last_name):
    # Return a formatted name neatly
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nplease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\n Hello, {formatted_name}")