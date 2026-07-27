
items = []

while True:

    print("\nMenu:")
    print("1. Add item")
    print("2. Show items")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item: ")
        items.append(item)

    elif choice == "2":
        print("items:", items)

    elif choice == "3":
        item = input("Enter item to remove: ")
        
        if item in items:
            items.remove(item)
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == "4":
        print("Goodbye!")

    else:
        print("Invalid choice ")


        


def show_menu():
    print("\nMenu:")
    print("1. Add item")
    print("2. Show items")
    print("3. Remove item")
    print("4. Exit")


def show_items(items):
    if not items:
        print("No items in the list.")
    else:
        print("Items:")
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")


def main():

    items = []

    while True:

        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter item: ")
            items.append(item)

        elif choice == "2":
            show_items(items)

        elif choice == "3":
            item = input("Enter item to remove: ")

            if item in items:
                items.remove(item)
                print("Item removed.")
            else:
                print("Item not found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()



