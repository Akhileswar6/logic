# Recursion
def factorial(n):
    if n <= 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))


# Logic
def factorial_number(num):
    res = 1

    for i in range(1, num + 1):
        res *= i
    
    return res

print(factorial_number(5))

