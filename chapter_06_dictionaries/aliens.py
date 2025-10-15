# Aliens.py beginning of dictionary

# # Initialize the alien_0 dictionary
# alien_0 = {'color': 'green', 'points': 5}

# # Print the alien_0 color
# print(alien_0['color'])

# # initialize and set the new_points variable to the alien_0 points
# new_points = alien_0['points']

# # Print the new points
# print(new_points)

# alien_0['x position'] = 0
# alien_0['y position'] = 0

# print(alien_0)

# # Back  to Aliens with calling for multiple aliens creation
# alien_0 = {'color': 'green', 'points': 5,}
# alien_1 = {'color': 'yellow', 'points': 10,}
# alien_2 = {'color': 'red', 'points': 15,}

# # nest them within a list
# aliens = [alien_0, alien_1, alien_2]

# # Loop for each item in the lsit
# for alien in aliens:
#     print(alien)


# Looping to create aliens

# Empty List to store the aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

# Print the final count
print(f"There are {len(aliens)} aliens.")