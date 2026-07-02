def count_nums(s):
    count = 0

    for i in s:
        if i.isalpha():
            count += 1

    return len(s) - count

print(count_nums("Akhil6834658736532746"))
