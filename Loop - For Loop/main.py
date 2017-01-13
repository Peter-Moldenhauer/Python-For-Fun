# Name: Peter Moldenhauer
# Date: 1/13/17
# Description: This program demonstrates the for loop in Python

# Declare an array of foods
foods = ["bacon", "tuna", "sausage", "ham", "beef"]

# Print out these food items one by one
# This loop will print out the name (ex. bacon) and length (ex. 5) for each element, each on a new line - 10 lines total
for f in foods:   # f is a variable that refers to a given element in foods
    print(f)
    print(len(f))   # keep this indented to stay within the loop, if its not indented it will just be treated as its own statement


# The above loop, loops through the entire array list
# To loop through a slice of the list you can do the following
# This example starts looping at the beginning of foods but stops before reaching index 2 - so just loops through bacon and tuna...
for f in foods[:2]:
    print(f)
    print(len(f))
