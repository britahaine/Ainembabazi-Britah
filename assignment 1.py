inventory = {}

def add_item():
    #Add a new item to the inventory.
    item_name = input("Enter item name: ")
    if item_name in inventory:
        print(f"Item '{item_name}' already exists. ")
        return
    
    try:
    
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
        price = float(input("Enter price per unit: "))
        if price < 0:
            print("Price cannot be negative.")
            return
        inventory[item_name] = {'quantity': quantity, 'price': price}
        print(f"Item '{item_name}' added successfully.")
    except ValueError:
        print("Invalid input. Quantity and price must be numbers.")

def update_item():
    #Update quantity of an existing item.
    item_name = input("Enter item name to update: ")
    if item_name not in inventory:
        print(f"Item '{item_name}' not found.")
        return
    try:
        quantity_change = int(input("Enter quantity to add/subtract (use negative to reduce): "))
        new_quantity = inventory[item_name]['quantity'] + quantity_change
        if new_quantity < 0:
            print("Cannot reduce quantity below 0.")
            return
        inventory[item_name]['quantity'] = new_quantity
        print(f"Updated '{item_name}' quantity to {new_quantity}.")
    except ValueError:
        print("Invalid input. Quantity must be a number.")

def remove_item():
    #Remove an item from the inventory.
    item_name = input("Enter item name to remove: ").strip().lower()
    if item_name in inventory:
        del inventory[item_name]
        print(f"Item '{item_name}' removed successfully.")
    else:
        print(f"Item '{item_name}' not found.")

def display_inventory():
    #Display all inventory items.
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n=== Inventory ===")
    print(f"{'Item':<20} {'Quantity':<10} {'Price':<10}")
    print("-" * 40)
    for item, details in inventory.items():
        print(f"{item:<20} {details['quantity']:<10} ${details['price']:.2f}")
    print("=================\n")

def main():
    #Main program loop for the inventory management system.
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item Quantity")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            display_inventory()
        elif choice == '5':
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()