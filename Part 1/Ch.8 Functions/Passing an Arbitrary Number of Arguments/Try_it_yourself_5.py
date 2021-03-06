# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a different number
# of arguments each time.

def make_sandwhich(*items):
    """Make a sandwhich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("......adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwhich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwhich('turkey', 'apple slices', 'honey mustard')
make_sandwhich('peanut butter', 'strawberry jam')
# 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
# a profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color = 'blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year = 1991, color = 'white',
                     headlights = 'popup')
print(my_accord)
