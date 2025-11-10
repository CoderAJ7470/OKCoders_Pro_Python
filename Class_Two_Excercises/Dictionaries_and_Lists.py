contacts = {}

def add_contact(name, phone, email):
    """Add a new contact"""
    contacts[name] = {
        'phone': phone,
        'email': email
    }

def get_contact(name):
    """Get contact info"""
    if name in contacts:
        return contacts[name]
    return None

# Usage
add_contact('Alice', '555-1234', 'alice@email.com')
add_contact('Bob', '678-4321', 'bob@maile.com')

print(f'Contacts list: {contacts}')