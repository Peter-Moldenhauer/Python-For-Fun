# Name: Peter Moldenhauer
# Date: 1/12/17
# Description: This program demonstrates strings in Python

# Access individual characters from a string
# Think of the string as an array and just use the array index to access a specific character
user = "Billy Robinson"
print(user[6])   # Print R to the screen

# The above method access the string from left to right (starting at array index 0)
# You can also access a string from right to left, -1 is always the last character in the string
print(user[-1])  # Print n to the screen
print(user[-3])  # Print s to the screen

# Slice out a section of a string
# You need to use 2 numbers, the 1st is where you want to start and 2nd is where you want to stop (does not include the stop character in sliced part)
# Use the colon to tell where you want to start and stop
print(user[4:9])  # Prints y Rob to the screen

# If you dont include the 1st number in front of the colon, then it automatically starts at the beginning of the string
print(user[:9])  # Prints Billy Rob to the screen

# Same goes if you dont put the 2nd number after the colon, it automatically goes to end of the string
print(user[4:])   # Prints y Robinson to the screen

# To get the length of a string, use the len() function
print(len(user))   # Prints 14 to the screen 