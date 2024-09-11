# Ethan Lawrence
# september 11 2024
# String Concatenation

# Input area
firstName = input('What is your first name? \n')
lastName = input('What is your last name? \n')
city = input('What city do you reside in ' + firstName + '? \n')
state = input('What state is that in? \n')
age = int(input('How old are you ' + firstName + '? \n'))
height = int(input('How tall are you in inches? \n'))

welcomeMessage = 'Hello again!'
print('----------') # Divider

# Part 1
# Use concatenation to build and display a string that displays which city and state you live in

print(city + ' ' + state)


# Part 2
# Create a custom message that welcomes the user by first name to a game you created
# Create one variable to store the user's first name
# Create another variable that stores the welcome message
# Use concatenation to create the customized message

print(welcomeMessage + ' ' + firstName)


# Part 3
# Assign a number to your age variable
# Use the built-in Python str( ) function to convert your age to a string (when doing concatenation)
# Use concatenation to display a sentence that tells us your first name and age

print(firstName + ' You are still ' + str(age) + ' years old correct?')




# Part 4
# Use an f-string to build and display a string that contains your first name, last name, and your height in inches

print(f'User {firstName} {lastName} is {height} inches tall')