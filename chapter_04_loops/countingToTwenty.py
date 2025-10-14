# 4-3 Counting to Twenty
# Count to Twenty printing each number all inclusive

# start the loop for each value in range
for value in range(1, 21):
    # Print each vaue within the loops indent
    print(value)

# 4-4 Count to 1 Million
# for value in range(1,1_000_000_000): # That CPU GOOOOO BRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
#     print(value) # CTRL C To interupt if you run it 

# Comment 4-4 out to save time


# SUMMING 1 Mil 4-5

# Create the list
oneToOneMil = []

# Incorrect way to do this makes you go step by step
# for value in range(1,1_000_000_000):
#     oneToOneMil.append(value)

# Fixed method
oneToOneMil = list(range(1,1_000_001))


print(sum(oneToOneMil))
print(min(oneToOneMil))
print(max(oneToOneMil))

# New list between 3 and 30
threeToThrirty = list(range(3,30,3))

# Loop for each number
for value in threeToThrirty:
    # Print each value in the list
    print(value)


# List one through ten for cubed values
oneThroughTen = list(range(1,10))


for value in oneThroughTen:
    print(value ** 3)