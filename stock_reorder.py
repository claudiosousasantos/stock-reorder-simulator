coffee_stock = 1          # Initial stock of coffee beans
reorder_threshold = 2     # Minimum stock before reordering
reorder_amount = 10       # How many units we add each time we reorder

while coffee_stock <= reorder_threshold:
    print(f"Stock is low ({coffee_stock}). Reordering coffee beans!")
    coffee_stock += reorder_amount
    print(f"New stock after reorder: {coffee_stock}")

print("Current stock:", coffee_stock)