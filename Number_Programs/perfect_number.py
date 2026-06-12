def is_perfect(n):
    res = 0

    for i in range(1, n):
        if n % i == 0:
            res += i

    if res == n:
        return True
    else:
        return False
    
print(is_perfect(28))