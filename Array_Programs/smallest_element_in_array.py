def smallest_number(arr):
    smallest = arr[0]

    for i in arr:
        if i < smallest:
            smallest = i

    return smallest
    
print(smallest_number([23,3,51,21,1,0,-2,4]))
