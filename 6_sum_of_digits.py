def sum_digits(nums):
    result = 0

    while nums > 0:
        digit = nums % 10
        result += digit
        nums //= 10

    return result

print(sum_digits(123))