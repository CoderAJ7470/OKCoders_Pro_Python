# Note: Not all questions in the practice are included here.

# 6. What does the variable bacon contain after the following code runs?

# bacon = 20
# bacon + 1

# Ans: The value of bacon is still 20, because its value does not change after the code runs. The expression "bacon + 1" will evaluate to 21, but that is not gettign stored into bacon, so bacon will still be 20


# ------------------------------------


# 7. What would the following expressions output?

# 'spam' + 'spamspam'
# 'spam' * 3

#  Ans: Both will evaluate to 'spamspamspam'


# ------------------------------------


# 8. Why is 'eggs' a valid variable name while the number 100 is invalid?

# Ans: For two reasons - a variable has to have a descriptive name that shows what it is storing, and the other being that Python will throw an error if you try to assign a value to 100, since Python will take 100 to be an integer value, and any assignment like 100 = <whatever value here> will be taken by Python as an attempt to change the value, which is not possible.


# ------------------------------------


# 9. Why does the following expression cause an error, and how can it be fixed? > 'I eat + 99 + ' burritos.'

# Ans: This will throw an error because Python takes 99 as an integer value, while the rest are strings. Integer values cannot be concatenated to strings without converting them to strings first. So the solution to fix this would be: 'I eat ' + str(99) + ' burritos.' Another solution would be to just put everything into a format string: f'I eat {99} burritos.'
