def largest_number(arr):
    largest = 0

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest

print(largest_number([1,2,4,5,9,10]))