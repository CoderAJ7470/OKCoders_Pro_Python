# Check if a key exists in a dictionary
picnic_items = {
  'apples': 5,
  'cups': 2,
  'pizzas': 10
}

hasPizzas = picnic_items.get('pizzas', 'No pizzas found')

# Will print "I am bringing 10 pizzas to the picnic."
if hasPizzas:
    print(f'I am bringing {picnic_items['pizzas']} pizzas to the picnic.')
else: print('I am not bringing any pizzas to the picnic')

# ----------------

picnic_items = {
  'apples': 5,
  'cups': 2
}

# Will print "I am not bringing any pizzas to the picnic."
hasPizzas = picnic_items.get('pizzas', 0)

if hasPizzas:
    print(f'I am bringing {picnic_items['pizzas']} pizzas to the picnic.')
else: print('I am not bringing any pizzas to the picnic')

