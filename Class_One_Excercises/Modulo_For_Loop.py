# Use a for loop to count to 10, and print <number> is even if it's even, otherwise print <number> is odd

# Here, the range function takes two arguments - the first number is the one from where you want the for loop to begin iterating. So in this case, it will start from 1. The second number is the one which specifies how many times the for lopp should iterate, but not inclusive, of that number. So this for loop will iterate 10 times.

# The syntax "f" in the print lines is to format the output to include the value of the variable "x" in each iteration. This is very similar to a template string in JavaScript.
for x in range(1, 11):
  if x % 2 == 0:
    print(f'{x} is even')
  else: print(f'{x} is odd')