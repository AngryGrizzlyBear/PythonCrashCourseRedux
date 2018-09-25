import pizza
# You can import specific functions.
# from pizza import make_pizza
# You can import as many functions as you want.
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# If I imported only make_pizza, then calling it would look like this
# make_pizza(16, 'pepperoni')

# You can make short-cuts too, if you felt like it
# import pizza as p
# p.make_pizza(etc)

# You can have python import every function in your module by:
# from pizza import *
# Not usually a good idea to use that if you didn't write the code.
