# 3-1 Names: Store the names of a few of your friends in a list called names.
# Print each person's name by accessing each element in the list, one at time.

names = ['frank', 'james', 'johhny', 'sarah', 'samantha']

print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())

# 3-2 Start with the list you used in Exercise 3-1, but instead of just print each person's name,
# print a message to them. The text of each message should be the same ,but each message should be
# personalized with the person's name.

print("Hello there, " + names[0].title() +  ". Would you like to play a game today?")
print("What's new, " + names[1].title() + "?")
print("Want to grab a bite to eat for lunch, " + names[2].title() + "?")
print("Where are we going today, " + names[3].title() + "?")
print("Did you and Thomas ever get married, " + names[4].title() + "?" )