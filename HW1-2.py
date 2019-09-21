def is_beaty(n):
    string_repr = str(abs(n))

    digits_sum = 0
    for digit in string_repr:
        digits_sum += int(digit)
    if n % digits_sum == 0:
        return True
    else:
        return False

print (is_beaty(20))


