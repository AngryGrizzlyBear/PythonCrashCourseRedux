# 3-1 Names: Store the names of a few of your friends in a list called names.
# Print each person's name by accessing each element in the list, one at time.

names = ['frank', 'james', 'johhny', 'sarah', 'samantha']

print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())

# 3-2 Greetings: Start with the list you used in Exercise 3-1, but instead of just print each person's name,
# print a message to them. The text of each message should be the same ,but each message should be
# personalized with the person's name.

print("Hello there, " + names[0].title() +  ". Would you like to play a game today?")
print("What's new, " + names[1].title() + "?")
print("Want to grab a bite to eat for lunch, " + names[2].title() + "?")
print("Where are we going today, " + names[3].title() + "?")
print("Did you and Thomas ever get married, " + names[4].title() + "?")

# 3-3 Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your
# list to print a series of statements about these items, such as "I would
# like to own a Honda motorcycle."

favorite_transportation = ['nissan', 'ducati', 'train', 'spirit']

print("I really enjoy my " + favorite_transportation[0].title() + ". It's great on gas mileage.")
print("I would like to ride a " + favorite_transportation[1].title() + " bike. It looks stylish.")
print("I want to take the bullet " + favorite_transportation[2] + " train in Japan. It's fast!")
print("Have you ever flown with " + favorite_transportation[3].title() + " Airlines? They're funny!")