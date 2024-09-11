# Concatenation Practice

# Ethan Lawrence
# september 11 2024
# String Concatenation in Python

# Work with your assigned partner
# Each person in your team should take turns writing the code to create and display longer strings
# Check your partner's code for spelling, capitalization, and coding errors
# Correct any bugs in your code


#Info gathering!
firstName = input('Please Input your first name: \n')
middleName = input('Please input your middle name: \n')
lastName = input('now input your last name: \n')
yearBorn = int(input('What year were you born in? \n'))
travelDream = input('Where would you like to travel to? \n')
print('----------') # Seperating inputs from outputs

# Part 1
# Create variables to store your first, middle, and last name
# Have Python print a message that contains your concatenated full name, i.e., your combined first, middle and last names

fullName = firstName + ' ' + middleName + ' ' + lastName
print(f"Hello {fullName}! \n")

# Part 2
# Assume you're building a Space Invaders game
# Use concatenation to create and display a custom welcome message that includes the player's first name

print('Welcome back to the defence ' + firstName + ' ready to defend the earth from the space invaders? \n')

# Part 3
# Use concatenation to build and display a string that includes your first name, last name, and the year you were born

print(firstName + ' ' + lastName + ' ' + str(yearBorn) + ' \n')

# Part 4
# Use concatenation to create and display a sentence that says which country in the world
# you would visit if money were no object

print('You would like to visit ' + travelDream + ', yes? \n')