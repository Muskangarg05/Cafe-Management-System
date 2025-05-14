# WELCOME--
print("...Welcome to the WAHH TAJ CAFE🍹... \n\n ->Place Your Order From The Menu---\n")
menu = {
    "tulsi adrakh chai" : 45,
    "strawberry shake" : 150,
    "blueberry shake" : 150,
    "latte" : 80,
    "hot coffee" : 80,
    "cold coffee" : 100,
    "mojito" : 150,
    "cold drink" : 40
}
# PRINTING MENU--

for item in menu:
     print(f"{item}: {menu[item]}")
print("\n")     

# TAKING ORDER AND ADD IN LIST--

order_items = input("Place your order (separated by commas): ").lower().split(",")
order_items = [item.strip() for item in order_items]
total_amount = 0

# ASKING FOR FINALIZE OR CHANGING ORDER--
while True:
    choice = input("Want to Change , Remove item or Final the order: ").lower().strip()
    print("\n")

# CHANGE ITEM--
    if choice == "change":
# ALL ITEMS CHANGING--    
        change_all = input("Do you want to change the entire order? (yes/no): ").lower().strip()
        if change_all == 'yes':
             order_items = input("Re-enter your full order (separated by commas): ").lower().split(",")
             order_items = [item.strip() for item in order_items] 
             print(f"Your new order is: {order_items}")
# ONLY FEW OF THEM TO CHANGE--             
        else:
            item_to_change = input("Enter item you want to replace(enter only 1 item at once): ").lower().strip()
            if item_to_change in order_items:
               new_item = input("Enter your new item: ").lower().strip()
               if new_item in menu:
                    order_items[order_items.index(item_to_change)] = new_item
               else:
                    print("Item not present in menu\n")    
            else:
             print("This item is not in your current order\n")

# REMOVE ITEM--
    elif choice == "remove":
         item_to_remove = input("Item you want to remove: ").lower().strip()
         if item_to_remove in order_items:
              order_items.remove(item_to_remove)
         else:
              print("This item already not present in list\n")     

# FINALIZE ORDER--
    else:
         break

print("your current order is-> " , order_items)
# CALCULATE PAYMENT--
for item in order_items:
     item = item.strip()
     if item in menu:
          total_amount += menu[item]
     else: 
          print("Your item is not in list\n")  

print(f"Total_Amount to pay is: {total_amount}")         
print("-->THANKS! YOUR ORDER IS PREPAIRING😊...")
