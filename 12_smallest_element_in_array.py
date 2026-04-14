def smallest_number(arr):
    smallest = arr[0]

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

    return smallest
    
print(smallest_number([23,3,51,21,1]))
