def armstrong(num):
    power = len(str(num))
    res = 0

    original = num
    while num > 0:
        digit = num % 10
        res = res + digit ** power
        num //= 10


    if original == res:
        return "Armstrong"
    else:
        return "Not armstrong"

print(armstrong(153))