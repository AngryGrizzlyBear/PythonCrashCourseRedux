# 10-11 Favorite Number: Write a program that prompts for the user's favorite
# number. User json.dump() to store this number in a file. Write a separate
# program that reads in this value and prints the message, "I know your favorite
# number! It's _____."



# 10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11
# into one file. If the number is already stored, report the favorite number to the user.
# If not, prompt for the user's favorite number and store it in a a file. Run the program twice
# to see that it works.

# 10-3. Verify User: The final listing for remember_me.py assumes either that the user has already
# entered their username or that the program is running for the first time. We should modify it
# in case the current user is not the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if this is  the correct username.
# If it's not, call get_new_username() to get the correct username.