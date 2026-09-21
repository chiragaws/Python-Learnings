# Chapter-2/011_TwoInputs.py
# Demonstrates handling multiple inputs and string operations in Python

# Prompt the user to enter their name and age separated by a space
# The input() function captures user input as a string
# .split() splits the string into a list using whitespace as delimiter
# The result is unpacked into 'name' and 'age' variables
name, age = input("Enter your name and age separated by a space: ").split()

# Print a personalized greeting using the user's input
# Note: age remains a string here - for real applications, convert to int with int(age)
print("Hello " + name + ", you are " + age + " years old.")
#Demonstrates handling multiple inputs and string operations using Comma
name, age = input("Enter your name and age separated by a comma: ").split(",")
print("Hello " + name + ", you are " + age + " years old.")
# The user is prompted to enter their name and age separated by a space or comma