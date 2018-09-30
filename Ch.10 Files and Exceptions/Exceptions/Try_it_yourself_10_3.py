# 10-6. Additon: One common problem when prompting for numerical input occurs
# when people provide text instead of numbers. When you try to convert
# the input to an int, you'll get a TypeError. Write a program that prompts for
# two numbers. Add them togetherand print the result. Catch the TypeError if either
# input value is not an umber, and print a friendly error merssage. Test your
# program by entering two numbers and then by entering some text instead of a number.
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)

except ValueError:
    print("Sorry, I really needed a number.")

else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user
# can continue entering numbers even if they make a mistake and enter text instead of a number.

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")

# 10-8. Cats and Dogs: Mkae two files, cats.txt and dogs.txt. Store at least three names of cats
# in the first file and three names of dogs sin the second file. Write a program that tries to read
# these and print the contents of the files to the screen. Wrap your code in a try-except block to
# catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files
# to a different location on your system, and make sure the code in the xcept block executes properly.

# 10-9. Silent Cats and Dogs: Modify your except block in Excersie 10-8 to fail silently if either
# file is missing.

# 10-10. Common words: no.