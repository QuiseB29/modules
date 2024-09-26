def add_contact(contacts, name, phone):
    # Check if contact already exists
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Contact with name '{name}' already exists.")
            return
    # Add new contact if not a duplicate
    contacts.append({'name': name, 'phone': phone})

def delete_contact(contacts, name):
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            return contacts.pop(i)
    print(f"Contact with name '{name}' not found.")
    return None

def display_contact(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    for contact in contacts:
        if 'name' in contact and 'phone' in contact:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        else:
            print("Invalid contact format.")

