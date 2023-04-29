import pickle5 as pickle


# Load the phone directory from the file (or create a new one)
try:
    with open("phone_dir.txt", "rb") as file:
        phone_dir = pickle.load(file)
except FileNotFoundError:
    phone_dir = {}

# Define a function to add a new entry to the phone directory
def add_entry(phone_dir):
    name = input("Enter a name: ")
    number = input("Enter a phone number: ")
    phone_dir[name] = number
    with open("phone_dir.txt", "wb") as file:
        pickle.dump(phone_dir, file)

# Define a function to look up a phone number by name
def search(phone_dir):
    name = input("Enter a name to search: ")
    if name in phone_dir:
        print(f"{name}'s phone number is {phone_dir[name]}")
    else:
        print(f"No phone number found for {name}")

# Run the phone directory program in a loop until the user chooses to quit
while True:
    choice = input("What do you want to do? (1) Add entry (2) Search (3) Quit\n")
    if choice == "1":
        add_entry(phone_dir)
    elif choice == "2":
        search(phone_dir)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
