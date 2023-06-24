# Bitwise operators

# & (ampersand) - bitwise conjunction
# | (bar) - bitwise disjunction
# ~ (tilde) - bitwise negation
# ^ (caret) - bitwise exclusive or (xor)

# XOR Table

# | a | b | not a | not b | a and not b | not a and b | (a and not b) or (not a and b)   |
# | 0 | 0 |   1   |  1    |      0      |     0       |                0                 |
# | 0 | 1 |   1   |  0    |      0      |     1       |                1                 |
# | 1 | 0 |   0   |  1    |      1      |     0       |                1                 |
# | 1 | 1 |   0   |  0    |      0      |     0       |                0                 |

a = 0b100000001
b = 0b011111110
c = 0b10011100
d = -c - 1  # equivalent to bitwise negation
e = 0b1
f = 0b0

print(a & b)
print(a | b)
print(~ c)
print(d)
print(e ^ f)

# Each of these two-argument operators can be used in abbreviated form. These are the examples of their equivalent
# notations:

# x &= y
# x |= y
# x ^= y
