# RecursionError: maximum recursion depth exceeded
def factorial(n):
    return n * factorial(n - 1)


print(factorial(4))
