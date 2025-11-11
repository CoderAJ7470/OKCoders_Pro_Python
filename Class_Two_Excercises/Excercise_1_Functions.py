import math

# Create a function that converts from Celsius to Fahrenheit

# def celsius_to_fahrenheit(celsius):
#     temp_in_fahrenheit = (celsius * 1.8) + 32
#     return f'{celsius} degrees Celsius is {temp_in_fahrenheit} degrees fahrenheit'

# print(celsius_to_fahrenheit(0))
# print(celsius_to_fahrenheit(34))
# print(celsius_to_fahrenheit(18))

# ------------------------------------------------

# Password Validator

# def has_a_number(input_string):
#     return any(char.isdigit() for char in input_string)

# def is_valid_password(password):
#     has_a_number = has_a_number(password)
#     if len(password) == 8 and has_a_number:
#         return True
#     else: return False

# print(f'Is co0lPass a valid password? {is_valid_password('co0lPass')}')
# print(f'Is notcoolPass a valid password? {is_valid_password('notcoolPass')}')

# ------------------------------------------------

# List Statistics - pass in a list or dictionary of numbers, and return a dictionary with min, max, average and total count

def get_stats(numbers):
    # Find the smallest number (min);
    smallest_number = min(numbers)
    largest_number = max(numbers)
    
    # Using the sum() function to find the average here. Can also import the statistics library and use the mean() function from that like so: statistics.mean(numbers), but I'm probably jumping a bit far ahead with that right now :-)
    # Formatted to 2 decimal places without using the round() function
    average = math.floor((sum(numbers) / len(numbers)) * 100) / 100
    total_count = len(numbers)

    # Return a dictionary with the calculated min, max, average and total
    stats = {
        'Minimum Value': smallest_number,
        'Maximum Value': largest_number,
        'Average': average,
        'Total Count': total_count
    }

    return stats

# Create a list of numbers. Optionally, you can also pass in a dictionary
list_of_numbers = [3.4, -3, 10, 5, 7.5, 6]

# Now call the get_stats function, passing in the list created above
stats_from_list = get_stats(list_of_numbers)

# Print the stats dictionary
print('Here are the stats for the specified dictionary:\n')
print(stats_from_list)
