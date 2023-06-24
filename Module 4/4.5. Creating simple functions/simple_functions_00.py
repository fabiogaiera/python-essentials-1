# Body Mass Index function
def bmi(weight, height):
    if type(weight) == float and type(height) == float:
        return weight / height ** 2
    else:
        return None


print(bmi(52.5, 1.65))
print(bmi("12.5", 13.4))
