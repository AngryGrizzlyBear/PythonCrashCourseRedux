motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Appending
motorcycles.append('ducati')
print(motorcycles)
# This is my own personal test that I'm conducting out of curiosity.

list = input("What's your favorite car? ")

favorite_car = []

favorite_car.append(list)

print(favorite_car)

print("Your favorite car is " + str(favorite_car[0]).title() + "!")

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Inserting Elements into a list

motorcycles.insert(0, 'ducati')

print(motorcycles)

# Removing Elements from a list

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing an Item using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Popping items from any position in a list
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + '.')

# Removing an item by value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")