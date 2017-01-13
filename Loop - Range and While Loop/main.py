# Name: Peter Moldenhauer
# Date: 1/13/17
# Description: This program demonstrates range and while


# A range of numbers allows you to create a loop without a list (array)
# This will print 0 through 9, each on new line.
for x in range(10):
    print(x)

# This will print Hello World 10 times, each on a new line
for x in range(10):
    print("Hello World")

# Instead of just 10 (first example) give a range of numbers to loop through - ues two numbers to represent the start and end
# By x would start at 0, but in this example x starts at 5 and goes until 12 (does not include 12)
for x in range(5, 12):
    print(x)

# Now, use three numbers. 1st is the starting number 2nd is the end "up to" number 3rd is the increment number
# This will count from 10 to 40 but do it in steps of 5
for x in range(10, 40, 5):
    print(x)


#     While Loop Example...
# A while loop loops as long as a certain condition is true
myVar = 5

while myVar < 10:
    print(myVar)
    myVar += 1      # increment myVar by 1 with each iteration