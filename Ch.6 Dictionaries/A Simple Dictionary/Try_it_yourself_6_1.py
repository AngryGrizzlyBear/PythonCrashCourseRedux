# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person = {'first_name': 'Paul',
          'last_name': 'Stevenson',
          'age': 34,
          'city': 'Hekkinville',
          }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program

favorite_numbers = {
    'Stan': 32,
    'Nicole': 7,
    'Steve': 38,
    'Mike': 12,
    'Ross': 343,
    }

print("Stan's favorite number is " + str(favorite_numbers['Stan']) + "!")
print("Nicole's favorite number is " + str(favorite_numbers['Nicole']) + "!")
print("Steve's favorite number is " + str(favorite_numbers['Steve']) + "!")
print("Mike's favorite number is " + str(favorite_numbers['Mike']) + "!")
print("Ross's favorite number is " + str(favorite_numbers['Ross']) + "!")