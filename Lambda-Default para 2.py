import math

lengthOrigin = (lambda x=1, y=1: math.sqrt(x*x+y*y))

# Calculate distance from point (-5; 2) to origin
L = lengthOrigin(3)
print("L() = ", L)
"""
# Calculate default point distance (1; 1)
L = lengthOrigin(1,1)
print("L(1;1) = ", L)

# what about passing no arguments?
L = lengthOrigin()
print("L() = ", L)
"""