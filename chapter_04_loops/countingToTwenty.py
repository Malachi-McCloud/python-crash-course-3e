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

for value in range(1,1_000_000_000):
    oneToOneMil.append(value)


print(sum(oneToOneMil))