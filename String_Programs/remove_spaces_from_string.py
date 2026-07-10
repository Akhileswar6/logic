def remove_spaces(s):
    res = ""

    for i in s:
        if i != " ":
            res += i

    return res

print(remove_spaces("Akhil eswar"))