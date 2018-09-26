# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the Restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def descsribe_resturant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_resturant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('the mighty hippo', 'chicken')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.descsribe_resturant()
restaurant.open_resturant()
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.