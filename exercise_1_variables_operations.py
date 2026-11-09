print("--- Task 1: temperature ---")
celsius = int(input("Enter a temperature in Celsius: "))
fahrenheit =  celsius * 9 / 5 + 32
print(f"{celsius} C is {fahrenheit} F")


print("\n --- Task 2: shopping bill ---")
price = int(input("Enter a price: "))
quantity = int(input("Enter a quantity: "))
vat_rate = float(input("Enter a vat: "))
total_cost = round(price * quantity * (1 + vat_rate), 2)
print(f"{quantity} items at £{price} plus VAT costs £{total_cost}")
