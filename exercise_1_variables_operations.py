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

print("\n --- Task 3: Hours and minutes ---")
total_minutes = int(input("Enter a total minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{hours} hours and {minutes} minutes left")

print("\n --- Task 4: names ---")
first_name = input("Enter a first name: ")
last_name = input("Enter a last name: ")
full_name = f"{first_name} {last_name}"
name_length = len(full_name)
print(f"{full_name} has {name_length}")


