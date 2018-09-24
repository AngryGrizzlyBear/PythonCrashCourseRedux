# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwhich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwhiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

print("\n")
while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print("I'm working on your " + current_sandwhich + " sandwhich.")
    finished_sandwhiches.append(current_sandwhich)

print("\n")
for sandwhich in finished_sandwhiches:
    print("I made a " + sandwhich + " sandwich.")
# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.


# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.