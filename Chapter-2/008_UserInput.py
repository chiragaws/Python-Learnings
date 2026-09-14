#User Input
#Input function allows user to provide input to the program.
name = input("What is your name? ")
print("Hello, " + name + "!")
#Input function always returns a string. If you want to take an integer input, you need to convert it to an integer using int() function.
age = int(input("What is your age? "))
print("You are " + str(age) + " years old.")