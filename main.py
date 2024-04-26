import mood_responses

def main():
    while True:
        print("\n1. Happy")
        print("2. Sad")
        print("3. Excited")
        print("4. Exit")
        choice = input("How are you feeling today? ")

        if choice == "1":
            mood = "happy"
            print(f"Glad you are feeling {mood}")
        elif choice == "2":
            mood = "sad"
            print(f"Cheer up! Hope it gets better.")
        elif choice == "3":
            mood = "excited"
            print("We can see the excitement on your face!")
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
