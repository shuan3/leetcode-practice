log=[["supply","item1",5,100],["sell","item1",3],["return","item1",2,100,80],["sell","item1",1]]
#return an array representing the profit of each transaction
from typing import List
def solution(log)->List[int]:
    profit=[]
    inventory={}
    for i in log:
        if i[0]=="supply":
            if i[1] in inventory:
                inventory[i[1]]+=[i[3]]*i[2]
            else:
                inventory[i[1]]=[i[3]]*i[2]
        elif i[0]=="sell":
            if i[1] in inventory and len(inventory[i[1]])>=i[2]:
                # print(i[2],inventory[i[1]])
                # for i, x in enumerate(inventory[i[1]]):
                #     print(i,x)
                # print([x for i, x in enumerate(inventory[i[1]]) if i < i[2]])
                # print(inventory[i[1]][0:i[2]])
                profit.append([sum(inventory[i[1]][0:i[2]]) ])
                inventory[i[1]]=inventory[i[1]][i[2]:]
                
        elif i[0]=="return":
            if i[1] in inventory:
                inventory[i[1]]+=[i[4]]*i[2]
                profit.append([-1*sum(inventory[i[1]][0:i[2]]) ])
            else:
                inventory[i[1]]=[i[4]]*i[2]
         

    return profit

# print([1]*3.pop([1]))
print(solution(log))

# class Product:
#     def __init__(self, name, quantity, price):
#         self.name = name
#         self.quantity = quantity
#         self.price = price

#     def __str__(self):
#         return f"{self.name}: Quantity={self.quantity}, Price=${self.price:.2f}"


# class Inventory:
#     def __init__(self):
#         self.products = {}  # Dictionary to store products (name: Product object)

#     def add_product(self, name, quantity, price):
#         if name in self.products:
#             print(f"Product '{name}' already exists. Use update_quantity() to change quantity.")
#             return

#         product = Product(name, quantity, price)
#         self.products[name] = product
#         print(f"Product '{name}' added successfully.")

#     def update_quantity(self, name, quantity_change):
#         if name not in self.products:
#             print(f"Product '{name}' not found in inventory.")
#             return

#         self.products[name].quantity += quantity_change
#         if self.products[name].quantity < 0:
#             self.products[name].quantity = 0 #Prevent negative quantities
#             print("Warning: Quantity cannot be negative. Setting to 0.")
#         print(f"Quantity of '{name}' updated to {self.products[name].quantity}.")

#     def update_price(self, name, new_price):
#         if name not in self.products:
#             print(f"Product '{name}' not found in inventory.")
#             return

#         self.products[name].price = new_price
#         print(f"Price of '{name}' updated to ${new_price:.2f}.")

#     def remove_product(self, name):
#         if name not in self.products:
#             print(f"Product '{name}' not found in inventory.")
#             return

#         del self.products[name]
#         print(f"Product '{name}' removed from inventory.")

#     def get_product(self, name):
#         if name not in self.products:
#             print(f"Product '{name}' not found in inventory.")
#             return None
#         return self.products[name]

#     def list_products(self):
#         if not self.products:
#             print("Inventory is empty.")
#             return

#         print("Current Inventory:")
#         for product in self.products.values():
#             print(product)

#     def calculate_inventory_value(self):
#         total_value = 0
#         for product in self.products.values():
#             total_value += product.quantity * product.price
#         return total_value


# # Example Usage:
# inventory = Inventory()

# inventory.add_product("Laptop", 10, 1200.00)
# inventory.add_product("Mouse", 20, 25.00)
# inventory.add_product("Keyboard", 15, 75.00)

# inventory.list_products()

# inventory.update_quantity("Laptop", -5)
# inventory.update_quantity("Monitor", 5) #Product not found

# inventory.update_price("Mouse", 30.00)

# inventory.remove_product("Keyboard")
# inventory.remove_product("Keyboard") #Product not found

# inventory.list_products()

# total_value = inventory.calculate_inventory_value()
# print(f"Total inventory value: ${total_value:.2f}")



# #Demonstrates negative quantity prevention
# inventory.update_quantity("Laptop", -100)
# inventory.list_products()



# from collections import defaultdict

# def process_transaction_log(transaction_log):
#     """
#     Processes a transaction log to calculate supply, revenue, and item counts.

#     Args:
#         transaction_log: A list of lists, where each inner list represents a transaction
#                          in the format [supply, item_name, count, price].

#     Returns:
#         A dictionary containing the processed information:
#             {
#                 "supply": {item_name: total_supply, ...},
#                 "revenue": {item_name: total_revenue, ...},
#                 "item_count": {item_name: total_count, ...}
#             }
#     """

#     supply = defaultdict(int)
#     revenue = defaultdict(float)  # Use float for prices/revenue
#     item_count = defaultdict(int)

#     for transaction in transaction_log:
#         supply_change, item_name, count, price = transaction

#         supply[item_name] += supply_change * count # Supply change can be negative

#         revenue[item_name] += count * price
#         item_count[item_name] += count

#     return {
#         "supply": dict(supply),  # Convert defaultdict to regular dict for cleaner output
#         "revenue": dict(revenue),
#         "item_count": dict(item_count)
#     }



# # Example transaction log (supply changes can be negative)
# transaction_log = [
#     [100, "Laptop", 5, 1200.00],
#     [-50, "Laptop", 2, 1200.00],  # Example of supply decrease
#     [50, "Mouse", 10, 25.00],
#     [25, "Keyboard", 5, 75.00],
#     [75, "Mouse", 5, 25.00],
#     [100, "Laptop", 3, 1250.00], #Different Price
# ]

# processed_data = process_transaction_log(transaction_log)
# print(processed_data)


# transaction_log_empty = []
# processed_data = process_transaction_log(transaction_log_empty)
# print(processed_data)


# transaction_log_negative_supply = [
#     [-100, "Laptop", 5, 1200.00],
# ]

# processed_data = process_transaction_log(transaction_log_negative_supply)
# print(processed_data)


# transaction_log_zero_count = [
#     [100, "Laptop", 0, 1200.00],
# ]

# processed_data = process_transaction_log(transaction_log_zero_count)
# print(processed_data)