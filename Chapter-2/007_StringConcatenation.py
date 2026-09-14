# Strings
#Collection of characters in single or double quotes.
first_name = "Chirag"
last_name = "Kukreja"
# String Concatenation
full_name = first_name + " " + last_name  # Concatenating first name and last name with a space in between
print(full_name)  # Output: Chirag Kukreja
# You cannot add a string and an integer directly. You need to convert the integer to a string first.
age = 25
# print("My name is " + full_name + " and I am " + age + " years old.")  # This will raise a TypeError
# Correct way to concatenate string and integer 
print("My name is " + full_name + " and I am " + str(age) + " years old.")  # Output: My name is Chirag Kukreja and I am 25 years old.
# We can use multiply operator to repeat a string multiple times.
print("Hello! " * 3)  # Output: Hello! Hello! Hello!
