import contact_manager
import datetime

current_time = datetime.datetime.now()
print("Today date is ",current_time)

def main():
    contacts = []
    while True:
        print("\n1. Add Contact")
        print("2. Display Contact")
        print("3. Delete Contact")
        choice = input("Choose an option")
        if choice == "1":
            name = input("Enter Name:")
            phone = input("Enter Phone:")
            contact_manager.add_contact(contacts, name, phone)
        
        elif choice == "2":
            contact_manager.display_contact(contacts)
        
        elif choice == "3":
            name = input("Enter Name to delete:")
            if contact_manager.delete_contact(contacts, name) is not None:
                print("Contact deleted")
            else:
                print("Contact not found")
        
        elif choice == "4":
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
