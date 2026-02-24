produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce, dairy]

print("Groceries:")
for grocery in groceries:
    print(grocery)
    for item in grocery:
        print(f" - {item}")
    print("")