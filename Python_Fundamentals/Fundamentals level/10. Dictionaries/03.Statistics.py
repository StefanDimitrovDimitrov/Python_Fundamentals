"""
You seem to be doing great at your first job. You have now successfully completed the first 2 of your tasks and your boss decides to give you as your next task something more challenging. You have to accept all the new products coming in the bakery and finally gather some statistics.
You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics". Sometimes you may receive a product more than once. In that case you have to add the new quantity to the existing one. When you receive the "statistics" command, print the following:
"Products in stock:
- {product1}: {quantity1}
- {product2}: {quantity2}
…
Total Products: {count_all_products}
Total Quantity: {sum_all_quantities}"
Example
Input
bread: 4
cheese: 2
ham: 1
bread: 1
statistics

Output
Products in stock:
- bread: 5
- cheese: 2
- ham: 1
Total Products: 3
Total Quantity: 8





"""



products = {}

while True:

    command = input()

    if command == "statistics":
        break

    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product not in products:
        products[product] = 0
    products[product] += quantity

print("Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")