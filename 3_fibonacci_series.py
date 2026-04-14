def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    fib = [0,1]

    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])

    return fib

print(fibonacci_series(7))