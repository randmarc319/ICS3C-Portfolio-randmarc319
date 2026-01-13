price = float(input("Item price:"))

tax_rate = float(input("Tax Rate:"))

tax = (tax_rate * price + price)

print(f"Subtotal:{price}$")

print(f"Tax:{tax_rate * price:.2f}$")

print(f"Total:{tax:.2f}$")
    
