# defining the dictionary for a grocery list inventory.
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread":(117, "Bakery"),
    "Apples":(141, "Produce")

}

# retrieve the item bread and store it in bread_details.
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", grocery_inventory.get("Bread"))

# Adding A new item "Eggs".
grocery_inventory.update({"Cookies": (143, "Bakery")})
print("Inventory after adding Cookies:", grocery_inventory)

# Removing the Item "Eggs".
removed_item = grocery_inventory.pop("Eggs")
print("Remove Item:", removed_item)
print("Inventory after removing Eggs:", grocery_inventory)
