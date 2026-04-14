# def is_prime(n):
#     res = 0
    
#     for i in range(1,n):
#         if n % i == 0:
#             res += i

#     return res == n

# print(is_prime(28))




# def isPrime(n):
n = int(input())
count = 0
for i in range(2, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i,end=" ")
    count = 0


# print(isPrime(21))
