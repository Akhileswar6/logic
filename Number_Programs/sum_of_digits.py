def sum_digits(num):
    res = 0

    while num > 0:
        digit = num % 10
        res += digit
        num //= 10

    return res

print(sum_digits(46))