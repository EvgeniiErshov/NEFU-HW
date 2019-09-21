def is_self_dividing(n):
    string_repr = str(abs(n))

    for digit in string_repr:
        if digit == '0' or n % int(digit) > 0:
            return False
    else:
        return True


print(is_self_dividing(1024))