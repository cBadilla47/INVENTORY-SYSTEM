from datetime import datetime


class Product:
    def __init__(self, item_id, item_name, stock_count, price):
        self.item_id = item_id
        self.item_name = item_name
        self.stock_count = stock_count
        self.price = price
        self.history = []

    def add_history_entry(self, action, quantity, performed_by):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} - {action} {quantity} {self.item_name}(s) by {performed_by}"
        self.history.append(entry)

    def get_history(self):
        return self.history



class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, item_id, item_name, stock_count, price, added_by):
        if item_id in self.inventory:
            self.inventory[item_id]['stock_count'] += stock_count
            self.inventory[item_id]['product'].add_history_entry("Added", stock_count, added_by)
        else:
            new_product = Product(item_id, item_name, stock_count, price)
            self.inventory[item_id] = {'stock_count': stock_count, 'product': new_product}
            self.inventory[item_id]['product'].add_history_entry("Added", stock_count, added_by)
        print(f"{stock_count} {item_name}(s) added to inventory.")

    def remove_product(self, item_id, removed_by):
        if item_id in self.inventory:
            current_stock = self.inventory[item_id]['stock_count']
            if current_stock > 0:
                try:
                    quantity_to_remove = int(input(f"Enter the quantity to remove (1-{current_stock}): "))
                    if 1 <= quantity_to_remove <= current_stock:
                        self.inventory[item_id]['stock_count'] -= quantity_to_remove
                        self.inventory[item_id]['product'].add_history_entry("Removed", quantity_to_remove, removed_by)
                        print(f"{quantity_to_remove} {self.inventory[item_id]['product'].item_name}(s) removed from inventory by {removed_by}.")
                    else:
                        print("Invalid quantity. Please enter a valid quantity.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            else:
                print(f"No {self.inventory[item_id]['product'].item_name} available.")
        else:
            print(f"Item with ID {item_id} is not in the inventory.")

    def check_item_details(self, item_id):
        if item_id in self.inventory:
            product = self.inventory[item_id]['product']
            return f"Item ID: {item_id}\nName: {product.item_name}\nStock Count: {self.inventory[item_id]['stock_count']}\nPrice: {product.price}"
        else:
            return f"Item with ID {item_id} is not in the inventory."

    def get_inventory(self):
        return self.inventory

    def show_history(self):
        for item_id, data in self.inventory.items():
            product = data['product']
            print(f"Item ID: {item_id}\nItem Name: {product.item_name}\nHistory:")
            for entry in product.get_history():
                print(entry)



def main():
    inventory_instance = Inventory()

    # Predefined list of items to add to the inventory
    predefined_items = [
        {"item_id": "1", "item_name": "IPHONE 12", "stock_count": 10, "price": 38000},
        {"item_id": "2", "item_name": "IPHONE 13", "stock_count": 20, "price": 40000},
        {"item_id": "3", "item_name": "IPHONE 14", "stock_count": 30, "price": 45000}
    ]

    for item in predefined_items:
        inventory_instance.add_product(item["item_id"], item["item_name"], item["stock_count"], item["price"], "Admin")

    while True:
        print("\n1. Stock-in")
        print("2. Stock-Out")
        print("3. Check Item Details")
        print("4. Show History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter item ID: ")
            item_name = input("Enter item name: ")
            stock_count = int(input("Enter stock count: "))
            price = float(input("Enter price: "))
            
            try:
                added_by = input("Enter your name: ")
            except Exception:
                added_by = input("Enter your name: ")

            inventory_instance.add_product(item_id, item_name, stock_count, price, added_by)
        elif choice == "2":
            item_id = input("Enter item ID: ")
            
            try:
                removed_by = input("Enter your name: ")
            except Exception:
                removed_by = input("Enter your name: ")

            inventory_instance.remove_product(item_id, removed_by)
        elif choice == "3":
            item_id = input("Enter item ID: ")
            print(inventory_instance.check_item_details(item_id))
        elif choice == "4":
            inventory_instance.show_history()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
