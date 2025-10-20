# Restaurant Exercise 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine, openOrClosed):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        # 9-1 final step
        self.openOrClosed = openOrClosed
        self.numberServed = 0

    # Create a method that calls the name and cuisine and prints a descriptive message
    def describe_restaurant(self):
        description_message = (f"{self.restaurant_name} is a {self.cuisine} restaurant.")
        return description_message
    
    # 9-4 setting a new value in the numberServed
    def updated_numberServed(self, customers):
        self.numberServed += customers
    
    # 9-1 Final step adding 9-4 to this for the amount served
    def open_restaurant(self):
        status_Message = (f"The {self.restaurant_name} is {self.openOrClosed}. the restaurant served {self.numberServed} people")
        return status_Message

# Create the instance of the object
my_Restaurant = Restaurant("Butcher's Block", "steakhouse", "Closed")

# Update the number of customers served via the method
my_Restaurant.updated_numberServed(500)

# Run the description of the restaurant from the first exercise
print(my_Restaurant.describe_restaurant())
# Show the number of customers before second increment 500
print(my_Restaurant.open_restaurant())

# Increment again by 500 = 1000
my_Restaurant.updated_numberServed(500)

# This should be the 1000 as the object was updated
print(my_Restaurant.open_restaurant())