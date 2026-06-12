def is_palindrome(num):
    original = num
    res = 0

    while num > 0:
        digit = num % 10
        res = res * 10 + digit
        num //= 10

    if original == res:
        return True
    else:
        return False
    
print(is_palindrome(121))