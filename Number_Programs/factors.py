def factors(num):
    res = []

    for i in range(1,num):
        if num % i == 0:
            res.append(i)

    return res

print(factors(8))