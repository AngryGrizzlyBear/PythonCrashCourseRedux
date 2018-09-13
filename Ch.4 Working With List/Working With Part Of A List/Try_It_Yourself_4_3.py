# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# •	 Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# •	 Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.

burgers = ['cheeseburger', 'hamburger', 'bacon cheeseburger', 'western cheeseburger', 'chilli burger']
print("The first three items in this list are:")
for burger in burgers[:3]:
    print(burger.title())

print("\nThree items from the middle of the list are:")
for burger in burgers[2:5]:
    print(burger.title())

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

pizzas = ['pepperoni', 'meat lovers', 'cheese', 'sausage', 'hawaiian']
friends_pizzas = pizzas[:]

pizzas.append('bbq')
friends_pizzas.append('four cheese')

print("My pizzas are:")
print(pizzas)
print("\nMy friend loves these pizzas:")
print(friends_pizzas)

for pizza in pizzas[5:]:
    print("I added:")
    print(pizza.title())

for pizza2 in friends_pizzas[5:]:
    print("My friend added:")
    print(pizza2.title())