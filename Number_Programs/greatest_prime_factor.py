def greatestprimefactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(greatestprimefactor(21))  # Output: 7


