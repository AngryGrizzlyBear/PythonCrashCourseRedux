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


