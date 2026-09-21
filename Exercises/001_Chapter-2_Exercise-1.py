# Exercises/001_Chapter-2_Exercise-1.py
# This program calculates the average of three numbers entered by the user

# Step 1: Get input from user and split into individual strings
# - input() captures user input as a string (e.g., "1,2,3")
# - .split(",") breaks the string into a list of strings (e.g., ["1", "2", "3"])
number_one, number_two, number_three = input("Enter three numbers separated by commas: ").split(",")

# Step 2: Calculate the average (with error handling for invalid inputs)
# - Convert each string to float to handle decimal numbers
# - Sum the three numbers and divide by 3 to get the average
# - The f-string formats the result into a readable message
Average = print(f"Average of the given number is {float(number_one) + float(number_two) + float(number_three) / 3}")
