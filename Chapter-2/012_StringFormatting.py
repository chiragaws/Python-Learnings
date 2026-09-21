# Chapter-2/012_StringFormatting.py
# Demonstrates two ways to format strings in Python: concatenation and f-strings

# First method: String concatenation using + operator
# - Stores name and age as separate variables
# - Converts age (integer) to string using str() for concatenation
# - Creates a greeting message by joining strings
name = "Chirag"
age = 25
print("Hello " + name + ", you are " + str(age) + " years old.")

# Second method: f-string formatting (Python 3.6+)
# - Uses f-prefix to create a formatted string
# - Directly embeds variables inside curly braces {}
# - Automatically handles type conversion (no need for str() here)
# - More readable and efficient than concatenation
print(f"Hello {name}, you are {age} years old.")

# Third print statement: Demonstrating dynamic value calculation in f-strings
# - Shows how f-strings can include expressions directly
# - Calculates {age+2} on-the-fly (25 + 2 = 27)
# - Creates a new greeting with the calculated value
# - Highlights f-strings' ability to embed computations
print(f"Hello {name}, you are {age+2} years old.")