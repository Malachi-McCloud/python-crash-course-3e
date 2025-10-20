# Continuation of Car file to use importing

# Added electric car same as below for pull and inheritance can be done

# Has same alias systems as most c family languages as ec for electric car shortening etc

# Ready to move on after this feel like this example and chapter have been dragging due to rehashing.
from car import Car, ElectricCar

my_new_car = Car('volkswagen', 'golf', 2025)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 25
my_new_car.read_odometer()