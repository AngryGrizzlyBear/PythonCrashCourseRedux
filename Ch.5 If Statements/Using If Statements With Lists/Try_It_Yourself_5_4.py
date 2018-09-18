# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# •	 If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging
# in again.

user_names = ['eric', 'lisa', 'tim', 'thomas', 'admin']

for user in user_names:
    if user == 'admin':
        print("Hello, " + user.title() + "! Would you like to see a status report?")
    else:
        print("Hello, " + user.title() + ". Thank you for logging in again.")


# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# •	 If the list is empty, print the message We need to find some users!
# •	 Remove all of the usernames from your list, and make sure the correct
# message is printed.

user_names = []

if user_names:
    for user in user_names:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again!")
else:
    print("We need to find some users!")

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# •	 Make a list of five or more usernames called current_users.
# •	 Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# •	 Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# •	 Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.

current_users = ['jaime', 'thomas', 'martin', 'stephen', 'nancy']
new_users = ['stacy', 'jaime', 'thomas', 'stan', 'lucy']

for users in new_users:
    if users in current_users:
        print("Sorry," + users + " is not available. You will have to input a new username.")
    else:
        print(users + ". This name is available!")

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# •	 Store the numbers 1 through 9 in a list.
# •	 Loop through the list.
# •	 Use an if-elif-else chain inside the loop to print the proper ordinal ending
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")