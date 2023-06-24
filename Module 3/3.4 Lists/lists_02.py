numbers = [10, 5, 7, 2, 1]
print("List content:", numbers)
print("List's length:", len(numbers))

del numbers[1]
print("List content:", numbers)
print("List's length:", len(numbers))

# You can't access an element which doesn't exist
print(numbers[4])
numbers[4] = 1
