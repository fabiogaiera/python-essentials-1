dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

"""
When you write a big or lengthy expression, it may be a good idea to keep it vertically aligned. 
This is how you can make your code more readable and more programmer-friendly, e.g.:
"""

# Example 1:
dictionary = {
    "cat": "chat",
    "dog": "chien",
    "horse": "cheval"
}

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }
