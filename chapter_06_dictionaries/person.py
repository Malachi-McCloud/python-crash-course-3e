# Person Exercise 6-1
# Create a dictionary to store information about a person first, last, age, and city they live in.

# Initialize and Set the dictionary
person_01 = {
    'firstName' : 'Malachi',
    'lastName' : 'McCloud',
    'age' : '28',
    'city' : 'Norfolk'
}
person_02 = {
    'firstName' : 'Kaiser',
    'lastName' : 'Wihelm',
    'age' : '55',
    'city' : 'Brandenburg'
}
person_03 = {
    'firstName' : 'John',
    'lastName' : 'Smith',
    'age' : '50',
    'city' : 'Norfolk'
}

# Print every line
print(person_01['firstName'])
print(person_01['lastName'])
print(person_01['age'])
print(person_01['city'])

# Favorite Numbers 6-2 
favorite_numbers = {
    1 : 'Sam',
    2 : 'Bob',
    3 : 'Frank',
    4 : 'Doug',
    5 : 'Sarah'
}

# Print the user based on he favorite number
print(favorite_numbers[1])
print(favorite_numbers[2])
print(favorite_numbers[3])
print(favorite_numbers[4])
print(favorite_numbers[5])

# 6-7 
# Create persons list
persons = [person_01, person_02, person_03]

for person in persons:
    print(person)