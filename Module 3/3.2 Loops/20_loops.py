# LAB

blocks = int(input("Enter the number of blocks: "))
height = 0

if blocks == 0:
    height = 0
elif blocks == 1:
    height = 1
else:
    level = 1
    while blocks >= 0:
        if blocks < level:
            break
        else:
            blocks -= level
            height += 1
            level += 1

print("The height of the pyramid:", height)
