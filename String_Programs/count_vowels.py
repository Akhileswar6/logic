def count_vowels(s):
    vowels = "aeiou"
    s = s.lower()       

    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1

    return count

print(count_vowels("aKhIl"))
