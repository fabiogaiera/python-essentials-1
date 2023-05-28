# LAB

def is_prime(num):
    prime = True

    if num == 1:
        return prime
    else:
        count = 2
        while count < num:
            if num % count == 0:
                prime = False
                break
            count += 1

    return prime


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
