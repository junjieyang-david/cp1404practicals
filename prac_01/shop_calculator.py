LOWEST_TOTAL_PRICE_IN_DISCOUNT = 100
DISCOUNT_RATE = 0.1
amount = 0
total_price = 0
numbers = int(input("Number of items: "))
if numbers < 0 :
    print("Invalid number of items!")
    numbers = int(input("Number of items: "))
while amount < numbers:
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
    amount += 1
if total_price > LOWEST_TOTAL_PRICE_IN_DISCOUNT:
    total_price -= total_price * DISCOUNT_RATE
print(f"Total price for {numbers} items is ${total_price:.2f}.")