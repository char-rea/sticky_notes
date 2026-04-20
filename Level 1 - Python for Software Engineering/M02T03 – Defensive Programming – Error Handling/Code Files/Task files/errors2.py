# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth" #missing _ in fullspec and also missing the f before the string to allow for string interpolation

print(full_spec) #error: SyntaxError, error missing _ in the name for full spec

