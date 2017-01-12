# Name: Peter Moldenhauer
# Date: 1/11/17
# Description: This program demonstrates strings in Python

# Inclose strings in either double quotes or single quotes
print("Hello World")
print('My name is Peter Moldenhauer')

# Use double quotes if inside the string you use a single quote(s)
print("Don't forget to use double quotes to enclose don't")

# Enclose string in single quotes if you want to use double quotes in string
print('My computer said "hello world" to me')

# Use an escape character if you want to print a single quote or double quote
# An escape character just uses a backslash with the character you want to use (ex. \' for a single quote)
print('This \' is enclosed with single quotes')

# To print out a file path to a folder on your desktop, you need to be careful
# This goes for anytime you are using \n in your string in general - because \n is an escape character for a new line
# Put r right before the first quotation mark - This means print out the raw string with no special meaning, just as is
print(r"C:\Peter\Desktop\newFile")

# Examples of adding strings together like numbers...
firstName = "Peter "
print(firstName + "Moldenhauer") # This prints Peter Moldenhauer
print(firstName + "Smith") # This prints Peter Smith

# Multiplying strings - this will print Peter 5 times
print(firstName * 5) 