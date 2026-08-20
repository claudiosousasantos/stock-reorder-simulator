flour_stock = 3            # Initial stock of flour (kg)
reorder_threshold = 5      # Minimum stock before reordering
reorder_amount = 20        # How many kg we add each time we reorder

while flour_stock <= reorder_threshold:
    print(f"Flour stock is low ({flour_stock}kg). Reordering flour!")
    flour_stock += reorder_amount
    print(f"New stock after reorder: {flour_stock}kg")

print("Current flour stock:", flour_stock, "kg")