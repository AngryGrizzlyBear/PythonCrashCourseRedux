# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

programming_meaning = {'Variable': 'To name something.',
                       'List': 'A variable that holds a collective of information.',
                       'Dictionary': 'Holds even more stuff. Think of a bigger list with options.',
                       'Loops': 'Goes around and around.',
                       'For Loops': 'Cooler than while loops.',
                       'More Loops': 'Is more loops.',
                       'Key': 'Is the first variable in a dictionary list.',
                       'Value': 'assigned variable to the key.',
                       'Hrm': "I really can't think of anything else.",
                       'Maybe': "I'm lazy?"}

for name, meaning in programming_meaning.items():
    print("The definition of " + name.title() + " is: " + meaning)

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary

rivers = {'ganges': 'india',
          'mississipi': 'mississipi',
          'nile': 'egypt',
          }

for river, place in rivers.items():
    print("\nThe " + river.title() + " River is located in "
          + place.title() + "!")