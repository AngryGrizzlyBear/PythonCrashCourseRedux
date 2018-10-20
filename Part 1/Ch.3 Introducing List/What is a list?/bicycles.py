bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# I'm just calling the first item from the list here.
print(bicycles[0])

# I'm now neatly capitolizing the item with title.
print(bicycles[0].title())

# Index Positions starting at 0, not 1.

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])

# Using Individual Values from a list

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)