"""Homework 2 - needs to be presented before exam day"""

# Prove "and" operation takes precedence over "or" operation by setting parentheses in (False or False and True or True)

# Set two bits to work with
bit0 = 0
bit1 = 1

# Print the result of the expression without parentheses
print(bit0 | bit0 & bit1 | bit1)
# Print the result of the expression with parentheses around "and" operation
print(bit0 | (bit0 & bit1) | bit1)
# Print the result of the expression with parentheses around "or" operation
print((bit0 | bit0) & (bit1 | bit1))
