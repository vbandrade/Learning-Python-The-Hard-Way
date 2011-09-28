# Cars available
cars = 100

# Spaces in each car
space_in_a_car = 4.0

# Drivers available
drivers = 30

# Number of passengers
passengers = 90

# Cars left
cars_not_driven = cars - drivers

# Assigned cars
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are onnly", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."