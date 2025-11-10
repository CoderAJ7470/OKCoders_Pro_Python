# Create a function that converts from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    temp_in_fahrenheit = (celsius * 1.8) + 32
    return f'{celsius} degrees Celsius is {temp_in_fahrenheit} degrees fahrenheit'

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(34))
print(celsius_to_fahrenheit(18))

# ------------------------------------------------

# Create a password 

def has_a_number(input_string):
    return any(char.isdigit() for char in input_string)

def is_valid_password(password):
    has_a_number = has_a_number(password)
    if len(password) == 8 and has_a_number:
        return True
    else: return False

print(f'Is co0lPass a valid password? {is_valid_password('co0lPass')}')
print(f'Is notcoolPass a valid password? {is_valid_password('notcoolPass')}')
