dictionary = {"cat": "chat", "horse": "cheval", "dog": "chien"}

print("Original dictionary")
for key in dictionary.keys():
    print(key, "->", dictionary[key])

print()

print("Sorted dictionary")
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
