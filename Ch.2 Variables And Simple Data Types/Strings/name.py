name = "ada lovelace"

print(name.title())

# Could also use
print(name.upper())
print(name.lower())

# Here's another example
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

# Added example
print("Hello, " + full_name.title() + '!')

# We're going to use Whitespaces
print("Python")
print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavascript")

# Stripping Whitespace
favorite_language = "'python '"
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())