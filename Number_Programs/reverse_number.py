def reverse_number(num):
    res = 0

    while num > 0:
        digit = num % 10
        res = res * 10 + digit
        num //= 10

    return res

print(reverse_number(2345))
