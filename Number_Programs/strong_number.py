def is_strong(num):
    original = num
    res = 0

    while num > 0:
        digit = num % 10
        
        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        res += fact
        num //= 10

    return res == original


print(is_strong(145))
