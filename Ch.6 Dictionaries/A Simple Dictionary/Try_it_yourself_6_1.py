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

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

programming_meaning = {'Variable': 'To name something.',
                       'List': 'A variable that holds a collective of information.',
                       'Dictionary' : 'Holds even more stuff. Think of a bigger list with options.',
                       'Loops': 'Goes around and around.',
                       'For Loops': 'Cooler than while loops.'}

word = 'Variable'
print(word +' : ' + programming_meaning['Variable'])
word = 'List'
print("\n" + word + ' : ' + programming_meaning['List'])
word = 'Dictionary'
print("\n" + word + ' : ' + programming_meaning['Dictionary'])
word = 'Loops'
print("\n" + word + ': ' + programming_meaning['Loops'])
word = 'For loops'
print("\n"+ word + ' : ' + programming_meaning['For Loops'])