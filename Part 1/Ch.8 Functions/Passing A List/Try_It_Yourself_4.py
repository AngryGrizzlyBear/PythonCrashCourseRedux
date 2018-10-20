# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.

def show_magicians():
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians()

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.


# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.