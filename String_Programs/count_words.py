def count_words(s):
    s = s.split()
    count = 0

    for i in s:
        count += 1

    return count

print(count_words("Akhil eswar"))