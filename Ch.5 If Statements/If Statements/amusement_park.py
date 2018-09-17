# The if-elif-else chain

age = 12

if age < 4:
    print("Your admission costs is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# Alternative method
age = 22

if age < 4:
    price = 0
elif age < 18:
    price = 5
# Using Multiple elif Blocks
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")