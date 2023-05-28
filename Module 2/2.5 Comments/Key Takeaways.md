# 2.5 Comments

## Key takeaways

1. Comments can be used to leave additional information in code. They are omitted at runtime. The information left in
   source code is addressed to human readers. In Python, a comment is a piece of text that begins with #. The comment
   extends to the end of line.

2. If you want to place a comment that spans several lines, you need to place # in front of them all. Moreover, you can
   use a comment to mark a piece of code that is not needed at the moment (see the last line of the snippet below),
   e.g.:

    ```
    # This program prints
    # an introduction to the screen.
    print("Hello!")  # Invoking the print() function
    # print("I'm Python.")
    ```

3. Whenever possible and justified, you should give self-commenting names to variables, e.g., if you're using two
   variables to store a length and width of something, the variable names length and width may be a better choice than
   my_var1 and my_var2.

4. It's important to use comments to make programs easier to understand, and to use readable and meaningful variable
   names in code. However, it's equally important not to use variable names that are confusing, or leave comments that
   contain wrong or incorrect information!

5. Comments can be important when you are reading your own code after some time (trust us, developers do forget what
   their own code does), and when others are reading your code (can help them understand what your programs do and how
   they do it more quickly).
