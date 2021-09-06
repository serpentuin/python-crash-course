my_pizzas = ["chicken pepperoni", "hawaiian chicken", "super supreme"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("spicy tuna")
friend_pizzas.append("chickensaurus")

print("\nMy favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())