# LAB

secret_number = 777

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

var = int(input())

while secret_number != var:
    print("Ha ha! You're stuck in my loop!")
    var = int(input())
else:
    print("Well done, muggle! You are free now.")
