def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add Item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty. Please try again.")

        elif choice == '2':
            # Remove Item
            if not shopping_list:
                print("The shopping list is empty.")
                continue
                
            print("Current shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
                
            try:
                item_num = int(input("Enter the number of the item to remove: "))
                if 1 <= item_num <= len(shopping_list):
                    removed_item = shopping_list.pop(item_num - 1)
                    print(f"'{removed_item}' has been removed from the shopping list.")
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            # View List
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")

        elif choice == '4':
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()