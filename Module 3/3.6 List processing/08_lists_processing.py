# LAB

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

list_without_repeated = []

for i in my_list:
    if i not in list_without_repeated:
        list_without_repeated.append(i)

my_list = list_without_repeated

print("The list with unique elements only:")
print(my_list)
