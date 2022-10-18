# Creating constants
TO_KGS = 0.453592

# Assigning input values to a variable
var_pounds = float(input("Type the value in pounds: "))

# function for changing kgs to pounds

var_kgs = float(var_pounds*TO_KGS)

# Rounding off the value to 2 decimal places
# Change it according to your preference
print("That is", var_kgs.__round__(2), "kilograms")

# A cleaner way of rounding off
print("That is", round(var_kgs, 2), "kilograms")


