list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
# ['B', 'C']

del list_2[0]
# ['C']

print(list_3)
# Output is ['C']
