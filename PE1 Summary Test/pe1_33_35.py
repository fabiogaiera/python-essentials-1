x = int(input())  # 3
y = int(input())  # 2

x = x % y  # 3%2 = 1
x = x % y  # 1%2 = 1
y = y % x  # 2%1 = 0

print(y)  # 0
