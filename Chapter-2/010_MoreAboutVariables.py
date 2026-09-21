# Chapter-2/010_MoreAboutVariables.py
# Demonstrates variable assignment, string concatenation, and simple arithmetic operations

# Create a tuple-like assignment with multiple variables
# 'name' will store a string, 'age' will store an integer
name, age = "Chirag", 25

# Print a personalized greeting using string concatenation
# Note: age needs to be converted to string using str() for concatenation
print("Hello " + name + ", you are " + str(age) + " years old.")

# Initialize three variables (x, y, z) with the same value (1)
# This is a shorthand way to write x = 1; y = 1; z = 1
x = y = z = 1

# Print the sum of x, y, and z (1 + 1 + 1 = 3)
# Demonstrates simple arithmetic operations
print(x + y + z)
