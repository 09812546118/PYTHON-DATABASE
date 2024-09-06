from os import system

# List to store names
names: list = []

def display_menu() -> None:
    system("cls")
    menu_options: tuple = (
        "------- Main Menu -------",
        "1. Add Name",
        "2. Find Name",
        "3. Delete Name",
        "4. Update Name",
        "5. Display All Names",
        "0. Quit/Exit",
        "-------------------------"
    )
    for option in menu_options:
        print(option)

def add_name() -> None:
    system("cls")
    name = input("Enter a new name: ")
    names.append(name)
    print("\nNew Name Added: ", name)

def find_name() -> None:
    system("cls")
    name = input("Enter name to search: ")
    if name in names:
        print(f"{name} is found in the name list.")
    else:
        print(f"{name} is NOT found in the name list.")

def update_name() -> None:
    system("cls")
    old_name = input("Enter the name you want to update: ")
    if old_name in names:
        new_name = input(f"Enter new name to replace {old_name}: ")
        names[names.index(old_name)] = new_name
        print(f"{old_name} has been successfully updated to {new_name}.")
    else:
        print(f"{old_name} is NOT found in the name list.")

def delete_name() -> None:
    system("cls")
    name = input("Enter name to delete: ")
    if name in names:
        opt = input(f"Do you really want to delete {name} (yes, no)? ").strip().lower()
        if opt == "yes":
            names.remove(name)
            print(f"{name} has been successfully removed from the list.")
        else:
            print(f"{name} has not been removed from the list.")
    else:
        print(f"{name} is NOT found in the name list.")

def display_all_names() -> None:
    system("cls")
    if names:
        print("List of Names:")
        for name in names:
            print(name)
    else:
        print("The name list is empty.")
    input("Press Enter to continue...")

def main() -> None:
    while True:
        display_menu()
        option = input("Enter Option (0..5): ").strip()
        
        if option == "0":
            print("Goodbye!")
            break
        elif option == "1":
            add_name()
        elif option == "2":
            find_name()
        elif option == "3":
            delete_name()
        elif option == "4":
            update_name()
        elif option == "5":
            display_all_names()
        else:
            print("Invalid option. Please choose a valid option (0..5).")

if __name__ == "__main__":
    main()
