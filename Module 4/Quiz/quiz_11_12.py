try:
    first_prompt = input("Enter the first value: ")  # kangaroo
    a = len(first_prompt)  # 8
    second_prompt = input("Enter the second value: ")  # 0
    b = len(second_prompt) * 2  # 2
    print(a / b)  # 4.0
except ZeroDivisionError:
    print("Do not divide by zero!")
except ValueError:
    print("Wrong value")
except:
    print("Error. Error. Error")
