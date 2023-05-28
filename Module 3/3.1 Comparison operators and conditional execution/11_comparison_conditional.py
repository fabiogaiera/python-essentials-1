# LAB

income = float(input("Enter the annual income: "))

limit = 85528

if income < 0:
    tax = 0.0
elif income < limit:
    tax = (income * 0.18) - 556.2
else:
    tax = 14839.2 + ((income - limit) * 0.32)

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
