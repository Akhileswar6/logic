def perfectNumber(n):
    res = 0
    
    for i in range(1,n):
        if n % i == 0:
            res += i

    return res == n

print(perfectNumber(28))

