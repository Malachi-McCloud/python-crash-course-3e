# Removing prefixes

message = 'https://nostarch.com'

# Prints nostarch.com
print(message.removeprefix('https://'))

# Added to show this is just the presented value not the stored
print(message)

# Now with the suffix .com gone
print(message.removesuffix('.com'))

# Now Both
print(message.removesuffix('.com').removeprefix('https://'))