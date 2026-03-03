# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for product, valuse in products.items():
    price = float(valuse[0])
    quantity = int(valuse[1])
    total_sales = price * quantity
    print(f"Total Sales for {product}: ${total_sales}")
    total_sales_list.append(total_sales)
total_sum =sum(total_sales_list)
print(f"\nTotal sum of all sales: ${total_sum}")
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
