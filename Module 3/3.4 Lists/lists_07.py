my_list = [1, 2, 3, 4]

total = 0
for i in my_list:
    total += i
print(total)

print()

total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)
