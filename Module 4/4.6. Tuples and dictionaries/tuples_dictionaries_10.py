dictionary = {"Bob": 123456, "Alice": 444333, "Fabio": 987654}
print(dictionary)

# Modify a value
dictionary['Bob'] = 333222
print(dictionary)

# Add a pair key:value
dictionary["Margarita"] = 192837
print(dictionary)

# Add a pair key: value
dictionary.update({"Alejandro": 229933})
print(dictionary)

# Remove a pair key:value
del dictionary['Bob']
print(dictionary)

# Remove last element
dictionary.popitem()
print(dictionary)
