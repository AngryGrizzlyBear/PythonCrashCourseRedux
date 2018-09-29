# 10-3. Guest: Write a program that prompts the user for thier name. When they
# respond, write their name to a file called guest.txt
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)
# 10-4. Guest Book: Write a while loop that prompts users for their name. When they
# enter their nmae, print a greeting to the screen and add a line recording their
# visit in a file called guest_book.txt Make sure each entry ap0pears on a new line
# in the file.

# 10-5 Programming Poll: Write a while lloop that asls people why they like programming.
# Each time someone enters a reason, add their reason to a file that stores all the
# responses.