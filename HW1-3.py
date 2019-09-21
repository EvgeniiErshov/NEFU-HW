import math

def is_power_of_two(n):

    sqrt_for = math.sqrt(n)

    if sqrt_for**2 == n:
        return True
    else:
        return False


print (is_power_of_two(9))
print (math.sqrt(9))