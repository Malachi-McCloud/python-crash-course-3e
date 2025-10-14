# Conditional Tests Exercise 5-1
# Goal Write a series of conditional test print a statement describing each test

# we will use the car test
car = 'Chevy'


if car.lower() == 'toyota':
    print("Your car is from Japan")


# Moving on to 5-2 Test for equality dpme amd inequality between strings

if car.lower() != "toyota" or "subara" or "honda":
    print("Your car is not made in Japan")


cars = ['toyota', 'ford']

if 'toyota' in cars:
    print("You own a Toyota")
if 'ford' in cars:
    print("You own a ford.")
if 'chevy' in cars:
    print("You own a chevy") # test case to see if its just slotting on all
