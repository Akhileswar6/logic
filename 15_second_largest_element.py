def second_largest_element(arr):
    if len(arr) < 2:
        return None

    first = second = 0
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second



print(second_largest_element([32,726,34,323,34325]))







