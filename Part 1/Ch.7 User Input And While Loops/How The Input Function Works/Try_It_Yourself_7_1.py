# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.

car = input("What kind of rental car would you like to rent today? : ")
print("Okay, let me see if I can find you a " + car + ".")

# 7-2. Restaurant Seating: Write aprogram that asks the user how many
# people are in their dinner group. If the answer is more than eight, print a message
# saying they'll have to wait for a table. Otherwise, report that their table is ready.

dinner = input("How many are in your dinner party: ")
dinner = int(dinner)

if dinner > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

# Multiples of Ten: Ask the user for a number, and then report
# whether the number is a multple of 10 or not.

number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")