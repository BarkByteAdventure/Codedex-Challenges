# The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

# Create a weight conversion program that:

#    Asks the user what their Earth weight is (as a float).
#    Asks the user for a planet number (as an int).

# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

# To calculate the user's weight:
# destination weight=Earth weight × relative gravity

# Number	Planet	Relative Gravity
#   1       Mercury	    0.38
#   2	    Venus   	0.91
#   3   	Mars	    0.38
#   4   	Jupiter 	2.53
#   5   	Saturn  	1.07
#   6   	Uranus  	0.89
#   7   	Neptune 	1.14

# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.

earth_weight = float(input("What is your weight?"))

planet_number = int(input("Which planet would you like to know your weight on?"))

if planet_number == 1:
    relative_gravity = 0.38
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on Mercury is {destination_weight} kg")
elif planet_number == 2:
    relative_gravity = 0.91
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on Venus is {destination_weight} kg")
elif planet_number == 3:
    relative_gravity = 0.38
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on Mars is {destination_weight} kg")
elif planet_number == 4:
    relative_gravity = 2.53
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on Jupiter is {destination_weight} kg")
elif planet_number == 5:
    relative_gravity = 1.07
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on Saturn is {destination_weight} kg") 
elif planet_number == 6:
    relative_gravity = 0.89
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on Uranus is {destination_weight} kg")
elif planet_number == 7:
    relative_gravity = 1.14
    destination_weight = earth_weight * relative_gravity
    print(f"Your weight on Neptune is {destination_weight} kg")
else:
    print("Invalid planet number. Please try again.")
