def is_armstrong(n):
    power = len(str(n))
    res = 0

    original = n
    while n > 0:
        digit = n % 10
        res = res + digit ** power
        n //= 10

    if original == res:
        return True
    else:
        return False
    
print(is_armstrong(153))