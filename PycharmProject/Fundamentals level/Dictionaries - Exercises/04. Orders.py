products_quantity = {}
products_price = {}

while True:
    command = input()

    if command == "buy":
        break

    name = command.split()[0]
    price = float(command.split()[1])
    quantities = int(command.split()[2])

    if name not in products_quantity:
        products_quantity[name] = quantities
        products_price[name] = price

    else:
        products_quantity[name] += quantities
        products_price[name] = price

products_total_price = {}
for k in products_quantity.keys():
    total_price = (products_quantity[k] * products_price[k])
    products_total_price[k] = total_price

for k, v in products_total_price.items():
    print(f"{k} -> {v:.2f}")