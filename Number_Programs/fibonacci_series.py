def fibonacci_series(n):
    first = 0
    second = 1

    for i in range(n):
        print(first, end=' ')

        next_num = first + second
        first = second
        second = next_num

    return next_num
print(fibonacci_series(12))