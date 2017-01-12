# Name: Peter Moldenhauer
# Date: 1/12/17
# Description: This program demonstrates arrays (lists) in Python

# Declare an array of numbers that represents players jersey numbers on a sports team
players = [29, 34, 47, 67, 82]

# Just like a string, you can type the array name and the postion to access specific elements of the array
# Note: Like all arrays, the first element is at postion 0
# The statement below will print 34, the second element but at index position 1...
print(players[1])

# Change an array element to a new value - change 47 to 74
players[2] = 74
print(players[2])

# Print all of the elements in the array - prints [29, 34, 74, 67, 82]
print(players)

# Add new items to the end of the array (method 1)
# Add one array with another array - prints [29, 34, 74, 67, 82, 1, 2, 3, 4, 5] to the screen
print(players + [1, 2, 3, 4, 5])
# Node this does not perminantly change the players array, just temporarilly adds on the other array

# Add new items to the end of the array (method 2)
players.append(999)  # Takes only 1 argument
print(players)  # Prints [29, 34, 74, 67, 82, 999] to the screen

# Slice items from array, similar to strings
# Use the : with a starting number and ending number
print(players[:2]) # Prints [29, 34]

# Can also use the above method with : to change the given values in the list
# This changes multiple items with multiple values at once
players[:2] = [0, 0]
print(players)  # Prints [0, 0, 74, 67, 82, 999]

# Use the same method to completely remove elements from the array by assigning the range to []
# Delete items from array...
players[:2] = []
print(players)  # Prints [74, 67, 82, 999]

# Delete entire array...
players[:] = []
print(players)  # Prints [] 
