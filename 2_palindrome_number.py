def palindrome_number(num):
    original = num

    res = 0
    while num > 0:
        digit = num % 10
        res = res * 10 + digit
        num //= 10

    if original == res:
        return "Palindrome"
    else:
        return "Not palindrome"


print(palindrome_number(23432))

