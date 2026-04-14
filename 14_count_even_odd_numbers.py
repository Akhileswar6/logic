def even_odd_count(n):
    even = 0
    odd = 0

    while n > 0:
        res = n % 10
        if res % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10

    return even, odd

print(even_odd_count(8760))

        
