# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the
# change.
# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

resturant_menu = ('cheeseburger', 'fries', 'milkshake', 'tacos', 'sushi', 'nachos', 'ravioli')
print("This is our current menu:")
for items in resturant_menu:
    print(items.title())

# resturant_menu[0] = 'super burger'

resturant_menu = ('cheeseburger', 'fries', 'milkshake', 'tacos', 'sushi', 'nachos', 'onion rings', 'mega burger')
print("Our menu has changed. We've made it bigger, stronger, and more flavorful than before! "
      "\nPlease see below.:")
for new_items in resturant_menu:
    print(new_items.title())
