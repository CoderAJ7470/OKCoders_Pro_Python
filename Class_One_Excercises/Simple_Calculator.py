# A simple calculator where the user is asked to input two numbers, then asked what operation the user wants to do - addition, subtraction, multiplication or division

# If the user enters 0 as the second number, the program will use that as the numerator and inform the user as such, since division by 0 is not allowed.

# Ask for the two numbers. This is the shorthand way of asking for an input and then converting it to the integer type.
number_one = int(input('Please enter a number: '))
number_two = int(input('Please enter a second number: '))

# Ask the user which operation is preferred.
chosen_operation = input('Please choose your operation for these two numbers: +, -, * or /')

# An informative message telling the user which numbers he/she input, and which operation was chosen. The syntax "f" below is to format the output to include the value of the variable "x" in each iteration. This is very similar to a template string in JavaScript.
print(f'You entered numbers {number_one} and {number_two}, and chose the {chosen_operation} operation. The result is:')

# Perform the operation chosen and output (print) the result. In the division case, check for division by zero
if chosen_operation == '+':
  print(number_one + number_two)
elif chosen_operation == '-':
  if number_one > number_two:
    print(number_one - number_two)
  else: print(number_two - number_one)
elif chosen_operation == '*':
  print(number_one * number_two)
elif chosen_operation == '/':
  if number_two == 0:
    print(f'Since you entered the second number as "0", using that as the numerator since division by 0 is not allowed. The result is: {number_two / number_one}')
  else: print(f'Result is: {number_one / number_two}')
else: print('The operation you chose is invalid. Please choose +, -, * or /.')