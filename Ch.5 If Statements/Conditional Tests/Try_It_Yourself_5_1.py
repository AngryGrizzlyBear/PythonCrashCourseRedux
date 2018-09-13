# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# •	 Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# •	 Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

car = 'ducati'
other_car = 'BMW'
print("Is car == ducati? I predict True.")
print(car == 'ducati')

print("\nIs car == subaru? I predict False")
print(car == 'subaru')

print("\nIs car == nissan? I predict False.")
print(car == 'nissan')

print("\nIs car == ducati.lower? I predict True.")
print(car.lower() == 'ducati')

print("\nIs other car.upper  == 'BMW? I predict True.")
print(other_car.upper() == 'BMW')

print("\nIs other car == 'BMW? I predict True.")
print(other_car == 'BMW')

print("\nIs car == to other car? I predict False.")
print(car == other_car)

print("\nIs car.lower == other_car lower? I predict False.")
print(car.lower() == other_car.lower())

print("\nIs other car != car? I predict True.")
print(other_car != car)

print("\n Is car = BMW? I predict False.")
print(car == 'BMW')