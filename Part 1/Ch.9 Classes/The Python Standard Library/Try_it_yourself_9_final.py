# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary.
from collections import OrderedDict


glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

# 9-14. Dice: The module random contains functions that generate random numbers
# in a variety of ways. The function randint() returns an integer in the
# range you provide. The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.


