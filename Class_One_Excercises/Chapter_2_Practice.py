# Note: not all questions have been done here

# 4. To what do the following expressions evaluate?
# (5 > 4) and (3 == 5) --> True and False; result is False
# not (5 > 4) --> not True; result is False
# (5 > 4) or (3 == 5) --> True or False; result is True
# (True and True) and (True == False) --> T and F; result is False
# (not False) or (not True) --> T or F; result is True

# ------------------------------------

# 5. What are the six comparison operators?
# Ans: ==, !=, <, >, <=, >=,

# 9. Write code that prints "Hello" if "1" is stored in "spam", "Howdy" if "2" is stored in "spam", and "Greetings!" if anything else is stored in "spam".

spam = 'yo, wasssaaaaaaap!' # If you know, you know

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')