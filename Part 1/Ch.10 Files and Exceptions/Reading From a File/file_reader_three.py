# Making a list of lines from a File
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in line:
    print(line.rstrip())
