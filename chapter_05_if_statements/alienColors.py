# Alien Colors 5-3, 5-4, 5-5

# Assign an alien_color as if we shot down a ufo and found an alien
alien_color = 'green'

# Statement if the color is green you earned 5 points
if alien_color == 'green':
    print(f"Congratulations the alien was {alien_color} you earn 5 points")
# 5-4 add a second color with 10 points 
elif alien_color == 'yellow':
    print(f"Congratulations the alien was {alien_color} you earn 10 points")
elif alien_color == 'red':
    print(f"Congratulations the alien was {alien_color} you earn 15 points")
# Add a way for the program to not fail if there wasn't an alien
else:
    print("Sorry no aliens detected")


