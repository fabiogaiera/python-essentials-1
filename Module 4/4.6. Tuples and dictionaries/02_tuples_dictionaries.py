my_tuple = (1, 10, 100, 1000)

my_tuple.append(10000)  # AttributeError: 'tuple' object has no attribute 'append'
del my_tuple[0]
my_tuple[1] = -10
