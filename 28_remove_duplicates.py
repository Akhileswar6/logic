def duplicates(nums):
    dup = []

    for num in nums:
        if num not in dup:
            dup.append(num)
    return dup

print(duplicates([1,2,3,4,3,2,1,5,6,7,8,7])) 



