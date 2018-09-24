def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()

# Passing information to a Function

def greet_user_two(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user_two('stan')