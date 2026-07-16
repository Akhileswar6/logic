def largest_number(arr):
    largest = arr[0]

    for i in arr:
        if i > largest:
            largest = i

    return largest

print(largest_number([1,2,4,5,9,10]))