# 10-1. Learning Python: Open a blank file in your text editor and write a few lines
# Summarizing what you've learned about Python so far. Start each line with the phrase
# In Python you can... Save the file asd learning_python.txt in the same directory as
# Your exercises from this chapter. Write a program that reads the file and prints what you
# wrote three times. Print the contents once by reading in the entire file once by looping over
# the file objevct, and once by storing the lines in a list and then working with them
# outside the with block.

filename = 'learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in as list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

# 10-2. Learning C: You can use the replace() method to replace any word in a string with a different word.
# Read in each line from the  file you just created, learning_python.txt, and replace the word
# Python with the name of another language, such as C. Print each modified line to the screen.

filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
print(line.replace('Python', 'C'))

