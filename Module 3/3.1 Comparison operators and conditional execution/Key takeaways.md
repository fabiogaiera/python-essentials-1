# 3.1 Comparison operators and conditional execution

## Key takeaways

1. The comparison (otherwise known as relational) operators are used to compare values.

| Operator | Description                                                                                                 | Example |
|----------|-------------------------------------------------------------------------------------------------------------|---------|
| ==       | returns True if operands' values are equal, and False otherwise                                             | x == y  |
| !=       | returns True if operands' values are not equal, and False otherwise                                         | x != y  |
| >        | True if the left operand's value is greater than the right operand's value, and False otherwise             | x > y   |
| <        | True if the left operand's value is less than the right operand's value, and False otherwise                | x < y   |
| >=       | True if the left operand's value is greater than or equal to the right operand's value, and False otherwise | x >= y  |
| <=       | True if the left operand's value is less than or equal to the right operand's value, and False otherwise    | x <= y  |

2. When you want to execute some code only if a certain condition is met, you can use a conditional statement:

    - a single if statement, e.g.:

       ```
         x = 10
 
         if x == 10: # condition
             print("x is equal to 10")  # Executed if the condition is True.
 
       ```
    - a series of if statements, e.g.:

       ```
       x = 10
 
       if x > 5: # condition one
           print("x is greater than 5")  # Executed if condition one is True.
 
       if x < 10: # condition two
           print("x is less than 10")  # Executed if condition two is True.
 
       if x == 10: # condition three
           print("x is equal to 10")  # Executed if condition three is True.
       ```

      Each if statement is tested separately.

    - an if-else statement, e.g.:

       ```
       x = 10
 
       if x < 10:  # Condition
           print("x is less than 10")  # Executed if the condition is True.
 
       else:
           print("x is greater than or equal to 10")  # Executed if the condition is False.
 
       ```

    - a series of if statements followed by an else, e.g.:

       ```
       x = 10
 
       if x > 5:
           print("x > 5")
 
       if x > 8:
           print("x > 8")
 
       if x > 10:
           print("x > 10")
 
       else:
           print("else will be executed")
 
      ```

      Each if is tested separately. The body of else is executed if the last `if` is False.

    - The if-elif-else statement, e.g.:

      ```
      x = 10
 
      if x == 10:
          print("x == 10")
 
      if x > 15:
         print("x > 15")
 
      elif x > 10:
         print("x > 10")
 
      elif x > 5:
         print("x > 5")
 
      else:
         print("else will not be executed")
      ```
      If the condition for if is False, the program checks the conditions of the subsequent elif blocks – the first elif
      block that is True is executed. If all the conditions are False, the else block will be executed.

    - Nested conditional statements, e.g.:

      ```
      x = 10

      if x > 5:
          if x == 6:
              print("nested: x == 6")
          elif x == 10:
              print("nested: x == 10")
          else:
              print("nested: else")
      else:
          print("else")
      ```