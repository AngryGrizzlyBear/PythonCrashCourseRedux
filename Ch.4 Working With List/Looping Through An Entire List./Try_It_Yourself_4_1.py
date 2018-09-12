# 4-1 Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# •	 Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

# Part One
pizza_list = ['pepperoni', 'meat lovers', 'sausage']
for pizza in pizza_list:
    print(pizza)

# Part Two. I wanted to separate these to show the steps of each.
pizza_list = ['pepperoni', 'meat lovers', 'sausage']
for pizza in pizza_list:
    print("I really love " + pizza.title() + "!")
print("I really enjoy all types of pizza. Meat Lovers, Pepperoni, and Sausage are all great pizzas. I "
      "really love pizza!")

# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# •	 Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!

# Part One.
common_animals = ['dog', 'wolf', 'bear']
for animal in common_animals:
    print(animal)

# Part Two. Similar reasons as above.
common_animals = ['dog', 'wolf', 'bear']
for animal in common_animals:
    print("A " + animal + " would make a great pet!")
print("These animals look very similar and have a lot in common; however, I'm not too sure about"
      "the bear though.\nYou'll have to do your research on that one. Be careful out there!\nStill"
      " each has been proven to make great pets!")