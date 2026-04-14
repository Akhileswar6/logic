def reverse_number(nums):
    res = 0

    while nums > 0:
        digit = nums % 10
        res = res * 10 + digit
        nums //= 10

    return res

print(reverse_number(234467))
