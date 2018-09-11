# 3-8 Seeing the World: Think of at least five places in the world you'd like to visit.
# Store th locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don't worry about printing the list neatly,
# just print it as a raw Python list.
# Use sorted to print your list in reverse alphabetical order without changing the order of the original
# list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# Show that your list is still in order by printing it again.
# Use reverse to change the order of your list. Print the list to show that it's order has changed.
# Use reverse() to change the order of your list again. Print the list to show it's back
# to its original order.
# Use sort() to change your list so it's stored in reverse alphabetical order. Print the list to show that
# it's order has changed.
# Use sort() to change your list so it's stored in reverse alphabetical order. Print the list to show that its order has
# changed.

travel_places = ['Tokyo', 'Nagasaki', 'Kyoto', 'Akihabara', 'Nagano']
print(travel_places)
print(sorted(travel_places))
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.sort()
print(travel_places)
travel_places.sort(reverse=True)
print(travel_places)
