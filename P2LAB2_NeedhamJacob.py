# Jacob Needham
# 06/20/26
# P2LAB2
# program that creates a dictionary key and value pairs


#cars dictionary declaration
cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

#get keys from the dictionary
cars_keys = cars.keys()

#print(cars_keys)

print(*cars, sep = ", ")

#Get the car name from the user
car_name = input("Enter a vehicle to see it's mpg: ")
print()

#Get mpg for that car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per Gallon.")
print()


#Get Users projected Miles
miles_driven = float(input(
    f"How many miles will you Drive the {car_name}? "
))
print()

#Calculate gallons needed for input car to arrive at destination
gallons_needed = miles_driven/car_mpg

#Display redults with f string
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")



