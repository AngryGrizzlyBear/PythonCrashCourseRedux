squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions...I feel like I'll be seeing this later
squares = [value**2 for value in range(1,11)]
print(squares)